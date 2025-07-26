import pandas as pd
import glob
import os
from pathlib import Path

from pathlib import Path

folder_path = Path("D:/Ama-VSProject")  # Or Path(r"D:\Ama-VSProject")

print(folder_path)  # Before calling os.listdir or .glob

excel_files = [f for f in folder_path.iterdir() if f.suffix == ".xlsx"]
print(excel_files)




Base_dir = "D:\\"
Root_folder = "Ama-VSProject"
folder_path = os.path.join(Base_dir, Root_folder)
excel_files = [
    os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(".xlsx")
]
print(excel_files)


Base_dir = r"D:\Ama-VSProject"
excel_files = [
    os.path.join(Base_dir, f) for f in os.listdir(Base_dir) if f.endswith(".xlsx")
]
print(excel_files)


# --- 2. Define File Paths ---
Base_dir = r"D"
Root_folder = r"Ama-VSProject"
filename = r"BP_Activity.xlsx"
folder_path = os.path.join(Base_dir, Root_folder)

print(folder_path)

excel_files = [
    os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(".xlsx")
]

print(excel_files)  # This will print a list of all Excel files in the folder


excel_file = glob.glob(excel_file + "/*.xlsx")
print("Excel files in location:", excel_file)

df = pd.read_excel(excel_file[0], sheet_name=sheet_name)

df2 = pd.read_excel(excel_file[1], sheet_name=sheet_name)


work_folder = os.path.join(folder, "*.xlsx")

excel_file = glob.glob(work_folder)


file_path = os.path.join(Base_dir, Root_folder, filename)

print(file_path)

file = glob.glob(file_path + "/*.pdf")

print(file)
