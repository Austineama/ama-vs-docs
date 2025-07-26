import pandas as pd


def read_excel_smart_header(file_path, engine="xlrd"):
    df = pd.read_excel(file_path, engine=engine)
    # Extract header row
    header_row = df.iloc[0]
    meta = {"header_row": header_row}
    return df, meta
