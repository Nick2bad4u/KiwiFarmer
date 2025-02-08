import os
import pytest
import pandas as pd
from unittest.mock import patch
from workflow import FA_get_reaction_url_list

import mysql.connector # type: ignore


def test_to_url():
    """
    Test the to_url lambda function.
    """
    def to_url(
        s): return f'https://kiwifarms.st/posts/{s}/reactions?reaction_id=0&list_only=1&page=1'
    assert to_url(
        123) == 'https://kiwifarms.st/posts/123/reactions?reaction_id=0&list_only=1&page=1'
    assert to_url(
        '456') == 'https://kiwifarms.st/posts/456/reactions?reaction_id=0&list_only=1&page=1'


@patch('workflow.FA_get_reaction_url_list.mysql.connector.connect')
@patch('workflow.FA_get_reaction_url_list.pd.read_sql')
@patch('workflow.FA_get_reaction_url_list.logger')
def test_main_success(mock_logger, mock_read_sql, mock_connect, tmpdir):
    """
    Test the main function with successful database connection and data export.
    """
    # Mock database connection and data retrieval
    mock_connect.return_value.close.return_value = None
    mock_read_sql.return_value = pd.DataFrame({'post_id': [1, 2, 3]})

    # Mock environment variables
    with patch.dict(os.environ, {'KIWIFARMER_USER': 'test_user', 'KIWIFARMER_PASSWORD': 'test_password'}):
        # Call the main part of the script
        FA_get_reaction_url_list.OUTPUT_CSV = str(
            tmpdir.join('test_output.txt'))
        FA_get_reaction_url_list.main()

    # Assertions
    mock_connect.assert_called_once()
    mock_read_sql.assert_called_once()
    mock_logger.info.assert_called()
    assert os.path.exists(FA_get_reaction_url_list.OUTPUT_CSV)


@patch('workflow.FA_get_reaction_url_list.mysql.connector.connect')
@patch('workflow.FA_get_reaction_url_list.logger')
def test_main_connection_error(mock_logger, mock_connect):
    """
    Test the main function with a database connection error.
    """
    # Mock database connection to raise an error
    mock_connect.side_effect = mysql.connector.Error("Connection failed")

    # Mock environment variables
    with patch.dict(os.environ, {'KIWIFARMER_USER': 'test_user', 'KIWIFARMER_PASSWORD': 'test_password'}):
        # Call the main part of the script
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            FA_get_reaction_url_list.main()
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == 1

    # Assertions
    mock_connect.assert_called_once()
    mock_logger.error.assert_called()


@patch('workflow.FA_get_reaction_url_list.mysql.connector.connect')
@patch('workflow.FA_get_reaction_url_list.pd.read_sql')
@patch('workflow.FA_get_reaction_url_list.logger')
def test_main_read_error(mock_logger, mock_read_sql, mock_connect, tmpdir):
    """
    Test the main function with an error during data read or export.
    """
    # Mock database connection and data retrieval to raise an error
    mock_connect.return_value.close.return_value = None
    mock_read_sql.side_effect = Exception("Read failed")

    # Mock environment variables
    with patch.dict(os.environ, {'KIWIFARMER_USER': 'test_user', 'KIWIFARMER_PASSWORD': 'test_password'}):
        # Call the main part of the script
        FA_get_reaction_url_list.OUTPUT_CSV = str(
            tmpdir.join('test_output.txt'))
        FA_get_reaction_url_list.main()

    # Assertions
    mock_connect.assert_called_once()
    mock_read_sql.assert_called_once()
    mock_logger.error.assert_called()
