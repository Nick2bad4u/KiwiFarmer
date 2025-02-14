# -*- coding: UTF-8 -*-

"""Download and write to file the HTML for the reaction pages of all posts.
"""

###############################################################################

import os
import logging
import sys

# Add the parent directory to the sys.path to import kiwifarmer module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

###############################################################################

URL_LIST_FILE = os.path.join('..', '..', 'data_20210224', 'reaction_url_list.txt')
OUTPUT_DIR = os.path.join('..', '..', 'data_20210224', 'downloaded_reactions')
NUM_THREADS = 1
THRESHOLD_KB = 7
MAX_RETRIES = 3

###############################################################################

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def load_url_list(file_path):
    with open(file_path, 'r') as f:
        url_list = f.read().splitlines()
    url_list = list(filter(None, url_list))
    return url_list

def setup_selenium():
    options = Options()
    options.headless = True  # Run in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)
    return driver

def download_page(url, driver, first_run=False):
    try:
        if first_run:
            time.sleep(7)
        else:
            time.sleep(2)
        driver.get(url)
        content = driver.page_source
        return content
    except Exception as e:
        logger.error(f"Failed to download {url}: {e}")
        return None

def save_content(content, filename):
    output_file = os.path.join(OUTPUT_DIR, filename)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

def url_to_filename(url):
    # Extract the post ID and page number from the URL
    parts = url.split('/')
    post_id = parts[4]  # Get the post ID from the URL
    page_param = url.split('page=')[-1]  # Extract the page number
    return f'posts_{post_id}_reactions_page_{page_param}.html'

def process_url(driver, url, downloaded_files):
    filename = url_to_filename(url)
    if filename in downloaded_files:
        logger.info(f"Skipping already downloaded file: {filename}")
        return

    retries = 0
    while retries < MAX_RETRIES:
        content = download_page(url, driver)
        if content:
            size_kb = len(content.encode('utf-8')) / 1024
            if size_kb >= THRESHOLD_KB:
                save_content(content, filename)
                downloaded_files.add(filename)
                break
            else:
                logger.info(f"Retry {retries+1}/{MAX_RETRIES}: File {filename} below size threshold ({size_kb:.2f} KB). Retrying...")
        retries += 1

def download_many_files(url_list):
    driver = setup_selenium()
    downloaded_files = set(os.listdir(OUTPUT_DIR))
    with ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
        futures = [executor.submit(process_url, driver, url, downloaded_files) for url in url_list]
        for future in as_completed(futures):
            future.result()
    driver.quit()

if __name__ == '__main__':
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    logger.info(f"Loading URL list from {URL_LIST_FILE}")
    url_list = load_url_list(URL_LIST_FILE)
    logger.info(f"Loaded {len(url_list)} URLs")

    logger.info("Starting download of reaction pages")
    download_many_files(url_list)
    logger.info("Completed download of reaction pages")
    logger.info("Script finished")

###############################################################################
