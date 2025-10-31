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

def per_order_revenue(df: pd.DataFrame) -> pd.DataFrame:

    

    return NotImplemented

def avg_revenue(df: pd.DataFrame) -> float:
    df_copy = df.copy()
    return float(df_copy["revenue"].mean())
    
    

def aov_count(df: pd.DataFrame):

    return NotImplemented

# def top_three(df: pd.DataFrame):


# def rev_by_month(df: pd.DataFrame):


# def rev_outliers(df: pd.DataFrame):