import os
import pytest
from unittest.mock import MagicMock, patch, mock_open
from bs4 import BeautifulSoup
from kiwifarmer import base, templates
import logging

import mysql.connector  # type: ignore


@pytest.fixture
def mock_env(monkeypatch):
    monkeypatch.setenv('KIWIFARMER_USER', 'testuser')
    monkeypatch.setenv('KIWIFARMER_PASSWORD', 'testpass')


@pytest.fixture
def mock_db():
    conn = MagicMock()
    cursor = MagicMock()
    conn.cursor.return_value = cursor
    return conn, cursor


@patch('os.listdir')
@patch('builtins.open', new_callable=mock_open, read_data='<html></html>')
@patch('mysql.connector.connect')
def test_insert_pages(mock_connect, mock_file, mock_listdir, mock_env, mock_db):
    conn, cursor = mock_db
    mock_connect.return_value = conn
    mock_listdir.return_value = ['page1.html', 'page2.html']

    # Mock base.Page and base.Post
    with patch.object(base, 'Page') as MockPage, patch.object(base, 'Post') as MockPost:
        mock_page_instance = MagicMock()
        mock_page_instance.get_post_soups.return_value = [
            'post_soup1', 'post_soup2']
        MockPage.return_value = mock_page_instance

        mock_post_instance = MagicMock()
        mock_post_instance.post_insertion = ('some post insert data', )
        mock_post_instance.blockquote_insertions = [('bq1', ), ('bq2', )]
        mock_post_instance.link_insertions = [('link1', ), ('link2', )]
        mock_post_instance.image_insertions = [('img1', ), ('img2', )]
        MockPost.return_value = mock_post_instance

        # Run script logic
        import workflow.BC_insert_pages  # The script should connect and process pages

        assert mock_connect.called
        assert mock_listdir.called
        cursor.execute.assert_any_call(
            templates.ADD_POST, mock_post_instance.post_insertion)
        cursor.executemany.assert_any_call(
            templates.ADD_BLOCKQUOTE, mock_post_instance.blockquote_insertions)
        cursor.executemany.assert_any_call(
            templates.ADD_LINK, mock_post_instance.link_insertions)
        cursor.executemany.assert_any_call(
            templates.ADD_IMAGE, mock_post_instance.image_insertions)
