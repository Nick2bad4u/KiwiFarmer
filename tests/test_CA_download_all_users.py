import os
import pytest
from unittest.mock import patch, MagicMock


@pytest.fixture
def mock_driver():
    return MagicMock()


def test_setup_selenium():
    with patch('selenium.webdriver.Chrome') as mock_chrome:
        driver_instance = MagicMock()
        mock_chrome.return_value = driver_instance
        from workflow.CA_download_all_users import setup_selenium
        driver = setup_selenium()
        assert driver == driver_instance


def test_login_to_kiwifarms(mock_driver):
    with patch('03-A_download_all_users.BeautifulSoup') as mock_bs, \
            patch('03-A_download_all_users.logger') as mock_logger:
        soup_mock = MagicMock()
        mock_bs.return_value = soup_mock
        soup_mock.find.side_effect = [
            MagicMock(attrs={'id': 'username_field'}),
            MagicMock(attrs={'id': 'password_field'})
        ]
        os.environ['KIWIFARMS_USERNAME'] = 'testuser'
        os.environ['KIWIFARMS_PASSWORD'] = 'testpass'
        from workflow.CA_download_all_users import login_to_kiwifarms
        login_to_kiwifarms(mock_driver)
        mock_driver.find_element_by_id.assert_any_call('username_field')
        mock_driver.find_element_by_id.assert_any_call('password_field')
        mock_logger.info.assert_any_call("Logged in successfully")


def test_download_member_pages(mock_driver):
    with patch('builtins.open', new_callable=MagicMock) as mock_open, \
            patch('03-A_download_all_users.logger') as mock_logger:
        from workflow.CA_download_all_users import download_member_pages
        test_urls = ["http://example.com/user1", "http://example.com/user2"]
        download_member_pages(mock_driver, test_urls, "/fake_output_dir")
        assert mock_driver.get.call_count == 2
        assert mock_open.call_count == 2
        mock_logger.info.assert_any_call(
            f"Successfully downloaded {test_urls[0]}")


if __name__ == '__main__':
    pytest.main()
