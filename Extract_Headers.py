import pandas as pd
import glob

def extract_headers(file_pattern):
    """
    Extracts headers from the first sheet of all Excel files matching the pattern.
    """
    files = glob.glob(file_pattern)
    all_headers = []

    for file in files:
        try:
            df = pd.read_excel(file, sheet_name=0, header=0, nrows=0) # Read only headers
            headers = df.columns.tolist()
            all_headers.extend(headers)
        except Exception as e:
            print(f"Error reading {file}: {e}")

    return all_headers
