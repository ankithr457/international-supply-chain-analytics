# International Supply Chain Analytics

A reproducible portfolio project with synthetic SAP-style sales orders for four warehouse regions.

## Features
- 1,200 simulated orders
- Blocked order, stock shortage and delivery delay modeling
- Fulfillment and on-time delivery KPIs
- CSV export for downstream Power BI analysis
- Unit tests

## Run
```bash
python src/run.py
python -m unittest discover -s tests -v
```

The published Python code uses only the standard library. `requirements.txt` lists pandas for possible extensions.

## Scope and limitations
All data are synthetic. No live SAP connection or actual SAP transaction execution. A native Power BI PBIX file and executable KNIME workflow are not included in this repository.
