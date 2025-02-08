# -*- coding: UTF-8 -*-

"""Generate list of all connection URLs (followers and following) for all members using their downloaded HTML files.
"""

###############################################################################

import os
import re
import logging
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

###############################################################################

MEMBER_DIR = '../../data_20210224/downloaded_members_about'
CONNECTION_LIST = '../../data_20210224/connection_url_list.txt'

###############################################################################

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def get_users(soup, category):
    f = soup.find('h4', {'class': 'block-textHeader'}, text=re.compile(category))
    if f is None:
        return 0
    else:
        following = f.parent
        users = following.find_all('a', 'avatar avatar--s')
        users = list(filter(None, [user.get('data-user-id') for user in users]))
        n_users = len(users)
        t = following.find('a', {'data-xf-click': 'overlay'})
        if t is None:
            n_additional_users = 0
        else:
            n_additional_users = int(t.text[8: -6])
        return n_users + n_additional_users

def get_followers(soup):
    return get_users(soup=soup, category='Followers')

def get_following(soup):
    return get_users(soup=soup, category='Following')

def get_member_id(soup):
    meta_tag = soup.find('meta', {'property': 'og:url'})
    if meta_tag is not None:
        url = meta_tag['content']
        s = url.split('.')
        if len(s) == 3:
            return int(s[-1].split('/')[0])
        else:
            return int(s[1].split('/')[-2])
    else:
        logger.error("Meta tag with property 'og:url' not found")
        return None

def get_data(soup):
    member_id = get_member_id(soup)
    if member_id is None:
        return None
    d = {
        'member_id': member_id,
        'followers': get_followers(soup),
        'following': get_following(soup),
    }
    return d

if __name__ == '__main__':
    files = os.listdir(MEMBER_DIR)
    N_files = len(files)

    dl = list()

    for i, file in enumerate(files):
        logger.info(f'[ {i} / {N_files} ] Processing {file}')
        try:
            with open(os.path.join(MEMBER_DIR, file), 'r') as f:
                soup = BeautifulSoup(f.read(), features="lxml")
            data = get_data(soup)
            if data is not None:
                dl.append(data)
        except Exception as e:
            logger.error(f'Failed to process {file}: {e}')

    if dl:
        df = pd.DataFrame(dl)

        ndf = df[(df['followers'] > 0) | (df['following'] > 0)]

        get_num = lambda s: int(np.ceil(s / 50))

        ndf['followers_pages'] = ndf['followers'].apply(get_num)
        ndf['following_pages'] = ndf['following'].apply(get_num)

        url_list = list()

        for i in range(ndf.shape[0]):
            row = ndf.iloc[i]
            member_id = row['member_id']
            for j in range(1, row['followers_pages'] + 1):
                url = f'https://kiwifarms.st/members/{member_id}/followers/page-{j}'
                url_list.append(url)
            for j in range(1, row['following_pages'] + 1):
                url = f'https://kiwifarms.st/members/{member_id}/following/page-{j}'
                url_list.append(url)

        with open(CONNECTION_LIST, 'w') as f:
            for url in url_list:
                f.write(url + '\n')

        logger.info('Script finished')
    else:
        logger.warning('No valid member data found. Exiting script.')

###############################################################################