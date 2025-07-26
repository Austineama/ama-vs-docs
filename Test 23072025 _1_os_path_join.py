# Import necessary libraries
import os
import pandas as pd
import logging
import glob
from pathlib import Path

# --- 1. Configure Logging ---# Change to DEBUG for more detail, WARNING/ERROR for less
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

ROOT_DIR = r"D:\\"
FOLDER = "Ama-VSProject"
FILE_PATTERN = "plan_1.xlsx"
filepath = os.path.join(ROOT_DIR, FOLDER, FILE_PATTERN)

df = pd.read_excel(filepath)

print(df)

df = pd.read_excel(os.path.join(ROOT_DIR, FOLDER, "plan_1.xlsx"))

cols = df.filter(like="MD\n(ft)", axis=1).columns
df.loc[0:5, cols]


df.loc[0:5, df.filter(like="Comments", axis=1)]


rows_count = df.shape[0]
df.loc[0:30, ["MD\n(ft)"]]
print(df.columns)


data = open(p / "plan_1.xlsx").read()


data = open(os.path.join(ROOT_DIR, FOLDER, "plan_1.xlsx")).read()


p = Path(ROOT_DIR) / FOLDER
xlsx_files = list(p.rglob("*.xlsx"))  # recursive

for fp in xlsx_files:
    print("File path:", fp)
