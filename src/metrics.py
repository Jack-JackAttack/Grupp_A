import pandas as pd


def rev_unit_count(df: pd.DataFrame):                                           # Skapar en ny df som är grupperad efter städer som lägger till revenue och units från huvudfilen, sorterad på revenue.
    summary_df: pd.DataFrame = (df
                                .groupby("city", observed=True)
                                .agg(Revenue = ("revenue", "sum"),
                                     Units = ("units", "sum"),
                                     )
                                .sort_values("Revenue", ascending=False)
                                )
    return summary_df



# def rev_per_category(df: pd.DataFrame):
def rev_per_category(df: pd.DataFrame):
    summary_df: pd.DataFrame = (df
                                .groupby("category", observed=True)
                                .agg(Revenue = ("revenue", "sum"),
                                     Units = ("units", "sum"),
                                     )
                                .sort_values("Revenue", ascending=False)
                                )
    return summary_df



def rev_per_city(df):
    sorted_cities = (df.groupby("city", observed=True)
                   .agg(Revenue = ("revenue", "sum"))
                   .sort_values("Revenue", ascending=False)
                   )
    return sorted_cities


# def aov_count(df: pd.DataFrame):

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
    rev_summery_per_catagory = df.groupby("category")["revenue"].agg(["sum", "mean", "median", "std", "min", "max"])
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

# def top_three(df: pd.DataFrame):


# def rev_by_month(df: pd.DataFrame):


# def rev_outliers(df: pd.DataFrame):