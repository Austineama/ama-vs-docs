import pandas as pd

# Load the Excel file
df = pd.read_excel(r"D:\Ama-VSProject\SS_1.xlsx")

# First look at the data
df

# print all the column names
df.columns

print(df.head(25))  # Display the first few rows
df.dtypes  # Display data types of each column

# Save the combined DataFrame to an Excel file
df.to_excel(r"D:\Ama-VSProject\merged_BP_activity.xlsx", index=False)
print("merged DataFrame saved to 'merged_BP_activity.xlsx'.")
