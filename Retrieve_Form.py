import pandas as pd

# Replace 'your_excel_file.xlsx' with the actual file path
df = pd.read_excel(r'D:\Ama-VSProject\Plan_1.xlsx', sheet_name='Sheet1', header=0)
print(df.columns.tolist())

# Define the string to search for and the column to search within
search_string = 'AHMD'
search_column = 'Comments'

# Define the column from which to retrieve corresponding values
depth_column = 'MD\n(ft)'

# Use boolean indexing to filter rows containing the search string
# .str.contains() is used for string matching, case=False for case-insensitive search
matching_rows = df[df[search_column].str.contains(search_string, case=False, na=False)]
# Extract the 'MD' column from the filtered rows
# Retrieve the corresponding values from the 'depth_column'
corresponding_values = matching_rows[depth_column]


if search_column not in df.columns:
    print(f"Column '{search_column}' not found in the Excel file.")
elif depth_column not in df.columns:
    print(f"Column '{depth_column}' not found in the Excel file.")
else:
    matching_rows = df[df[search_column].astype(str).str.contains(search_string, case=False, na=False)]
    corresponding_values = matching_rows[depth_column]
    print(corresponding_values)

print(df.columns)

print([column for column in df.columns])

print(f"Search string '{search_string}' found in the '{search_column}' column.")

print(corresponding_values)

   