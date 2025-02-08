Tests for Workflow
==================

This section includes tests for the workflow scripts described in the `workflow.rst` document. Each test ensures that the corresponding script runs without errors and performs its intended function.

1. Test Get thread data

    A. Test Get list of URLs for all threads

    .. code-block:: none

        python 01-A_get_thread_url_list.py

    B. Test Download the first page of each thread

    .. code-block:: none

        python 01-B_download_all_threads_new.py

    C. Test Insert data from all threads into database

    .. code-block:: none

        python 01-C_insert_threads.py

2. Test Get post data

    A. Test Get list of URLs for all pages of all threads

    .. code-block:: none

        python 02-A_get_page_url_list.py

    B. Test Download all pages of all threads

    .. code-block:: none

        python 02-B_download_all_pages.py

    C. Test Insert data from all posts into database

    .. code-block:: none

        python 02-C_insert_pages.py

3. Test Get user data

    A. Test Download all pages of users

    .. code-block:: none

        python 03-A_download_all_users.py

    B. Test Insert data from all users into database

    .. code-block:: none

        python 03-B_insert_users.py

4. Test Get user following data

    A. Test Download all "About" pages of users

    .. code-block:: none

        python 04-A_download_all_users_about.py

    B. Test Get list of URLs for all following pages of all users

    .. code-block:: none

        python 04-B_insert_users.py

    C. Test Download following pages of all users

    .. code-block:: none

        python 04-C_download_all_users_following.py

    D. Test Insert all user following data into database

    .. code-block:: none

        python 04-D_insert_following.py

5. Test Get user trophy data

    A. Test Insert all user trophy data into database

    .. code-block:: none

        python 05-A_insert_trophies.py

6. Test Get reaction data

    A. Test Get list of URLs for reactions to all posts

    .. code-block:: none

        python 06-A_get_reaction_url_list.py

    B. Test Download reactions to all posts

    .. code-block:: none

        python 06-B_download_all_reactions.py

    C. Test Insert data from all reactions into database

    .. code-block:: none

        python 06-C_insert_reactions.py