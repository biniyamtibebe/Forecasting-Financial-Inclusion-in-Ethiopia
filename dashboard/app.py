import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

import streamlit as st
from src.data_loader import load_unified_data, split_by_record_type
from src.eda import plot_indicator_trend


st.set_page_config(layout="wide")
st.title("Forecasting Financial Inclusion in Ethiopia")

df = load_unified_data(
    r"c:\Users\hp\Pictures\Forecasting Financial Inclusion in Ethiopia\Forecasting-Financial-Inclusion-in-Ethiopia\data\processed\ethiopia_fi_enriched.csv"
)

obs, events, targets, _ = split_by_record_type(df)

def safe_metric(df, indicator_code, year):
    subset = df.query(
        "indicator_code == @indicator_code and year == @year"
    )
    if subset.empty:
        return "N/A"
    return f"{subset['value_numeric'].iloc[0]}%"

st.header("Overview")
col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Account Ownership (2024)",
        safe_metric(obs, "ACC_OWNERSHIP", 2024)
    )

with col2:
    # 🔴 replace with the REAL code from your dataset
    st.metric(
        "Digital Payment Usage (2024)",
        safe_metric(obs, "MOBILE_MONEY_ACCOUNT", 2024)
    )

st.header("Data Explorer")
st.dataframe(obs)
st.header("Trends")

col1, col2 = st.columns(2)

with col1:
    fig = plot_indicator_trend(
        obs,
        indicator_code="ACC_OWNERSHIP",
        title="Account Ownership – Ethiopia",
        ylabel="% of adults"
    )
    st.pyplot(fig)


with col2:
    try:
        fig = plot_indicator_trend(
            obs,
            indicator_code="MM_ACCOUNT_OWNERSHIP",
            title="Mobile Money Account Ownership – Ethiopia",
            ylabel="% of adults"
        )
        st.pyplot(fig)
    except ValueError:
        st.info("Mobile money time-series data not available.")

