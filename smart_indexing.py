
import pandas as pd

def auto_index_dataframe(df):
    depth_keywords = ['DEPTH', 'MD', 'TVD']
    time_keywords = ['TIME', 'DATE', 'DATETIME']

    df_cols = [str(c).upper() for c in df.columns]

    # Check for depth-based indexing
    for col in df.columns:
        col_upper = str(col).upper()
        if any(keyword in col_upper for keyword in depth_keywords):
            df = df.sort_values(by=col).reset_index(drop=True)
            df.index.name = None
            return df

    # Check for datetime-based indexing
    for col in df.columns:
        col_upper = str(col).upper()
        if any(keyword in col_upper for keyword in time_keywords):
            try:
                df[col] = pd.to_datetime(df[col], errors='coerce')
                df = df.sort_values(by=col).reset_index(drop=True)
                df.index.name = None
                return df
            except Exception:
                continue

    return df  # Return as-is if no indexing match
