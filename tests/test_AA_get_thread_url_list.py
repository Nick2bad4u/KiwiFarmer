import os
import unittest
from unittest.mock import patch, MagicMock
from selenium.common.exceptions import WebDriverException
from workflow.AA_get_thread_url_list import download_sitemap_with_selenium, OUTPUT_DIR, SITEMAPS, URL_PREFIX
import workflow.AA_get_thread_url_list

class TestDownloadSitemapWithSelenium(unittest.TestCase):

    @patch('AA_get_thread_url_list.webdriver.Chrome')
    @patch('AA_get_thread_url_list.ChromeDriverManager')
    def test_download_sitemap_with_selenium_success(self, mock_chrome_driver_manager, mock_chrome):
        mock_driver = MagicMock()
        mock_chrome.return_value = mock_driver
        mock_driver.page_source = '<html></html>'

        url = 'http://example.com'
        content = download_sitemap_with_selenium(url)

        mock_chrome_driver_manager().install.assert_called_once()
        mock_chrome.assert_called_once()
        mock_driver.get.assert_called_once_with(url)
        self.assertEqual(content, '<html></html>')

    @patch('AA_get_thread_url_list.webdriver.Chrome')
    @patch('AA_get_thread_url_list.ChromeDriverManager')
    def test_download_sitemap_with_selenium_failure(self, mock_chrome_driver_manager, mock_chrome):
        mock_driver = MagicMock()
        mock_chrome.return_value = mock_driver
        mock_driver.get.side_effect = WebDriverException('Test Exception')

        url = 'http://example.com'
        content = download_sitemap_with_selenium(url)

        mock_chrome_driver_manager().install.assert_called_once()
        mock_chrome.assert_called_once()
        mock_driver.get.assert_called_once_with(url)
        self.assertIsNone(content)

class TestMainFunctionality(unittest.TestCase):

    @patch('AA_get_thread_url_list.download_sitemap_with_selenium')
    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    @patch('os.makedirs')
    def test_main_functionality(self, mock_makedirs, mock_open, mock_download_sitemap):
        mock_download_sitemap.return_value = '<urlset><url><loc>https://kiwifarms.net/threads/123</loc></url><url><loc>https://kiwifarms.net/members/456</loc></url></urlset>'

        # Simulate running the main block
        with patch('AA_get_thread_url_list.__name__', '__main__'):
            mock_makedirs.assert_called_once_with(OUTPUT_DIR, exist_ok=True)
            self.assertEqual(mock_open.call_count, 4)  # 2 for writing sitemaps, 2 for writing URLs
            mock_download_sitemap.assert_any_call(URL_PREFIX + SITEMAPS[0])
            mock_download_sitemap.assert_any_call(URL_PREFIX + SITEMAPS[1])

if __name__ == '__main__':
    unittest.main()