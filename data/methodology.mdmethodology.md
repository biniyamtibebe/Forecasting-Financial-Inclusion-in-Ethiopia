# Methodology Overview

## Data Structure
Unified schema with four record types:
- observation
- event
- impact_link
- target

This avoids pre-assigning events to pillars and reduces bias.

---

## Event Impact Modeling
Event impacts are modeled as **additive directional adjustments**
to trend-based forecasts.

Assumptions:
- Effects may lag by 6–18 months
- Multiple events compound
- Magnitudes reflect plausible ranges, not precise estimates

Limitations:
- Sparse survey years
- Operator data not always representative
- No causal identification strategy

---

## Forecasting Approach
Given limited historical points:
- Linear trend used as baseline
- Event-adjusted scenarios layered on top
- Forecasts presented as ranges, not point truths
