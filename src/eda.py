# src/eda.py
import matplotlib.pyplot as plt

def plot_indicator_trend(df, indicator_code, title, ylabel):
    data = (
        df[df["indicator_code"] == indicator_code]
        .dropna(subset=["year", "value_numeric"])
        .sort_values("year")
    )

    if data.empty:
        raise ValueError(f"No data found for {indicator_code}")

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(data["year"], data["value_numeric"], marker="o")
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.set_xlabel("Year")
    ax.grid(True)

    return fig

