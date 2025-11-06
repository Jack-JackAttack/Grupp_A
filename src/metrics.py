import pandas as pd

# Creates a new df grouped by cities, total revenue and total units, sorted by revenue.
def rev_unit_count(df: pd.DataFrame) -> pd.DataFrame:
    summary_df: pd.DataFrame = (df
                                .groupby("city", observed=True)
                                .agg(Revenue = ("revenue", "sum"),
                                     Units = ("units", "sum"),
                                     )
                                .sort_values("Revenue", ascending=False)
                                )
    return summary_df

# Creates a new df that returns total revenue, total units per category.
def rev_per_category(df: pd.DataFrame) -> pd.DataFrame:
    summary_df: pd.DataFrame = (df
                                .groupby("category", observed=True)
                                .agg(Revenue = ("revenue", "sum"),
                                     Units = ("units", "sum"),
                                     )
                                .sort_values("Revenue", ascending=False)
                                )
    return summary_df

# Creates a df of cities and total revenue per city, sorted by revenue.
def rev_per_city(df: pd.DataFrame) -> pd.DataFrame:
    sorted_cities: pd.DataFrame = (df.groupby("city", observed=True)
                   .agg(Revenue = ("revenue", "sum"))
                   .sort_values("Revenue", ascending=False)
                   )
    return sorted_cities

# Count total revenue across and amount of unit sold and Revenue / Units across the board
def rev_count(df: pd.DataFrame) -> pd.DataFrame:

    total_revenue = float(df["revenue"].sum())
    total_units = int(df["units"].sum())
    revenue_per_units = round( total_revenue / total_units, 2) if total_units != 0 else None

    summary_rev = {
        "Revenue_Total": total_revenue,
        "Units_Total": total_units,
        "Revenue_Per_Units": revenue_per_units
    }
    return pd.DataFrame([summary_rev])

# Show the total, mean, median, std, min, max of all the Revenue
def rev_summery(df: pd.DataFrame) -> pd.DataFrame:
    rev_summery = df["revenue"].agg(["sum", "mean", "median", "std", "min", "max"])
    return rev_summery

# Show the Total, Mean, Median, Std, Min, Max per category of revenue
def rev_summery_per_catagory(df: pd.DataFrame) -> pd.DataFrame:
    rev_summery_per_catagory = (df
                                .groupby("category")["revenue"]
                                .agg(["sum",
                                      "mean",
                                      "median",
                                      "std",
                                      "min",
                                      "max"]
                                      )
                                ).round(2)
    return rev_summery_per_catagory

# Show Total Revenue and Units sold per Category with the Revenue / Unit per Category
def rev_category_per_unit(df: pd.DataFrame) -> pd.DataFrame:
    category_revenue: pd.DataFrame = (df
                                .groupby("category", observed=True)
                                .agg(Revenue_Total = ("revenue", "sum"),
                                     Units_Sold = ("units", "sum"),
                                     )
                                .assign(Revenue_per_Unit = lambda d: (d["Revenue_Total"] / d["Units_Sold"]).round(2))
                                .sort_values("Revenue_Total", ascending=False)
                                )

    return category_revenue

# Creates a new df with outliers based on category, if no category is written units will be used as default.
def rev_outliers(df: pd.DataFrame, x: str = "units") -> pd.DataFrame:
    if x not in df.columns:
        raise ValueError(f"{x} finns inte i listan, angre rätt kolumn: {", ".join(df.columns)}")

    Q1 = df[x].quantile(0.25)
    Q3 = df[x].quantile(0.75)
    IQR = Q3 - Q1

    low = Q1 - 1.5 * IQR
    high = Q3 + 1.5 * IQR

    outliers_df= df[(df[x] < low) | (df[x] > high)]
    return outliers_df.sort_values(x, ascending=False)