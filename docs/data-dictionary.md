# Data Dictionary

The committed files are generated simulation outputs. The CLI does not import external operational CSVs.

## orders.csv

Grain: One order. Baseline rows: 1,200.

| Column | Meaning |
| --- | --- |
| `order_id` | Unique synthetic sales-order identifier. |
| `warehouse` | Warehouse region used for grouping and filtering. |
| `ordered_units` | Requested quantity for the order. |
| `available_units` | Per-order stock availability snapshot. |
| `blocked` | Administrative block flag. Blocked orders fulfill zero units. |
| `delivery_delay_days` | Synthetic delay relative to the promised delivery time. Negative means early. |
| `fulfilled_units` | Quantity fulfilled after the block and availability rules. |
| `shortage_units` | Maximum of ordered minus available units and zero, including blocked orders. |
| `on_time_in_full` | True only for an unblocked, fully fulfilled order with delay at most zero. |
| `status` | Exclusive primary status: Blocked, Stock shortage, Late, or On track. |

## Aggregation Rules

Stock fields are snapshots. Do not sum them across orders or dates as a physical balance. Ratio measures must be recomputed from their numerator and denominator, rather than averaged across groups. Boolean flags overlap unless the methodology defines an exclusive status.

The exception register is a filtered order table. It excludes On track rows. Warehouse scorecard ratios use the same denominators as the full-dataset metrics.
