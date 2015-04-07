# Copyright Collab 2013-2015

"""
Tests for the :py:mod:`require_license.storage` module.
"""

from __future__ import unicode_literals

import os
import codecs
from datetime import datetime, date

from django.conf import settings
from django.test import TestCase
from django.core.management import call_command

from require_license import version


class StorageTestCase(TestCase):
    """
    Tests for :py:mod:`~require_license.storage`.
    """
    def test_licenseHeaderMixin(self):
        """
        :py:class:`~require_license.storage.LicenseHeaderMixin` adds a license
        header to the minified JS module.
        """
        call_command('collectstatic', interactive=False, dry_run=False,
            clear=False, verbosity=0)

        file_path = os.path.join(
            settings.STATIC_ROOT, settings.REQUIRE_BASE_URL,
            settings.REQUIRE_STANDALONE_MODULES['app']['out']
        )

        # minified file created
        self.assertTrue(os.path.exists(file_path))

        # verify header
        with codecs.open(file_path, 'rb', encoding='utf-8') as output_file:
            lines = output_file.readlines()[:6]

            self.assertEqual(lines[0],
                '/*! Copyright MyCompany {} - v{} ({})\n'.format(
                datetime.now().year,
                version,
                date.today()))

            self.assertEqual(lines[-2],
                ' * For a list of these libraries and their licenses,'
                ' visit http://example.com/license.\n')
