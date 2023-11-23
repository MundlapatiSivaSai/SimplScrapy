import requests
from bs4 import BeautifulSoup
import csv

def fetch_page(url):
    """
    Fetches the webpage at the given URL.

    Args:
    url (str): The URL of the webpage to fetch.

    Returns:
    str: The HTML content of the page, or None if there was an error.
    """
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_data(html, selector):
    """
    Extracts data from HTML based on the given CSS selector.

    Args:
    html (str): HTML content of the webpage.
    selector (str): CSS selector for the data to be extracted.

    Returns:
    list: A list of extracted data.
    """
    soup = BeautifulSoup(html, 'html.parser')
    elements = soup.select(selector)
    return [element.get_text().strip() for element in elements]

def save_to_csv(data, filename):
    """
    Saves the extracted data to a CSV file.

    Args:
    data (list): The data to be saved.
    filename (str): The name of the file to save the data.
    """
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow([row])

def main():
    """
    Main function to execute the web scraping.
    """
    url = 'https://www.promptcloud.com'  # Replace with your target URL
    selector = 'h1'  # Replace with your target element's CSS selector
    html = fetch_page(url)
    if html:
        data = extract_data(html, selector)
        save_to_csv(data, 'output.csv')
        print("Data scraping complete. Check output.csv for results.")

if __name__ == "__main__":
    main()
