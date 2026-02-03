# src/forecasting.py

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


def trend_forecast(series: pd.Series, start_year: int, end_year: int):
    """
    Linear trend forecast with confidence bands.
    """
    y = series.values
    X = series.index.values.reshape(-1, 1)

    model = LinearRegression()
    model.fit(X, y)

    years = np.arange(start_year, end_year + 1)
    preds = model.predict(years.reshape(-1, 1))

    return pd.Series(preds, index=years)


def scenario_forecast(base_forecast, scenario="base"):
    """
    Simple scenario adjustments.
    """
    if scenario == "optimistic":
        return base_forecast * 1.05
    if scenario == "pessimistic":
        return base_forecast * 0.95
    return base_forecast
