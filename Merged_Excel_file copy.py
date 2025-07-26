import pandas as pd

# Read the two Excel files
df1 = pd.read_excel(r"D:\Ama-VSProject\Data\Activity_reading.xlsx")
df2 = pd.read_excel(r"D:\Ama-VSProject\Data\BP_reading.xlsx")

# Spot-check first few rows of Date columns
print(df1["Date"].head())
print(f"Invalid dates: {df1['Date'].isnull().sum()}")  # Count bad conversions

# Spot-check first few rows of Date columns
print(df2["Date"].head())
print(f"Invalid dates: {df2['Date'].isnull().sum()}")

# Convert Date columns to datetime (optional, but good practice)
df1["Date"] = pd.to_datetime(df1["Date"], format="mixed")
df2["Date"] = pd.to_datetime(df2["Date"], format="mixed")

# Merge both dataframes on 'Date'
merged_df = pd.merge(
    df2, df1, on="Date", how="left"
)  # keeps all BP readings, joins Activity by Date

# Save the result
merged_df.to_excel(r"D:\Ama-VSProject\merged_BP_activity.xlsx", index=False)

print(
    "✅ Merged file created successfully at D:\\Ama-VSProject\\merged_BP_activity.xlsx"
)
