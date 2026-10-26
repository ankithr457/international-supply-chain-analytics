"""Reproducible simulated ERP logistics case study. No real SAP integration."""
from pathlib import Path
import random
import csv

REGIONS = ("Germany", "Hong Kong", "Taiwan", "Malaysia")

def simulate(n=1200, seed=42):
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
            "on_time_rate": round(sum(r["delivery_delay_days"] <= 0 for r in rows) / len(rows), 4) if rows else 0}

def main():
    rows = simulate()
    output = Path(__file__).resolve().parents[1] / "reports"
    output.mkdir(exist_ok=True)
    with (output / "orders.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader(); writer.writerows(rows)
    print(metrics(rows))

if __name__ == "__main__": main()
