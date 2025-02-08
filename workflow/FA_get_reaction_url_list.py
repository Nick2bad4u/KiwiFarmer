# -*- coding: UTF-8 -*-

"""Read column from table in database and export to CSV
"""

###############################################################################

import os
import logging
import mysql.connector  # type: ignore
import pandas as pd

###############################################################################

COMMAND = 'SELECT post_id FROM posts'
DATABASE = 'kiwifarms_20210224'
OUTPUT_CSV = '../../data_20210224/reaction_url_list.txt'

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
        logger.info("Connected to the database successfully")
    except mysql.connector.Error as err:
        logger.error(f"Error connecting to the database: {err}")
        exit(1)

    # Read column from table and export to CSV
    # ---------------------------------------------------------------------------#

    try:
        df = pd.read_sql(sql=COMMAND, con=cnx)
        logger.info("Data read from database successfully")

        def to_url(
            s): return f'https://kiwifarms.st/posts/{s}/reactions?reaction_id=0&list_only=1&page=1'
        url_list = df['post_id'].apply(to_url)
        url_list.to_csv(OUTPUT_CSV, header=False, index=False)
        logger.info(f"Data exported to {OUTPUT_CSV} successfully")
    except Exception as e:
        logger.error(f"Failed to read from database or export data: {e}")
    finally:
        cnx.close()
        logger.info("Closed database connection")

    logger.info("Script finished")

###############################################################################
