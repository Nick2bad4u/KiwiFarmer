import os
import pytest
from bs4 import BeautifulSoup

# Assuming preprocess_reactions.py is in the examples directory
from examples import preprocess_reactions

INPUT_DIR = 'test_data'  # Use a test directory
DECLARATION = '<!DOCTYPE html>'

# Create a test directory and files for testing


@pytest.fixture(scope="module", autouse=True)
def setup_test_data():
    if not os.path.exists(INPUT_DIR):
        os.makedirs(INPUT_DIR)

    # Create some test files
    with open(os.path.join(INPUT_DIR, 'test_file_1.html'), 'w', encoding='utf-8') as f:
        f.write(DECLARATION + '<html lang="en"><head><meta property="og:url" content="example.com"></head><body></body></html>')

    with open(os.path.join(INPUT_DIR, 'test_file_2.html'), 'w', encoding='utf-8') as f:
        f.write(DECLARATION + '<html lang="en"><head></head><body></body></html>' + DECLARATION +
                '<html lang="en"><head><meta property="og:url" content="example.com"></head><body></body></html>')

    with open(os.path.join(INPUT_DIR, 'test_file_3.html'), 'w', encoding='utf-8') as f:
        f.write('<html><body>Cloudflare Error</body></html>' + DECLARATION +
                '<html lang="en"><head><meta property="og:url" content="example.com"></head><body></body></html>')

    with open(os.path.join(INPUT_DIR, 'test_file_4.html'), 'w', encoding='utf-8') as f:
        f.write(DECLARATION + '<html lang="en"><head><meta property="og:url" content="example.com"></head><body></body></html>' +
                '<html><body>Cloudflare Error</body></html>')

    with open(os.path.join(INPUT_DIR, 'test_file_5.html'), 'w', encoding='utf-8') as f:
        f.write('<html><body>Cloudflare Error</body></html>' +
                DECLARATION + '<html lang="en"><head></head><body></body></html>')

    yield  # Provide a teardown mechanism

    # Clean up test files and directory after tests
    for file in os.listdir(INPUT_DIR):
        os.remove(os.path.join(INPUT_DIR, file))
    os.rmdir(INPUT_DIR)


def test_preprocess_reactions():
    # Modify the INPUT_DIR in the module to point to the test directory
    preprocess_reactions.INPUT_DIR = INPUT_DIR

    # Call the main function to process the files
    preprocess_reactions.main()

    # Assert that the files have been modified as expected
    with open(os.path.join(INPUT_DIR, 'test_file_1.html'), 'r', encoding='utf-8') as f:
        content = f.read()
        assert '<meta property="og:url" content="example.com"/>' in content

    with open(os.path.join(INPUT_DIR, 'test_file_2.html'), 'r', encoding='utf-8') as f:
        content = f.read()
        assert '<meta property="og:url" content="example.com"/>' in content
        assert content.count(DECLARATION) == 1

    with open(os.path.join(INPUT_DIR, 'test_file_3.html'), 'r', encoding='utf-8') as f:
        content = f.read()
        assert '<meta property="og:url" content="example.com"/>' in content

    with open(os.path.join(INPUT_DIR, 'test_file_4.html'), 'r', encoding='utf-8') as f:
        content = f.read()
        assert '<meta property="og:url" content="example.com"/>' in content

    with open(os.path.join(INPUT_DIR, 'test_file_5.html'), 'r', encoding='utf-8') as f:
        content = f.read()
        assert '<meta property="og:url" content="example.com"/>' not in content
        assert DECLARATION not in content


# Mock the main execution block
preprocess_reactions.main = test_preprocess_reactions
