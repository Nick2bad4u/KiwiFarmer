
KiwiFarmer
==========

![Alt](https://repobeats.axiom.co/api/embed/3ab62a4d52db28cc259144d42f26e64742445948.svg "Repobeats analytics image")

KiwiFarmer is a Python package for scraping KiwiFarms threads and posts, extracting field values, and storing the results in a created MySQL database.

Run script
----------

KiwiFarmer includes a script (`run_smat.py`) for indexing all KiwiFarms posts into an Elasticsearch instance. The script uses a Redis database to keep track of which pages have already been indexed, which avoids redundant reindexing operations.
The script can be run perpetually using the command:

.. code-block:: bash

  watch -n0 python run_smat.py

Workflow
--------

KiwiFarmer also includes scripts for a workflow that downloads all website pages as HTML files, extracts relevant field data, and stores the data in a MySQL database.
These scripts are in the `workflow/` subdirectory in the package root directory.
For more information, see `docs/workflow.rst`

TODO
----

* add additional user fields for user signature and location

* expand unit tests

  * verify correctness of functions

* expand instructions and info of docs

* config file parsing

* analysis tools/utilities/visualizations

* improve input argument handling for classes (e.g. type conversion/checking)

## File List

Here is a list of files included in this repository:

- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/.gitignore" style="color: #1f764d;">.gitignore</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/.pre-commit-config.yaml" style="color: #717b76;">.pre-commit-config.yaml</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/CNAME" style="color: #d91285;">CNAME</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/file_list.txt" style="color: #b98b19;">file_list.txt</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/generate-file-list.py" style="color: #c547da;">generate-file-list.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/kiwifarms.conf" style="color: #5db4bf;">kiwifarms.conf</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/kiwifarms_20210224.json" style="color: #2c845a;">kiwifarms_20210224.json</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/kiwifarms_combined_database.json" style="color: #077b0c;">kiwifarms_combined_database.json</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/kiwifarms_following_20210224.json" style="color: #eae831;">kiwifarms_following_20210224.json</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/kiwifarms_reorganized_database.json" style="color: #156ebf;">kiwifarms_reorganized_database.json</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/kiwifarms_trophies_20210224.json" style="color: #23efcd;">kiwifarms_trophies_20210224.json</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/kiwifarms_users_20210224.json" style="color: #a7d0d6;">kiwifarms_users_20210224.json</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/pytest.ini" style="color: #e5d6f3;">pytest.ini</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/README.md" style="color: #a1cefe;">README.md</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/README.rst" style="color: #80787e;">README.rst</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/requirements.txt" style="color: #73a9b8;">requirements.txt</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/run_smat.py" style="color: #175707;">run_smat.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/script.log" style="color: #306d53;">script.log</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/setup.py" style="color: #3cc642;">setup.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/sitemap.xml" style="color: #98c4cc;">sitemap.xml</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/sort_json_database.py" style="color: #8ea211;">sort_json_database.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/visualization.log" style="color: #d6a332;">visualization.log</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/_config.yml" style="color: #e172f6;">_config.yml</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/.github/dependabot.yml" style="color: #82df76;">.github\dependabot.yml</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/.github/labeler.yml" style="color: #050f9f;">.github\labeler.yml</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/.github/ISSUE_TEMPLATE/bug_report.md" style="color: #1e01c5;">.github\ISSUE_TEMPLATE\bug_report.md</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/.github/ISSUE_TEMPLATE/feature_request.md" style="color: #bc9bc0;">.github\ISSUE_TEMPLATE\feature_request.md</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/.github/PULL_REQUEST_TEMPLATE/pull_request_template.md" style="color: #7660a2;">.github\PULL_REQUEST_TEMPLATE\pull_request_template.md</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/.github/workflows/ActionLint.yml" style="color: #a1d616;">.github\workflows\ActionLint.yml</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/.github/workflows/Bandit.yml" style="color: #cc5c86;">.github\workflows\Bandit.yml</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/.github/workflows/black-formatter.yml" style="color: #cf2c3f;">.github\workflows\black-formatter.yml</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/.github/workflows/codeql.yml" style="color: #4bb960;">.github\workflows\codeql.yml</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/.github/workflows/dependency-review.yml" style="color: #748118;">.github\workflows\dependency-review.yml</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/.github/workflows/greetings.yml" style="color: #2b287c;">.github\workflows\greetings.yml</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/.github/workflows/label.yml" style="color: #a3569d;">.github\workflows\label.yml</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/.github/workflows/ossar.yml" style="color: #f68180;">.github\workflows\ossar.yml</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/.github/workflows/osv-scanner.yml" style="color: #d25451;">.github\workflows\osv-scanner.yml</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/.github/workflows/pylint.yml" style="color: #bddeae;">.github\workflows\pylint.yml</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/.github/workflows/scorecards.yml" style="color: #ab886e;">.github\workflows\scorecards.yml</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/.github/workflows/sitemap.yml" style="color: #763431;">.github\workflows\sitemap.yml</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/.github/workflows/sobelow.yml" style="color: #87f15c;">.github\workflows\sobelow.yml</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/.github/workflows/stale.yml" style="color: #7e160f;">.github\workflows\stale.yml</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/.github/workflows/static.yml" style="color: #c579dd;">.github\workflows\static.yml</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/.github/workflows/super-linter.yml" style="color: #9f4883;">.github\workflows\super-linter.yml</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/.vscode/settings.json" style="color: #4fcaf1;">.vscode\settings.json</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/connection_url_list.json" style="color: #4a4f62;">data\connection_url_list.json</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/connection_url_list.txt" style="color: #655b7f;">data\connection_url_list.txt</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/member_url_list.txt" style="color: #458c47;">data\member_url_list.txt</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/page_url_list.txt" style="color: #654ea4;">data\page_url_list.txt</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/reaction_data.json" style="color: #3237a9;">data\reaction_data.json</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/reaction_url_list.txt" style="color: #a43787;">data\reaction_url_list.txt</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/sitemap-1.xml" style="color: #115593;">data\sitemap-1.xml</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/sitemap-2.xml" style="color: #2ae072;">data\sitemap-2.xml</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/sitemap-3.xml" style="color: #bd8bfa;">data\sitemap-3.xml</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/sitemap-4.xml" style="color: #41d10c;">data\sitemap-4.xml</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/thread_url_list.txt" style="color: #a806c8;">data\thread_url_list.txt</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members/10.html" style="color: #c64d90;">data\downloaded_members\10.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members/11.html" style="color: #ec9d7c;">data\downloaded_members\11.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members/12.html" style="color: #98fe37;">data\downloaded_members\12.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members/3.html" style="color: #c601f7;">data\downloaded_members\3.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members/4.html" style="color: #1a9298;">data\downloaded_members\4.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members/5.html" style="color: #742e42;">data\downloaded_members\5.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members/6.html" style="color: #d9dc0b;">data\downloaded_members\6.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members/7.html" style="color: #97686d;">data\downloaded_members\7.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members/8.html" style="color: #459473;">data\downloaded_members\8.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members/9.html" style="color: #80b3b4;">data\downloaded_members\9.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members_about/members.brooklynbailiff.3.about.html" style="color: #b370a2;">data\downloaded_members_about\members.brooklynbailiff.3.about.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members_about/members.champthom.2.about.html" style="color: #738338;">data\downloaded_members_about\members.champthom.2.about.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members_about/members.null.1.about.html" style="color: #bb1f80;">data\downloaded_members_about\members.null.1.about.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page1.html" style="color: #3da937;">data\downloaded_members_connections\1.followers.connections.page1.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page10.html" style="color: #15ccea;">data\downloaded_members_connections\1.followers.connections.page10.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page11.html" style="color: #c62d2c;">data\downloaded_members_connections\1.followers.connections.page11.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page12.html" style="color: #9ad939;">data\downloaded_members_connections\1.followers.connections.page12.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page13.html" style="color: #a65989;">data\downloaded_members_connections\1.followers.connections.page13.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page14.html" style="color: #63be93;">data\downloaded_members_connections\1.followers.connections.page14.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page15.html" style="color: #d42cc9;">data\downloaded_members_connections\1.followers.connections.page15.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page16.html" style="color: #5baa00;">data\downloaded_members_connections\1.followers.connections.page16.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page17.html" style="color: #64b538;">data\downloaded_members_connections\1.followers.connections.page17.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page18.html" style="color: #dbb5ae;">data\downloaded_members_connections\1.followers.connections.page18.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page19.html" style="color: #6a9aaa;">data\downloaded_members_connections\1.followers.connections.page19.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page2.html" style="color: #c8685d;">data\downloaded_members_connections\1.followers.connections.page2.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page20.html" style="color: #1d54b4;">data\downloaded_members_connections\1.followers.connections.page20.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page21.html" style="color: #f1641c;">data\downloaded_members_connections\1.followers.connections.page21.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page22.html" style="color: #e3a39d;">data\downloaded_members_connections\1.followers.connections.page22.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page23.html" style="color: #031a8f;">data\downloaded_members_connections\1.followers.connections.page23.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page24.html" style="color: #dc59d2;">data\downloaded_members_connections\1.followers.connections.page24.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page25.html" style="color: #5508eb;">data\downloaded_members_connections\1.followers.connections.page25.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page26.html" style="color: #ed52b2;">data\downloaded_members_connections\1.followers.connections.page26.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page27.html" style="color: #c6ab5c;">data\downloaded_members_connections\1.followers.connections.page27.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page28.html" style="color: #9bd80c;">data\downloaded_members_connections\1.followers.connections.page28.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page29.html" style="color: #3ee3c9;">data\downloaded_members_connections\1.followers.connections.page29.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page3.html" style="color: #a086fb;">data\downloaded_members_connections\1.followers.connections.page3.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page4.html" style="color: #65fa76;">data\downloaded_members_connections\1.followers.connections.page4.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page5.html" style="color: #2cd425;">data\downloaded_members_connections\1.followers.connections.page5.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page6.html" style="color: #8bf235;">data\downloaded_members_connections\1.followers.connections.page6.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page7.html" style="color: #e68f67;">data\downloaded_members_connections\1.followers.connections.page7.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page8.html" style="color: #73f94e;">data\downloaded_members_connections\1.followers.connections.page8.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_members_connections/1.followers.connections.page9.html" style="color: #22eb9e;">data\downloaded_members_connections\1.followers.connections.page9.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_pages/steven-bonnell-ii-destiny-destiny-gg.29205_page-1.html" style="color: #ba2c87;">data\downloaded_pages\steven-bonnell-ii-destiny-destiny-gg.29205_page-1.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_pages/steven-bonnell-ii-destiny-destiny-gg.29205_page-2.html" style="color: #81d80f;">data\downloaded_pages\steven-bonnell-ii-destiny-destiny-gg.29205_page-2.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_reactions/posts_100_reactions_page_1.html" style="color: #4b0d2c;">data\downloaded_reactions\posts_100_reactions_page_1.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_reactions/posts_1_reactions_page_1.html" style="color: #8aa571;">data\downloaded_reactions\posts_1_reactions_page_1.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_reactions/posts_2127398_reactions_page_1.html" style="color: #914016;">data\downloaded_reactions\posts_2127398_reactions_page_1.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_reactions/posts_96_reactions_page_1.html" style="color: #e90ed5;">data\downloaded_reactions\posts_96_reactions_page_1.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/christian-sees-the-sights.14.html" style="color: #f4fcac;">data\downloaded_threads\christian-sees-the-sights.14.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/christian-sees-the-sights.32.html" style="color: #2fcce8;">data\downloaded_threads\christian-sees-the-sights.32.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/christian-sees-the-sights.32_page-2.html" style="color: #52e2a4;">data\downloaded_threads\christian-sees-the-sights.32_page-2.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/christian-sees-the-sights.32_page-3.html" style="color: #ab9e2e;">data\downloaded_threads\christian-sees-the-sights.32_page-3.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/so-this-is-completely-permanent.12.html" style="color: #6791d9;">data\downloaded_threads\so-this-is-completely-permanent.12.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/so-this-is-completely-permanent.30.html" style="color: #a5e82e;">data\downloaded_threads\so-this-is-completely-permanent.30.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/the-general-forum-rules.10.html" style="color: #4b1a66;">data\downloaded_threads\the-general-forum-rules.10.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/the-general-forum-rules.28.html" style="color: #4fe69b;">data\downloaded_threads\the-general-forum-rules.28.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/the-universal-rules.24.html" style="color: #7ea3ac;">data\downloaded_threads\the-universal-rules.24.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/the-universal-rules.6.html" style="color: #725a2b;">data\downloaded_threads\the-universal-rules.6.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/welcome-to-the-new-permanent-cwcki-forums.1.html" style="color: #c61e5b;">data\downloaded_threads\welcome-to-the-new-permanent-cwcki-forums.1.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/welcome-to-the-new-permanent-cwcki-forums.18.html" style="color: #d0e371;">data\downloaded_threads\welcome-to-the-new-permanent-cwcki-forums.18.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/welcome-to-the-new-permanent-cwcki-forums.18_page-2.html" style="color: #5a1fe5;">data\downloaded_threads\welcome-to-the-new-permanent-cwcki-forums.18_page-2.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/welcome-to-the-new-permanent-cwcki-forums.18_page-3.html" style="color: #1e7ca4;">data\downloaded_threads\welcome-to-the-new-permanent-cwcki-forums.18_page-3.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/welcome-to-the-new-permanent-cwcki-forums.1_page-2.html" style="color: #212716;">data\downloaded_threads\welcome-to-the-new-permanent-cwcki-forums.1_page-2.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/welcome-to-the-new-permanent-cwcki-forums.1_page-3.html" style="color: #03e26a;">data\downloaded_threads\welcome-to-the-new-permanent-cwcki-forums.1_page-3.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/what-has-chris-chan-ruined-for-you.17.html" style="color: #f8eeaa;">data\downloaded_threads\what-has-chris-chan-ruined-for-you.17.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/what-has-chris-chan-ruined-for-you.17_page-2.html" style="color: #ab5c1f;">data\downloaded_threads\what-has-chris-chan-ruined-for-you.17_page-2.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/what-has-chris-chan-ruined-for-you.17_page-3.html" style="color: #24bef7;">data\downloaded_threads\what-has-chris-chan-ruined-for-you.17_page-3.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/what-has-chris-chan-ruined-for-you.17_page-4.html" style="color: #f536e2;">data\downloaded_threads\what-has-chris-chan-ruined-for-you.17_page-4.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/what-has-chris-chan-ruined-for-you.17_page-5.html" style="color: #11376c;">data\downloaded_threads\what-has-chris-chan-ruined-for-you.17_page-5.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/what-has-chris-chan-ruined-for-you.17_page-6.html" style="color: #3b2b73;">data\downloaded_threads\what-has-chris-chan-ruined-for-you.17_page-6.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/what-has-chris-chan-ruined-for-you.17_page-7.html" style="color: #e28ce2;">data\downloaded_threads\what-has-chris-chan-ruined-for-you.17_page-7.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/worst-sonichu-pages.16.html" style="color: #77fe87;">data\downloaded_threads\worst-sonichu-pages.16.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/worst-sonichu-pages.16_page-10.html" style="color: #b1c355;">data\downloaded_threads\worst-sonichu-pages.16_page-10.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/worst-sonichu-pages.16_page-11.html" style="color: #a39249;">data\downloaded_threads\worst-sonichu-pages.16_page-11.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/worst-sonichu-pages.16_page-12.html" style="color: #8297b3;">data\downloaded_threads\worst-sonichu-pages.16_page-12.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/worst-sonichu-pages.16_page-13.html" style="color: #008b7d;">data\downloaded_threads\worst-sonichu-pages.16_page-13.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/worst-sonichu-pages.16_page-14.html" style="color: #b63ec0;">data\downloaded_threads\worst-sonichu-pages.16_page-14.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/worst-sonichu-pages.16_page-15.html" style="color: #e80e27;">data\downloaded_threads\worst-sonichu-pages.16_page-15.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/worst-sonichu-pages.16_page-16.html" style="color: #7f455d;">data\downloaded_threads\worst-sonichu-pages.16_page-16.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/worst-sonichu-pages.16_page-17.html" style="color: #4d6c98;">data\downloaded_threads\worst-sonichu-pages.16_page-17.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/worst-sonichu-pages.16_page-18.html" style="color: #77e154;">data\downloaded_threads\worst-sonichu-pages.16_page-18.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/worst-sonichu-pages.16_page-19.html" style="color: #678ab8;">data\downloaded_threads\worst-sonichu-pages.16_page-19.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/worst-sonichu-pages.16_page-2.html" style="color: #f9444e;">data\downloaded_threads\worst-sonichu-pages.16_page-2.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/worst-sonichu-pages.16_page-20.html" style="color: #c0d233;">data\downloaded_threads\worst-sonichu-pages.16_page-20.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/worst-sonichu-pages.16_page-3.html" style="color: #d11537;">data\downloaded_threads\worst-sonichu-pages.16_page-3.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/worst-sonichu-pages.16_page-4.html" style="color: #1c406c;">data\downloaded_threads\worst-sonichu-pages.16_page-4.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/worst-sonichu-pages.16_page-5.html" style="color: #16db4b;">data\downloaded_threads\worst-sonichu-pages.16_page-5.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/worst-sonichu-pages.16_page-6.html" style="color: #277168;">data\downloaded_threads\worst-sonichu-pages.16_page-6.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/worst-sonichu-pages.16_page-7.html" style="color: #004bd3;">data\downloaded_threads\worst-sonichu-pages.16_page-7.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/worst-sonichu-pages.16_page-8.html" style="color: #dce630;">data\downloaded_threads\worst-sonichu-pages.16_page-8.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data/downloaded_threads/worst-sonichu-pages.16_page-9.html" style="color: #95ed7b;">data\downloaded_threads\worst-sonichu-pages.16_page-9.html</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data_visuals/follower_network.png" style="color: #6dd81a;">data_visuals\follower_network.png</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data_visuals/follower_network_analysis.png" style="color: #7d1d68;">data_visuals\follower_network_analysis.png</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data_visuals/messages_over_time.png" style="color: #cb5f1c;">data_visuals\messages_over_time.png</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data_visuals/message_length_distribution.png" style="color: #a05394;">data_visuals\message_length_distribution.png</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data_visuals/sentiment_distribution.png" style="color: #39d910;">data_visuals\sentiment_distribution.png</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data_visuals/top_contributors.png" style="color: #e85046;">data_visuals\top_contributors.png</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data_visuals/user_activity_heatmap.png" style="color: #db607c;">data_visuals\user_activity_heatmap.png</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data_visuals/user_role_distribution.png" style="color: #6cc8cf;">data_visuals\user_role_distribution.png</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data_visuals/word_cloud.png" style="color: #fbdb04;">data_visuals\word_cloud.png</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data_visuals/old/follower_network.png" style="color: #e8a721;">data_visuals\old\follower_network.png</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data_visuals/old/follower_network_analysis.png" style="color: #283894;">data_visuals\old\follower_network_analysis.png</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data_visuals/old/messages_over_time.png" style="color: #f6a634;">data_visuals\old\messages_over_time.png</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data_visuals/old/message_length_distribution.png" style="color: #ef9853;">data_visuals\old\message_length_distribution.png</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data_visuals/old/sentiment_distribution.png" style="color: #0c10a9;">data_visuals\old\sentiment_distribution.png</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data_visuals/old/top_contributors.png" style="color: #759c97;">data_visuals\old\top_contributors.png</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data_visuals/old/user_1_activity_heatmap.png" style="color: #efa79e;">data_visuals\old\user_1_activity_heatmap.png</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data_visuals/old/user_1_messages_over_time.png" style="color: #4cd79a;">data_visuals\old\user_1_messages_over_time.png</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data_visuals/old/user_2_activity_heatmap.png" style="color: #9fddad;">data_visuals\old\user_2_activity_heatmap.png</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data_visuals/old/user_2_messages_over_time.png" style="color: #6ec321;">data_visuals\old\user_2_messages_over_time.png</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data_visuals/old/user_activity_heatmap.png" style="color: #40d1db;">data_visuals\old\user_activity_heatmap.png</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data_visuals/old/user_role_distribution.png" style="color: #8238af;">data_visuals\old\user_role_distribution.png</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/data_visuals/old/word_cloud.png" style="color: #cf65a2;">data_visuals\old\word_cloud.png</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/docs/alias.rst_" style="color: #e60125;">docs\alias.rst_</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/docs/conf.py" style="color: #8db1dc;">docs\conf.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/docs/default_apidocs.sh" style="color: #7f2393;">docs\default_apidocs.sh</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/docs/index.rst" style="color: #ee4879;">docs\index.rst</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/docs/introduction.rst" style="color: #290dd3;">docs\introduction.rst</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/docs/make.bat" style="color: #061832;">docs\make.bat</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/docs/Makefile" style="color: #27db1f;">docs\Makefile</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/docs/overview.rst" style="color: #16049b;">docs\overview.rst</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/docs/quickstart.rst" style="color: #97792d;">docs\quickstart.rst</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/docs/workflow.rst" style="color: #1f3179;">docs\workflow.rst</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/docs/figs/database_schema.svg" style="color: #e40068;">docs\figs\database_schema.svg</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/docs/figs/favicon.ico" style="color: #541f94;">docs\figs\favicon.ico</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/docs/figs/logo.svg" style="color: #eed8fa;">docs\figs\logo.svg</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/docs/tests/test_alias.rst_" style="color: #488a15;">docs\tests\test_alias.rst_</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/docs/tests/test_conf.py" style="color: #1c6f69;">docs\tests\test_conf.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/docs/tests/test_index.rst" style="color: #8e30dd;">docs\tests\test_index.rst</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/docs/tests/test_make.bat" style="color: #37e876;">docs\tests\test_make.bat</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/docs/tests/test_Makefile" style="color: #73d7c7;">docs\tests\test_Makefile</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/docs/tests/test_overview.rst" style="color: #21524a;">docs\tests\test_overview.rst</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/docs/tests/test_quickstart.rst" style="color: #27c371;">docs\tests\test_quickstart.rst</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/docs/tests/test_workflow.rst" style="color: #73d69a;">docs\tests\test_workflow.rst</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/examples/export_database_csv.py" style="color: #db1e67;">examples\export_database_csv.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/examples/preprocess_reactions.py" style="color: #bc6895;">examples\preprocess_reactions.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/kiwifarmer/base.py" style="color: #b048f5;">kiwifarmer\base.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/kiwifarmer/functions.py" style="color: #e9bdba;">kiwifarmer\functions.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/kiwifarmer/templates.py" style="color: #b84215;">kiwifarmer\templates.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/kiwifarmer/utils.py" style="color: #bfed9d;">kiwifarmer\utils.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/kiwifarmer/__init__.py" style="color: #0c9afe;">kiwifarmer\__init__.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/kiwifarmer/__pycache__/base.cpython-311.pyc" style="color: #2b1f40;">kiwifarmer\__pycache__\base.cpython-311.pyc</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/kiwifarmer/__pycache__/functions.cpython-311.pyc" style="color: #473303;">kiwifarmer\__pycache__\functions.cpython-311.pyc</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/kiwifarmer/__pycache__/templates.cpython-311.pyc" style="color: #d9e337;">kiwifarmer\__pycache__\templates.cpython-311.pyc</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/kiwifarmer/__pycache__/utils.cpython-311.pyc" style="color: #1bce5a;">kiwifarmer\__pycache__\utils.cpython-311.pyc</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/kiwifarmer/__pycache__/__init__.cpython-311.pyc" style="color: #46aca2;">kiwifarmer\__pycache__\__init__.cpython-311.pyc</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/tests/test_AA_get_thread_url_list.py" style="color: #5adb87;">tests\test_AA_get_thread_url_list.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/tests/test_AB_download_all_threads.py" style="color: #f7a0c4;">tests\test_AB_download_all_threads.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/tests/test_AC_insert_threads.py" style="color: #883ef8;">tests\test_AC_insert_threads.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/tests/test_BA_get_page_url_list.py" style="color: #fb1a33;">tests\test_BA_get_page_url_list.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/tests/test_BB_download_all_pages.py" style="color: #fbea30;">tests\test_BB_download_all_pages.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/tests/test_BC_insert_pages.py" style="color: #572a38;">tests\test_BC_insert_pages.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/tests/test_CA_download_all_users.py" style="color: #931c6b;">tests\test_CA_download_all_users.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/tests/test_CB_insert_users.py" style="color: #ef8a15;">tests\test_CB_insert_users.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/tests/test_DA_download_all_users_about.py" style="color: #48d760;">tests\test_DA_download_all_users_about.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/tests/test_DB_get_users_following_list.py" style="color: #f15544;">tests\test_DB_get_users_following_list.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/tests/test_DC_download_all_users_following.py" style="color: #5c124b;">tests\test_DC_download_all_users_following.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/tests/test_DD_insert_following.py" style="color: #698dc5;">tests\test_DD_insert_following.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/tests/test_EA_insert_trophies.py" style="color: #dc10f9;">tests\test_EA_insert_trophies.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/tests/test_export_database_csv.py" style="color: #c7e3e0;">tests\test_export_database_csv.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/tests/test_FA_get_reaction_url_list.py" style="color: #9b3ba3;">tests\test_FA_get_reaction_url_list.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/tests/test_FB_download_all_reactions.py" style="color: #c6e90f;">tests\test_FB_download_all_reactions.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/tests/test_FC_preprocess_reactions.py" style="color: #d03e41;">tests\test_FC_preprocess_reactions.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/tests/test_FD_insert_reactions.py" style="color: #37d016;">tests\test_FD_insert_reactions.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/tests/test_FE_get_more_reactions.py" style="color: #c3218d;">tests\test_FE_get_more_reactions.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/tests/test_preprocess_reactions.py" style="color: #caa2dd;">tests\test_preprocess_reactions.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/tests/test_run_smat.py" style="color: #92f272;">tests\test_run_smat.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/tests/old_tests/base.py" style="color: #634be0;">tests\old_tests\base.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/tests/old_tests/conftest.py" style="color: #cd7dad;">tests\old_tests\conftest.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/tests/old_tests/functions.py" style="color: #0186a0;">tests\old_tests\functions.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/tests/old_tests/utils.py" style="color: #88bbbb;">tests\old_tests\utils.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/tests/old_tests/__init__.py" style="color: #2bfadf;">tests\old_tests\__init__.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/AA_get_thread_url_list.py" style="color: #c15ebb;">workflow\AA_get_thread_url_list.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/AB_download_all_threads.py" style="color: #33f079;">workflow\AB_download_all_threads.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/AC_insert_threads.py" style="color: #62f12d;">workflow\AC_insert_threads.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/BA_get_page_url_list.py" style="color: #4797cb;">workflow\BA_get_page_url_list.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/BB_download_all_pages.py" style="color: #12d3b6;">workflow\BB_download_all_pages.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/BC_insert_pages.py" style="color: #8fe210;">workflow\BC_insert_pages.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/CA_download_all_users.py" style="color: #2894cd;">workflow\CA_download_all_users.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/CB_insert_users.py" style="color: #af3d17;">workflow\CB_insert_users.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/DA_download_all_users_about.py" style="color: #22598b;">workflow\DA_download_all_users_about.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/DB_get_users_following_list.py" style="color: #a11b5a;">workflow\DB_get_users_following_list.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/DC_download_all_users_following.py" style="color: #522215;">workflow\DC_download_all_users_following.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/DD_insert_following.py" style="color: #ee30f6;">workflow\DD_insert_following.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/EA_insert_trophies.py" style="color: #dacd29;">workflow\EA_insert_trophies.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/FA_get_reaction_url_list.py" style="color: #38bd96;">workflow\FA_get_reaction_url_list.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/FB_download_all_reactions.py" style="color: #633415;">workflow\FB_download_all_reactions.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/FC_preprocess_reactions.py" style="color: #d82d7a;">workflow\FC_preprocess_reactions.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/FD_insert_reactions.py" style="color: #5b48e5;">workflow\FD_insert_reactions.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/FE_get_more_reactions.py" style="color: #28f615;">workflow\FE_get_more_reactions.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/GA_combine_data.py" style="color: #feb01a;">workflow\GA_combine_data.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/GB_organize_data.py" style="color: #d7a1ff;">workflow\GB_organize_data.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/GC_visualize_data_user_specific.py" style="color: #0e5654;">workflow\GC_visualize_data_user_specific.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/GD_visualize_follower_networks.py" style="color: #c5c5cf;">workflow\GD_visualize_follower_networks.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/GF_visualize_more_data.py" style="color: #c60db2;">workflow\GF_visualize_more_data.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/old_workflows/01-A_get_thread_url_list.py" style="color: #3af343;">workflow\old_workflows\01-A_get_thread_url_list.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/old_workflows/01-B_download_all_threads.py" style="color: #301ccc;">workflow\old_workflows\01-B_download_all_threads.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/old_workflows/01-C_insert_threads.py" style="color: #5a8051;">workflow\old_workflows\01-C_insert_threads.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/old_workflows/02-A_get_page_url_list.py" style="color: #50ca2d;">workflow\old_workflows\02-A_get_page_url_list.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/old_workflows/02-B_download_all_pages.py" style="color: #38a6e1;">workflow\old_workflows\02-B_download_all_pages.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/old_workflows/02-C_insert_pages.py" style="color: #5458c1;">workflow\old_workflows\02-C_insert_pages.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/old_workflows/03-A_download_all_users.py" style="color: #ffefe3;">workflow\old_workflows\03-A_download_all_users.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/old_workflows/03-B_insert_users.py" style="color: #d2e538;">workflow\old_workflows\03-B_insert_users.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/old_workflows/04-A_download_all_users_about.py" style="color: #b2f574;">workflow\old_workflows\04-A_download_all_users_about.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/old_workflows/04-B_get_users_following_list.py" style="color: #5fc8d3;">workflow\old_workflows\04-B_get_users_following_list.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/old_workflows/04-C_download_all_users_following.py" style="color: #cad134;">workflow\old_workflows\04-C_download_all_users_following.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/old_workflows/04-D_insert_following.py" style="color: #27e9ae;">workflow\old_workflows\04-D_insert_following.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/old_workflows/05-A_insert_trophies.py" style="color: #e498b9;">workflow\old_workflows\05-A_insert_trophies.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/old_workflows/06-A_get_reaction_url_list.py" style="color: #b776fd;">workflow\old_workflows\06-A_get_reaction_url_list.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/old_workflows/06-B_download_all_reactions.py" style="color: #15f0db;">workflow\old_workflows\06-B_download_all_reactions.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/old_workflows/06-C_preprocess_reactions.py" style="color: #3d05ba;">workflow\old_workflows\06-C_preprocess_reactions.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/old_workflows/06-D_insert_reactions.py" style="color: #5d599a;">workflow\old_workflows\06-D_insert_reactions.py</a>
- <a href="https://github.com/Nick2bad4u/KiwiFarmer/blob/main/workflow/old_workflows/06-E_get_more_reactions.py" style="color: #ec77e2;">workflow\old_workflows\06-E_get_more_reactions.py</a>


