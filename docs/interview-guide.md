# Project explanation and interview practice

## Short explanation
This project explores order fulfillment and exception prioritization using synthetic operations data. Python generates the data, applies documented business rules and exports a filterable offline dashboard and CSV reports. Fixed seeds make the results reproducible.

## Demonstrate in five minutes
1. Run `python src/run.py` and open `reports/dashboard.html`.
2. Explain the full-dataset cards and filter one warehouse.
3. Search for Blocked and export the filtered records.
4. Open `docs/methodology.md` and explain one formula with a small example.
5. Run the unit tests and describe one edge case they protect.

## Worked example
An unblocked order requests 10 units with 6 available. Fulfillment is 6, shortage is 4, unit fill rate is 60%. Even with an early delivery, OTIF fails because the order is incomplete. If blocked, fulfilled units are zero and the order is excluded from the fill-rate denominator.

## Questions to practise
- Why separate fill rate from OTIF?
- Which assumptions would fail with real operational data?
- How would you validate an imported CSV before analysis?
- Which rule has the largest effect on the output?
- What would you change before connecting an ERP system?

## Next practical exercise
Change the seed and number of orders, predict the direction of change, rebuild and explain the result. Read every function in `src/run.py` before discussing implementation in an interview.

Describe your own role and assistance accurately. These are portfolio simulations, not employment projects or measured cost-saving deployments.
