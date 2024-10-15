import os
import csv
import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def perform_pos_tagging(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    # Tokenize the text
    tokens = nltk.word_tokenize(text)

    # Perform POS tagging
    tagged = nltk.pos_tag(tokens)

    return tagged

def process_files_in_folder(input_folder, output_folder):
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith('.txt'):  # Change the extension as needed
                input_file_path = os.path.join(root, file)
                output_file_path = os.path.join(output_folder, file.replace('.txt', '_pos_tagged.csv'))

                pos_tagged_data = perform_pos_tagging(input_file_path)

                with open(output_file_path, 'w', newline='') as output_file:
                    csv_writer = csv.writer(output_file)
                    csv_writer.writerow(['Word', 'POS Tag'])
                    csv_writer.writerows(pos_tagged_data)

                print(f'POS tagged information saved to {output_file_path}')

# Specify the input and output folder paths
input_folder_path = r'C:\\Users\\azrif\\Desktop\\ProjectGutenberg_Webcrawling-main\\sent_split_data\\sent_split_data\\'
output_folder_path = r'C:\\Users\\azrif\\Desktop\\ProjectGutenberg_Webcrawling-main\\tagger1_result'

# Process files in the specified input folder and save POS tagged information to the output folder
process_files_in_folder(input_folder_path, output_folder_path)
