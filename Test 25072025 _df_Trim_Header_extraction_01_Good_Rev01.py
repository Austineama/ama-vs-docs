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
df = pd.read_excel(filepath)

# Quick check on the data- Assess the shape -First few rows
df.shape
print(df.shape)

# print(df.iloc[21])  # print the 21st row
print(df.iloc[21])

# d Data Cleaning
df0 = df.copy()
# Trim the data:cut off row 0-21, and keep 20-147, and keep the columns shown
df1 = df.iloc[21:148, [0, 1, 2, 3, 4, 9, 10, 11]]

# Promote first row to header safely
header = df1.iloc[0]
df1.columns = header
df1 = df1[0:].reset_index(drop=True)
df1.head(4)

# Check for depth-based indexing
depth_keywords = ["DEPTH", "MD", "TVD"]
df1_cols = [str(c).upper() for c in df1.columns]
for col in df1.columns:
    col_upper = str(col).upper()
    if any(keyword in col_upper for keyword in depth_keywords):
        df1 = df1.sort_values(by=col).reset_index(drop=True)
        df1.index.name = None
        break
