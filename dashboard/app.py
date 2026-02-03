
import sys
from pathlib import Path

# Ensure project root is on PYTHONPATH
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

import streamlit as st
import pandas as pd
from src.data_loader import load_unified_data, split_by_record_type  # Expected to work now
from src.eda import plot_indicator_trend
from src.forecasting import forecast_indicator  # Ensure this is also imported properly#import the forecasting function

# Ensure project root is on PYTHONPATH
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

# App config
st.set_page_config(layout="wide")
st.title("Forecasting Financial Inclusion in Ethiopia")

# Load data
df = load_unified_data(
    r"c:\Users\hp\Pictures\Forecasting Financial Inclusion in Ethiopia"
    r"\Forecasting-Financial-Inclusion-in-Ethiopia\data\processed"
    r"\ethiopia_fi_enriched.csv"
)

obs, events, targets, _ = split_by_record_type(df)

# Ensure year column exists
if "year" not in obs.columns:
    obs["year"] = pd.to_datetime(obs["observation_date"]).dt.year

# Helper: safe metric
def safe_metric(df, indicator_code, year):
    subset = df[(df["indicator_code"] == indicator_code) & (df["year"] == year)]
    return f"{subset['value_numeric'].iloc[0]}%" if not subset.empty else "N/A"

# Overview
st.header("Overview")
col1, col2 = st.columns(2)

with col1:
    st.metric("Account Ownership (2024)", safe_metric(obs, "ACC_OWNERSHIP", 2024))

with col2:
    st.metric("Digital Payment Usage (2024)", safe_metric(obs, "USG_DIGITAL_PAYMENT", 2024))

# Key Trends
st.header("Key Trends")
col1, col2 = st.columns(2)

with col1:
    fig = plot_indicator_trend(obs, indicator_code="ACC_OWNERSHIP", title="Account Ownership – Ethiopia", ylabel="% of adults")
    st.pyplot(fig)

with col2:
    try:
        fig = plot_indicator_trend(obs, indicator_code="USG_DIGITAL_PAYMENT", title="Digital Payment Usage – Ethiopia", ylabel="% of adults")
        st.pyplot(fig)
    except ValueError:
        st.info("Digital payment time-series data not available.")

# Interactive Indicator Explorer
st.header("Interactive Indicator Explorer")
indicator = st.selectbox("Select an indicator", sorted(obs["indicator_code"].unique()))
filtered = obs[obs["indicator_code"] == indicator]

if filtered.empty:
    st.warning("No data available for this indicator.")
else:
    st.line_chart(filtered.set_index("year")["value_numeric"])

# Raw Observation Data
st.header("Raw Observation Data")
st.dataframe(obs)

# Inclusion Projections
st.header("📈 Inclusion Projections")
forecast = forecast_indicator(df, "ACC_OWNERSHIP", horizon=3)

chart_df = pd.concat([
    df[(df["indicator_code"] == "ACC_OWNERSHIP") & (df["gender"].isna())][["year", "value_numeric"]].rename(columns={"value_numeric": "rate"}).assign(type="Observed"),
    forecast.rename(columns={"forecast": "rate"}).assign(type="Forecast")
])

st.line_chart(chart_df, x="year", y="rate", color="type")