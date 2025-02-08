Test Quickstart
===============

.. _sec-test-installation:

Test Installation
-----------------

To test the installation of *KiwiFarmer*, follow these steps:

1. Clone the repository:

    .. code-block:: bash

      git clone https://github.com/gaius-gracchus/KiwiFarmer.git
      cd KiwiFarmer

2. Install the package:

    .. code-block:: bash

      pip install .

3. Verify the installation by importing *KiwiFarmer* in a Python shell:

    .. code-block:: python

      import kiwifarmer
      print(kiwifarmer.__version__)

.. _sec-test-docs:

Test Documentation Build
------------------------

To test the documentation build process, follow these steps:

1. Install the documentation dependencies:

    .. code-block:: bash

      pip install .[docs]

2. Build the documentation:

    .. code-block:: bash

      cd docs
      rm -rf source/
      bash default_apidocs.sh
      make clean
      make html

3. Verify the documentation build by opening the file ``docs/_build/html/index.html`` in a web browser.

.. _sec-test-tests:

Test Running Built-in Tests
---------------------------

To test the built-in tests, follow these steps:

1. Install the test dependencies:

    .. code-block:: bash

      pip install .[tests]

2. Grant MySQL privileges:

    .. code-block:: bash

      mysql -u root -p
      GRANT ALL PRIVILEGES ON kiwifarms_test.* TO '<user>'@'localhost';

3. Run the test suite:

    .. code-block:: bash

      python -m pytest