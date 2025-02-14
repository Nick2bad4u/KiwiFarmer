# -*- coding: UTF-8 -*-

"""Create list of files with all reaction pages that have at least one reaction.
"""

###############################################################################

import os
import logging
import sys

# Add the parent directory to the sys.path to import kiwifarmer module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


###############################################################################

INPUT_DIR =os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'downloaded_reactions')
OUTPUT_FILE_GOOD =os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'downloaded_reactions_filtered.txt')
NO_REACTIONS_STR = "No one has reacted to this content yet."

###############################################################################

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

if __name__ == '__main__':
    logger.info(f"Scanning directory: {INPUT_DIR}")

    files = os.scandir(INPUT_DIR)
    num_files = len(list(files))

    logger.info(f"Found {num_files} files in the directory")

    with open(OUTPUT_FILE_GOOD, 'w') as fout:
        for file in os.scandir(INPUT_DIR):
            if file.is_file():
                try:
                    with open(file.path, 'r', encoding='utf-8') as fin:
                        doc = fin.read()
                    if NO_REACTIONS_STR not in doc:
                        fout.write(file.name + '\n')
                        logger.info(
                            f"File {file.name} has reactions and is added to the list")
                    else:
                        logger.info(f"File {file.name} has no reactions")
                except Exception as e:
                    logger.error(f"Failed to process file {file.name}: {e}")

    logger.info(
        f"Filtered list of files with reactions saved to {OUTPUT_FILE_GOOD}")
    logger.info("Script finished")

###############################################################################
