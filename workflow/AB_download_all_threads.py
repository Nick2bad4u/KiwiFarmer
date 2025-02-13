"""Download all pages for all threads using Selenium.
"""

###############################################################################

import os
import sys
import time
import logging

# Add the parent directory to the sys.path to import kiwifarmer module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from concurrent.futures import ThreadPoolExecutor, as_completed

from kiwifarmer.utils import (
    page_filename_to_url,
    page_url_to_filename,
)

###############################################################################

URL_LIST_FILE = os.path.join('..', '..', 'data_20210224', 'thread_url_list.txt')
OUTPUT_DIR = os.path.join('..', '..', 'data_20210224', 'downloadedThreads')
NUM_THREADS = 1
THRESHOLD_KB = 20

###############################################################################

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()


def load_url_list(file_path):
    with open(file_path, 'r') as f:
        url_list = f.read().splitlines()
    return url_list


def setup_selenium():
    options = Options()
    options.headless = True  # Run in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)
    return driver


def download_page(url, driver):
    try:
        driver.get(url)
        time.sleep(5)  # Allow time for the page to load
        content = driver.page_source
        return content
    except Exception as e:
        logger.error(f"Failed to download {url}: {e}")
        return None


def save_content(content, url):
    filename = page_url_to_filename(url)
    output_file = os.path.join(OUTPUT_DIR, filename)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)


def process_urls(url_list):
    driver = setup_selenium()
    for url in url_list:
        content = download_page(url, driver)
        if content:
            save_content(content, url)
    driver.quit()


def download_many_files(url_list):
    # Split the URL list into chunks based on the number of threads
    chunk_size = len(url_list) // NUM_THREADS
    url_chunks = [url_list[i:i + chunk_size] for i in range(0, len(url_list), chunk_size)]

    with ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
        futures = [executor.submit(process_urls, chunk) for chunk in url_chunks]
        for future in as_completed(futures):
            future.result()


if __name__ == '__main__':
    logger.info("Script started")
    logger.info(f"Loading URL list from {URL_LIST_FILE}")
    url_list = load_url_list(URL_LIST_FILE)
    logger.info(f"Loaded {len(url_list)} URLs")

    logger.info("Starting download of threads")
    download_many_files(url_list)
    logger.info("Completed download of threads")
    logger.info("Script finished")

###############################################################################