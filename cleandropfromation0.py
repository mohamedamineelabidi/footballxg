import pandas as pd
import os

# Load the combined data
combined_data_path = 'C:\\Users\\elabi\\Combined_Clubs_Data.xlsx'
combined_df = pd.read_excel(combined_data_path)

# Remove rows where all elements match the header row
header_row = combined_df.columns.tolist()
cleaned_df = combined_df[combined_df.ne(header_row).any(axis=1)]

# Drop duplicate rows
cleaned_df = cleaned_df.drop_duplicates()

# Handle missing values
# For this example, we fill missing values with 0; you can customize this as needed
cleaned_df = cleaned_df.fillna(0)

# Ensure consistent data types (assuming all numeric columns should be floats)
numeric_columns = ['xG', 'xGA', 'Poss', 'xA', 'KP', 'PPA', 'PrgP']
for col in numeric_columns:
    cleaned_df[col] = cleaned_df[col].astype(float)

# Drop rows where Formation is 0
cleaned_df = cleaned_df[cleaned_df['Formation'] != 0]

# Construct the Desktop path and ensure it exists
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
if not os.path.exists(desktop_path):
    os.makedirs(desktop_path)

cleaned_output_path = os.path.join(desktop_path, 'Cleaned_Combined_Clubs_Data.xlsx')

# Save the cleaned DataFrame to a new Excel file on the Desktop
cleaned_df.to_excel(cleaned_output_path, index=False)

print(f'Cleaned data saved to {cleaned_output_path}')
