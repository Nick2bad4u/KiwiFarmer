# KiwiFarmer

![Alt](https://repobeats.axiom.co/api/embed/3ab62a4d52db28cc259144d42f26e64742445948.svg 'Repobeats analytics image')

KiwiFarmer is a Python package for scraping KiwiFarms threads and posts, extracting field values, and storing the results in a created MySQL database.

## Run script

KiwiFarmer includes a script (`run_smat.py`) for indexing all KiwiFarms posts into an Elasticsearch instance. The script uses a Redis database to keep track of which pages have already been indexed, which avoids redundant reindexing operations.
The script can be run perpetually using the command:

.. code-block:: bash

watch -n0 python run_smat.py

## Workflow

KiwiFarmer also includes scripts for a workflow that downloads all website pages as HTML files, extracts relevant field data, and stores the data in a MySQL database.
These scripts are in the `workflow/` subdirectory in the package root directory.
For more information, see `docs/workflow.rst`

## TODO

- add additional user fields for user signature and location

- expand unit tests

  - verify correctness of functions

- expand instructions and info of docs

- config file parsing

- analysis tools/utilities/visualizations

- improve input argument handling for classes (e.g. type conversion/checking)

## File List

<p> # Here is a list of files included in this repository:</p>

<ul><h2>Py</h2>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/docs/conf.py" style="color: #9b16fb;">docs\conf.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/docs/tests/test_conf.py" style="color: #1e46e7;">docs\tests\test_conf.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/examples/export_database_csv.py" style="color: #106c2c;">examples\export_database_csv.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/examples/preprocess_reactions.py" style="color: #fe0140;">examples\preprocess_reactions.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/generate-file-list.py" style="color: #451cff;">generate-file-list.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/kiwifarmer/__init__.py" style="color: #b748c3;">kiwifarmer\__init__.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/kiwifarmer/base.py" style="color: #c2450f;">kiwifarmer\base.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/kiwifarmer/functions.py" style="color: #ad0208;">kiwifarmer\functions.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/kiwifarmer/templates.py" style="color: #e22c0c;">kiwifarmer\templates.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/kiwifarmer/utils.py" style="color: #343bac;">kiwifarmer\utils.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/run_smat.py" style="color: #c8faaf;">run_smat.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/setup.py" style="color: #eafdac;">setup.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/sort_json_database.py" style="color: #6290f1;">sort_json_database.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/tests/old_tests/__init__.py" style="color: #205d08;">tests\old_tests\__init__.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/tests/old_tests/base.py" style="color: #39196f;">tests\old_tests\base.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/tests/old_tests/conftest.py" style="color: #54a1d0;">tests\old_tests\conftest.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/tests/old_tests/functions.py" style="color: #0b0e9f;">tests\old_tests\functions.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/tests/old_tests/utils.py" style="color: #beeede;">tests\old_tests\utils.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/tests/test_AA_get_thread_url_list.py" style="color: #c2f33d;">tests\test_AA_get_thread_url_list.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/tests/test_AB_download_all_threads.py" style="color: #db2a8f;">tests\test_AB_download_all_threads.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/tests/test_AC_insert_threads.py" style="color: #4c8399;">tests\test_AC_insert_threads.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/tests/test_BA_get_page_url_list.py" style="color: #0af16f;">tests\test_BA_get_page_url_list.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/tests/test_BB_download_all_pages.py" style="color: #e09875;">tests\test_BB_download_all_pages.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/tests/test_BC_insert_pages.py" style="color: #e5fd30;">tests\test_BC_insert_pages.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/tests/test_CA_download_all_users.py" style="color: #b48ec2;">tests\test_CA_download_all_users.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/tests/test_CB_insert_users.py" style="color: #ac5d65;">tests\test_CB_insert_users.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/tests/test_DA_download_all_users_about.py" style="color: #6ed5cc;">tests\test_DA_download_all_users_about.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/tests/test_DB_get_users_following_list.py" style="color: #e3fef7;">tests\test_DB_get_users_following_list.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/tests/test_DC_download_all_users_following.py" style="color: #8742f7;">tests\test_DC_download_all_users_following.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/tests/test_DD_insert_following.py" style="color: #eb596f;">tests\test_DD_insert_following.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/tests/test_EA_insert_trophies.py" style="color: #1f2600;">tests\test_EA_insert_trophies.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/tests/test_FA_get_reaction_url_list.py" style="color: #e463b3;">tests\test_FA_get_reaction_url_list.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/tests/test_FB_download_all_reactions.py" style="color: #643f7f;">tests\test_FB_download_all_reactions.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/tests/test_FC_preprocess_reactions.py" style="color: #618e98;">tests\test_FC_preprocess_reactions.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/tests/test_FD_insert_reactions.py" style="color: #48c448;">tests\test_FD_insert_reactions.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/tests/test_FE_get_more_reactions.py" style="color: #7f6a87;">tests\test_FE_get_more_reactions.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/tests/test_export_database_csv.py" style="color: #33b687;">tests\test_export_database_csv.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/tests/test_preprocess_reactions.py" style="color: #9b87e4;">tests\test_preprocess_reactions.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/tests/test_run_smat.py" style="color: #90a8fe;">tests\test_run_smat.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/AA_get_thread_url_list.py" style="color: #32c904;">workflow\AA_get_thread_url_list.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/AB_download_all_threads.py" style="color: #63b5c8;">workflow\AB_download_all_threads.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/AC_insert_threads.py" style="color: #bec8f0;">workflow\AC_insert_threads.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/BA_get_page_url_list.py" style="color: #6d6f46;">workflow\BA_get_page_url_list.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/BB_download_all_pages.py" style="color: #3ca96a;">workflow\BB_download_all_pages.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/BC_insert_pages.py" style="color: #024425;">workflow\BC_insert_pages.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/CA_download_all_users.py" style="color: #25e747;">workflow\CA_download_all_users.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/CB_insert_users.py" style="color: #8d97fb;">workflow\CB_insert_users.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/DA_download_all_users_about.py" style="color: #655bd3;">workflow\DA_download_all_users_about.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/DB_get_users_following_list.py" style="color: #3ce480;">workflow\DB_get_users_following_list.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/DC_download_all_users_following.py" style="color: #902089;">workflow\DC_download_all_users_following.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/DD_insert_following.py" style="color: #d91e7b;">workflow\DD_insert_following.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/EA_insert_trophies.py" style="color: #063de1;">workflow\EA_insert_trophies.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/FA_get_reaction_url_list.py" style="color: #70da53;">workflow\FA_get_reaction_url_list.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/FB_download_all_reactions.py" style="color: #35a490;">workflow\FB_download_all_reactions.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/FC_preprocess_reactions.py" style="color: #57474a;">workflow\FC_preprocess_reactions.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/FD_insert_reactions.py" style="color: #0a5c08;">workflow\FD_insert_reactions.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/FE_get_more_reactions.py" style="color: #cbbd2d;">workflow\FE_get_more_reactions.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/GA_combine_data.py" style="color: #717979;">workflow\GA_combine_data.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/GB_organize_data.py" style="color: #88d3fe;">workflow\GB_organize_data.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/GC_visualize_data_user_specific.py" style="color: #631705;">workflow\GC_visualize_data_user_specific.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/GD_visualize_follower_networks.py" style="color: #b553a1;">workflow\GD_visualize_follower_networks.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/GF_visualize_more_data.py" style="color: #be44f9;">workflow\GF_visualize_more_data.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/old_workflows/01-A_get_thread_url_list.py" style="color: #d4257d;">workflow\old_workflows\01-A_get_thread_url_list.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/old_workflows/01-B_download_all_threads.py" style="color: #dd2252;">workflow\old_workflows\01-B_download_all_threads.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/old_workflows/01-C_insert_threads.py" style="color: #c0196f;">workflow\old_workflows\01-C_insert_threads.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/old_workflows/02-A_get_page_url_list.py" style="color: #a3dd96;">workflow\old_workflows\02-A_get_page_url_list.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/old_workflows/02-B_download_all_pages.py" style="color: #393adb;">workflow\old_workflows\02-B_download_all_pages.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/old_workflows/02-C_insert_pages.py" style="color: #326c14;">workflow\old_workflows\02-C_insert_pages.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/old_workflows/03-A_download_all_users.py" style="color: #ca1877;">workflow\old_workflows\03-A_download_all_users.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/old_workflows/03-B_insert_users.py" style="color: #c008d3;">workflow\old_workflows\03-B_insert_users.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/old_workflows/04-A_download_all_users_about.py" style="color: #889687;">workflow\old_workflows\04-A_download_all_users_about.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/old_workflows/04-B_get_users_following_list.py" style="color: #c8ebaa;">workflow\old_workflows\04-B_get_users_following_list.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/old_workflows/04-C_download_all_users_following.py" style="color: #a38c42;">workflow\old_workflows\04-C_download_all_users_following.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/old_workflows/04-D_insert_following.py" style="color: #b89386;">workflow\old_workflows\04-D_insert_following.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/old_workflows/05-A_insert_trophies.py" style="color: #a628cd;">workflow\old_workflows\05-A_insert_trophies.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/old_workflows/06-A_get_reaction_url_list.py" style="color: #311ab8;">workflow\old_workflows\06-A_get_reaction_url_list.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/old_workflows/06-B_download_all_reactions.py" style="color: #90647e;">workflow\old_workflows\06-B_download_all_reactions.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/old_workflows/06-C_preprocess_reactions.py" style="color: #42e1ab;">workflow\old_workflows\06-C_preprocess_reactions.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/old_workflows/06-D_insert_reactions.py" style="color: #c64933;">workflow\old_workflows\06-D_insert_reactions.py</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/workflow/old_workflows/06-E_get_more_reactions.py" style="color: #f2f88b;">workflow\old_workflows\06-E_get_more_reactions.py</a></li>
<h2>JSON</h2>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/.vscode/settings.json" style="color: #833454;">.vscode\settings.json</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/connection_url_list.json" style="color: #8e6cac;">data\connection_url_list.json</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/reaction_data.json" style="color: #a0c6fb;">data\reaction_data.json</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/kiwifarms_20210224.json" style="color: #c42dcf;">kiwifarms_20210224.json</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/kiwifarms_combined_database.json" style="color: #f8d2e3;">kiwifarms_combined_database.json</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/kiwifarms_following_20210224.json" style="color: #d923a5;">kiwifarms_following_20210224.json</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/kiwifarms_reorganized_database.json" style="color: #afdae1;">kiwifarms_reorganized_database.json</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/kiwifarms_trophies_20210224.json" style="color: #3067c6;">kiwifarms_trophies_20210224.json</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/kiwifarms_users_20210224.json" style="color: #dd1de1;">kiwifarms_users_20210224.json</a></li>
<h2></h2>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/.gitignore" style="color: #9a8609;">.gitignore</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/.pre-commit-config.yaml" style="color: #0e9a0a;">.pre-commit-config.yaml</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/CNAME" style="color: #64c79f;">CNAME</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/file_list.txt" style="color: #00d797;">file_list.txt</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/kiwifarms.conf" style="color: #de0d31;">kiwifarms.conf</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/pytest.ini" style="color: #3f5171;">pytest.ini</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/README.md" style="color: #e417b9;">README.md</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/README.rst" style="color: #f88ab0;">README.rst</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/requirements.txt" style="color: #42fc87;">requirements.txt</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/script.log" style="color: #59d30f;">script.log</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/sitemap.xml" style="color: #b0fc3c;">sitemap.xml</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/visualization.log" style="color: #f9f3d1;">visualization.log</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/_config.yml" style="color: #648227;">_config.yml</a></li>
<h2>data</h2>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/connection_url_list.txt" style="color: #d0643a;">data\connection_url_list.txt</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/member_url_list.txt" style="color: #7bcf52;">data\member_url_list.txt</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/page_url_list.txt" style="color: #0a36b5;">data\page_url_list.txt</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/reaction_url_list.txt" style="color: #70ea50;">data\reaction_url_list.txt</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/sitemap-1.xml" style="color: #7ff39f;">data\sitemap-1.xml</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/sitemap-2.xml" style="color: #5f3150;">data\sitemap-2.xml</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/sitemap-3.xml" style="color: #3ee585;">data\sitemap-3.xml</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/sitemap-4.xml" style="color: #f67e5e;">data\sitemap-4.xml</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/thread_url_list.txt" style="color: #eaaab5;">data\thread_url_list.txt</a></li>
<h2>data\downloaded_members</h2>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members/10.html" style="color: #3d97c0;">data\downloaded_members\10.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members/11.html" style="color: #9b0493;">data\downloaded_members\11.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members/12.html" style="color: #d2395a;">data\downloaded_members\12.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members/3.html" style="color: #1ee280;">data\downloaded_members\3.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members/4.html" style="color: #9ce346;">data\downloaded_members\4.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members/5.html" style="color: #21c456;">data\downloaded_members\5.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members/6.html" style="color: #963d04;">data\downloaded_members\6.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members/7.html" style="color: #4795ac;">data\downloaded_members\7.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members/8.html" style="color: #2bc013;">data\downloaded_members\8.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members/9.html" style="color: #498903;">data\downloaded_members\9.html</a></li>
<h2>data\downloaded_members_about</h2>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members_about/members.brooklynbailiff.3.about.html" style="color: #3f2cf5;">data\downloaded_members_about\members.brooklynbailiff.3.about.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members_about/members.champthom.2.about.html" style="color: #15538c;">data\downloaded_members_about\members.champthom.2.about.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members_about/members.null.1.about.html" style="color: #3095d5;">data\downloaded_members_about\members.null.1.about.html</a></li>
<h2>data\downloaded_members_connections</h2>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page1.html" style="color: #e7de55;">data\downloaded_members_connections\1.followers.connections.page1.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page10.html" style="color: #f02568;">data\downloaded_members_connections\1.followers.connections.page10.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page11.html" style="color: #75ec95;">data\downloaded_members_connections\1.followers.connections.page11.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page12.html" style="color: #1606f3;">data\downloaded_members_connections\1.followers.connections.page12.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page13.html" style="color: #6cfa7d;">data\downloaded_members_connections\1.followers.connections.page13.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page14.html" style="color: #d57842;">data\downloaded_members_connections\1.followers.connections.page14.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page15.html" style="color: #2159c0;">data\downloaded_members_connections\1.followers.connections.page15.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page16.html" style="color: #3bc2ec;">data\downloaded_members_connections\1.followers.connections.page16.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page17.html" style="color: #db4b5b;">data\downloaded_members_connections\1.followers.connections.page17.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page18.html" style="color: #1429cb;">data\downloaded_members_connections\1.followers.connections.page18.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page19.html" style="color: #9dd542;">data\downloaded_members_connections\1.followers.connections.page19.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page2.html" style="color: #43e86d;">data\downloaded_members_connections\1.followers.connections.page2.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page20.html" style="color: #c950e1;">data\downloaded_members_connections\1.followers.connections.page20.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page21.html" style="color: #e0eba6;">data\downloaded_members_connections\1.followers.connections.page21.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page22.html" style="color: #506e6f;">data\downloaded_members_connections\1.followers.connections.page22.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page23.html" style="color: #f86d26;">data\downloaded_members_connections\1.followers.connections.page23.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page24.html" style="color: #2c8763;">data\downloaded_members_connections\1.followers.connections.page24.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page25.html" style="color: #08c616;">data\downloaded_members_connections\1.followers.connections.page25.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page26.html" style="color: #fdc49e;">data\downloaded_members_connections\1.followers.connections.page26.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page27.html" style="color: #93a5dc;">data\downloaded_members_connections\1.followers.connections.page27.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page28.html" style="color: #a28421;">data\downloaded_members_connections\1.followers.connections.page28.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page29.html" style="color: #a57d6d;">data\downloaded_members_connections\1.followers.connections.page29.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page3.html" style="color: #90166e;">data\downloaded_members_connections\1.followers.connections.page3.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page4.html" style="color: #7086b9;">data\downloaded_members_connections\1.followers.connections.page4.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page5.html" style="color: #85d06a;">data\downloaded_members_connections\1.followers.connections.page5.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page6.html" style="color: #766927;">data\downloaded_members_connections\1.followers.connections.page6.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page7.html" style="color: #eb0342;">data\downloaded_members_connections\1.followers.connections.page7.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page8.html" style="color: #80ac1a;">data\downloaded_members_connections\1.followers.connections.page8.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page9.html" style="color: #73481e;">data\downloaded_members_connections\1.followers.connections.page9.html</a></li>
<h2>data\downloaded_pages</h2>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_pages/steven-bonnell-ii-destiny-destiny-gg.29205_page-1.html" style="color: #032fd1;">data\downloaded_pages\steven-bonnell-ii-destiny-destiny-gg.29205_page-1.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_pages/steven-bonnell-ii-destiny-destiny-gg.29205_page-2.html" style="color: #da360a;">data\downloaded_pages\steven-bonnell-ii-destiny-destiny-gg.29205_page-2.html</a></li>
<h2>data\downloaded_reactions</h2>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_reactions/posts_100_reactions_page_1.html" style="color: #613b17;">data\downloaded_reactions\posts_100_reactions_page_1.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_reactions/posts_1_reactions_page_1.html" style="color: #c8cb9f;">data\downloaded_reactions\posts_1_reactions_page_1.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_reactions/posts_2127398_reactions_page_1.html" style="color: #0df19f;">data\downloaded_reactions\posts_2127398_reactions_page_1.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_reactions/posts_96_reactions_page_1.html" style="color: #300636;">data\downloaded_reactions\posts_96_reactions_page_1.html</a></li>
<h2>data\downloaded_threads</h2>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/christian-sees-the-sights.14.html" style="color: #e150be;">data\downloaded_threads\christian-sees-the-sights.14.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/christian-sees-the-sights.32.html" style="color: #ab1787;">data\downloaded_threads\christian-sees-the-sights.32.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/christian-sees-the-sights.32_page-2.html" style="color: #0930a2;">data\downloaded_threads\christian-sees-the-sights.32_page-2.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/christian-sees-the-sights.32_page-3.html" style="color: #cac952;">data\downloaded_threads\christian-sees-the-sights.32_page-3.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/so-this-is-completely-permanent.12.html" style="color: #d12649;">data\downloaded_threads\so-this-is-completely-permanent.12.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/so-this-is-completely-permanent.30.html" style="color: #6bc768;">data\downloaded_threads\so-this-is-completely-permanent.30.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/the-general-forum-rules.10.html" style="color: #9e4e87;">data\downloaded_threads\the-general-forum-rules.10.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/the-general-forum-rules.28.html" style="color: #25fb94;">data\downloaded_threads\the-general-forum-rules.28.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/the-universal-rules.24.html" style="color: #69e46a;">data\downloaded_threads\the-universal-rules.24.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/the-universal-rules.6.html" style="color: #1e1ead;">data\downloaded_threads\the-universal-rules.6.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/welcome-to-the-new-permanent-cwcki-forums.1.html" style="color: #a0af15;">data\downloaded_threads\welcome-to-the-new-permanent-cwcki-forums.1.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/welcome-to-the-new-permanent-cwcki-forums.18.html" style="color: #b15763;">data\downloaded_threads\welcome-to-the-new-permanent-cwcki-forums.18.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/welcome-to-the-new-permanent-cwcki-forums.18_page-2.html" style="color: #cbf78f;">data\downloaded_threads\welcome-to-the-new-permanent-cwcki-forums.18_page-2.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/welcome-to-the-new-permanent-cwcki-forums.18_page-3.html" style="color: #0969ba;">data\downloaded_threads\welcome-to-the-new-permanent-cwcki-forums.18_page-3.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/welcome-to-the-new-permanent-cwcki-forums.1_page-2.html" style="color: #0c1f28;">data\downloaded_threads\welcome-to-the-new-permanent-cwcki-forums.1_page-2.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/welcome-to-the-new-permanent-cwcki-forums.1_page-3.html" style="color: #53d87b;">data\downloaded_threads\welcome-to-the-new-permanent-cwcki-forums.1_page-3.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/what-has-chris-chan-ruined-for-you.17.html" style="color: #b757d8;">data\downloaded_threads\what-has-chris-chan-ruined-for-you.17.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/what-has-chris-chan-ruined-for-you.17_page-2.html" style="color: #50cbc4;">data\downloaded_threads\what-has-chris-chan-ruined-for-you.17_page-2.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/what-has-chris-chan-ruined-for-you.17_page-3.html" style="color: #669b17;">data\downloaded_threads\what-has-chris-chan-ruined-for-you.17_page-3.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/what-has-chris-chan-ruined-for-you.17_page-4.html" style="color: #acaffc;">data\downloaded_threads\what-has-chris-chan-ruined-for-you.17_page-4.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/what-has-chris-chan-ruined-for-you.17_page-5.html" style="color: #63f0a6;">data\downloaded_threads\what-has-chris-chan-ruined-for-you.17_page-5.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/what-has-chris-chan-ruined-for-you.17_page-6.html" style="color: #aac148;">data\downloaded_threads\what-has-chris-chan-ruined-for-you.17_page-6.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/what-has-chris-chan-ruined-for-you.17_page-7.html" style="color: #9d8cb4;">data\downloaded_threads\what-has-chris-chan-ruined-for-you.17_page-7.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/worst-sonichu-pages.16.html" style="color: #dffbb2;">data\downloaded_threads\worst-sonichu-pages.16.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/worst-sonichu-pages.16_page-10.html" style="color: #7ff79b;">data\downloaded_threads\worst-sonichu-pages.16_page-10.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/worst-sonichu-pages.16_page-11.html" style="color: #1738f8;">data\downloaded_threads\worst-sonichu-pages.16_page-11.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/worst-sonichu-pages.16_page-12.html" style="color: #2f96d5;">data\downloaded_threads\worst-sonichu-pages.16_page-12.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/worst-sonichu-pages.16_page-13.html" style="color: #97aed9;">data\downloaded_threads\worst-sonichu-pages.16_page-13.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/worst-sonichu-pages.16_page-14.html" style="color: #25a821;">data\downloaded_threads\worst-sonichu-pages.16_page-14.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/worst-sonichu-pages.16_page-15.html" style="color: #472ac6;">data\downloaded_threads\worst-sonichu-pages.16_page-15.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/worst-sonichu-pages.16_page-16.html" style="color: #5b77fe;">data\downloaded_threads\worst-sonichu-pages.16_page-16.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/worst-sonichu-pages.16_page-17.html" style="color: #3bf4ba;">data\downloaded_threads\worst-sonichu-pages.16_page-17.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/worst-sonichu-pages.16_page-18.html" style="color: #bdb500;">data\downloaded_threads\worst-sonichu-pages.16_page-18.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/worst-sonichu-pages.16_page-19.html" style="color: #874e14;">data\downloaded_threads\worst-sonichu-pages.16_page-19.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/worst-sonichu-pages.16_page-2.html" style="color: #bb4bf5;">data\downloaded_threads\worst-sonichu-pages.16_page-2.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/worst-sonichu-pages.16_page-20.html" style="color: #c032f1;">data\downloaded_threads\worst-sonichu-pages.16_page-20.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/worst-sonichu-pages.16_page-3.html" style="color: #a88237;">data\downloaded_threads\worst-sonichu-pages.16_page-3.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/worst-sonichu-pages.16_page-4.html" style="color: #444bc8;">data\downloaded_threads\worst-sonichu-pages.16_page-4.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/worst-sonichu-pages.16_page-5.html" style="color: #d593cd;">data\downloaded_threads\worst-sonichu-pages.16_page-5.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/worst-sonichu-pages.16_page-6.html" style="color: #d4a3be;">data\downloaded_threads\worst-sonichu-pages.16_page-6.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/worst-sonichu-pages.16_page-7.html" style="color: #efa06a;">data\downloaded_threads\worst-sonichu-pages.16_page-7.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/worst-sonichu-pages.16_page-8.html" style="color: #8328ff;">data\downloaded_threads\worst-sonichu-pages.16_page-8.html</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data/downloaded_threads/worst-sonichu-pages.16_page-9.html" style="color: #ee2087;">data\downloaded_threads\worst-sonichu-pages.16_page-9.html</a></li>
<h2>data_visuals</h2>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data_visuals/follower_network.png" style="color: #67cc08;">data_visuals\follower_network.png</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data_visuals/follower_network_analysis.png" style="color: #47ad3c;">data_visuals\follower_network_analysis.png</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data_visuals/messages_over_time.png" style="color: #55e240;">data_visuals\messages_over_time.png</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data_visuals/message_length_distribution.png" style="color: #c07efd;">data_visuals\message_length_distribution.png</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data_visuals/sentiment_distribution.png" style="color: #5c640e;">data_visuals\sentiment_distribution.png</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data_visuals/top_contributors.png" style="color: #067a0e;">data_visuals\top_contributors.png</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data_visuals/user_activity_heatmap.png" style="color: #c3e143;">data_visuals\user_activity_heatmap.png</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data_visuals/user_role_distribution.png" style="color: #3523f3;">data_visuals\user_role_distribution.png</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data_visuals/word_cloud.png" style="color: #6ad5fd;">data_visuals\word_cloud.png</a></li>
<h2>data_visuals\old</h2>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data_visuals/old/follower_network.png" style="color: #636d13;">data_visuals\old\follower_network.png</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data_visuals/old/follower_network_analysis.png" style="color: #bab9b5;">data_visuals\old\follower_network_analysis.png</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data_visuals/old/messages_over_time.png" style="color: #779224;">data_visuals\old\messages_over_time.png</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data_visuals/old/message_length_distribution.png" style="color: #2eb839;">data_visuals\old\message_length_distribution.png</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data_visuals/old/sentiment_distribution.png" style="color: #a5d1a6;">data_visuals\old\sentiment_distribution.png</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data_visuals/old/top_contributors.png" style="color: #088e1d;">data_visuals\old\top_contributors.png</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data_visuals/old/user_1_activity_heatmap.png" style="color: #05c771;">data_visuals\old\user_1_activity_heatmap.png</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data_visuals/old/user_1_messages_over_time.png" style="color: #67bb61;">data_visuals\old\user_1_messages_over_time.png</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data_visuals/old/user_2_activity_heatmap.png" style="color: #54d805;">data_visuals\old\user_2_activity_heatmap.png</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data_visuals/old/user_2_messages_over_time.png" style="color: #9f738c;">data_visuals\old\user_2_messages_over_time.png</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data_visuals/old/user_activity_heatmap.png" style="color: #b0344c;">data_visuals\old\user_activity_heatmap.png</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data_visuals/old/user_role_distribution.png" style="color: #59cdd9;">data_visuals\old\user_role_distribution.png</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/data_visuals/old/word_cloud.png" style="color: #b09d4f;">data_visuals\old\word_cloud.png</a></li>
<h2>docs</h2>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/docs/alias.rst_" style="color: #370e0f;">docs\alias.rst_</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/docs/default_apidocs.sh" style="color: #55cfcf;">docs\default_apidocs.sh</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/docs/index.rst" style="color: #f1abec;">docs\index.rst</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/docs/introduction.rst" style="color: #81e5a0;">docs\introduction.rst</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/docs/make.bat" style="color: #e26359;">docs\make.bat</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/docs/Makefile" style="color: #56c071;">docs\Makefile</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/docs/overview.rst" style="color: #093da2;">docs\overview.rst</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/docs/quickstart.rst" style="color: #b996a0;">docs\quickstart.rst</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/docs/workflow.rst" style="color: #129717;">docs\workflow.rst</a></li>
<h2>docs\figs</h2>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/docs/figs/database_schema.svg" style="color: #2658b7;">docs\figs\database_schema.svg</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/docs/figs/favicon.ico" style="color: #892963;">docs\figs\favicon.ico</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/docs/figs/logo.svg" style="color: #e024a9;">docs\figs\logo.svg</a></li>
<h2>docs\tests</h2>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/docs/tests/test_alias.rst_" style="color: #938bb8;">docs\tests\test_alias.rst_</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/docs/tests/test_index.rst" style="color: #be0382;">docs\tests\test_index.rst</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/docs/tests/test_make.bat" style="color: #b3bbe2;">docs\tests\test_make.bat</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/docs/tests/test_Makefile" style="color: #b76b4c;">docs\tests\test_Makefile</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/docs/tests/test_overview.rst" style="color: #7b491e;">docs\tests\test_overview.rst</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/docs/tests/test_quickstart.rst" style="color: #a61820;">docs\tests\test_quickstart.rst</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/docs/tests/test_workflow.rst" style="color: #f23c76;">docs\tests\test_workflow.rst</a></li>
<h2>kiwifarmer\__pycache__</h2>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/kiwifarmer/__pycache__/base.cpython-311.pyc" style="color: #487fc1;">kiwifarmer\__pycache__\base.cpython-311.pyc</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/kiwifarmer/__pycache__/functions.cpython-311.pyc" style="color: #7c4d80;">kiwifarmer\__pycache__\functions.cpython-311.pyc</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/kiwifarmer/__pycache__/templates.cpython-311.pyc" style="color: #86e953;">kiwifarmer\__pycache__\templates.cpython-311.pyc</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/kiwifarmer/__pycache__/utils.cpython-311.pyc" style="color: #360fff;">kiwifarmer\__pycache__\utils.cpython-311.pyc</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/kiwifarmer/__pycache__/__init__.cpython-311.pyc" style="color: #c85ba7;">kiwifarmer\__pycache__\__init__.cpython-311.pyc</a></li>
<h2>.github</h2>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/.github/dependabot.yml" style="color: #1e1055;">.github\dependabot.yml</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/.github/labeler.yml" style="color: #fa96ab;">.github\labeler.yml</a></li>
<h2>.github\ISSUE_TEMPLATE</h2>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/.github/ISSUE_TEMPLATE/bug_report.md" style="color: #77c706;">.github\ISSUE_TEMPLATE\bug_report.md</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/.github/ISSUE_TEMPLATE/feature_request.md" style="color: #9a2ae4;">.github\ISSUE_TEMPLATE\feature_request.md</a></li>
<h2>.github\PULL_REQUEST_TEMPLATE</h2>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/.github/PULL_REQUEST_TEMPLATE/pull_request_template.md" style="color: #04d447;">.github\PULL_REQUEST_TEMPLATE\pull_request_template.md</a></li>
<h2>.github\workflows</h2>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/.github/workflows/ActionLint.yml" style="color: #615e8e;">.github\workflows\ActionLint.yml</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/.github/workflows/Bandit.yml" style="color: #a10f55;">.github\workflows\Bandit.yml</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/.github/workflows/black-formatter.yml" style="color: #159389;">.github\workflows\black-formatter.yml</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/.github/workflows/codeql.yml" style="color: #31f2dd;">.github\workflows\codeql.yml</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/.github/workflows/dependency-review.yml" style="color: #2d645e;">.github\workflows\dependency-review.yml</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/.github/workflows/greetings.yml" style="color: #856c3c;">.github\workflows\greetings.yml</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/.github/workflows/label.yml" style="color: #34c282;">.github\workflows\label.yml</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/.github/workflows/ossar.yml" style="color: #e1d846;">.github\workflows\ossar.yml</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/.github/workflows/osv-scanner.yml" style="color: #43c128;">.github\workflows\osv-scanner.yml</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/.github/workflows/pylint.yml" style="color: #6f2128;">.github\workflows\pylint.yml</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/.github/workflows/scorecards.yml" style="color: #583e92;">.github\workflows\scorecards.yml</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/.github/workflows/sitemap.yml" style="color: #258af3;">.github\workflows\sitemap.yml</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/.github/workflows/sobelow.yml" style="color: #7bdd73;">.github\workflows\sobelow.yml</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/.github/workflows/stale.yml" style="color: #d7f397;">.github\workflows\stale.yml</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/.github/workflows/static.yml" style="color: #c867b6;">.github\workflows\static.yml</a></li>
<li><a href="https://github.com/Nick2bad4u/Kiwifarmer/blob/main/.github/workflows/super-linter.yml" style="color: #646076;">.github\workflows\super-linter.yml</a></li></ul>
