import os
import re

def remove_tags(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Remove <a>, <p>, and <h> tags using regular expression
    content_without_tags = re.sub(r'<a\b[^>]*>|<p\b[^>]*>|<h\b[^>]*>', '', content)

    with open(file_path, 'w') as file:
        file.write(content_without_tags)

def process_files_in_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.txt'):  # Change the extension as needed
                file_path = os.path.join(root, file)
                remove_tags(file_path)
                print(f'Removed <a>, <p>, and <h> tags from {file_path}')

# Specify the folder path
folder_path = '/Users/sundaramrajashree/PycharmProjects/Webscraping/sent_split_data'

# Process files in the specified folder
process_files_in_folder(folder_path)
