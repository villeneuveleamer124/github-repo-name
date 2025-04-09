import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to retrieve {url}")

html_content = fetch_html("https://example.com")
soup = BeautifulSoup(html_content, "html.parser")

# Example: Extract text content from the HTML
text_content = soup.get_text()

print(text_content)
