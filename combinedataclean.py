import pandas as pd

# Load the combined data
combined_data_path = 'C:\\Users\\elabi\\Combined_Clubs_Data.xlsx'
combined_df = pd.read_excel(combined_data_path)

# Remove rows where all elements match the header row
header_row = combined_df.columns.tolist()
cleaned_df = combined_df[combined_df.ne(header_row).any(axis=1)]

# Save the cleaned DataFrame to a new Excel file
cleaned_output_path = 'C:\\Users\\elabi\\Cleaned_Combined_Clubs_Data.xlsx'
cleaned_df.to_excel(cleaned_output_path, index=False)

print(f'Cleaned data saved to {cleaned_output_path}')

