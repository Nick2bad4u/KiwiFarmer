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
from kiwifarmer import base  # Ensure this module and class are correctly implemented and imported

###############################################################################

PAGE_DIR = os.path.join('..', '..', 'data_20210224', 'downloaded_members_connections')
START = 0
DATABASE_FILE = 'kiwifarms_following_20210224.json'

###############################################################################

# Configure logging
logging.basicConfig(level=logging.DEBUG,  # Set to DEBUG to capture more detailed logs
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
    logger.info(f"Data saved to {file_path}")

if __name__ == '__main__':
    # Load existing data as a dictionary with member_id as the key
    existing_data = load_existing_data(DATABASE_FILE)
    logger.debug(f"Loaded existing data: {existing_data}")

    # Process HTML files of pages, insert fields into JSON
    # ---------------------------------------------------------------------------#

    if not os.path.exists(PAGE_DIR):
        logger.error(f"PAGE_DIR does not exist: {PAGE_DIR}")
    else:
        pages = os.listdir(PAGE_DIR)
        logger.debug(f"Pages found in PAGE_DIR: {pages}")

        pages = [p for p in pages if '_followers' in p]
        N_pages = len(pages)
        logger.debug(f"Filtered pages: {pages}")
        logger.debug(f"Found {N_pages} pages to process")

        for i, page_file in enumerate(pages[START:]):
            logger.info(f'[ {i + START} / {N_pages} ] Processing {page_file}')
            try:
                with open(os.path.join(PAGE_DIR, page_file), 'r', encoding='utf-8') as f:
                    following_page = BeautifulSoup(f.read(), 'lxml')
                    logger.debug(f"Loaded HTML content for {page_file}")

                # Ensure the updated script to match new HTML structure
                body = following_page.find('ol', {'class': 'block-body'})
                if body:
                    users = body.find_all('li', {'class': 'block-row block-row--separated'})
                    user_ids = []
                    for user in users:
                        user_link = user.find('a', {'class': 'avatar avatar--s'})
                        if user_link and 'data-user-id' in user_link.attrs:
                            user_id = user_link['data-user-id']
                            if user_id.isdigit():
                                user_ids.append(int(user_id))
                                logger.debug(f"Found user ID: {user_id}")
                            else:
                                logger.warning(f"Non-numeric user ID found: {user_id}")
                        else:
                            logger.warning(f"User link not found or does not contain 'data-user-id': {user}")

                    logger.debug(f"Extracted user IDs: {user_ids}")

                    # Create the Following object
                    try:
                        following = base.Following(following_page=following_page)  # Ensure this class is implemented correctly
                    except Exception as e:
                        logger.error(f"Error initializing Following object: {e}")
                        continue

                    # Convert following details to a dictionary
                    following_data = {
                        'member_id': following.member_id,
                        'following_list': following.following_list
                    }
                    logger.debug(f"Following data: {following_data}")

                    # Check if the member already exists in the data
                    if following.member_id in existing_data:
                        # Update the existing member's data
                        existing_data[following.member_id].update(following_data)
                        logger.info(f'Updated existing member {following.member_id}')
                    else:
                        # Add a new member entry
                        existing_data[following.member_id] = following_data
                        logger.info(f'Added new member {following.member_id} to data list')
                else:
                    logger.warning(f'No block-body found in {page_file}')

            except Exception as e:
                logger.error(f'Failed to process {page_file}: {e}')

        # Save all data to JSON file
        save_data(DATABASE_FILE, existing_data)

    logger.info("Script finished")

###############################################################################