import pandas as pd  # Import pandas for data handling
import re  # Import regex library for pattern matching

# Function to find the header row dynamically
def find_header_row(file_path, sheet_name, keywords, max_rows=30):
    """
    Dynamically finds the header row in an Excel file based on keywords.

    Args:
        file_path (str): The path to the Excel file.
        sheet_name (str): The name of the sheet to read.
        keywords (list): A list of keywords that must all be present in the header row.
        max_rows (int): The maximum number of rows to check for the header.

    Returns:
        int: The row number of the header row (0-indexed), or None if not found.
    """
    try:
        preview = pd.read_excel(file_path, sheet_name=sheet_name, header=None, nrows=max_rows)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred reading the Excel file: {e}")
        return None

    for i, row in preview.iterrows():
        # Convert each cell to uppercase strings for comparison
        normalized_row = [str(cell).strip().upper() for cell in row]
        # Check if all keywords are present in the row
        if all(any(keyword in cell for cell in normalized_row) for keyword in keywords):
            return i  # Return the row number if found
    return None  # Return None if header row isn't found


# Set up file paths and configuration
file_path_pd_setting = r'D:\Ama-VSProject\PD_Setting.xlsx'  # Corrected file path!
file_path_plan_2 = r'D:\Ama-VSProject\Plan_2_Results.xlsx'

sheet_name = 'Sheet1'  # Name of the sheet to read
search_keywords = ['COMMENTS', 'MD\n(FT)']  # Keywords to locate header row

# Locate header row based on keywords
header_row = find_header_row(file_path_pd_setting, sheet_name, search_keywords) #use the file path that needs the header row
if header_row is None:
    raise ValueError("Could not find a row containing all keywords as header.")

# Load the data, starting from the determined header row
df2 = pd.read_excel(file_path_pd_setting, sheet_name=sheet_name, header=header_row) #load with header row
# Normalize column names to be uppercase and stripped of extra spaces
df2.columns = df2.columns.str.strip().str.upper() #only the dataframe you find the header for needs this

try:
    df1 = pd.read_excel(file_path_plan_2)  # Read Plan_2_Results.xlsx with standard header
except FileNotFoundError:
    print(f"Error: File not found at {file_path_plan_2}")
    exit()
except Exception as e:
    print(f"An error occurred reading Plan_2_Results.xlsx: {e}")
    exit()

# Print the columns of both DataFrames for debugging
print("Columns in df1:", df1.columns.tolist())
print("Columns in df2:", df2.columns.tolist())

# Clean the Depth columns and force them to be numeric.
df1['Depth'] = pd.to_numeric(df1['Depth'], errors='coerce')
df2['Depth'] = pd.to_numeric(df2['Depth'], errors='coerce')

# Handle NaN values: crucial step!
print(f"Number of NaN values in df1['Depth']: {df1['Depth'].isna().sum()}")
print(f"Number of NaN values in df2['Depth']: {df2['Depth'].isna().sum()}")

df1 = df1.dropna(subset=['Depth'])
df2 = df2.dropna(subset=['Depth'])

#Confirm removal of NaN values
print(f"Number of NaN values in df1['Depth'] after removal: {df1['Depth'].isna().sum()}")
print(f"Number of NaN values in df2['Depth'] after removal: {df2['Depth'].isna().sum()}")

#Show some data from the dataframe to verify that is correct
print(df1.head())
print(df2.head())

# Perform the merge
merged_df = pd.merge(df1, df2, on='Depth', how='inner')  # Ensure 'Depth' is the common column

# Sort by Depth if desired (only works if Depth is numeric!)
merged_df = merged_df.sort_values('Depth')  # Assuming depth is in feet

# Output to Excel
merged_file_path = r'D:\Ama-VSProject\merged_PD_Setting_Formation.xlsx'
try:
    merged_df.to_excel(merged_file_path, index=False)
    print(f"✅ Merged file created successfully at {merged_file_path}")
except Exception as e:
    print(f"An error occurred writing to the Excel file: {e}")
