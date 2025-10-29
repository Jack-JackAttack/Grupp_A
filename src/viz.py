import matplotlib.pyplot as plt
import pandas as pd

def revenue_per_month(df: pd.DataFrame):

    df["date"] = pd.to_datetime(df["date"])
    df_month = df.groupby(df["date"].dt.month)["revenue"].sum()
    fig, ax = plt.subplots()
    ax.plot(df_month.index, df_month.values)
    ax.set_title("Försäljning per månad 2024")
    ax.set_xlabel("Månad")
    ax.set_ylabel("Intäkt")
    plt.grid(True, axis="y")
    fig.tight_layout()
    return ax
