# src/forecasting.py

import pandas as pd
import numpy as np

def forecast_indicator(df, indicator_code, horizon):
    # Check the fiscal_year column
    if 'fiscal_year' not in df.columns:
        raise KeyError("The DataFrame must contain a 'fiscal_year' column.")
    
    # Convert fiscal_year to numeric and drop NaN
    df['fiscal_year'] = pd.to_numeric(df['fiscal_year'], errors='coerce')
    df.dropna(subset=['fiscal_year'], inplace=True)

    # Simulated forecast values
    forecast_years = df['fiscal_year'].max() + np.arange(1, horizon + 1)
    forecast_values = np.random.rand(horizon) * 100  # Example data for demonstration

    return pd.DataFrame({
        'fiscal_year': forecast_years,
        'forecast': forecast_values
    })