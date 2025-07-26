# Ama.py
import pandas as pd

# Define the file paths for your two XLSX files
file_path_1 = r'D:\Ama-VSProject\Data\Activity_reading.xlsx'
file_path_2 = r'D:\Ama-VSProject\Data\BP_reading.xlsx'


# Read the first Excel file into a DataFrame
df1 = pd.read_excel(file_path_1)

# Read the second Excel file into another DataFrame
df2 = pd.read_excel(file_path_2)

# Now df1 and df2 contain the data from my respective Excel files
# You can perform operations on these DataFrames as needed
print("DataFrame 1 (df1):")
print(df1.head())

print("\nDataFrame 2 (df2):")
print(df2.head())


