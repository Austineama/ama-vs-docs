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
FILE = "plan_1.xlsx"
filepath = ROOT_DIR / FOLDER / FILE
# suggest the doc string
df = pd.read_excel(filepath)
print(df)

# Load the data from the Excel file
df = pd.read_excel(filepath)

# Display basic information about the DataFrame
print("DataFrame Info:")
print(df.info())

# Display summary statistics for numerical columns
print("\nSummary Statistics:")
print(df.describe())

# Check for any missing values in the DataFrame
missing_values = df.isnull().sum()
print("\nMissing Values in Each Column:")
print(missing_values)

# Display the first few rows of the DataFrame
print("\nFirst Few Rows:")
print(df.head())

# Example: Analyze specific columns (e.g., 'MD\n(ft)' and 'Comments')
if "MD\n(ft)" in df.columns and "Comments" in df.columns:
    # Display unique values in 'Comments'
    unique_comments = df["Comments"].unique()
    print("\nUnique Comments:")
    print(unique_comments)

    # Plot a histogram of 'MD\n(ft)' if data is numeric
    if pd.api.types.is_numeric_dtype(df["MD\n(ft)"]):
        import matplotlib.pyplot as plt

        plt.hist(df["MD\n(ft)"].dropna(), bins=20, edgecolor="k")
        plt.xlabel("MD\n(ft)")
        plt.ylabel("Frequency")
        plt.title("Histogram of MD\n(ft)")
        plt.show()
