import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from scipy import stats

def forecast_with_uncertainty(df, indicator_code, horizon=3, alpha=0.05):
    data = (
        df[
            (df["record_type"] == "observation") &
            (df["indicator_code"] == indicator_code) &
            (df["gender"].isna())
        ]
        .dropna(subset=["year", "value_numeric"])
        .sort_values("year")
    )

    X = data["year"].values.reshape(-1, 1)
    y = data["value_numeric"].values

    model = LinearRegression()
    model.fit(X, y)

    # Residuals for uncertainty
    y_hat = model.predict(X)
    residuals = y - y_hat
    sigma = residuals.std(ddof=1)

    last_year = int(data["year"].max())
    future_years = np.arange(last_year + 1, last_year + horizon + 1)
    X_future = future_years.reshape(-1, 1)

    preds = model.predict(X_future)

    z = stats.norm.ppf(1 - alpha / 2)

    return pd.DataFrame({
        "year": future_years,
        "forecast": preds,
        "lower": preds - z * sigma,
        "upper": preds + z * sigma
    })
