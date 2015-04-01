# Copyright Collab 2013-2015

"""
Tests for the :py:mod:`require_license.storage` module.
"""

import os

from django.conf import settings
from django.test import TestCase
from django.core.management import call_command


class StorageTestCase(TestCase):
    """
    Tests for :py:mod:`~require_license.storage`.
    """
    def test_licenseHeaderMixin(self):
        """
        :py:class:`~require_license.storage.LicenseHeaderMixin` adds a license
        header to the minified JS module.
        """
        call_command("collectstatic", interactive=False, dry_run=False,
            clear=False, verbosity=0)

        # minified file created
        self.assertTrue(os.path.exists(os.path.join(
            settings.STATIC_ROOT, settings.REQUIRE_BASE_URL,
            settings.REQUIRE_STANDALONE_MODULES["app"]["out"])))
