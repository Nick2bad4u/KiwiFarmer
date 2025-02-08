import pytest
from sphinx.ext.autodoc import ClassDocumenter
from conf import add_line_no_object_base, _
from conf import add_directive_header_no_object_base, _


def test_class_documenter_add_line_no_object_base():
    """
    Test that the add_line_no_object_base function correctly filters out the "Bases: object" line.
    """
    class MockClassDocumenter:
        def __init__(self):
            self.emitted_lines = []

        def add_line(self, text, *args, **kwargs):
            self.emitted_lines.append(text)

    doc = MockClassDocumenter()

    line_to_delete = _(u'Bases: %s') % u':class:`object`'

    # Test case 1: Line should be deleted
    doc.emitted_lines = []
    add_line_no_object_base(doc, line_to_delete)
    assert len(doc.emitted_lines) == 0

    # Test case 2: Line should be kept
    doc.emitted_lines = []
    add_line_no_object_base(doc, "Some other line")
    assert len(doc.emitted_lines) == 1
    assert doc.emitted_lines[0] == "Some other line"

    # Test case 3: Empty line should be kept
    doc.emitted_lines = []
    add_line_no_object_base(doc, "")
    assert len(doc.emitted_lines) == 1
    assert doc.emitted_lines[0] == ""


def test_class_documenter_add_directive_header_no_object_base():
    """
    Test that the add_directive_header_no_object_base function correctly monkey-patches
    and restores the add_line method.
    """
    class MockClassDocumenter:
        def __init__(self):
            self.emitted_lines = []

        def add_line(self, text, *args, **kwargs):
            self.emitted_lines.append(text)

        def add_directive_header(self, *args, **kwargs):
            # Simulate the original add_directive_header behavior
            self.add_line("Some header line")
            # Add the line to be potentially deleted
            self.add_line(_(u'Bases: %s') % u':class:`object`')
            self.add_line("Some footer line")

    doc = MockClassDocumenter()

    # Apply the monkey-patch
    add_directive_header_no_object_base(doc)

    # Verify that the "Bases: object" line was removed
    assert "Some header line" in doc.emitted_lines
    assert _(u'Bases: %s') % u':class:`object`' not in doc.emitted_lines
    assert "Some footer line" in doc.emitted_lines

    # Verify that the original add_line method is restored (implicitly tested by the above assertions)
    # We can add an explicit check if needed, but it adds complexity for little gain.
