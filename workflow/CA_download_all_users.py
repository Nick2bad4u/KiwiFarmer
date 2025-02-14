# -*- coding: UTF-8 -*-

"""Download and write to file the HTML for all KiwiFarms users.
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
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException, TimeoutException

###############################################################################

OUTPUT_DIR =os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'downloaded_members'))
LOGIN_URL = 'https://kiwifarms.st/login/'
URL_LIST_FILE =os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'member_url_list.txt'))

###############################################################################

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()


def setup_selenium():
    options = Options()
    options.headless = False  # Change to True if you want to run headless
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)
    return driver


def login_to_kiwifarms(driver):
    driver.get(LOGIN_URL)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    try:
        username_id = soup.find('input', {'autocomplete': 'username'})['id']
        password_id = soup.find('input', {'type': 'password'})['id']

        driver.find_element_by_id(username_id).send_keys(
            os.getenv('KIWIFARMS_USERNAME'))
        driver.find_element_by_id(password_id).send_keys(
            os.getenv('KIWIFARMS_PASSWORD'))
        driver.find_element_by_css_selector(
            '.button--primary.button.button--icon.button--icon--login').click()
        logger.info("Logged in successfully")
    except (NoSuchElementException, TimeoutException) as e:
        logger.error(f"Error during login: {e}")
        driver.quit()
        raise


def download_member_pages(driver, url_list, output_dir):
    for i, url in enumerate(url_list):
        logger.info(f"Processing {i}: {url}")
        try:
            driver.get(url + '#about')
            with open(os.path.join(output_dir, f'{i}.html'), 'w', encoding='utf-8') as f:
                f.write(driver.page_source)
            logger.info(f"Successfully downloaded {url}")
        except Exception as e:
            logger.error(f"Failed to download {url}: {e}")


if __name__ == '__main__':
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(URL_LIST_FILE, 'r') as f:
        url_list = f.read().splitlines()

    driver = setup_selenium()
    try:
        # login_to_kiwifarms(driver)
        download_member_pages(driver, url_list, OUTPUT_DIR)
    finally:
        driver.quit()
        logger.info("Script finished")

###############################################################################
