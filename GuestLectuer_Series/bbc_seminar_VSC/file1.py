import requests
from bs4 import BeautifulSoup

# URL of the BBC webpage
url = "https://www.bbc.com/"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example 1: Using find_all() to find all <a> tags
    all_a_tags = soup.find_all('a')
    print("Example 1 - Find All <a> Tags:")
    for tag in all_a_tags[:5]:  # Print the first 5 tags for brevity
        print(tag)

    # Example 2: Using find() to find the first <h1> tag
    first_h1_tag = soup.find('h1')
    print("\nExample 2 - Find First <h1> Tag:")
    print(first_h1_tag)



else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
