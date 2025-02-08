import os
import pytest
from unittest.mock import patch, mock_open
from workflow.DA_download_all_users_about import load_url_list, setup_selenium, download_page, save_content, process_url, download_many_files

# Mocking constants
URL_LIST_FILE = 'test_url_list.txt'
OUTPUT_DIR = 'test_output_dir'


@pytest.fixture
def mock_url_list_file(tmpdir):
    # Create a temporary file with a list of URLs for testing
    url_list = ["http://example.com/user1",
                "http://example.com/user2", "http://example.com/user3"]
    file_path = tmpdir.join(URL_LIST_FILE)
    with open(file_path, 'w') as f:
        f.write('\n'.join(url_list))
    return str(file_path)


@pytest.fixture
def mock_output_dir(tmpdir):
    # Create a temporary directory for output files
    output_dir = tmpdir.mkdir(OUTPUT_DIR)
    return str(output_dir)


def test_load_url_list(mock_url_list_file):
    url_list = load_url_list(mock_url_list_file)
    assert len(url_list) == 3
    assert all("about" in url for url in url_list)


@patch('workflow.A_download_all_users_about.webdriver.Chrome')
def test_setup_selenium(MockChrome):
    setup_selenium()
    assert MockChrome.called


@patch('workflow.A_download_all_users_about.webdriver.Chrome')
def test_download_page(MockChrome):
    mock_driver = MockChrome.return_value
    mock_driver.page_source = "<html>Test Content</html>"
    mock_driver.get.return_value = None
    url = "http://example.com/test"
    content = download_page(url, mock_driver)
    assert content == "<html>Test Content</html>"
    mock_driver.get.assert_called_once_with(url)


def test_save_content(mock_output_dir):
    content = "Test content to be saved."
    filename = "test_file.html"
    save_content(content, filename)
    file_path = os.path.join(mock_output_dir, filename)
    assert os.path.exists(file_path)
    with open(file_path, 'r') as f:
        saved_content = f.read()
    assert saved_content == content


@patch('workflow.A_download_all_users_about.setup_selenium')
@patch('workflow.A_download_all_users_about.download_page')
@patch('workflow.A_download_all_users_about.save_content')
def test_process_url(mock_setup_selenium, mock_download_page, mock_save_content):
    mock_driver = mock_setup_selenium.return_value
    mock_download_page.return_value = "Test content"
    url = "http://example.com/test"
    filename = "test_file.html"
    process_url(url, filename)
    mock_setup_selenium.assert_called_once()
    mock_download_page.assert_called_once_with(url, mock_driver)
    mock_save_content.assert_called_once_with("Test content", filename)
    mock_driver.quit.assert_called_once()


@patch('workflow.A_download_all_users_about.process_url')
def test_download_many_files(mock_process_url):
    url_list = ["http://example.com/user1", "http://example.com/user2"]
    download_many_files(url_list)
    assert mock_process_url.call_count == len(url_list)
    mock_process_url.assert_called_with(url_list[-1], '1.html')
