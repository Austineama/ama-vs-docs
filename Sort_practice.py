#import necessary libraries-Panda
import pandas as pd
# This script sorts a DataFrame by the 'Date' column and saves it to an Excel file.
# Load the Excel file
Data_df = pd.read_excel(r'D:\Ama-VSProject\Data.xlsx')

#convert 'Date' column to datetime format
Data_df['Date'] = pd.to_datetime(Data_df['Date'])

# Sort the DataFrame by 'Date' column
Data_df = Data_df.sort_values(by='Date')

#show the first few rows of the sorted DataFrame
print(Data_df.head())  # Display the first few rows

# Save the sorted DataFrame to an Excel file
Data_df.to_excel(r'D:\Ama-VSProject\Sorted_Data.xlsx', index=False)
 
print("Sorted DataFrame saved to 'Sorted_Data.xlsx'.")
