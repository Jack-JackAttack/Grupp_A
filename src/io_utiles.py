import pandas as pd

def load_file(csv_path: str):
   
    df = pd.read_csv(csv_path)
    df_clean = df.dropna().drop_duplicates().reset_index(drop=True)

    if "date" in df_clean.columns:
        df_clean["date"] = pd.to_datetime(df_clean["date"], errors="coerce")
        
    return df_clean