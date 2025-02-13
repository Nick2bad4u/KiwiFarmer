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

class TrophyPage:
    def __init__(self, user_page):
        self.user_page = user_page
        self.member_id = self._extract_member_id()
        self.trophies = self._extract_trophies()

    def _extract_member_id(self):
        # Extract member ID from the URL or other relevant part of the page
        # For example, if the URL is "/members/null.1/about", the member ID is "1"
        # This is just a placeholder, adjust according to your actual HTML structure
        title_div = self.user_page.find('div', {'class': 'p-title'})
        if title_div:
            title_h1 = title_div.find('h1')
            if title_h1:
                return title_h1.text.strip()
        return None

    def _extract_trophies(self):
        trophies = []
        trophy_list = self.user_page.find('ol', {'class': 'listPlain'})
        if trophy_list:
            for trophy in trophy_list.find_all('li', {'class': 'block-row'}):
                trophy_data = {}
                # Extract trophy points
                points = trophy.find('span', {'class': 'contentRow-figure--text'})
                if points:
                    try:
                        trophy_data['points'] = int(points.text.strip())
                    except ValueError:
                        trophy_data['points'] = 0  # Default to 0 if parsing fails
                # Extract trophy name
                name = trophy.find('h2', {'class': 'contentRow-header'})
                if name:
                    trophy_data['name'] = name.text.strip()
                # Extract trophy description
                description = trophy.find('div', {'class': 'contentRow-minor'})
                if description:
                    trophy_data['description'] = description.text.strip()
                # Extract trophy date
                date = trophy.find('time', {'class': 'u-dt'})
                if date:
                    trophy_data['date'] = date.get('datetime', '')
                trophies.append(trophy_data)
        return trophies

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
            trophy_page = TrophyPage(user_page=user_page)

            # Ensure that the TrophyPage class has a member_id attribute
            if not hasattr(trophy_page, 'member_id') or not trophy_page.member_id:
                logger.error(f'TrophyPage object has no valid member_id for {page_file}')
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