# -*- coding: UTF-8 -*-

"""Test initialization of the `User` class.
"""

###############################################################################

import os
import logging
from bs4 import BeautifulSoup
import mysql.connector  # type: ignore
from mysql.connector import errorcode  # type: ignore
from kiwifarmer import base, templates

###############################################################################

USER_PAGE_DIR = '../../data_20210224/downloaded_members'
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

    # Process HTML files of user pages, insert fields into `user` table in database
    # ---------------------------------------------------------------------------#

    user_pages = os.listdir(USER_PAGE_DIR)
    N_user_pages = len(user_pages)

    for i, user_page_file in enumerate(user_pages[START:]):
        logger.info(
            f'[ {i + START} / {N_user_pages} ] Processing {user_page_file}')

        with open(os.path.join(USER_PAGE_DIR, user_page_file), 'r') as f:
            user_page = BeautifulSoup(f.read(), 'lxml')

        user = base.User(user_page=user_page)

        try:
            cursor.execute(templates.ADD_USER, user.user_insertion)
            logger.info(
                f'Successfully inserted user {user_page_file} into database')
        except mysql.connector.Error as err:
            logger.error(
                f'Error inserting user {user_page_file} into database: {err.msg}')

    cnx.commit()
    cursor.close()
    cnx.close()

    logger.info('Script finished')

###############################################################################
