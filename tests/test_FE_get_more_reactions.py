import os
import pytest
from unittest.mock import patch, MagicMock
import pandas as pd
from bs4 import BeautifulSoup

import mysql.connector  # type: ignore

from workflow.FE_get_more_reactions import (
    setup_selenium,
    download_page,
    save_content,
    process_reaction_page,
    get_url_list,
    run,
    DATABASE,
    COMMAND
)


@pytest.fixture
def mock_selenium_driver():
    with patch('FE_get_more_reactions.webdriver.Chrome') as MockDriver:
        mock_driver = MagicMock()
        MockDriver.return_value = mock_driver
        yield mock_driver


@pytest.fixture
def mock_mysql_connector():
    with patch('FE_get_more_reactions.mysql.connector.connect') as MockConnector:
        mock_cnx = MagicMock()
        mock_cursor = MagicMock()
        mock_cnx.cursor.return_value = mock_cursor
        MockConnector.return_value = mock_cnx
        yield mock_cnx, mock_cursor


def test_setup_selenium(mock_selenium_driver):
    driver = setup_selenium()
    assert driver is not None
    mock_selenium_driver.assert_called_once()


def test_download_page(mock_selenium_driver):
    mock_selenium_driver.page_source = "<html><body>Test Content</body></html>"
    url = "http://example.com"
    content = download_page(url, mock_selenium_driver)
    assert content == "<html><body>Test Content</body></html>"
    mock_selenium_driver.get.assert_called_once_with(url)


def test_download_page_failure(mock_selenium_driver, caplog):
    mock_selenium_driver.get.side_effect = Exception("Failed to load")
    url = "http://example.com"
    content = download_page(url, mock_selenium_driver)
    assert content is None
    assert f"Failed to download {url}" in caplog.text


def test_save_content(tmpdir):
    output_dir = str(tmpdir)
    filename = "test_file.html"
    content = "<html><body>Test Content</body></html>"
    save_content(content, output_dir, filename)
    filepath = os.path.join(output_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        saved_content = f.read()
    assert saved_content == content


def test_get_url_list(mock_mysql_connector):
    mock_cnx, mock_cursor = mock_mysql_connector
    mock_df = pd.DataFrame({
        'post_id': [1, 1, 2, 2, 2],
        'other_col': [1, 2, 3, 4, 5]
    })
    with patch('FE_get_more_reactions.pd.read_sql', return_value=mock_df):
        urls = get_url_list(page=1)
        assert len(urls) == 0

    mock_df2 = pd.DataFrame({
        'post_id': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        'other_col': [1]*50
    })
    with patch('FE_get_more_reactions.pd.read_sql', return_value=mock_df2):
        urls = get_url_list(page=0)
        assert len(urls) == 1


def test_get_url_list_db_error(mock_mysql_connector, caplog):
    mock_mysql_connector[0].connect.side_effect = mysql.connector.Error(
        "Connection failed")
    urls = get_url_list(page=1)
    assert urls == []
    assert "Error connecting to the database" in caplog.text


@patch('FE_get_more_reactions.base.ReactionPage')
@patch('FE_get_more_reactions.base.Reaction')
def test_process_reaction_page(MockReaction, MockReactionPage, tmpdir, mock_mysql_connector):
    mock_cnx, mock_cursor = mock_mysql_connector
    output_dir = str(tmpdir)
    page_file = "test_page.html"
    filepath = os.path.join(output_dir, page_file)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("<html><body><div>Reaction</div></body></html>")

    mock_reaction_page = MagicMock()
    mock_reaction_page.get_reaction_soups.return_value = [
        BeautifulSoup("<div>Reaction</div>", 'lxml')]
    mock_reaction_page.post_id = 123
    MockReactionPage.return_value = mock_reaction_page

    mock_reaction = MagicMock()
    mock_reaction.reaction_insertion = {'key': 'value'}
    MockReaction.return_value = mock_reaction

    process_reaction_page(page_file, output_dir, mock_cursor)

    mock_cursor.execute.assert_called()

# The 'run' function involves too much external interaction (file system, database, selenium)
# to be easily unit tested.  Consider refactoring to isolate the parts that interact with
# external systems from the core logic, to make it more testable.
