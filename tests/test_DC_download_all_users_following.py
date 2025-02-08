import os
import pytest
from unittest.mock import patch, mock_open

from workflow.DC_download_all_users_following import (
    filename_to_url,
    url_to_filename,
    load_url_list,
    setup_selenium,
    download_page,
    save_content,
    process_url,
    download_many_files,
    URL_BASE,
    OUTPUT_DIR,
    URL_LIST_FILE
)


def test_filename_to_url():
    filename = "user1_followers.html"
    expected_url = URL_BASE + "members/user1/followers.html"
    assert filename_to_url(filename) == expected_url


def test_url_to_filename():
    url = URL_BASE + "members/user1/following.html"
    expected_filename = "user1_following.html"
    assert url_to_filename(url) == expected_filename


def test_load_url_list():
    content = "url1\nurl2\n"
    with patch("builtins.open", mock_open(read_data=content)) as mock_file:
        url_list = load_url_list("dummy_file_path")
        assert url_list == ["url1", "url2"]


def test_load_url_list_empty_lines():
    content = "url1\n\nurl2\n"
    with patch("builtins.open", mock_open(read_data=content)) as mock_file:
        url_list = load_url_list("dummy_file_path")
        assert url_list == ["url1", "url2"]


@patch('workflow.C_download_all_users_following.webdriver.Chrome')
@patch('workflow.C_download_all_users_following.Service')
@patch('workflow.C_download_all_users_following.ChromeDriverManager')
def test_setup_selenium(mock_chrome_driver_manager, mock_service, mock_chrome):
    setup_selenium()
    mock_chrome_driver_manager().install.assert_called_once()
    mock_service.assert_called_once()
    mock_chrome.assert_called_once()


@patch('workflow.C_download_all_users_following.webdriver.Chrome')
def test_download_page(mock_chrome):
    mock_driver = mock_chrome.return_value
    mock_driver.page_source = "<html>Test Content</html>"
    url = "http://example.com"
    content = download_page(url, mock_driver)
    assert content == "<html>Test Content</html>"
    mock_driver.get.assert_called_once_with(url)


@patch('workflow.C_download_all_users_following.webdriver.Chrome')
def test_download_page_failure(mock_chrome):
    mock_driver = mock_chrome.return_value
    mock_driver.get.side_effect = Exception("Simulated error")
    url = "http://example.com"
    content = download_page(url, mock_driver)
    assert content is None
    mock_driver.get.assert_called_once_with(url)


@patch("builtins.open", new_callable=mock_open)
def test_save_content(mock_file):
    filename = "test.html"
    content = "<html>Test Content</html>"
    save_content(content, filename)
    mock_file.assert_called_once_with(os.path.join(
        OUTPUT_DIR, filename), 'w', encoding='utf-8')
    mock_file().write.assert_called_once_with(content)


@patch('workflow.C_download_all_users_following.setup_selenium')
@patch('workflow.C_download_all_users_following.download_page')
@patch('workflow.C_download_all_users_following.save_content')
def test_process_url(mock_save_content, mock_download_page, mock_setup_selenium):
    url = "http://example.com"
    mock_driver = mock_setup_selenium.return_value
    mock_download_page.return_value = "<html>Test Content</html>"
    process_url(url)
    mock_setup_selenium.assert_called_once()
    mock_download_page.assert_called_once_with(url, mock_driver)
    mock_save_content.assert_called_once_with(
        "<html>Test Content</html>", 'example.com.html')
    mock_driver.quit.assert_called_once()


@patch('workflow.C_download_all_users_following.process_url')
def test_download_many_files(mock_process_url):
    url_list = ["http://example.com/1", "http://example.com/2"]
    download_many_files(url_list)
    assert mock_process_url.call_count == 2
    mock_process_url.assert_any_call("http://example.com/1")
    mock_process_url.assert_any_call("http://example.com/2")
