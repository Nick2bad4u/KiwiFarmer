"""
This module tests the functionality of the FC_preprocess_reactions script.
It includes tests for the main function, ensuring that it correctly identifies
files with reactions, excludes files without reactions or empty files,
and writes the names of files with reactions to the output file.
The tests use pytest fixtures and mocks to create a controlled environment
for testing, including a temporary input directory with mock files and
patching the script's dependencies on os.scandir and file I/O.
"""
import os
import pytest
from unittest.mock import patch, mock_open
from workflow.FC_preprocess_reactions import INPUT_DIR, OUTPUT_FILE_GOOD, NO_REACTIONS_STR
import workflow.FC_preprocess_reactions as fc_preprocess


@pytest.fixture
def mock_input_dir(tmpdir):
    """Creates a temporary directory and populates it with mock files."""
    input_dir = tmpdir.mkdir("input")
    # Create files with and without reactions
    input_dir.join("file_with_reactions.txt").write(
        "Some content with reactions.")
    input_dir.join("file_without_reactions.txt").write(NO_REACTIONS_STR)
    input_dir.join("empty_file.txt").write("")
    return str(input_dir)


def test_main_function(mock_input_dir, tmpdir, caplog):
    """Tests the main function of the script."""
    output_file = tmpdir.join("output.txt")

    # Patch the necessary variables and functions
    with patch("FC_preprocess_reactions.INPUT_DIR", mock_input_dir), \
            patch("FC_preprocess_reactions.OUTPUT_FILE_GOOD", str(output_file)), \
            patch("os.scandir") as mock_scandir:

        # Mock the return value of os.scandir to return a list of mock files
        class MockDirEntry:
            def __init__(self, name, path, is_file_value=True):
                self.name = name
                self.path = path
                self._is_file = is_file_value

            def is_file(self):
                return self._is_file

        mock_files = [
            MockDirEntry("file_with_reactions.txt", os.path.join(
                mock_input_dir, "file_with_reactions.txt")),
            MockDirEntry("file_without_reactions.txt", os.path.join(
                mock_input_dir, "file_without_reactions.txt")),
            MockDirEntry("empty_file.txt", os.path.join(
                mock_input_dir, "empty_file.txt")),
        ]
        mock_scandir.return_value = mock_files

        # Call the main function
        fc_preprocess.main()

    # Assert that the output file contains the correct file names
    with open(str(output_file), "r") as f:
        output_content = f.read().splitlines()
    assert "file_with_reactions.txt" in output_content
    assert "file_without_reactions.txt" not in output_content
    assert "empty_file.txt" not in output_content

    # Assert that the log messages are correct
    assert "File file_with_reactions.txt has reactions and is added to the list" in caplog.text
    assert "File file_without_reactions.txt has no reactions" in caplog.text
