import os
import pytest
from bs4 import BeautifulSoup
from unittest.mock import patch, mock_open
from workflow import generate_page_urls

@pytest.fixture
def mock_functions():
    with patch('kiwifarmer.workflow.functions') as mock_functions:
        yield mock_functions

@pytest.fixture
def mock_os_listdir():
    with patch('os.listdir') as mock_listdir:
        yield mock_listdir

@pytest.fixture
def mock_open_file():
    with patch('builtins.open', mock_open(read_data='<html></html>')) as mock_file:
        yield mock_file

@pytest.fixture
def mock_beautifulsoup():
    with patch('bs4.BeautifulSoup', return_value=BeautifulSoup('<html></html>', 'lxml')) as mock_soup:
        yield mock_soup

def test_generate_page_urls(mock_functions, mock_os_listdir, mock_open_file, mock_beautifulsoup, tmpdir):
    input_dir = tmpdir.mkdir("input")
    output_dir = tmpdir.mkdir("output")
    page_list_filename = 'page_url_list.txt'

    # Mock the list of files in the input directory
    mock_os_listdir.return_value = ['thread1.html', 'thread2.html']

    # Mock the function to get the last page of a thread
    mock_functions.get_thread_last_page.return_value = 3

    # Call the function to generate page URLs
    generate_page_urls.generate_page_urls(str(input_dir), str(output_dir), page_list_filename)

    # Check that the output file is created
    output_file_path = os.path.join(output_dir, page_list_filename)
    assert os.path.exists(output_file_path)

    # Check the contents of the output file
    with open(output_file_path, 'r') as f:
        lines = f.readlines()
        assert len(lines) == 6
        assert lines[0].strip() == 'https://kiwifarms.st/threads/thread1/page-1/'
        assert lines[1].strip() == 'https://kiwifarms.st/threads/thread1/page-2/'
        assert lines[2].strip() == 'https://kiwifarms.st/threads/thread1/page-3/'
        assert lines[3].strip() == 'https://kiwifarms.st/threads/thread2/page-1/'
        assert lines[4].strip() == 'https://kiwifarms.st/threads/thread2/page-2/'
        assert lines[5].strip() == 'https://kiwifarms.st/threads/thread2/page-3/'