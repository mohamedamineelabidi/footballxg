import os
import pandas as pd

# Directory containing the Excel files
input_directory = r'C:\Users\elabi\output'
output_file_path = r'C:\Users\elabi\Combined_Clubs_Data.xlsx'

# Define the columns to extract
stats_columns = ['Formation', 'xG', 'xGA', 'Poss']
match_logs_columns = ['xA', 'KP', 'PPA', 'PrgP']

# Initialize an empty DataFrame to store the combined data
combined_df = pd.DataFrame()

# Loop through each file in the directory
for filename in os.listdir(input_directory):
    if filename.endswith('.xlsx'):
        file_path = os.path.join(input_directory, filename)
        
        # Load the necessary sheets from the Excel file
        stats_df = pd.read_excel(file_path, sheet_name='Stats')
        match_logs_df = pd.read_excel(file_path, sheet_name='Match Logs')
        
        # Extract the columns
        stats_extracted = stats_df[stats_columns]
        match_logs_extracted = match_logs_df[match_logs_columns]
        
        # Combine the extracted columns into a single DataFrame
        combined_data = pd.concat([stats_extracted, match_logs_extracted], axis=1)
        
        # Append to the consolidated DataFrame
        combined_df = pd.concat([combined_df, combined_data], ignore_index=True)

# Save the consolidated DataFrame to a new Excel file
combined_df.to_excel(output_file_path, index=False)

print(f'Consolidated data saved to {output_file_path}')

