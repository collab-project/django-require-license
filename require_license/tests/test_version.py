# Copyright Collab 2015

"""
Tests for the :py:mod:`require_license` module.
"""

from django.test import TestCase

from require_license import get_version


class VersionTestCase(TestCase):
    """
    Tests for :py:mod:`~require_license` versioning information.
    """
    def test_regularVersion(self):
        """
        :py:func:`~require_license.get_version` returns a string version without
        any beta tags, eg. `1.0.1`.
        """
        version = (1, 0, 1)
        self.assertEqual(get_version(version), '1.0.1')

    def test_betaVersion(self):
        """
        :py:func:`~require_license.get_version` returns a string version with beta tags,
        eg. `1.2.3b1`.
        """
        version = (1, 2, 3, 'b1')
        self.assertEqual(get_version(version), '1.2.3b1')
