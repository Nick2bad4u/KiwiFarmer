import os
import pytest
import pandas as pd
from unittest.mock import patch
from examples import export_database_csv

import mysql.connector  # type: ignore


@pytest.fixture
def mock_db_connection():
    """Mocks the database connection."""
    with patch('mysql.connector.connect') as mock_connect:
        yield mock_connect


@pytest.fixture
def mock_dataframe():
    """Creates a mock DataFrame for testing."""
    data = {'author_user_id': [1, 2, 3],
            'post_text': [b'test1', b'test2', b'test3']}
    return pd.DataFrame(data)


def test_export_database_csv(mock_db_connection, mock_dataframe, tmp_path):
    """Tests the export_database_csv script."""

    # Mock the database connection to return the mock DataFrame
    mock_db_connection.return_value.cursor.return_value.fetchall.return_value = mock_dataframe.values.tolist()
    mock_db_connection.return_value.cursor.return_value.description = [
        ('author_user_id',), ('post_text',)]

    # Patch pandas.read_sql to return the mock_dataframe
    with patch('pandas.read_sql', return_value=mock_dataframe):
        # Define a temporary output CSV file
        output_csv = tmp_path / "test_posts.csv"

        # Patch the OUTPUT_CSV variable in the module
        with patch('examples.export_database_csv.OUTPUT_CSV', str(output_csv)):
            # Call the script's main execution block
            export_database_csv.main()

        # Assert that the file was created
        assert output_csv.exists()

        # Read the generated CSV and assert its contents
        read_df = pd.read_csv(output_csv)
        assert 'author_user_id' in read_df.columns
        assert 'post_text' in read_df.columns
        assert len(read_df) == 3


def test_main_handles_db_connection_error(mock_db_connection):
    """Tests that the script handles database connection errors."""
    mock_db_connection.side_effect = mysql.connector.Error(
        "Failed to connect to database")
    with pytest.raises(mysql.connector.Error) as excinfo:
        export_database_csv.main()
    assert "Failed to connect to database" in str(excinfo.value)
