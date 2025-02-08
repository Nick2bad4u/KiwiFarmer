import os
import pytest
from unittest.mock import patch, mock_open
from workflow import FB_download_all_reactions as fb_downloader

# Constants for testing
TEST_URL_LIST_FILE = 'test_url_list.txt'
TEST_OUTPUT_DIR = 'test_output_dir'
TEST_URL = 'https://www.facebook.com/some_post/reactions/more/?surface=permalink&ft_ent_identifier=12345'
TEST_HTML_CONTENT = '<html><body>Test Content</body></html>'


@pytest.fixture
def setup_test_environment(tmpdir):
    # Create a temporary directory for output
    test_output_dir = tmpdir.mkdir(TEST_OUTPUT_DIR)

    # Create a dummy URL list file
    with open(TEST_URL_LIST_FILE, 'w') as f:
        f.write(TEST_URL + '\n')

    yield str(test_output_dir)  # Provide the path to the test function

    # Teardown (optional): Remove the created files and directories
    # tmpdir.remove(ignore_errors=True)  # Use tmpdir fixture to handle cleanup


def test_load_url_list(setup_test_environment):
    url_list = fb_downloader.load_url_list(TEST_URL_LIST_FILE)
    assert isinstance(url_list, list)
    assert len(url_list) == 1
    assert url_list[0] == TEST_URL


def test_url_to_filename():
    filename = fb_downloader.url_to_filename(TEST_URL)
    assert filename == 'reactions_more_.html'


@patch('workflow.FB_download_all_reactions.webdriver.Chrome')
def test_download_page(mock_chrome):
    mock_driver = mock_chrome.return_value
    mock_driver.page_source = TEST_HTML_CONTENT
    content = fb_downloader.download_page(TEST_URL, mock_driver)
    assert content == TEST_HTML_CONTENT
    mock_driver.get.assert_called_once_with(TEST_URL)


@patch('workflow.FB_download_all_reactions.open', new_callable=mock_open, create=True)
def test_save_content(mock_file, setup_test_environment):
    output_dir = setup_test_environment
    test_filename = 'test_file.html'
    fb_downloader.OUTPUT_DIR = output_dir  # Override the OUTPUT_DIR
    fb_downloader.save_content(TEST_HTML_CONTENT, test_filename)
    mock_file.assert_called_once_with(os.path.join(
        output_dir, test_filename), 'w', encoding='utf-8')
    mock_file().write.assert_called_once_with(TEST_HTML_CONTENT)


@patch('workflow.FB_download_all_reactions.setup_selenium')
@patch('workflow.FB_download_all_reactions.download_page')
@patch('workflow.FB_download_all_reactions.save_content')
def test_process_url(mock_save_content, mock_download_page, mock_setup_selenium):
    mock_driver = mock_setup_selenium.return_value
    mock_download_page.return_value = TEST_HTML_CONTENT
    test_filename = 'reactions_more_.html'
    url = TEST_URL
    fb_downloader.process_url(url)
    mock_setup_selenium.assert_called_once()
    mock_download_page.assert_called_once_with(url, mock_driver)
    mock_save_content.assert_called_once()
    mock_driver.quit.assert_called_once()


@patch('workflow.FB_download_all_reactions.process_url')
def test_download_many_files(mock_process_url):
    url_list = [TEST_URL, TEST_URL + '2']
    fb_downloader.download_many_files(url_list)
    assert mock_process_url.call_count == 2
    mock_process_url.assert_called_with(url_list[1])
