import os
import logging
import sys
import json

# Add the parent directory to the sys.path to import kiwifarmer module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bs4 import BeautifulSoup
from kiwifarmer import base

###############################################################################

PAGE_DIR =os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'downloaded_pages'))
THREAD_DIR =os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'downloaded_threads'))
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
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def extract_messages(thread_soup):
    messages = []
    for message in thread_soup.find_all('article', class_='message--post'):
        user = message.find('a', class_='username')
        user_name = user.text.strip() if user else 'Unknown'
        user_id = user['data-user-id'] if user and 'data-user-id' in user.attrs else 'Unknown'

        content = message.find('div', class_='bbWrapper')
        content_text = content.text.strip() if content else 'No content'

        timestamp = message.find('time', class_='u-dt')
        timestamp_text = timestamp['datetime'] if timestamp else 'Unknown'

        message_data = {
            'user_name': user_name,
            'user_id': user_id,
            'content': content_text,
            'timestamp': timestamp_text,
        }
        messages.append(message_data)

    return messages

if __name__ == '__main__':
    # Load existing data as a dictionary with thread_id as the key
    existing_data = load_existing_data(DATABASE_FILE)

    # Process HTML files of threads, insert fields into JSON
    # ---------------------------------------------------------------------------#

    threads = os.listdir(THREAD_DIR)
    N_threads = len(threads)

    for i, thread_file in enumerate(threads[START:]):
        logger.info(f'[ {i + START} / {N_threads} ] Processing {thread_file}')

        with open(os.path.join(THREAD_DIR, thread_file), 'r', encoding='utf-8') as f:
            thread_soup = BeautifulSoup(f.read(), 'lxml')

        thread = base.Thread(thread_page=thread_soup)

        # Check for missing fields
        if not thread.thread_id or not thread.thread_title:
            logger.warning(f'Skipping {thread_file} due to missing thread_id or thread_title')
            continue

        if thread.thread_timestamp is not None:
            # Extract messages from the thread
            messages = extract_messages(thread_soup)

            # Check if the thread already exists in the data
            if thread.thread_id in existing_data:
                # Update the existing thread's messages
                existing_data[thread.thread_id]['messages'].extend(messages)
                logger.info(f'Updated existing thread {thread.thread_id} with new messages')
            else:
                # Add a new thread entry
                thread_data = {
                    'thread_id': thread.thread_id,
                    'title': thread.thread_title,
                    'timestamp': thread.thread_timestamp,
                    'messages': messages,
                }
                existing_data[thread.thread_id] = thread_data
                logger.info(f'Added new thread {thread.thread_id} to data list')
        else:
            logger.error(f'Failed to process {thread_file} due to missing timestamp')

    # Save all data to JSON file
    save_data(DATABASE_FILE, existing_data)

    logger.info('Script finished')
###############################################################################