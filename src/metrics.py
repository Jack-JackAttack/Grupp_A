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


# def aov_count(df: pd.DataFrame):

def rev_order_id_count(df: pd.DataFrame) -> pd.DataFrame:
    summary_df: pd.DataFrame = (df
                                .groupby("order_id", observed=True)
                                .agg(Order_Revenue = ("revenue", "sum"),
                                     Order_Units = ("units", "sum"),
                                    )
                                )
    return summary_df

def per_category_revenue(df: pd.DataFrame) -> pd.DataFrame:

    per_category : pd.DataFrame = (df
                                .groupby("category", observed=True)
                                .agg(Revenue = ("revenue", "sum"),
                                     Units = ("units", "sum"),
                                     )
                                .sort_values("Revenue", ascending=False)
                                )
    return per_category 
    
    

def rev_summery_per_catagory(df: pd.DataFrame) -> pd.DataFrame:
    rev_summery_per_catagory = df.groupby("category")["revenue"].agg(["sum", "mean", "median", "std", "min", "max"])
    return rev_summery_per_catagory

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