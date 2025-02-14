# -*- coding: UTF-8 -*-

"""Download all pages for all threads using Selenium to bypass JavaScript challenges.
"""

###############################################################################

import os
import sys
import time
import logging

# Add the parent directory to the sys.path to import kiwifarmer module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from kiwifarmer import base, templates

###############################################################################

OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))

SITEMAPS = [
    'sitemap-1.xml',
    'sitemap-2.xml'
]

URL_PREFIX = 'https://kiwifarms.st/'

THREAD_PATTERN = 'https://kiwifarms.net/threads/'
MEMBER_PATTERN = 'https://kiwifarms.net/members/'

THREAD_LIST_FILENAME = 'thread_url_list.txt'
MEMBER_LIST_FILENAME = 'member_url_list.txt'

###############################################################################

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()


def download_sitemap_with_selenium(url):
    options = Options()
    options.headless = True  # Run in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)

    try:
        driver.get(url)
        time.sleep(10)  # Allow time for the JavaScript challenge to be solved

        content = driver.page_source
        return content
    except Exception as e:
        logger.error(f"Failed to download {url}: {e}")
        return None
    finally:
        driver.quit()


if __name__ == '__main__':

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for sitemap in SITEMAPS:

        sitemap_url = URL_PREFIX + sitemap
        sitemap_content = download_sitemap_with_selenium(sitemap_url)

        if sitemap_content:
            output_sitemap = os.path.join(OUTPUT_DIR, sitemap)
            with open(output_sitemap, 'w', encoding='utf-8') as f:
                f.write(sitemap_content)

            with open(output_sitemap, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f.read(), 'xml')

            urls = soup.find_all('url')
            urls = [url.find('loc').text for url in urls]

            thread_urls = [
                url for url in urls if url.startswith(THREAD_PATTERN)]
            member_urls = [
                url for url in urls if url.startswith(MEMBER_PATTERN)]

            # Ensure the thread_url_list and member_url_list are written correctly
            thread_url_list = os.path.join(OUTPUT_DIR, THREAD_LIST_FILENAME)
            with open(thread_url_list, 'a', encoding='utf-8') as f:
                for url in thread_urls:
                    f.write(url + '\n')

            member_url_list = os.path.join(OUTPUT_DIR, MEMBER_LIST_FILENAME)
            with open(member_url_list, 'a', encoding='utf-8') as f:
                for url in member_urls:
                    f.write(url + '\n')

            logger.info(
                f"Processed {sitemap}: {len(thread_urls)} thread URLs and {len(member_urls)} member URLs")

###############################################################################