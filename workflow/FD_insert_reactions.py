# -*- coding: UTF-8 -*-

"""Insert reaction pages into database
"""

###############################################################################

import os
import logging
import sys

# Add the parent directory to the sys.path to import kiwifarmer module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bs4 import BeautifulSoup
import mysql.connector  # type: ignore
from mysql.connector import errorcode  # type: ignore
import requests
from kiwifarmer import base, templates, utils

###############################################################################

REACTION_PAGE_DIR =os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'downloaded_reactions')
REACTION_FILTERED_LIST =os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'downloaded_reactions_filtered.txt')
START = 0
DATABASE = 'kiwifarms_20210224'

###############################################################################

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()


def process_reaction_page(page_file, cursor):
    with open(os.path.join(REACTION_PAGE_DIR, page_file), 'r', encoding='utf-8') as f:
        _reaction_page = BeautifulSoup(f.read(), 'lxml')

    reaction_page = base.ReactionPage(reaction_page=_reaction_page)
    reaction_soups = reaction_page.get_reaction_soups()
    post_id = reaction_page.post_id

    for j, reaction in enumerate(reaction_soups):
        reaction = base.Reaction(reaction=reaction, post_id=post_id)
        cursor.execute(templates.ADD_REACTION, reaction.reaction_insertion)

###############################################################################


if __name__ == '__main__':
    # Connect to MySQL database
    # ---------------------------------------------------------------------------#

    try:
        cnx = mysql.connector.connect(
            user=os.getenv('KIWIFARMER_USER'),
            password=os.getenv('KIWIFARMER_PASSWORD'),
            host='127.0.0.1',
            database=DATABASE,
            charset='utf8mb4',
            collation='utf8mb4_bin',
            use_unicode=True
        )
        cursor = cnx.cursor()
        logger.info("Connected to the database successfully")
    except mysql.connector.Error as err:
        logger.error(f"Error connecting to the database: {err}")
        exit(1)

    for table_name in templates.TABLES.keys():
        table_description = templates.TABLES[table_name]
        try:
            logger.info(f"Creating table {table_name}: ", end='')
            cursor.execute(table_description)
            logger.info("OK")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                logger.info("already exists.")
            else:
                logger.error(err.msg)

    # Process HTML files of pages, insert fields into `post` table in database
    # ---------------------------------------------------------------------------#

    with open(REACTION_FILTERED_LIST, 'r') as f:
        pages = f.read().split('\n')
    pages = list(filter(None, pages))

    N_pages = len(pages)

    for i, page_file in enumerate(pages[START:]):
        logger.info(f'[ {i + START} / {N_pages} ] Processing {page_file}')
        try:
            process_reaction_page(page_file, cursor)
            logger.info(f'Successfully processed {page_file}')
        except Exception as e:
            logger.error(f'Failed to process {page_file}: {e}')
            try:
                page_url = utils.reaction_filename_to_url(page_file)
                r = requests.get(page_url)
                output_file = os.path.join(REACTION_PAGE_DIR, page_file)
                with open(output_file, 'wb') as f:
                    f.write(r.content)
                process_reaction_page(page_file, cursor)
                logger.info(f'Re-downloaded and processed {page_file}')
            except Exception as e:
                logger.error(
                    f'Failed to re-download and process {page_file}: {e}')

    try:
        cnx.commit()
        logger.info("Committed changes to the database")
    except mysql.connector.Error as err:
        logger.error(f"Error committing changes to the database: {err}")
    finally:
        cursor.close()
        cnx.close()
        logger.info("Closed database connection")

    logger.info("Script finished")

###############################################################################
