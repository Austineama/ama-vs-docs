import pandas as pd
import glob

# Get a list of all Excel files in the specified path
excel_files = glob.glob(r'D:\Ama-VSProject\Data\*.xlsx')

# Create an empty list to store DataFrames
dfs = []

# Read each Excel file into a DataFrame and append to the list
for file in excel_files:
    df = pd.read_excel(file)  # Corrected this line
    dfs.append(df)

# Concatenate all DataFrames into a single DataFrame
combined_df = pd.concat(dfs, ignore_index=True)

# Export the combined DataFrame to a new Excel file
combined_df.to_excel('combined_BP_activity.xlsx', index=False)  # Removed extra space
