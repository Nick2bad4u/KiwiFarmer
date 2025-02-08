import os
import pytest
from bs4 import BeautifulSoup
from unittest.mock import patch
from kiwifarmer import base
from workflow import templates
import logging

import mysql.connector

# Mocking the database connection for testing purposes
@pytest.fixture
def mock_db_connection():
    with patch('mysql.connector.connect') as mock_connect:
        yield mock_connect

# Mocking BeautifulSoup for file reading
@pytest.fixture
def mock_beautifulsoup():
    with patch('bs4.BeautifulSoup') as mock_soup:
        yield mock_soup

# Mocking the base.Following class
@pytest.fixture
def mock_following():
    with patch('kiwifarmer.base.Following') as mock_follow:
        yield mock_follow

# Test for database connection
def test_database_connection(mock_db_connection):
    os.environ['KIWIFARMER_USER'] = 'test_user'
    os.environ['KIWIFARMER_PASSWORD'] = 'test_password'
    mock_db_connection.return_value.cursor.return_value = 'cursor'

    # Execute the database connection part of the script
    try:
        cnx = mysql.connector.connect(
            user=os.getenv('KIWIFARMER_USER'),
            password=os.getenv('KIWIFARMER_PASSWORD'),
            host='127.0.0.1',
            database='kiwifarms_20210224',
            charset='utf8mb4',
            collation='utf8mb4_bin',
            use_unicode=True
        )
        cursor = cnx.cursor()
    except mysql.connector.Error as err:
        assert False, f"Database connection failed: {err}"

    # Assertions
    mock_db_connection.assert_called_once()
    assert cursor == 'cursor'

# Test for processing HTML files
def test_process_html_files(mock_beautifulsoup, mock_following, mock_db_connection, tmpdir, caplog):
    caplog.set_level(logging.INFO)
    # Create a dummy HTML file for testing
    test_html_file = tmpdir.join('test_following_file.html')
    test_html_file.write("<html><body><div>Test HTML Content</div></body></html>")

    # Set up mocks
    mock_beautifulsoup.return_value = BeautifulSoup("<html></html>", 'lxml')
    mock_following.return_value.following_insertions = [('user1', 'followed1'), ('user2', 'followed2')]
    mock_cursor = mock_db_connection.return_value.cursor.return_value
    mock_cursor.executemany.return_value = None
    mock_db_connection.return_value.commit.return_value = None
    mock_db_connection.return_value.close.return_value = None

    # Patch necessary variables and functions
    with patch('os.listdir', return_value=[test_html_file.basename]), \
         patch('os.path.join', return_value=str(test_html_file)), \
         patch('builtins.open', test_html_file.open()):

        # Execute the HTML processing part of the script
        import workflow.DD_insert_following as script
        script.PAGE_DIR = str(tmpdir)
        script.START = 0
        script.DATABASE = 'test_db'

        script.main()

        # Assertions
        mock_beautifulsoup.assert_called()
        mock_following.assert_called()
        mock_cursor.executemany.assert_called_with(templates.ADD_FOLLOWING, [('user1', 'followed1'), ('user2', 'followed2')])
        mock_db_connection.return_value.commit.assert_called()
        mock_db_connection.return_value.close.assert_called()
        assert "Successfully processed" in caplog.text

# Test for exception handling during HTML processing
def test_process_html_files_exception(mock_beautifulsoup, mock_following, mock_db_connection, tmpdir, caplog):
    caplog.set_level(logging.ERROR)

    # Create a dummy HTML file for testing
    test_html_file = tmpdir.join('test_following_file.html')
    test_html_file.write("<html><body><div>Test HTML Content</div></body></html>")

    # Set up mocks to raise an exception
    mock_beautifulsoup.side_effect = Exception("Test Exception")

    # Patch necessary variables and functions
    with patch('os.listdir', return_value=[test_html_file.basename]), \
         patch('os.path.join', return_value=str(test_html_file)), \
         patch('builtins.open', test_html_file.open()):

        # Execute the HTML processing part of the script
        import workflow.DD_insert_following as script
        script.PAGE_DIR = str(tmpdir)
        script.START = 0
        script.DATABASE = 'test_db'

        script.main()

        # Assertions
        assert "Failed to process" in caplog.text

# Test for exception handling during database commit
def test_database_commit_exception(mock_beautifulsoup, mock_following, mock_db_connection, tmpdir, caplog):
    caplog.set_level(logging.ERROR)

    # Create a dummy HTML file for testing
    test_html_file = tmpdir.join('test_following_file.html')
    test_html_file.write("<html><body><div>Test HTML Content</div></body></html>")

    # Set up mocks to raise an exception during commit
    mock_db_connection.return_value.commit.side_effect = mysql.connector.Error("Test Database Error")

    # Patch necessary variables and functions
    with patch('os.listdir', return_value=[test_html_file.basename]), \
         patch('os.path.join', return_value=str(test_html_file)), \
         patch('builtins.open', test_html_file.open()):

        # Execute the HTML processing part of the script
        import workflow.DD_insert_following as script
        script.PAGE_DIR = str(tmpdir)
        script.START = 0
        script.DATABASE = 'test_db'

        script.main()

        # Assertions
        assert "Error committing changes to the database" in caplog.text