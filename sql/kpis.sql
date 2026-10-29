-- Independent KPI calculation from raw order fields, SQLite syntax.
SELECT
  COUNT(*) AS orders,
  SUM(blocked) AS blocked_orders,
  ROUND(1.0 * SUM(CASE WHEN blocked = 0 THEN MIN(ordered_units, available_units) ELSE 0 END)
    / NULLIF(SUM(CASE WHEN blocked = 0 THEN ordered_units ELSE 0 END), 0), 4) AS fill_rate,
  ROUND(1.0 * SUM(CASE WHEN blocked = 0 AND available_units >= ordered_units
    AND delivery_delay_days <= 0 THEN 1 ELSE 0 END) / COUNT(*), 4) AS otif_rate,
  SUM(CASE WHEN available_units < ordered_units THEN 1 ELSE 0 END) AS shortage_orders
FROM orders;
