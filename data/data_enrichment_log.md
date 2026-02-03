# Data Enrichment & Lineage Log

## Source Data
- Global Findex (Account Ownership, Digital Payments)
- National Bank of Ethiopia reports
- Operator-reported mobile money statistics

## Enrichment Steps
| Step | Description | Source | Confidence |
|----|-----------|--------|-----------|
| E1 | Added mobile money ownership indicators | NBE / Operator reports | Medium |
| E2 | Harmonized fiscal and calendar years | World Bank methodology | High |
| E3 | Imputed missing values (linear interpolation) | Internal method | Low–Medium |

## Notes
- No synthetic data introduced
- Imputations clearly flagged in `confidence` field
