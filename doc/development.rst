Development
===========

After checkout, install package in active virtualenv::

  pip install -e .


Testing
-------

Running tests with Tox_::

  tox -v

Running tests without Tox_::

  ./runtests.py

Directly with ``django-admin``::

  django-admin test --settings=require_license.tests.settings require_license


Coverage
--------

To generate a test coverage report using `coverage.py`_::

  coverage run --source='.' runtests.py
  coverage html

The resulting HTML report can be found in the ``htmlcov`` directory.


.. _Tox: http://tox.testrun.org/
.. _coverage.py: http://nedbatchelder.com/code/coverage/
