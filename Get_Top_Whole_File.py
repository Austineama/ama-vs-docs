import pandas as pd  # Import pandas for data handling
import re  # Import regex library for pattern matching

# Function to find the header row dynamically
def find_header_row(file_path, sheet_name, keywords, max_rows=30):
    # Read a few rows from the Excel file to find the header
    preview = pd.read_excel(file_path, sheet_name=sheet_name, header=None, nrows=max_rows)
    for i, row in preview.iterrows():
        # Convert each cell to uppercase strings for comparison
        normalized_row = [str(cell).strip().upper() for cell in row]
        # Check if all keywords are present in the row
        if all(any(keyword in cell for cell in normalized_row) for keyword in keywords):
            return i  # Return the row number if found
    return None  # Return None if header row isn't found

# Set up file paths and configuration
file_path = r'D:\Ama-VSProject\Plan_2.xlsx'  # Path to your Excel file
sheet_name = 'Sheet1'  # Name of the sheet to read
search_keywords = ['COMMENTS', 'MD\n(FT)']  # Keywords to locate header row

# Locate header row based on keywords
header_row = find_header_row(file_path, sheet_name, search_keywords)
if header_row is None:
    raise ValueError("Could not find a row containing all keywords as header.")

# Load the data, starting from the determined header row
df = pd.read_excel(file_path, sheet_name=sheet_name, header=header_row)

# Normalize column names to be uppercase and stripped of extra spaces
df.columns = df.columns.str.strip().str.upper()

# Define strings to search for in the data
search_strings = ['AHMD', 'LHRR', 'RUML', 'CPCK', 'WARA', 'MDDD', 'SFNY', 'SCFS', 'SEFS']

# Make sure search strings are in uppercase and stripped
search_strings = [s.upper().strip() for s in search_strings]

# Specify the exact column names after normalization
SEARCH_COLUMN = 'COMMENTS'
DEPTH_COLUMN = 'MD\n(FT)'

# Check if the required columns exist
missing_columns = []
if SEARCH_COLUMN not in df.columns:
    missing_columns.append(SEARCH_COLUMN)
if DEPTH_COLUMN not in df.columns:
    missing_columns.append(DEPTH_COLUMN)

# Raise an error if any columns are missing
if missing_columns:
    raise ValueError(f"The following columns are missing in the Excel file: {', '.join(missing_columns)}")

# Try filtering the data with simple string matching
try:
    df[SEARCH_COLUMN] = df[SEARCH_COLUMN].astype(str).str.upper()  # Convert entries to uppercase strings
    df_filtered = df[df[SEARCH_COLUMN].str.contains('|'.join(search_strings), na=False)]
    print("✅ Used clean .contains() filtering.")
except Exception as e:
    print("⚠️ Using regex method due to issues with .contains() filtering.")
    print(f"Error: {e}")
    # Use regex for robust searching in case of errors
    pattern = re.compile(r'|'.join(map(re.escape, search_strings)), re.IGNORECASE)
    df_filtered = df[df[SEARCH_COLUMN].apply(lambda x: bool(pattern.search(str(x))))]

# Process results only if data is found
if not df_filtered.empty:
    result_frames = []  # List to collect matching data
    for search_string in search_strings:
        # Find rows matching each search string
        matching_rows = df[df[SEARCH_COLUMN].str.contains(search_string, case=False, na=False, regex=False)]
        if not matching_rows.empty:
            # Store found data with the associated search string
            result_frame = pd.DataFrame({'Formation': search_string, 'Depth': matching_rows[DEPTH_COLUMN]})
            result_frames.append(result_frame)
    
    # Concatenate all results into a single table
    if result_frames:
        results = pd.concat(result_frames, ignore_index=True)
        print("Results:")
        print(results)
        
        # Save results to a new Excel file
        results_file_path = r'D:\Ama-VSProject\Plan_2_Results.xlsx'
        results.to_excel(results_file_path, index=False, sheet_name='Results')
        print(f"Results have been saved to {results_file_path}")
    else:
        print("No matching rows were processed into a result frame.")
else:
    print("No matching data found to process.")

# Print all column names in the DataFrame
print("Columns in the DataFrame:")
print(df.columns.tolist())

# Save the column names to an Excel file for reference
columns_file_path = r'D:\Ama-VSProject\Plan_2_Columns.xlsx'

pd.DataFrame({'Columns': df.columns}).to_excel(columns_file_path, index=False, sheet_name='Columns')
print(f"Columns have been saved to {columns_file_path}")

print("Script completed successfully.")
