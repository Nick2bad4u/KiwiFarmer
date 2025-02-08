Test Overview
=============

This section contains tests for the overview documentation.

Test 1: Check Image Inclusion
-----------------------------

Ensure that the database schema image is included correctly.

.. code-block:: restructuredtext

    .. image:: figs/database_schema.svg
      :target: _images/database_schema.svg
      :width: 100%

Expected Result:
- The image `figs/database_schema.svg` should be displayed.
- The image should link to `_images/database_schema.svg`.
- The image should have a width of 100%.

Test 2: Check Section Title
---------------------------

Ensure that the section title "Overview" is displayed correctly.

.. code-block:: restructuredtext

    Overview
    ========

Expected Result:
- The section title "Overview" should be displayed with an underline of equal signs.