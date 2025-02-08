# -*- coding: UTF-8 -*-

"""Test initialization of the `Thread` class.
"""

###############################################################################

import os
import logging

from bs4 import BeautifulSoup
import mysql.connector  # type: ignore
from mysql.connector import errorcode  # type: ignore

from kiwifarmer import base, templates

###############################################################################

THREAD_DIR = '../../data_20210224/downloaded_threads'

START = 0

DATABASE = 'kiwifarms_20210224'

###############################################################################

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

if __name__ == '__main__':

    # Create database (you only need to do this once)
    # ---------------------------------------------------------------------------#

    cnx = mysql.connector.connect(
        user=os.getenv('KIWIFARMER_USER'),
        passwd=os.getenv('KIWIFARMER_PASSWORD'),
        host='127.0.0.1',
        charset='utf8mb4',
        collation='utf8mb4_bin',
        use_unicode=True
    )

    cursor = cnx.cursor()
    try:
        logger.info(f'Creating database {DATABASE}')
        cursor.execute(
            f'CREATE DATABASE {DATABASE} character set utf8mb4 collate utf8mb4_bin')
        cnx.commit()
        logger.info(f'Database {DATABASE} created successfully')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_DB_CREATE_EXISTS:
            logger.info(f'Database {DATABASE} already exists.')
        else:
            logger.error(f'Error creating database: {err.msg}')
    finally:
        cursor.close()
        cnx.close()

    # Create tables in database (you only need to do this once)
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

    for table_name in templates.TABLES.keys():
        table_description = templates.TABLES[table_name]
        try:
            logger.info(f'Creating table {table_name}')
            cursor.execute(table_description)
            logger.info(f'Table {table_name} created successfully')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                logger.info(f'Table {table_name} already exists.')
            else:
                logger.error(f'Error creating table {table_name}: {err.msg}')

    # Process HTML files of threads, insert fields into `threads` table
    # ---------------------------------------------------------------------------#

    threads = os.listdir(THREAD_DIR)
    N_threads = len(threads)

    for i, thread_file in enumerate(threads[START:]):
        logger.info(f'[ {i + START} / {N_threads} ] Processing {thread_file}')

        with open(os.path.join(THREAD_DIR, thread_file), 'r') as f:
            thread_soup = BeautifulSoup(f.read(), 'lxml')

        thread = base.Thread(thread_page=thread_soup)

        try:
            cursor.execute(templates.ADD_THREAD, thread.thread_insertion)
            logger.info(f'Successfully inserted {thread_file} into database')
        except mysql.connector.Error as err:
            logger.error(
                f'Error inserting {thread_file} into database: {err.msg}')

    cnx.commit()
    cursor.close()
    cnx.close()

    logger.info('Script finished')

###############################################################################
