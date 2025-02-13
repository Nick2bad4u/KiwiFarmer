import unittest
from unittest.mock import patch, mock_open, MagicMock
from workflow import download_all_pages as dap
import os


class TestDownloadAllPages(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='http://example.com\nhttp://example2.com')
    def test_load_url_list(self, mock_file):
        url_list = dap.load_url_list('dummy_path')
        self.assertEqual(
            url_list, ['http://example.com', 'http://example2.com'])

    @patch('kiwifarmer.workflow.download_all_pages.webdriver.Chrome')
    @patch('kiwifarmer.workflow.download_all_pages.ChromeDriverManager')
    def test_setup_selenium(self, mock_chrome_driver_manager, mock_chrome):
        mock_chrome_driver_manager().install.return_value = 'dummy_path'
        driver = dap.setup_selenium()
        self.assertTrue(mock_chrome.called)
        self.assertTrue(driver.headless)

    @patch('kiwifarmer.workflow.download_all_pages.webdriver.Chrome')
    @patch('kiwifarmer.workflow.download_all_pages.time.sleep', return_value=None)
    def test_download_page(self, mock_sleep, mock_chrome):
        mock_driver = MagicMock()
        mock_chrome.return_value = mock_driver
        mock_driver.page_source = '<html></html>'
        content = dap.download_page('http://example.com', mock_driver)
        self.assertEqual(content, '<html></html>')

    @patch('builtins.open', new_callable=mock_open)
    @patch('kiwifarmer.workflow.download_all_pages.page_url_to_filename', return_value='dummy_filename.html')
    def test_save_content(self, mock_page_url_to_filename, mock_file):
        dap.save_content('<html></html>', 'http://example.com')
        mock_file.assert_called_once_with(os.path.join('..', '..', 'data_20210224', 'downloaded_pages', 'dummy_filename.html'), 'w', encoding='utf-8')
        mock_file().write.assert_called_once_with('<html></html>')

    @patch('kiwifarmer.workflow.download_all_pages.setup_selenium')
    @patch('kiwifarmer.workflow.download_all_pages.download_page', return_value='<html></html>')
    @patch('kiwifarmer.workflow.download_all_pages.save_content')
    def test_process_url(self, mock_save_content, mock_download_page, mock_setup_selenium):
        mock_driver = MagicMock()
        mock_setup_selenium.return_value = mock_driver
        dap.process_url('http://example.com')
        mock_download_page.assert_called_once_with(
            'http://example.com', mock_driver)
        mock_save_content.assert_called_once_with(
            '<html></html>', 'http://example.com')
        mock_driver.quit.assert_called_once()

    @patch('kiwifarmer.workflow.download_all_pages.process_url')
    @patch('kiwifarmer.workflow.download_all_pages.ThreadPoolExecutor')
    def test_download_many_files(self, mock_thread_pool_executor, mock_process_url):
        mock_executor = MagicMock()
        mock_thread_pool_executor.return_value.__enter__.return_value = mock_executor
        dap.download_many_files(['http://example.com', 'http://example2.com'])
        self.assertEqual(mock_executor.submit.call_count, 2)


if __name__ == '__main__':
    unittest.main()
