# -*- coding: UTF-8 -*-

"""Generate list of all `page_url`s for all threads, using as input the directory
containing the HTML files for all threads.
"""

###############################################################################

import os
import logging
from bs4 import BeautifulSoup
from kiwifarmer import functions

###############################################################################

INPUT_DIR = '../../data_20210224/downloaded_threads/'
OUTPUT_DIR = '../../data_20210224'
PAGE_LIST_FILENAME = 'page_url_list.txt'

###############################################################################

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def generate_page_urls(input_dir, output_dir, page_list_filename):
    files = sorted(os.listdir(input_dir))
    all_pages = []

    for file in files:
        thread_output_dir = file[:-5]
        logger.info(f"Processing {file}")

        with open(os.path.join(input_dir, file), 'r') as f:
            soup = BeautifulSoup(f.read(), 'lxml')

        last_page = functions.get_thread_last_page(thread_page=soup)

        pages = [f'https://kiwifarms.st/threads/{file[:-5]}/page-{i}/' for i in range(1, last_page + 1)]
        all_pages.extend(pages)

    output_url_list = os.path.join(output_dir, page_list_filename)

    with open(output_url_list, 'w') as f:
        for page in all_pages:
            f.write(page + '\n')

    logger.info(f"Generated {len(all_pages)} page URLs")

if __name__ == '__main__':
    logger.info("Script started")
    generate_page_urls(INPUT_DIR, OUTPUT_DIR, PAGE_LIST_FILENAME)
    logger.info("Script finished")

###############################################################################