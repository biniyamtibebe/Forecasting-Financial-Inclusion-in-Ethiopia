# src/impact_model.py

import pandas as pd
import numpy as np


def build_event_indicator_matrix(impact_links: pd.DataFrame) -> pd.DataFrame:
    """
    Create Event × Indicator association matrix.
    """
    matrix = (
        impact_links
        .pivot_table(
            index="parent_id",
            columns="related_indicator",
            values="impact_magnitude",
            aggfunc="mean"
        )
        .fillna(0)
    )

    return matrix


def apply_event_impacts(
    base_series: pd.Series,
    events: pd.DataFrame,
    impact_links: pd.DataFrame
) -> pd.Series:
    """
    Apply lagged event impacts to a baseline time series.
    """
    series = base_series.copy()

    for _, link in impact_links.iterrows():
        event = events.loc[events["id"] == link["parent_id"]]
        if event.empty:
            continue

        event_year = int(event["year"].iloc[0] + link["lag_months"] / 12)

        if event_year in series.index:
            direction = 1 if link["impact_direction"] == "positive" else -1
            series.loc[event_year:] += direction * link["impact_magnitude"]

    return series
