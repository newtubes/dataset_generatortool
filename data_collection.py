

import logging
import requests
from bs4 import BeautifulSoup

def collect_data(urls, output_path):
    """
    Collects data from a list of URLs and appends it to a file.
    """
    for url in urls:
        logging.info(f"Starting data collection from {url}...")
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for bad status codes
            soup = BeautifulSoup(response.content, "html.parser")
            text = soup.get_text(separator='\n', strip=True)
            with open(output_path, "a", encoding="utf-8") as f:  # Use "a" for append mode
                f.write(text + "\n\n")  # Add some separation between content from different URLs
            logging.info(f"Successfully collected data from {url} and appended to {output_path}")
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to collect data from {url}. Error: {e}")
        except Exception as e:
            logging.error(f"An unexpected error occurred while collecting data from {url}: {e}")

