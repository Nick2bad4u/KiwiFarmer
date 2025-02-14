import os
import logging
import json
import sys
from bs4 import BeautifulSoup

# Add the parent directory to the sys.path to import kiwifarmer module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

###############################################################################

OUTPUT_DIR =os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'downloadedThreads')
OUTPUT_JSON =os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'reaction_data.json')
REACTION_OUTPUT_DIR =os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data')
REACTION_URL_LIST = os.path.join(REACTION_OUTPUT_DIR, 'reaction_url_list.txt')

###############################################################################

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def extract_reactions_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    reactions = []
    reactions_div = soup.find('div', class_='reactionsBar js-reactionsList is-active')
    if reactions_div:
        reaction_items = reactions_div.find_all('li')
        for item in reaction_items:
            reaction_id = item.find('span')['data-reaction-id']
            reaction_title = item.find('img')['title']
            reactions.append({
                'reaction_id': reaction_id,
                'reaction_title': reaction_title
            })

    # Extract the post ID
    post_id_element = soup.find('div', class_='message-userContent lbContainer js-lbContainer')
    post_id = post_id_element['data-lb-id'].split('-')[-1] if post_id_element else None

    return {
        'post_id': post_id,
        'reactions': reactions
    }

def process_html_files(output_dir):
    reaction_data = []
    post_ids = []
    for filename in os.listdir(output_dir):
        if filename.endswith('.html'):
            file_path = os.path.join(output_dir, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                html_content = file.read()
                extracted_data = extract_reactions_from_html(html_content)
                if extracted_data['post_id']:
                    post_ids.append(extracted_data['post_id'])
                extracted_data['file'] = filename
                reaction_data.append(extracted_data)
    return reaction_data, post_ids

def write_reaction_urls(post_ids, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for post_id in post_ids:
            url = f"https://kiwifarms.st/posts/{post_id}/reactions?reaction_id=0&list_only=1&page=1"
            file.write(url + '\n')

if __name__ == '__main__':
    try:
        reaction_data, post_ids = process_html_files(OUTPUT_DIR)
        with open(OUTPUT_JSON, 'w', encoding='utf-8') as json_file:
            json.dump(reaction_data, json_file, ensure_ascii=False, indent=4)
        logger.info(f"Data exported to {OUTPUT_JSON} successfully")

        write_reaction_urls(post_ids, REACTION_URL_LIST)
        logger.info(f"Reaction URLs written to {REACTION_URL_LIST} successfully")

    except Exception as e:
        logger.error(f"Failed to process HTML files or export data: {e}")

    logger.info("Script finished")
