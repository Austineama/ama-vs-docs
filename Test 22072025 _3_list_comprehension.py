# Import necessary libraries
import os
import pandas as pd
import logging
import glob

# --- 1. Configure Logging ---# Change to DEBUG for more detail, WARNING/ERROR for less
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
ROOT_DIR = r"D:\\"
FOLDER = "Ama-VSProject"
FILE_PATTERN = "*.xlsx"

file_path = os.path.join(ROOT_DIR, FOLDER, FILE_PATTERN)
print("File path:", file_path)

# Check if the directory exists
if not os.path.exists(os.path.join(ROOT_DIR, FOLDER)):
    print("Directory does not exist")
else:
    print("Directory exists")

# List all files in the directory
print("Directory contents:")
xlsx_files = [
    file
    for file in os.listdir(os.path.join(ROOT_DIR, FOLDER))
    if file.endswith(".xlsx")
]

print(xlsx_files)
