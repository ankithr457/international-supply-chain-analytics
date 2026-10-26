# International Supply Chain Analytics

Operations analytics portfolio by Ankith Ramesh Babu.

Identify blocked orders, stock shortages and delivery exceptions across Germany, Hong Kong, Taiwan and Malaysia.

All records are synthetic. This is an independent learning case study, with no employer data or live SAP connection.

## Quick start
Requires Python 3.11 or newer. No third-party packages or credentials.

```bash
git clone https://github.com/ankithr457/international-supply-chain-analytics.git
cd international-supply-chain-analytics
python src/run.py
python -m unittest discover -s tests -v
```

Open `reports/dashboard.html` in a browser. It works offline. Filter by warehouse, search any field and export matching records. Top cards show the full dataset, while charts and tables follow filters.

## Included outputs
`reports/` contains orders.csv, exception_register.csv, warehouse_scorecard.csv, kpis.json, dashboard.html.

The default run creates 1,200 orders with seed 42.

```bash
python src/run.py --orders 2400 --seed 7 --output reports/scenario
```

## Project structure
- `src/run.py`: deterministic simulation, analysis and command-line interface.
- `src/reporting.py`: CSV exports and self-contained dashboard.
- `tests/`: calculation, edge case, reproducibility and report integration checks.
- `docs/methodology.md`: formulas, assumptions and limits.
- `docs/interview-guide.md`: technical explanation and practice questions.
- `powerbi/`: matching DAX measures and import instructions.


## Results and scope
Default: 106 blocked orders, 78.57% unblocked unit fill rate and 8.92% OTIF.
These numbers describe the included simulation. They do not measure real company performance or validated savings.

Native Power BI `.pbix` and KNIME `.knwf` files are not included. Guides and DAX have not been executed in those desktop applications.
