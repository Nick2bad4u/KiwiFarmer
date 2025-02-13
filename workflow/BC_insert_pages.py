"""
This script processes HTML files of Kiwifarms thread pages, extracts
relevant information from each post, and inserts it into a JSON file.

The script iterates through HTML files located in the `PAGE_DIR` directory,
parses each file using BeautifulSoup, and extracts individual posts. For each
post, it extracts data such as author, content, and associated blockquotes,
links, and images. This data is then inserted into a JSON file specified by
the `DATABASE_FILE` constant.

The script uses logging to log progress and errors during execution.

Constants:
    PAGE_DIR (str): Relative path to the directory containing the downloaded
        HTML pages.
    START (int): Starting index for processing pages in the directory.
    DATABASE_FILE (str): Path to the JSON file to save the extracted data.
"""

###############################################################################

import os
import logging
import sys
import json

# Add the parent directory to the sys.path to import kiwifarmer module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bs4 import BeautifulSoup
from kiwifarmer import base

###############################################################################

PAGE_DIR = os.path.join('..', '..', 'data_20210224', 'downloaded_pages')
START = 0
DATABASE_FILE = 'kiwifarms_20210224.json'

###############################################################################

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def load_existing_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return []

def save_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == '__main__':
    # Load existing data
    data = load_existing_data(DATABASE_FILE)

    # Process HTML files of pages, insert fields into JSON
    # ---------------------------------------------------------------------------#

    pages = os.listdir(PAGE_DIR)
    N_pages = len(pages)

    for i, page_file in enumerate(pages[START:]):
        logger.info(f'[ {i + START} / {N_pages} ] Processing {page_file}')

        with open(os.path.join(PAGE_DIR, page_file), 'r', encoding='utf-8') as f:
            thread_page = BeautifulSoup(f.read(), 'lxml')

        try:
            page = base.Page(thread_page=thread_page)

            # Ensure thread_id and thread_title attributes are available
            thread_id = getattr(page, 'thread_id', None)
            thread_title = getattr(page, 'title', None)
            if thread_id is None or thread_title is None:
                raise AttributeError("Missing thread_id or thread_title")

            post_soups = page.get_post_soups()

            for j, post_soup in enumerate(post_soups):
                post = base.Post(post=post_soup)

                post_data = {
                    'thread_id': thread_id,
                    'thread_title': thread_title,
                    'post_id': post.post_id,
                    'author': post.author,
                    'content': post.content,
                    'timestamp': post.timestamp,
                    'blockquotes': post.blockquotes,
                    'links': post.links,
                    'images': post.images
                }

                data.append(post_data)
                logger.info(f'Successfully added post {j + 1} from {page_file} to data list')
        except AttributeError as e:
            logger.error(f'Failed to process {page_file}: {e}')

    # Save all data to JSON file
    save_data(DATABASE_FILE, data)

    logger.info('Script finished')

###############################################################################