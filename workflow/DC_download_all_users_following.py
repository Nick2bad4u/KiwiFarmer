# -*- coding: UTF-8 -*-

"""Download and write to file the HTML for the connection pages (followers and following) of all KiwiFarms users.
"""

###############################################################################

import os
import logging
import sys
from urllib.parse import urlparse

# Add the parent directory to the sys.path to import kiwifarmer module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from concurrent.futures import ThreadPoolExecutor, as_completed

###############################################################################

URL_LIST_FILE =os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'connection_url_list.txt'))
OUTPUT_DIR =os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'downloaded_members_connections'))
NUM_THREADS = 1
THRESHOLD_KB = 15

###############################################################################

URL_BASE = 'https://kiwifarms.net/members/'

def get_filename_from_url(url):
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.strip('/').split('/')
    user_id = path_parts[1]
    connection_type = path_parts[2]
    page_number = path_parts[3].replace('page-', '')
    filename = f"{user_id}.{connection_type}.connections.page{page_number}.html"
    return filename

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


def download_page(url, driver):
    try:
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


def process_url(url, driver):
    content = download_page(url, driver)
    if content:
        filename = get_filename_from_url(url)
        save_content(content, filename)


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

    logger.info("Starting download of connection pages")
    download_many_files(url_list)
    logger.info("Completed download of connection pages")
    logger.info("Script finished")
