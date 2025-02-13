# -*- coding: UTF-8 -*-

"""Test initialization of the `TrophyPage` class.
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

PAGE_DIR = os.path.join('..', '..', 'data_20210224', 'downloaded_members')
START = 0
DATABASE_FILE = 'kiwifarms_trophies_20210224.json'

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
    N_pages = len(pages)

    for i, page_file in enumerate(pages[START:]):
        logger.info(f'[ {i + START} / {N_pages} ] Processing {page_file}')
        try:
            with open(os.path.join(PAGE_DIR, page_file), 'r', encoding='utf-8') as f:
                user_page = BeautifulSoup(f.read(), 'lxml')
            trophy_page = base.TrophyPage(user_page=user_page)

            # Ensure that the TrophyPage class has a member_id attribute
            if not hasattr(trophy_page, 'member_id'):
                logger.error(f'TrophyPage object has no attribute member_id')
                continue

            # Convert trophy_page details to a dictionary
            trophy_data = {
                'member_id': trophy_page.member_id,
                'trophies': trophy_page.trophies
            }

            # Check if the member already exists in the data
            if trophy_page.member_id in existing_data:
                # Update the existing member's data
                existing_data[trophy_page.member_id].update(trophy_data)
                logger.info(f'Updated existing member {trophy_page.member_id}')
            else:
                # Add a new member entry
                existing_data[trophy_page.member_id] = trophy_data
                logger.info(f'Added new member {trophy_page.member_id} to data list')

        except Exception as e:
            logger.error(f'Failed to process {page_file}: {e}')

    # Save all data to JSON file
    save_data(DATABASE_FILE, existing_data)

    logger.info("Script finished")

###############################################################################