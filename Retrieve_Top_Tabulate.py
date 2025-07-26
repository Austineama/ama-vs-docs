import pandas as pd

# Load the Excel file
file_path = r'D:\Ama-VSProject\Plan_1.xlsx'
sheet_name = 'Sheet1'
header_row = 0
df = pd.read_excel(file_path, sheet_name=sheet_name, header=header_row)

# Use a list for flexibility and future updates
search_strings = [
    'AHMD', 'LHRR', 'RUML', 'CPCK', 
    'WARA', 'MDDD', 'SFNY', 'SCFS', 'SEFS'
]

# Use constants and strip column names to avoid errors from accidental whitespaces or hidden characters
SEARCH_COLUMN = 'Comments'.strip()
DEPTH_COLUMN = 'MD\n(ft)'.strip()

# Optional: use lowercase for consistent matching if needed
search_strings = [s.upper().strip() for s in search_strings]

# STEP 2: Apply filtering using .str.contains()
df_filtered = df[df[SEARCH_COLUMN].str.contains('|'.join(search_strings), na=False)]

# Check if necessary columns exist
missing_columns = []
if SEARCH_COLUMN not in df.columns:
    missing_columns.append(SEARCH_COLUMN)
if DEPTH_COLUMN not in df.columns:
    missing_columns.append(DEPTH_COLUMN)

if missing_columns:
    print(f"The following columns are missing in the Excel file: {', '.join(missing_columns)}")
else:
    # List to store DataFrames for each search string
    result_frames = []

    for search_string in search_strings:
        matching_rows = df[df[SEARCH_COLUMN].str.contains(search_string, case=False, na=False, regex=False)]
        # Create a DataFrame for each set of matches with the respective search string
        result_frame = pd.DataFrame({'Formation': search_string, 'Depth': matching_rows[DEPTH_COLUMN]})
        result_frames.append(result_frame)

    # Concatenate all DataFrames into a single DataFrame
    results = pd.concat(result_frames, ignore_index=True)
    
    # Display the result as a table
    print("Results:")
    print(results)
    
    # Save the results to a new Excel file
    results_file_path = r'D:\Ama-VSProject\Plan_1_Results.xlsx'
    results.to_excel(results_file_path, index=False, sheet_name='Results')
    print(f"Results have been saved to {results_file_path}")

# Debug: print all column names
print("Columns in the DataFrame:")
print(df.columns.tolist())

# Save the column names to an Excel file
columns_file_path = r'D:\Ama-VSProject\Plan_1_Columns.xlsx'
pd.DataFrame({'Columns': df.columns}).to_excel(columns_file_path, index=False, sheet_name='Columns')
print(f"Columns have been saved to {columns_file_path}")
