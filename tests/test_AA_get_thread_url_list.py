import pytest
import requests
from bs4 import BeautifulSoup


def get_thread_url_list(board_url, max_pages=2):
    """
    Retrieves a list of thread URLs from a given board URL, up to a maximum number of pages.

    Args:
        board_url (str): The URL of the board to scrape.
        max_pages (int, optional): The maximum number of pages to scrape. Defaults to 2.

    Returns:
        list: A list of thread URLs.
    """
    thread_urls = []
    for page_num in range(1, max_pages + 1):
        page_url = f"{board_url}?page={page_num}"
        try:
            response = requests.get(page_url)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all <a> tags within <li> tags that have the class "thread"
            thread_links = soup.find_all('li', class_='thread')
            for link in thread_links:
                a_tag = link.find('a')
                if a_tag:
                    thread_url = a_tag['href']
                    # Ensure the URL is absolute
                    if not thread_url.startswith('http'):
                        thread_url = board_url + thread_url
                    thread_urls.append(thread_url)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching page {page_num}: {e}")
            continue  # Go to the next page in case of an error

    return thread_urls


# Example usage (you can uncomment this for testing):
if __name__ == '__main__':
    # Replace with the actual board URL
    board_url = "https://kiwifarms.net/forums/internet-artifacts.21/"
    thread_urls = get_thread_url_list(board_url)
    for url in thread_urls:
        print(url)
