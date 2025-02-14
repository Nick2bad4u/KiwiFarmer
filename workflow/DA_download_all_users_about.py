# -*- coding: UTF-8 -*-

"""Download and write to file the HTML for the 'About' section of all KiwiFarms users.
"""

###############################################################################

import os
import logging
import sys

# Add the parent directory to the sys.path to import kiwifarmer module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from concurrent.futures import ThreadPoolExecutor, as_completed
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs

###############################################################################

URL_LIST_FILE = os.path.join('..', '..', 'data_20210224', 'member_url_list.txt')
OUTPUT_DIR = os.path.join('..', '..', 'data_20210224', 'downloaded_members_about')
NUM_THREADS = 1

###############################################################################

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()


def load_url_list(file_path):
    with open(file_path, 'r') as f:
        url_list = f.read().splitlines()
    url_list = list(filter(None, url_list))
    url_list = [url.rstrip('/') + '/about' for url in url_list]
    return url_list


def setup_selenium():
    options = Options()
    options.headless = True  # Run in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
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


def get_filename_from_url(url):
    parsed_url = urlparse(url)
    user_id = parsed_url.path.split('/')[-3:-1]
    filename = '.'.join(user_id) + '.about.html'
    return filename


def save_content(content, filename):
    output_file = os.path.join(OUTPUT_DIR, filename)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)


def process_url(url, driver):
    filename = get_filename_from_url(url)
    output_file = os.path.join(OUTPUT_DIR, filename)

    # Check if the file already exists
    if not os.path.exists(output_file):
        content = download_page(url, driver)
        if content:
            save_content(content, filename)
    else:
        logger.info(f"Skipping {url}, already downloaded")


def download_many_files(url_list):
    driver = setup_selenium()
    with ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
        futures = [executor.submit(process_url, url, driver) for url in url_list]
        for future in as_completed(futures):
            future.result()
    driver.quit()


if __name__ == '__main__':
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    logger.info(f"Loading URL list from {URL_LIST_FILE}")
    url_list = load_url_list(URL_LIST_FILE)
    logger.info(f"Loaded {len(url_list)} URLs")

    logger.info("Starting download of 'About' pages")
    download_many_files(url_list)
    logger.info("Completed download of 'About' pages")
    logger.info("Script finished")

###############################################################################
