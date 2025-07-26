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
FILE_PATTERN = "*.xlsx"

p = Path(ROOT_DIR) / FOLDER
xlsx_files = list(p.glob("*.xlsx"))  # like glob.glob

for fp in p.rglob("*.xlsx"):  # recursive
    print("File path:", fp)
