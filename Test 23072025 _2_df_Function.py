# Import necessary libraries
import os
import pandas as pd
import logging

from pathlib import Path

# --- 1. Configure Logging ---# Change to DEBUG for more detail, WARNING/ERROR for less
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

ROOT_DIR = Path(r"D:\\")
FOLDER = "Ama-VSProject"
FILE = "plan_2.xlsx"
filepath = ROOT_DIR / FOLDER / FILE

# Load the data from the Excel file
Original_df = pd.read_excel(filepath)
# First few rows
Original_df
print(Original_df.iloc[21])  # print the 21st row

# d Data Cleaning
df = Original_df.copy()
# Trim the data:cut off row 0-19, and keep 20-147
df1 = df.iloc[max(0, 21) : 148]
print(df1)
print(df1.iloc[0])
# create a copy of the trimmed data
df2 = df1.copy()
# drop some columns
df2 = df1.drop(df1.columns[[5, 6, 7, 8, 12, 13, 14, 15]], axis=1)

# df = df.drop(df.columns[[5, 6, 7, 8, 12, 13, 14, 15]], axis=1)
print("\nFirst Few Columns:")
print(df.head(24))

# get position of the header
for i, col in enumerate(df.columns):
    print(f"Column {i}: {col}")

Header_row_position = df.columns.get_loc("MD\n(ft)")
# print(Header_row_position)

# df = df.iloc[max(0, 19) : 148]- to cut off row 0-19,  and keep 20-147
print(df.head())
