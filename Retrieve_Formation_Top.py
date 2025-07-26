import pandas as pd
from streamlit import header

# Load the Excel file
file_path = r'D:\Ama-VSProject\Plan_1.xlsx'
sheet_name = 'Sheet1'
header_row = 0
df = pd.read_excel(file_path, sheet_name=sheet_name, header=header_row)

# Define the strings to search for and the column to search within
search_strings = ('AHMD', 'LHRR', 'RUML', 'CPCK', 'WARA', 'MDDD', 'SFNY', 'SCFS', 'SEFS')
search_column = 'Comments'
depth_column = 'MD\n(ft)'

# Check if necessary columns exist
missing_columns = []
if search_column not in df.columns:
    missing_columns.append(search_column)
if depth_column not in df.columns:
    missing_columns.append(depth_column)

if missing_columns:
    print(f"The following columns are missing in the Excel file: {', '.join(missing_columns)}")
else:
    # List to store DataFrames for each search string
    result_frames = []

    for search_string in search_strings:
        matching_rows = df[df[search_column].str.contains(search_string, case=False, na=False, regex=False)]
        # Create a DataFrame for each set of matches with the respective search string
        result_frame = pd.DataFrame({'Formation': search_string, 'Depth': matching_rows[depth_column]})
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
