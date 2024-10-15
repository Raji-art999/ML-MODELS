import os
import csv
from nltk.tokenize import sent_tokenize

# Path to the folder containing the files
folder_path = "/Users/sundaramrajashree/PycharmProjects/Webscraping/sent_split_data/acad_1990"

# Get a list of files in the folder
files = os.listdir(folder_path)

# Output CSV file path
output_csv_file = "tokenized_sentences.csv"

# Open CSV file for writing
with open(output_csv_file, 'w', newline='', encoding='utf-8') as csv_file:  # Change encoding if needed
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['File Name', 'Sentence'])

    # Iterate over each file
    for file_name in files:
        # Construct the full path to the file
        file_path = os.path.join(folder_path, file_name)

        # Read the contents of the file
        with open(file_path, 'r', encoding='latin-1') as file:  # Try 'latin-1' encoding
            text = file.read()

        # Tokenize the text
        sentences = sent_tokenize(text)

        # Write tokenized sentences to CSV
        for sentence in sentences:
            csv_writer.writerow([file_name, sentence])

print(f'Tokenized sentences saved to {output_csv_file}')
