# -*- coding: UTF-8 -*-

"""Test initialization of the `User` class.
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

USER_PAGE_DIR =os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'downloaded_members'))
START = 0
DATABASE_FILE = 'kiwifarms_users_20210224.json'

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
    # Load existing data as a dictionary with user_id as the key
    existing_data = load_existing_data(DATABASE_FILE)

    # Process HTML files of user pages, insert fields into JSON
    # ---------------------------------------------------------------------------#

    user_pages = os.listdir(USER_PAGE_DIR)
    N_user_pages = len(user_pages)

    for i, user_page_file in enumerate(user_pages[START:]):
        logger.info(f'[ {i + START} / {N_user_pages} ] Processing {user_page_file}')

        with open(os.path.join(USER_PAGE_DIR, user_page_file), 'r', encoding='utf-8') as f:
            user_page = BeautifulSoup(f.read(), 'lxml')

        try:
            user = base.User(user_page=user_page)
        except ValueError as e:
            logger.error(f'Error processing {user_page_file}: {e}')
            continue

        # Check for missing user_id or user_username
        if not user.user_id or not user.user_username:
            logger.warning(f'Skipping {user_page_file} due to missing user_id or user_username')
            continue

        # Convert user details to a dictionary
        user_data = {
            'user_username': user.user_username,
            'user_id': user.user_id,
            'user_image': user.user_image,
            'user_messages': user.user_messages,
            'user_reaction_score': user.user_reaction_score,
            'user_points': user.user_points,
            'user_joined': user.user_joined,
            'user_last_seen': user.user_last_seen,
            'user_blurb': user.user_blurb,
            'user_role': user.user_role,
        }

        # Check if the user already exists in the data
        if user.user_id in existing_data:
            # Update the existing user's data
            existing_data[user.user_id].update(user_data)
            logger.info(f'Updated existing user {user.user_id}')
        else:
            # Add a new user entry
            existing_data[user.user_id] = user_data
            logger.info(f'Added new user {user.user_id} to data list')

    # Save all data to JSON file
    save_data(DATABASE_FILE, existing_data)

    logger.info('Script finished')

###############################################################################