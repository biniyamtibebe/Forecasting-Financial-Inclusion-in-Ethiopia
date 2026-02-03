
# Forecasting Financial Inclusion in Ethiopia

## 📌 Project Overview

This project analyzes and forecasts **financial inclusion trends in Ethiopia**, with a primary focus on **account ownership and access to financial services**. The unified dataset combines observations, policy events, and contextual metadata, aiming to:

- Explore historical trends in financial inclusion
- Contextualize changes using major policy and infrastructure events
- Build a reproducible pipeline for analysis and forecasting
- Transparently document data gaps and limitations

The project emphasizes **analytical correctness and interpretability**, avoiding unsupported causal claims.

---

## 🎯 Objectives

1. **Exploratory Data Analysis (EDA)**
   - Analyze trends in account ownership and mobile money access
   - Identify data availability and gaps across indicators
   - Visualize trends with policy/event overlays

2. **Data Engineering**
   - Build a unified, schema-consistent dataset
   - Separate observations, events, and (potential) impact links
   - Ensure reproducibility and robustness

3. **Forecasting**
   - Forecast national account ownership trends
   - Use historical access indicators as the primary signal
   - Treat policy events as contextual, not causal inputs

4. **Documentation & Transparency**
   - Clearly document assumptions and limitations
   - Avoid overinterpretation of sparse or missing data

---

## 📂 Repository Structure

```plaintext
Forecasting-Financial-Inclusion-in-Ethiopia/
│
├── data/
│   ├── raw/
│   │   ├── ethiopia_fi_unified_data.xlsx
│   │   └── reference_codes.xlsx
│   └── processed/
│
├── notebooks/
│   ├── 01_data_inspection.ipynb
│   ├── 02_exploratory_analysis.ipynb
│   └── 03_forecasting.ipynb
│
├── src/
│   ├── data_loader.py
│   ├── eda.py
│   └── forecasting.py
│
├── figures/
│   └── plots/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🧾 Data Description

The dataset follows a unified schema with multiple record types:

### Record Types
- **observation**: Quantitative indicators over time (e.g., account ownership)
- **event**: Policy, regulatory, or infrastructure milestones (e.g., mobile money rollout)
- **impact_link**: Designed to link events to indicators (currently, no records present)

### Key Columns
- **record_id**: Unique identifier
- **record_type**: Type of record (observation / event / impact_link)
- **indicator_code**: Short indicator identifier
- **value_numeric**: Numeric observation value
- **observation_date**: Date of measurement (for observations)
- **collection_date**: Date of event or data collection
- **notes**: Metadata (e.g., gender disaggregation)

---

## 📊 Indicators Used

### Primary (Modelable)
- **ACC_OWNERSHIP**: Account ownership rate (% of adults)
- **ACC_MM_ACCOUNT**: Mobile money account ownership (% of adults)

### Contextual Only (Not Modelable)
- **USG*** indicators (digital payment usage, transaction counts, values): Exist in the schema but contain no numeric observations and are excluded from trend modeling.

---

## 📈 Exploratory Analysis

- Trends are visualized using yearly aggregation.
- Gender-disaggregated observations are excluded from national trends.
- Events are overlaid as vertical markers for context.
- No causal inference is claimed due to the lack of explicit impact links.

### Example Interpretation
Account ownership shows steady growth over time, with periods of slower change following major structural reforms.

---

## 🔮 Forecasting Approach

- **Forecast Target**: Account ownership rate.
- **Time Index**: Calendar year derived from `observation_date`.
- **Event Encoding**: Events are not encoded as causal features.
- **Forecast Interpretation**: Forecasts represent continuations of historical access trends.

### Priorities
- Transparency
- Reproducibility
- Analytical defensibility

---

## ⚠️ Limitations

- No impact_link records are available.
- Digital payment usage indicators lack numeric observations.
- Sparse time points limit model complexity.
- Results should not be interpreted as causal estimates.

These limitations are explicitly documented and reflected in the methodology.

---

## 🛠️ Setup & Usage

### Environment Setup
1. Set up a virtual environment:
   ```bash
   python -m venv .week10
   source .week10/bin/activate  # Windows: .week10\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Run Analysis
- Load and inspect data.
- Run EDA notebooks.
- Generate plots and forecasts.

---

## 📌 Key Design Principles

- **Defensive Coding**: Schema checks and empty guards.
- **Honest Analytics**: No forced plots or fabricated links.
- **Clear Documentation**: Data gaps are explicitly stated.

---

## 📬 Notes

This project is designed to be extensible. As more indicators or impact links become available, the pipeline can incorporate them with minimal changes.
```

T