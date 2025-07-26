import pandas as pd
import matplotlib.pyplot as plt

# Load the merged data (adjust path if needed)
merged_df = pd.read_excel(r'D:\Ama-VSProject\merged_BP_activity.xlsx')

print(merged_df.columns)

# Ensure 'Date' is datetime
merged_df['Date'] = pd.to_datetime(merged_df['Date'])

# Create the plot
plt.figure(figsize=(12, 6))
ax1 = plt.gca()
ax1.plot(merged_df['Date'], merged_df['Total steps'], label='Total steps', color='green')
ax1.set_ylabel('Total steps', color='green')
ax1.tick_params(axis='y', labelcolor='green')

ax2 = ax1.twinx()
ax2.plot(merged_df['Date'], merged_df['Systolic (mmHg)'], label='Systolic (mmHg)', color='red')
ax2.plot(merged_df['Date'], merged_df['Diastolic (mmHg)'], label='Diastolic (mmHg)', color='blue')
ax2.set_ylabel('Blood Pressure', color='red')
ax2.tick_params(axis='y', labelcolor='red')

plt.title('Total steps vs Blood Pressure Over Time')
ax1.set_xlabel('Date')
ax2.legend(loc='upper right')
plt.tight_layout()
plt.show()

import pandas as pd
from scipy.stats import pearsonr

# Assuming merged_df is your DataFrame
Total_steps = merged_df['Total steps']
Systolic_mmHg = merged_df['Systolic (mmHg)']
Diastolic_mmHg = merged_df['Diastolic (mmHg)']

# Calculate Pearson correlation
corr_Total_steps_Systolic_mmHg, _ = pearsonr(Total_steps, Systolic_mmHg)
corr_Total_steps_Diastolic_mmHg, _ = pearsonr(Total_steps, Diastolic_mmHg)

print(f"Correlation between Total steps and Systolic (mmHg): {corr_Total_steps_Systolic_mmHg:.2f}")
print(f"Correlation between Total steps and Diastolic (mmHg): {corr_Total_steps_Diastolic_mmHg:.2f}")


import matplotlib.pyplot as plt

plt.figure(figsize=(12, 5))

# Scatter plot for Total steps vs Systolic (mmHg)
plt.subplot(1, 2, 1)
plt.scatter(Total_steps, Systolic_mmHg, c='red', alpha=0.5)
plt.title('Total steps vs Systolic (mmHg)')
plt.xlabel('Total steps')
plt.ylabel('Systolic (mmHg)')

# Scatter plot for Total steps vs Diastolic
plt.subplot(1, 2, 2)
plt.scatter(Total_steps, Diastolic_mmHg, c='blue', alpha=0.5)
plt.title('Total steps vs Diastolic (mmHg)')
plt.xlabel('Total steps')
plt.ylabel('Diastolic (mmHg)')

plt.tight_layout()
plt.show()


from scipy.stats import pearsonr

# Calculate Pearson correlation


merged_df['Total steps'].fillna(merged_df['Total steps'].mean(), inplace=True)
merged_df['Systolic (mmHg)'].fillna(merged_df['Systolic (mmHg)'].mean(), inplace=True)
merged_df['Diastolic (mmHg)'].fillna(merged_df['Diastolic (mmHg)'].mean(), inplace=True)

# Correlation
corr_steps_systolic, p_systolic = pearsonr(merged_df['Total steps'], merged_df['Systolic (mmHg)'])
corr_steps_diastolic, p_diastolic = pearsonr(merged_df['Total steps'], merged_df['Diastolic (mmHg)'])

print(f"Correlation between Total Steps and Systolic (mmHg): {corr_steps_systolic:.2f}, p-value: {p_systolic:.4f}")
print(f"Correlation between Total Steps and Diastolic (mmHg): {corr_steps_diastolic:.2f}, p-value: {p_diastolic:.4f}")

# Regression
X = sm.add_constant(merged_df['Total steps'])

y_systolic = merged_df['Systolic (mmHg)']
y_diastolic = merged_df['Diastolic (mmHg)']

model_systolic = sm.OLS(y_systolic, X).fit()
model_diastolic = sm.OLS(y_diastolic, X).fit()

print(model_systolic.summary())
print(model_diastolic.summary())
