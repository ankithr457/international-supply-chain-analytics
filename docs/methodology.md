# Analytical Methodology

## Metric Definitions
- Unit fill rate: fulfilled units divided by ordered units on unblocked orders. Blocked orders have zero fulfillment and are excluded from this denominator.
- OTIF: orders that are unblocked, fully fulfilled and have a simulated delay <= 0, divided by all orders. A blocked or partial order never passes OTIF.
- Shortage: max(ordered units minus available units, 0). This flag also exists on blocked orders.
- Status priority: Blocked, Stock shortage, Late, On track. Underlying flags overlap, but the primary status is exclusive.
- Stock is a per-order availability snapshot, not an inventory ledger. Do not sum it as a warehouse balance.

## Operational Interpretation
Review blocked orders first for administrative release, then shortages for allocation, then late orders for transport follow-up. The scorecard compares regions under this simulation, not real service quality.

## Modeling Limitations
The uniform delay distribution deliberately creates exceptions. The 9.42% default OTIF is a simulation output, not an industry benchmark. No sales values, cost savings or business impact are claimed. Inventory is not shared across orders. Simulated delay is not proof of an actual delivery.

## Numerical Interpretation

The default OTIF follows the generator: 91% unblocked probability, 26 of 71 stock offsets permitting full quantity, and 3 of 11 delay values on time. Their product is approximately 9.09%. The observed 9.42% is a stress-case outcome. Unit fill excludes blocked demand; all-demand fulfillment is 73.53%. Country groups share identical assumptions.
