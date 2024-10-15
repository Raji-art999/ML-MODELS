import requests
from bs4 import BeautifulSoup

# URL of the webpage
url = "https://www.bbc.com/"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all <h3> elements
    all_h3_elements = soup.find_all('h3')

    # Create or open a text file to save the extracted text
    with open("extracted_texts.txt", "w", encoding="utf-8") as text_file:
        # Extract and save the text between <a> and </a> tags within <h3> elements
        for h3_element in all_h3_elements:
            # Find <a> tags within the <h3> element
            a_tags = h3_element.find_all('a')

            # Extract and save the text within <a> tags
            for a_tag in a_tags:
                link_text = a_tag.get_text(strip=True)
                if link_text:
                    text_file.write(link_text + "\n")

    print("Text has been saved to 'extracted_texts.txt'")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")