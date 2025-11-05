import pandas as pd

def load_file(csv_path: str):
   
    df = pd.read_csv(csv_path)
    df_clean = df.dropna().drop_duplicates().reset_index(drop=True)
    return df_clean

def check_revenue_correct(df: pd.DataFrame, fix: bool = False, tol: float = 0.01):

    """
    Control if revenue is price * units.
    fix will take price * units and make it the revenue.
    Make fix true if you want to fix any mistakes in original data.
    tol = tolerance: defult set to 0.01 can change  but usually not needed
    """

    df_copy = df.copy()
    
    # check if "price" "units" "revenue" is number and try to convert string to number, if it cant it makes it NA
    for col in ["price", "units", "revenue"]:
        df_copy[col] = pd.to_numeric(df_copy[col], errors="coerce")
    
    # Make a calculated revenue to check if revenue is correct by useing price * units
    df_copy["calculated_revenue"] = (df_copy["price"] * df_copy["units"]).round(2)

    # dose the comparison between revenue and calculated revenue
    diff_mask = (df_copy["revenue"].round(2) - df_copy["calculated_revenue"].round(2)).abs() > tol

    nan_mask = df_copy["price"].isna() | df_copy["units"].isna()

    mismatches = df_copy.loc[
                             diff_mask | nan_mask,
                             ["order_id", "price", "units", "revenue", "calculated_revenue"]
                            ]
    if fix:
        df_copy.loc[~nan_mask, "revenue"] = df_copy.loc[~nan_mask, "calculated_revenue"]
    df_copy = df_copy.drop(columns=["calculated_revenue"])
    return df_copy , mismatches