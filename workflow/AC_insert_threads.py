"""Test initialization of the `Thread` class.
"""

###############################################################################

import os
import sys
import logging
import json
from datetime import datetime

# Add the parent directory to the sys.path to import kiwifarmer module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bs4 import BeautifulSoup

from kiwifarmer import base

###############################################################################

THREAD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'downloaded_threads'))

START = 0

DATABASE_DIR = 'data/kiwifarms_threads'  # Changed to directory name

###############################################################################

# Configure logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def load_existing_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                logger.error(f"Existing data file {file_path} is corrupt. Returning empty dict.")
                return {}
    return {}

def save_data(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def convert_timestamp_to_human_readable(timestamp_str):
    """Convert ISO timestamp string to human-readable format (YYYY-MM-DD HH:MM:SS)."""
    try:
        dt = datetime.fromisoformat(timestamp_str)
        return dt.strftime('%Y-%m-%d %H:%M:%S')
    except ValueError:
        return 'Unknown'

def extract_messages(thread_soup):
    messages = []
    for message in thread_soup.find_all('article', class_='message--post'):
        user = message.find('a', class_='username')
        user_name = user.text.strip() if user else 'Unknown'
        user_id = user['data-user-id'] if user and 'data-user-id' in user.attrs else 'Unknown'

        # Convert user_id to integer if it's a digit
        if user_id.isdigit():
            user_id = int(user_id)

        content = message.find('div', class_='bbWrapper')
        content_text = content.text.strip() if content else 'No content'

        timestamp = message.find('time', class_='u-dt')
        timestamp_text = timestamp['datetime'] if timestamp else 'Unknown'

        # Convert timestamp to human-readable format
        timestamp_human_readable = convert_timestamp_to_human_readable(timestamp_text)

        message_data = {
            'user_name': user_name,
            'user_id': user_id,  # user_id is now an integer (if it's a digit)
            'content': content_text,
            'timestamp': timestamp_human_readable,  # Human-readable timestamp
        }
        messages.append(message_data)

    return messages

if __name__ == '__main__':

    # Create the directory if it doesn't exist
    if not os.path.exists(DATABASE_DIR):
        os.makedirs(DATABASE_DIR)

    # Process HTML files of threads, insert fields into JSON
    # ---------------------------------------------------------------------------#

    threads = os.listdir(THREAD_DIR)
    N_threads = len(threads)

    for i, thread_file in enumerate(threads[START:]):
        logger.info(f'[ {i + START} / {N_threads} ] Processing {thread_file}')

        with open(os.path.join(THREAD_DIR, thread_file), 'r', encoding='utf-8') as f:
            thread_soup = BeautifulSoup(f.read(), 'lxml')

        thread = base.Thread(thread_page=thread_soup)

        if thread.thread_timestamp is not None:
            thread_id = str(thread.thread_id)
            thread_file_path = os.path.join(DATABASE_DIR, f'{thread_id}.json')

            # Load existing data for this thread
            existing_data = load_existing_data(thread_file_path)

            # Extract messages from the thread
            messages = extract_messages(thread_soup)

            # Convert thread details to a dictionary
            thread_data = {
                'thread_id': thread.thread_id,
                'title': thread.thread_title,
                'timestamp': thread.thread_timestamp,
                'messages': messages,
            }

            # Check if the thread already exists
            if existing_data:
                logger.info(f'Thread {thread.thread_id} already exists. Skipping.')
            else:
                # Save thread data to JSON file
                save_data(thread_file_path, thread_data)
                logger.info(f'Successfully added {thread_file} to data list')
        else:
            logger.error(f'Failed to process {thread_file} due to missing timestamp')

    logger.info('Script finished')