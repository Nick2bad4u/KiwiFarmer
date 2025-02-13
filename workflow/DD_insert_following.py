# -*- coding: UTF-8 -*-

"""Test initialization of the `Following` class.
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
from kiwifarmer import base, templates

###############################################################################

PAGE_DIR = os.path.join('..', '..', 'data_20210224', 'downloaded_members_connections')
START = 0
DATABASE = 'kiwifarms_20210224'

###############################################################################

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

if __name__ == '__main__':

    # Connect to database
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

    # Process HTML files of pages, insert fields into `post` table in database
    # ---------------------------------------------------------------------------#

    pages = os.listdir(PAGE_DIR)
    pages = [p for p in pages if p.split('_')[1] == 'following']
    N_pages = len(pages)

    for i, page_file in enumerate(pages[START:]):
        logger.info(f'[ {i + START} / {N_pages} ] Processing {page_file}')
        try:
            with open(os.path.join(PAGE_DIR, page_file), 'r') as f:
                following_page = BeautifulSoup(f.read(), 'lxml')
            following = base.Following(following_page=following_page)
            cursor.executemany(templates.ADD_FOLLOWING,
                               following.following_insertions)
            logger.info(f'Successfully processed {page_file}')
        except Exception as e:
            logger.error(f'Failed to process {page_file}: {e}')

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
