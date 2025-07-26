import pandas as pd

# Read the two Excel files
df1 = pd.read_excel(r'D:\Ama-VSProject\Data\Activity_reading.xlsx')
df2 = pd.read_excel(r'D:\Ama-VSProject\Data\BP_reading.xlsx')

# Convert Date columns to datetime
df1['Date'] = pd.to_datetime(df1['Date'])
df2['Date'] = pd.to_datetime(df2['Date'])

# Merge both dataframes on 'Date'
merged_df = pd.merge(df2, df1, on='Date', how='left')  # keeps all BP readings, joins Activity by Date

# Sort by Date (optional)
merged_df = merged_df.sort_values('Date')

# Save the result
merged_df.to_excel(r'D:\Ama-VSProject\merged_Sorted_BP_activity.xlsx', index=False)

print("✅ Merged file created successfully at D:\\Ama-VSProject\\merged_BP_activity.xlsx")
