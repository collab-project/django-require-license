Development
===========

After checkout, install the package in an active virtualenv::

  pip install -e .

And install the required dependencies needed to run the tests::

  pip install -r require_license/tests/requirements.txt


Testing
-------

Running tests with Tox_::

  tox -v

Running tests without Tox_::

  ./runtests.py

Or directly with ``django-admin``::

  django-admin test --settings=require_license.tests.settings require_license


Coverage
--------

To generate a test coverage report using `coverage.py`_::

  coverage run --source='.' runtests.py
  coverage html

The resulting HTML report can be found in the ``htmlcov`` directory.


Documentation
-------------

Install Sphinx::

  pip install sphinx>=1.1.0

Change to the ``doc`` directory and run::

  make html

The resulting HTML documentation can be found in the ``doc/_build/html``
directory.


.. _Tox: http://tox.testrun.org/
.. _coverage.py: http://nedbatchelder.com/code/coverage/
