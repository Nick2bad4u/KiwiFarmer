# -*- coding: UTF-8 -*-

"""Test initialization of the `TrophyPage` class.
"""

###############################################################################

import os
import logging
from bs4 import BeautifulSoup
import mysql.connector
from mysql.connector import errorcode
from kiwifarmer import base, templates

###############################################################################

PAGE_DIR = '../../data_20210224/downloaded_members'
START = 0
DATABASE = 'kiwifarms_20210224'

###############################################################################

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

if __name__ == '__main__':

    # Connect to database
    #---------------------------------------------------------------------------#

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
    #---------------------------------------------------------------------------#

    pages = os.listdir(PAGE_DIR)
    N_pages = len(pages)

    for i, page_file in enumerate(pages[START:]):
        logger.info(f'[ {i + START} / {N_pages} ] Processing {page_file}')
        try:
            with open(os.path.join(PAGE_DIR, page_file), 'r') as f:
                user_page = BeautifulSoup(f.read(), 'lxml')
            trophy_page = base.TrophyPage(user_page=user_page)
            cursor.executemany(templates.ADD_TROPHY, trophy_page.trophy_insertions)
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