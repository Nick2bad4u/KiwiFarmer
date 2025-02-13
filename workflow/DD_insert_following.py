# -*- coding: UTF-8 -*-

"""Test initialization of the `Following` class.
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

PAGE_DIR = os.path.join('..', '..', 'data_20210224', 'downloaded_members_connections')
START = 0
DATABASE_FILE = 'kiwifarms_following_20210224.json'

###############################################################################

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def load_existing_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
                if not isinstance(data, dict):
                    logger.error(f"Existing data file {file_path} contains data of type {type(data)}, expected dict. Overwriting with empty dict.")
                    return {}
                return data
            except json.JSONDecodeError:
                logger.error(f"Existing data file {file_path} is corrupt. Overwriting with empty dict.")
                return {}
    return {}

def save_data(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

if __name__ == '__main__':
    # Load existing data as a dictionary with member_id as the key
    existing_data = load_existing_data(DATABASE_FILE)

    # Process HTML files of pages, insert fields into JSON
    # ---------------------------------------------------------------------------#

    pages = os.listdir(PAGE_DIR)
    pages = [p for p in pages if p.split('_')[1] == 'following']
    N_pages = len(pages)

    for i, page_file in enumerate(pages[START:]):
        logger.info(f'[ {i + START} / {N_pages} ] Processing {page_file}')
        try:
            with open(os.path.join(PAGE_DIR, page_file), 'r', encoding='utf-8') as f:
                following_page = BeautifulSoup(f.read(), 'lxml')
            following = base.Following(following_page=following_page)

            # Convert following details to a dictionary
            following_data = {
                'member_id': following.member_id,
                'following_list': following.following_list
            }

            # Check if the member already exists in the data
            if following.member_id in existing_data:
                # Update the existing member's data
                existing_data[following.member_id].update(following_data)
                logger.info(f'Updated existing member {following.member_id}')
            else:
                # Add a new member entry
                existing_data[following.member_id] = following_data
                logger.info(f'Added new member {following.member_id} to data list')

        except Exception as e:
            logger.error(f'Failed to process {page_file}: {e}')

    # Save all data to JSON file
    save_data(DATABASE_FILE, existing_data)

    logger.info("Script finished")

###############################################################################