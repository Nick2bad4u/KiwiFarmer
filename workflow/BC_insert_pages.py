# -*- coding: UTF-8 -*-
"""This script processes HTML files of Kiwifarms thread pages, extracts
relevant information from each post, and inserts it into a MySQL database.

The script iterates through HTML files located in the `PAGE_DIR` directory,
parses each file using BeautifulSoup, and extracts individual posts. For each
post, it extracts data such as author, content, and associated blockquotes,
links, and images. This data is then inserted into the `post` table and
related tables in the specified MySQL database.

The script uses environment variables for database credentials and logs
progress and errors using the logging module.  It handles potential database
errors during insertion and commits changes in batches.

Constants:
    PAGE_DIR (str): Relative path to the directory containing the downloaded
        HTML pages.
    START (int): Starting index for processing pages in the directory.
    DATABASE (str): Name of the MySQL database to connect to.

Test initialization of the `Thread` class.
"""

###############################################################################

import os
import logging
from bs4 import BeautifulSoup
import mysql.connector  # type: ignore
from mysql.connector import errorcode  # type: ignore

from kiwifarmer import base, templates

###############################################################################

PAGE_DIR = '../../data_20210224/downloaded_pages'
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

    # Process HTML files of pages, insert fields into `post` table in database
    # ---------------------------------------------------------------------------#

    pages = os.listdir(PAGE_DIR)
    N_pages = len(pages)

    for i, page_file in enumerate(pages[START:]):
        logger.info(f'[ {i + START} / {N_pages} ] Processing {page_file}')

        with open(os.path.join(PAGE_DIR, page_file), 'r') as f:
            thread_page = BeautifulSoup(f.read(), 'lxml')

        page = base.Page(thread_page=thread_page)
        post_soups = page.get_post_soups()

        for j, post_soup in enumerate(post_soups):
            post = base.Post(post=post_soup)

            try:
                cursor.execute(templates.ADD_POST, post.post_insertion)
                cursor.executemany(templates.ADD_BLOCKQUOTE,
                                   post.blockquote_insertions)
                cursor.executemany(templates.ADD_LINK, post.link_insertions)
                cursor.executemany(templates.ADD_IMAGE, post.image_insertions)
                logger.info(
                    f'Successfully inserted post {j + 1} from {page_file} into database')
            except mysql.connector.Error as err:
                logger.error(
                    f'Error inserting post {j + 1} from {page_file} into database: {err.msg}')

    cnx.commit()
    cursor.close()
    cnx.close()

    logger.info('Script finished')

###############################################################################
