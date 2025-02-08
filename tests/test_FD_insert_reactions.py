import os
import pytest
from bs4 import BeautifulSoup
from unittest.mock import patch
from workflow import FD_insert_reactions
from workflow.FD_insert_reactions import process_reaction_page

@pytest.fixture
def mock_reaction_page_dir(tmpdir):
    """
    Creates a temporary directory and sets it as the REACTION_PAGE_DIR.
    This ensures tests don't modify actual data directories.
    """
    original_reaction_page_dir = FD_insert_reactions.REACTION_PAGE_DIR
    FD_insert_reactions.REACTION_PAGE_DIR = str(tmpdir)
    yield str(tmpdir)
    FD_insert_reactions.REACTION_PAGE_DIR = original_reaction_page_dir

@pytest.fixture
def mock_reaction_page_file(mock_reaction_page_dir):
    """
    Creates a dummy reaction page file within the mock REACTION_PAGE_DIR.
    """
    test_html_content = "<html><body><div class='reaction'><p>Test Reaction</p></div></body></html>"
    test_file_path = os.path.join(mock_reaction_page_dir, "test_reaction_page.html")
    with open(test_file_path, "w", encoding="utf-8") as f:
        f.write(test_html_content)
    return "test_reaction_page.html"

def test_process_reaction_page(mock_reaction_page_dir, mock_reaction_page_file, mocker):
    """
    Tests the process_reaction_page function.
    Mocks the database cursor and asserts that execute is called.
    """
    # Mock the cursor and its execute method
    mock_cursor = mocker.MagicMock()

    # Mock base.ReactionPage and base.Reaction to avoid external dependencies
    mock_reaction_page = mocker.MagicMock()
    mock_reaction_page.get_reaction_soups.return_value = [BeautifulSoup("<div class='reaction'><p>Test Reaction</p></div>", 'lxml')]
    mock_reaction_page.post_id = 123
    mocker.patch("workflow.FD_insert_reactions.base.ReactionPage", return_value=mock_reaction_page)

    mock_reaction = mocker.MagicMock()
    mock_reaction.reaction_insertion = {"test": "data"}
    mocker.patch("workflow.FD_insert_reactions.base.Reaction", return_value=mock_reaction)

    # Call the function
    process_reaction_page(mock_reaction_page_file, mock_cursor)

    # Assert that cursor.execute was called with the expected arguments
    mock_cursor.execute.assert_called()