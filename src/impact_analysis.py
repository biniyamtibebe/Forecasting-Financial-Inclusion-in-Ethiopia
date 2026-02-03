import pandas as pd
import numpy as np

def align_events_with_indicators(df, indicator_code, window=2):
    indicator = (
        df[
            (df["record_type"] == "observation") &
            (df["indicator_code"] == indicator_code)
        ]
        .dropna(subset=["year", "value_numeric"])
    )

    events = df[df["record_type"] == "event"].dropna(subset=["year"])

    rows = []

    for _, e in events.iterrows():
        window_data = indicator[
            indicator["year"].between(e["year"], e["year"] + window)
        ]

        if not window_data.empty:
            delta = (
                window_data["value_numeric"].iloc[-1]
                - window_data["value_numeric"].iloc[0]
            )

            rows.append({
                "event": e["indicator"],
                "event_year": e["year"],
                "indicator": indicator_code,
                "change_over_window": delta
            })

    return pd.DataFrame(rows)
