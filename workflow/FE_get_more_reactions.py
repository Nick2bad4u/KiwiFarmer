# -*- coding: UTF-8 -*-

"""Get reaction pages for posts with more than one page of reactions
"""

###############################################################################

import os
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed

from bs4 import BeautifulSoup
import pandas as pd
import mysql.connector  # type: ignore
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from kiwifarmer.utils import (
    reaction_filename_to_url,
    reaction_url_to_filename,
)
from kiwifarmer import base, templates

###############################################################################

SEMAPHORE = 20
THRESHOLD_KB = 15
URL_PATTERN = 'https://kiwifarms.st/posts/{}/reactions?reaction_id=0&list_only=1&page={}'
COMMAND = 'SELECT * FROM reactions'
DATABASE = 'kiwifarms_20210224'
START = 0

###############################################################################

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()


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


def save_content(content, output_dir, filename):
    output_file = os.path.join(output_dir, filename)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)


def process_reaction_page(page_file, output_dir, cursor):
    with open(os.path.join(output_dir, page_file), 'r', encoding='utf-8') as f:
        _reaction_page = BeautifulSoup(f.read(), 'lxml')

    reaction_page = base.ReactionPage(reaction_page=_reaction_page)
    reaction_soups = reaction_page.get_reaction_soups()
    post_id = reaction_page.post_id

    for j, reaction in enumerate(reaction_soups):
        reaction = base.Reaction(reaction=reaction, post_id=post_id)
        cursor.execute(templates.ADD_REACTION, reaction.reaction_insertion)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


def get_url_list(page):
    try:
        cnx = mysql.connector.connect(
            user=os.getenv('KIWIFARMER_USER'),
            password=os.getenv('KIWIFARMER_PASSWORD'),
            host='127.0.0.1',
            database=DATABASE,
            charset='utf8mb4',
            collation='utf8mb4_bin',
            use_unicode=True
        )

        _rdf = pd.read_sql(sql=COMMAND, con=cnx)
        cnx.close()

        rdf = _rdf.drop_duplicates()
        d = rdf.groupby('post_id')['post_id'].agg('count')
        rerun = [post_id for post_id, count in d.items() if count >=
                 (page * 50)]
        urls = [URL_PATTERN.format(post_id, page + 1) for post_id in rerun]

        return urls
    except mysql.connector.Error as err:
        logger.error(f"Error connecting to the database: {err}")
        return []

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


def run(page):
    output_dir = f'../../data_20210224/downloaded_reactions/page_{page + 1}'
    os.makedirs(output_dir, exist_ok=True)

    url_list = get_url_list(page)

    driver = setup_selenium()
    with ThreadPoolExecutor(max_workers=SEMAPHORE) as executor:
        futures = [executor.submit(download_page, url, driver)
                   for url in url_list]
        for future in as_completed(futures):
            content = future.result()
            if content:
                filename = reaction_url_to_filename(future.url)
                save_content(content, output_dir, filename)

    driver.quit()

    # ---------------------------------------------------------------------------#

    try:
        cnx = mysql.connector.connect(
            user=os.getenv('KIWIFARMER_USER'),
            password=os.getenv('KIWIFARMER_PASSWORD'),
            host='127.0.0.1',
            database=DATABASE,
            charset='utf8mb4',
            collation='utf8mb4_bin',
            use_unicode=True
        )
        cursor = cnx.cursor()

        # Process all reaction pages
        # ---------------------------------------------------------------------------#

        pages = os.listdir(output_dir)
        N_pages = len(pages)

        for i, page_file in enumerate(pages[START:]):
            logger.info(f'[ {i + START} / {N_pages} ] Processing {page_file}')
            try:
                process_reaction_page(page_file, output_dir, cursor)
                logger.info(f'Successfully processed {page_file}')
            except Exception as e:
                logger.error(f'Failed to process {page_file}: {e}')

        cnx.commit()
        cursor.close()
        cnx.close()
        logger.info("Committed changes to the database and closed connection")
    except mysql.connector.Error as err:
        logger.error(f"Error connecting to the database: {err}")

###############################################################################


for page in range(1, 20):
    run(page=page)

###############################################################################
