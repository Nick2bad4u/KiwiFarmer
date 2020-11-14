# -*- coding: UTF-8 -*-

"""https://stackoverflow.com/a/46144596/13026442
"""

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

import asyncio

from kiwifarmer.utils import (
  reaction_filename_to_url,
  reaction_url_to_filename,
  download_many_files, )

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

URL_LIST_FILE = '../../data_fresh/thread_post_id_list.txt'

OUTPUT_DIR = '../../data_fresh/downloaded_reactions'

SEMAPHORE = 20

THRESHOLD_KB = 40

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

with open( URL_LIST_FILE, 'r' ) as f:
  url_list = f.read().split('\n')[ : 100 ]

asyncio.run( download_many_files(
  url_list = url_list,
  output_dir = OUTPUT_DIR,
  semaphore = SEMAPHORE,
  threshold_kb = THRESHOLD_KB,
  filename_to_url = reaction_filename_to_url,
  url_to_filename = reaction_url_to_filename ) )

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#