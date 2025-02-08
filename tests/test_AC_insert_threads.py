import os
import unittest
from unittest.mock import patch, MagicMock
from mysql.connector import errorcode  # type: ignore
from bs4 import BeautifulSoup
from kiwifarmer import base, templates
from workflow import insert_threads

import mysql.connector  # type: ignore


class TestInsertThreads(unittest.TestCase):

    @patch('workflow.insert_threads.mysql.connector.connect')
    @patch('workflow.insert_threads.os.listdir')
    @patch('workflow.insert_threads.open', new_callable=unittest.mock.mock_open, read_data='<html></html>')
    def test_insert_threads(self, mock_open, mock_listdir, mock_connect):
        # Mock environment variables
        os.environ['KIWIFARMER_USER'] = 'test_user'
        os.environ['KIWIFARMER_PASSWORD'] = 'test_password'

        # Mock database connection and cursor
        mock_cnx = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_cnx
        mock_cnx.cursor.return_value = mock_cursor

        # Mock listdir to return a list of fake thread files
        mock_listdir.return_value = ['thread1.html', 'thread2.html']

        # Mock BeautifulSoup and Thread class
        mock_thread = MagicMock()
        mock_thread.thread_insertion = (
            'thread_id', 'thread_title', 'thread_content')
        with patch('workflow.insert_threads.BeautifulSoup', return_value=BeautifulSoup('<html></html>', 'lxml')):
            with patch('workflow.insert_threads.base.Thread', return_value=mock_thread):

                # Run the script
                insert_threads.main()

                # Check database creation
                mock_cursor.execute.assert_any_call(
                    f'CREATE DATABASE {insert_threads.DATABASE} character set utf8mb4 collate utf8mb4_bin')
                mock_cnx.commit.assert_any_call()

                # Check table creation
                for table_name in templates.TABLES.keys():
                    mock_cursor.execute.assert_any_call(
                        templates.TABLES[table_name])

                # Check thread insertion
                for thread_file in mock_listdir.return_value:
                    mock_cursor.execute.assert_any_call(
                        templates.ADD_THREAD, mock_thread.thread_insertion)

                # Check commit and close calls
                self.assertEqual(mock_cnx.commit.call_count, 2)
                self.assertEqual(mock_cursor.close.call_count, 2)
                self.assertEqual(mock_cnx.close.call_count, 2)


if __name__ == '__main__':
    unittest.main()
