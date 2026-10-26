"""Reproducible order fulfillment and exception analysis."""
from pathlib import Path
import random
import csv
import json
import argparse
from reporting import write_csv, dashboard

REGIONS = ("Germany", "Hong Kong", "Taiwan", "Malaysia")

def simulate(n=1200, seed=42):
    if n < 0:
        raise ValueError("Order count must be nonnegative")
    rng = random.Random(seed)
    rows = []
    for i in range(n):
        qty = rng.randint(1, 120)
        stock = max(0, qty + rng.randint(-45, 25))
        blocked = rng.random() < .09
        delay = rng.randint(-2, 8)
        rows.append({"order_id": f"SO{i+1:05d}", "warehouse": rng.choice(REGIONS), "ordered_units": qty,
                     "available_units": stock, "blocked": blocked, "delivery_delay_days": delay,
                     "fulfilled_units": 0 if blocked else min(qty, stock)})
    return rows

def metrics(rows):
    total = sum(r["ordered_units"] for r in rows if not r["blocked"])
    filled = sum(r["fulfilled_units"] for r in rows)
    return {"orders": len(rows), "blocked_orders": sum(r["blocked"] for r in rows),
            "fill_rate": round(filled / total, 4) if total else 0,
            "otif_rate": round(sum(not r["blocked"] and r["fulfilled_units"] == r["ordered_units"] and r["delivery_delay_days"] <= 0 for r in rows) / len(rows), 4) if rows else 0}

def enrich(rows):
    result = []
    for row in rows:
        r = dict(row)
        r["shortage_units"] = max(0, r["ordered_units"] - r["available_units"])
        r["on_time_in_full"] = (not r["blocked"] and r["fulfilled_units"] == r["ordered_units"] and r["delivery_delay_days"] <= 0)
        r["status"] = "Blocked" if r["blocked"] else "Stock shortage" if r["shortage_units"] else "Late" if r["delivery_delay_days"] > 0 else "On track"
        result.append(r)
    return result


def build(output, n=1200, seed=42):
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    rows = enrich(simulate(n, seed))
    kpis = metrics(rows)
    kpis["shortage_orders"] = sum(r["shortage_units"] > 0 for r in rows)
    write_csv(output / "orders.csv", rows)
    write_csv(output / "exception_register.csv", [r for r in rows if r["status"] != "On track"], list(rows[0]) if rows else [])
    scorecard = []
    for warehouse in REGIONS:
        selected = [r for r in rows if r["warehouse"] == warehouse]
        m = metrics(selected)
        scorecard.append({"warehouse": warehouse, **m})
    write_csv(output / "warehouse_scorecard.csv", scorecard)
    (output / "kpis.json").write_text(json.dumps(kpis, indent=2) + "\n")
    dashboard(output / "dashboard.html", "International Supply Chain Analytics", "Order exceptions, stock availability and simulated on-time-in-full performance across four regions.",
              {"Orders": n, "Blocked orders": kpis["blocked_orders"], "Unit fill rate": f"{kpis['fill_rate']:.1%}", "On time in full": f"{kpis['otif_rate']:.1%}"}, rows, "warehouse", "shortage_units")
    return kpis


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--orders", type=int, default=1200)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1] / "reports")
    args = parser.parse_args()
    if args.orders < 1:
        parser.error("--orders must be at least 1")
    print(json.dumps(build(args.output, args.orders, args.seed), indent=2))
    print(f"Dashboard: {args.output / 'dashboard.html'}")


if __name__ == "__main__":
    main()
