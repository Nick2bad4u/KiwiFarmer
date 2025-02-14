import unittest
from unittest.mock import patch, mock_open, MagicMock
from workflow import download_all_threads as dat
import os


class TestDownloadAllThreads(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='http://example.com\nhttp://example.org')
    def test_load_url_list(self, mock_file):
        url_list = dat.load_url_list('dummy_path')
        self.assertEqual(
            url_list, ['http://example.com', 'http://example.org'])
        mock_file.assert_called_once_with('dummy_path', 'r')

    @patch('kiwifarmer.workflow.download_all_threads.webdriver.Chrome')
    @patch('kiwifarmer.workflow.download_all_threads.ChromeDriverManager.install')
    def test_setup_selenium(self, mock_install, mock_chrome):
        mock_driver = MagicMock()
        mock_chrome.return_value = mock_driver
        driver = dat.setup_selenium()
        self.assertEqual(driver, mock_driver)
        mock_chrome.assert_called_once()
        mock_install.assert_called_once()

    @patch('kiwifarmer.workflow.download_all_threads.webdriver.Chrome')
    @patch('kiwifarmer.workflow.download_all_threads.ChromeDriverManager.install')
    @patch('kiwifarmer.workflow.download_all_threads.time.sleep', return_value=None)
    def test_download_page(self, mock_sleep, mock_install, mock_chrome):
        mock_driver = MagicMock()
        mock_chrome.return_value = mock_driver
        mock_driver.page_source = '<html></html>'
        driver = dat.setup_selenium()
        content = dat.download_page('http://example.com', driver)
        self.assertEqual(content, '<html></html>')
        mock_driver.get.assert_called_once_with('http://example.com')
        mock_sleep.assert_called_once_with(5)

    @patch('kiwifarmer.workflow.download_all_threads.page_url_to_filename', return_value='example.html')
    @patch('builtins.open', new_callable=mock_open)
    def test_save_content(self, mock_file, mock_url_to_filename):
        dat.save_content('<html></html>', 'http://example.com')
        mock_file.assert_called_once_with(os.path.join('..', '..', 'data_20210224', 'downloaded_threads', 'example.html'), 'w', encoding='utf-8')
        mock_file().write.assert_called_once_with('<html></html>')

    @patch('kiwifarmer.workflow.download_all_threads.setup_selenium')
    @patch('kiwifarmer.workflow.download_all_threads.download_page', return_value='<html></html>')
    @patch('kiwifarmer.workflow.download_all_threads.save_content')
    def test_process_url(self, mock_save_content, mock_download_page, mock_setup_selenium):
        mock_driver = MagicMock()
        mock_setup_selenium.return_value = mock_driver
        dat.process_url('http://example.com')
        mock_setup_selenium.assert_called_once()
        mock_download_page.assert_called_once_with(
            'http://example.com', mock_driver)
        mock_save_content.assert_called_once_with(
            '<html></html>', 'http://example.com')
        mock_driver.quit.assert_called_once()


if __name__ == '__main__':
    unittest.main()
