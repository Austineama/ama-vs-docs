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


df = pd.read_excel(filepath)
print(df)


# Other options for joining paths within the Path function.
filepath = Path(ROOT_DIR, FOLDER, FILE)

filepath = Path(ROOT_DIR / FOLDER / FILE)
