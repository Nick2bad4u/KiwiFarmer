import json
import os
import glob
import logging
from bs4 import BeautifulSoup

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('script.log'),  # Log to a file
        logging.StreamHandler()  # Log to the console
    ]
)

# Define the directory containing the HTML files and the output JSON file
PAGE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'downloaded_members_connections'))
DATABASE_FILE = 'kiwifarms_following_20210224.json'

# Initialize a dictionary to store all user-following relationships
all_data = {}

# Load existing data from the JSON file (if it exists)
if os.path.exists(DATABASE_FILE):
    logging.info(f"Loading existing data from {DATABASE_FILE}...")
    with open(DATABASE_FILE, 'r', encoding='utf-8') as json_file:
        existing_data = json.load(json_file)
        all_data = existing_data.get("followers", {})  # Load existing followers data
    logging.info(f"Loaded data for {len(all_data)} users.")
else:
    logging.info(f"No existing data found. Starting from scratch.")

# Get a list of all HTML files in the directory
html_files = glob.glob(os.path.join(PAGE_DIR, '*.html'))
logging.info(f"Found {len(html_files)} HTML files to process.")

# Process each HTML file
for html_file in html_files:
    try:
        # Extract the username and user_id from the filename
        filename = os.path.basename(html_file)
        user_info = filename.replace('members.', '').replace('.about.html', '')
        user_id = user_info.split('.')[0]  # Extract the numeric user_id
        logging.info(f"Processing file: {filename} (User ID: {user_id})")

        # Load the HTML content from the file
        with open(html_file, 'r', encoding='utf-8') as file:
            html_content = file.read()

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract the following_user_ids and additional details from the list of followers
        followers_list = soup.find('ol', class_='block-body')
        if followers_list:
            for follower in followers_list.find_all('li', class_='block-row'):
                follower_data = {}
                follower_link = follower.find('a', href=True)
                if follower_link:
                    # Extract user_id from the URL
                    following_user_id = follower_link['href'].split('/')[-2]
                    follower_parts = following_user_id.rsplit('.', 1)
                    if len(follower_parts) == 2:
                        user_name, follower_id = follower_parts
                    else:
                        user_name = follower_parts[0]
                        follower_id = ""
                    follower_data = {
                        "user_name": user_name,
                        "user_id": int(follower_id) if follower_id.isdigit() else follower_id
                    }

                    # Add the follower data to the list if not already present
                    if user_id not in all_data:
                        all_data[user_id] = {}
                    if follower_id not in all_data[user_id]:
                        all_data[user_id][follower_id] = follower_data
                        logging.info(f"Added follower {follower_id} for user {user_id}.")
                    else:
                        logging.info(f"Follower {follower_id} already exists for user {user_id}.")

            logging.info(f"Found {len(all_data[user_id])} followers for user {user_id}.")
        else:
            logging.warning(f"No followers list found in file: {filename}")

    except Exception as e:
        logging.error(f"Error processing file {filename}: {e}")

# Wrap the data under a "followers" key
final_data = {"followers": all_data}

# Write the updated data to the JSON file
logging.info(f"Writing data to {DATABASE_FILE}...")
with open(DATABASE_FILE, 'w', encoding='utf-8') as json_file:
    json.dump(final_data, json_file, indent=4)
logging.info(f"Data saved successfully. Total users in dataset: {len(all_data)}.")

print(f"Data extracted and saved to {DATABASE_FILE}")