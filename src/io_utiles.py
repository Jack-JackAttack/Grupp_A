import pandas as pd

def load_file(csv_path: str):
   
    df = pd.read_csv(csv_path)
    df_clean = df.dropna().drop_duplicates().reset_index(drop=True)
    return df_clean

def check_revenue_correct(df: pd.DataFrame, fix: bool = False):

    """
    Control if revenue is price * units.
    fix will take price * units and make it the revenue.
    Make fix true if you want to fix any mistakes in original data.
    """

    df_copy = df.copy()
    df_copy["calculated_revenue"] = (df_copy["price"] * df_copy["units"]).round(2)

    mismatches = df_copy.loc[
                             df_copy["revenue"].round(2) != df_copy["calculated_revenue"].round(2),
                             ["order_id", "price", "units", "revenue", "calculated_revenue"]
                            ]
    if fix:
        df_copy["revenue"] = df_copy["calculated_revenue"]
    df_copy = df_copy.drop(columns=["calculated_revenue"])
    return df_copy , mismatches
    