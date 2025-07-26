# Import necessary libraries
import logging
import pandas as pd
import glob
import os

# Set up logging (this is usually done once, at the start of your script)
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


# Import logging for debugging purposes
# import logging
# Define a function to Read the Activity sheet from the Excel file
def load_activity_sheet(filepath: str, sheet_name: str = "Activity") -> pd.DataFrame:
    """Read a specific sheet (default 'Activity') from the specified Excel file.

    Args:
        filepath (str): Path to the Excel file.
        sheet_name (str): Name of the sheet to load (default is 'Activity').
    Returns:
        pd.DataFrame: DataFrame with the sheet's data.
    Raises:
        FileNotFoundError: If the file does not exist.
    """
    if not os.path.exists(filepath):
        logging.error(f"File not found: {filepath}")
        raise FileNotFoundError(f"File not found: {filepath}")
    logging.info(f"Loading sheet '{sheet_name}' from '{filepath}'...")
    return pd.read_excel(filepath, sheet_name=sheet_name)


def load_activity_data(filepath):
    """Read the Activity sheet from the Excel file."""
    return pd.read_excel(filepath, sheet_name="Activity")


Data_1 = "BP_Activity.xlsx"
# Define the file path for the Excel files
Data_location = r"D:\Ama-VSProject\*.xlsx"
# Load the Excel file
df1 = pd.read_excel(Data_1, sheet_name=None)  # Load all sheets
# Display Excel worksheet names
Excel_File_1 = pd.ExcelFile(Data_1)
sheet_names = Excel_File_1.sheet_names
print("Excel worksheet names:", sheet_names)
# Display the first few rows of each sheet
for sheet in sheet_names:
    print(f"First few rows of '{sheet}':")
    print(df1[sheet].head())
# Combine all sheets into a single DataFrame
print(df1.head(Data_1, sheet_name="Sheet2"))  # Display the first few rows
# Save the combined DataFrame to an Excel file
df1.to_excel(r"D:\Ama-VSProject\merged_BP_activity.xlsx", index=False)
print("merged DataFrame saved to 'merged_BP_activity.xlsx'.")

Data_location = r"D:\Ama-VSProject\BP_activity\*.xlsx"
# Get a list of all Excel files in the specified directory
files = glob.glob(Data_location)
# Print the list of files found
print("Files found:", files)
# Load each Excel file and append its content to a list
dataframes = []
for file in files:
    df = pd.read_excel(file)
    dataframes.append(df)
# Concatenate all DataFrames in the list into a single DataFrame
merged_df = pd.concat(dataframes, ignore_index=True)
# Display the first few rows of the merged DataFrame
print(merged_df.head())
# Save the combined DataFrame to an Excel file
merged_df.to_excel(r"D:\Ama-VSProject\merged_BP_activity.xlsx", index=False)
print("Merged DataFrame saved to 'merged_BP_activity.xlsx'.")
# Display the shape of the merged DataFrame
print("Shape of the merged DataFrame:", merged_df.shape)
# Display the columns of the merged DataFrame
print("Columns in the merged DataFrame:", merged_df.columns.tolist())
# Display the data types of the columns in the merged DataFrame
print("Data types of the columns in the merged DataFrame:")
print(merged_df.dtypes)
# Display the number of missing values in each column
print("Number of missing values in each column:")
print(merged_df.isnull().sum())
# Display the summary statistics of the merged DataFrame
print("Summary statistics of the merged DataFrame:")
print(merged_df.describe())
# Display the first few rows of the merged DataFrame
print(merged_df.head())
# Display the last few rows of the merged DataFrame
print("Last few rows of the merged DataFrame:")
print(merged_df.tail())
# Display the unique values in the 'Activity' column
print("Unique values in the 'Activity' column:")
print(merged_df["Activity"].unique())
# Display the number of unique values in the 'Activity' column
print("Number of unique values in the 'Activity' column:")
print(merged_df["Activity"].nunique())
# Display the value counts of the 'Activity' column
print("Value counts of the 'Activity' column:")
print(merged_df["Activity"].value_counts())
# Display the first few rows of the DataFrame
print("First few rows of the merged DataFrame:")
print(merged_df.head())
