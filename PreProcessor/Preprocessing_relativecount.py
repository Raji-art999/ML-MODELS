import pandas as pd

# Read the first CSV file
df1 = pd.read_csv('/Users/sundaramrajashree/PycharmProjects/Webscraping/tagger1_counts/aggregated_tagger1_counts.csv')

# Read the second CSV file
df2 = pd.read_csv('/Users/sundaramrajashree/PycharmProjects/Webscraping/output_folder/total_words_summary.csv')

# Extract relevant columns from the first file
columns_to_match = df1.columns[1:]

# Initialize the output dataframe
result_df = pd.DataFrame(columns=['Filename'] + list(columns_to_match))

# Strip extra words from 'Filename' column in df1
df1['Filename'] = df1['Filename'].str.replace('_pos_tagged$', '', regex=True)

# Iterate through rows in the second file
for index, row in df2.iterrows():
    filename = row['Filename']
    total_words = row['Total Words']

    # Strip extra words from the filename in df2
    filename = filename.replace('_pos_tagged', '')

    # Check if the filename (after stripping extra words) exists in the first file
    if filename in df1['Filename'].values:
        # Extract the corresponding row from the first file
        match_row = df1[df1['Filename'] == filename][columns_to_match].iloc[0]

        # Divide each value in the row by total_words
        match_row = (match_row / total_words) * 10000

        # Concatenate the row to the result dataframe
        result_df = pd.concat([result_df, pd.DataFrame({'Filename': [filename], **match_row})], ignore_index=True)
        print(result_df)
    else:
        print(f"Filename '{filename}' not found in df1.")

# Save the result dataframe to a new CSV file
result_df.to_csv('/Users/sundaramrajashree/PycharmProjects/Webscraping/tagger1_counts/frequency_count_tagger1_result.csv', index=False)
