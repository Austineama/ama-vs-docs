# Import necessary libraries
import os
import pandas as pd
import logging
from pathlib import Path
import re
import numpy as np

# --- 1. Configure Logging ---# Change to DEBUG for more detail, WARNING/ERROR for less
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

ROOT_DIR = Path(r"D:\\")
FOLDER = Path(ROOT_DIR) / "Ama-VSProject"
FILE = "plan_2.xlsx"
filepath = ROOT_DIR / FOLDER / FILE

# 1) Simple use
df, meta = read_excel_smart_header(r"D:\Ama-VSProject\Plan_2.xlsx")

print("Detected header row:", meta["header_row"])
print("Raw header:", meta["raw_header_values"])
print("Cleaned header:", meta["cleaned_header_values"])
print("Warnings:", meta["warnings"])
df.head()

# 2) Dynamic use
for file in os.listdir("D:\Ama-VSProject"):
    if file.endswith(".xlsx"):
        df, meta = read_excel_smart_header(f"D:\Ama-VSProject\{file}")
        print(f"File: {file}")
