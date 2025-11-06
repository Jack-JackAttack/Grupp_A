import matplotlib.pyplot as plt
import pandas as pd
from .metrics import (rev_per_city)

# Visualizes total revenue per month.
def revenue_per_month(df: pd.DataFrame):

    df_month = df.groupby(df["date"].dt.month)["revenue"].sum()
    fig, ax = plt.subplots()
    ax.plot(df_month.index, df_month.values, marker="o", linestyle="--")
    ax.set_title("Försäljning per månad 2024")
    ax.set_xlabel("Månad")
    ax.set_ylabel("Intäkt")
    plt.grid(True, axis="y")
    fig.tight_layout()
    return ax


# Visualizes total revenue per city.
def revenue_per_city_viz(df):

    sorted_cities = rev_per_city(df)
    fig, ax = plt.subplots()
    ax.barh(sorted_cities.index, sorted_cities["Revenue"])
    ax.set_title("Total intäkt per stad")
    ax.set_xlabel("Intäkt")
    ax.set_ylabel("Stad")
    ax.grid(True, axis="x")
    plt.tight_layout()
    return ax