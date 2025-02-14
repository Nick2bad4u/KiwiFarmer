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
PAGE_DIR = os.path.join('..', '..', 'data_20210224', 'downloaded_members_connections')
DATABASE_FILE = 'kiwifarms_following_20210224.json'

# Initialize a dictionary to store all user-following relationships
all_data = {}

# Load existing data from the JSON file (if it exists)
if os.path.exists(DATABASE_FILE):
    logging.info(f"Loading existing data from {DATABASE_FILE}...")
    with open(DATABASE_FILE, 'r', encoding='utf-8') as json_file:
        all_data = json.load(json_file)
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
        logging.info(f"Processing file: {filename} (User Info: {user_info})")

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
                    follower_data['user_id'] = following_user_id

                    # # Extract message count, points, and referrals
                    # content_row_minor = follower.find('div', class_='contentRow-minor')
                    # if content_row_minor:
                    #     pairs = content_row_minor.find_all('dl', class_='pairs pairs--inline')
                    #     for pair in pairs:
                    #         key = pair.find('dt').text.strip().lower()
                    #         value = pair.find('dd').text.strip()
                    #         follower_data[key] = value

                    # # Extract location (if available)
                    # content_row_lesser = follower.find('div', class_='contentRow-lesser')
                    # if content_row_lesser:
                    #     location = content_row_lesser.find('a', class_='u-concealed')
                    #     if location:
                    #         follower_data['location'] = location.text.strip()
                    #     else:
                    #         follower_data['location'] = None

                    # Add the follower data to the list
                    if user_info not in all_data:
                        all_data[user_info] = []
                    all_data[user_info].append(follower_data)

            logging.info(f"Found {len(all_data[user_info])} followers for user {user_info}.")
        else:
            logging.warning(f"No followers list found in file: {filename}")

    except Exception as e:
        logging.error(f"Error processing file {filename}: {e}")

# Write the updated data to the JSON file
logging.info(f"Writing data to {DATABASE_FILE}...")
with open(DATABASE_FILE, 'w', encoding='utf-8') as json_file:
    # Modify the keys to remove the extra parts and keep only the user_id
    cleaned_data = {key.split('.')[0]: value for key, value in all_data.items()}
    json.dump(cleaned_data, json_file, indent=4)
logging.info(f"Data saved successfully. Total users in dataset: {len(cleaned_data)}.")

print(f"Data extracted and saved to {DATABASE_FILE}")
