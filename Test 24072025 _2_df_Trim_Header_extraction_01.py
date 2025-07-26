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

# Quick check on the data- Assess the shape -First few rows
Original_df.shape
print(Original_df.shape)

print(Original_df.iloc[21])  # print the 21st row

# d Data Cleaning
df = Original_df.copy()
# Trim the data:cut off row 0-21, and keep 20-147, and keep the columns shown
df1 = df.iloc[21:148, [0, 1, 2, 3, 4, 9, 10, 11]]
# Promote first row to header safely
header = df1.iloc[0]
df1.columns = header
df1 = df1.reset_index(drop=True)
print(column_names)

# create a list of headers from row 0:
column_names = df1.columns = df1.iloc[0].tolist()


df1 = df1[1:].copy()

df1.columns = df1.iloc[0]
df1 = df1.iloc[1:]

print(df1[0:5])
print(df1.iloc[0])
