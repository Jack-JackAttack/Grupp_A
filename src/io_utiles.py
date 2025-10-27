import pandas as pd

def load_file(csv_path: str):
   
    df = pd.read_csv(csv_path)
    df_clean = df.dropna().drop_duplicates().reset_index(drop=True)
    return df_clean