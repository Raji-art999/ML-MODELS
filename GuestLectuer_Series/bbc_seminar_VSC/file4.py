import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the BBC Sport section
url = 'https://www.bbc.com/sport'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all links (anchor tags) on the page
    links = soup.find_all('a')

    # Create a list to store sports-related URLs
    sports_urls = [link['href'] for link in links if '/sport/' in link.get('href', '')]

else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")

# Write the URLs to a text file
with open('sports_urls.txt', 'w', encoding='utf-8') as text_file:
    for url in sports_urls:
        text_file.write(url + '\n')

print("Sports URLs have been saved to 'sports_urls.txt'.")
