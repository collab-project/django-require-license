# Copyright Collab 2013-2016
# See LICENSE for details.

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


class StorageTestCase(TestCase):
    """
    Tests for :py:mod:`~require_license.storage`.
    """
    def tearDown(self):
        if hasattr(self, 'file_path') and os.path.exists(self.file_path):
            os.remove(self.file_path)

    def assertHeaderEqual(self, version, expectedVersion):
        """
        Assert the header is correct.
        """
        with self.settings(REQUIRE_LICENSE_HEADERS={
                os.path.join(settings.REQUIRE_BASE_URL, 'app.min.js'): {
                    'license_file': os.path.join(settings.REQUIRE_BASE_URL,
                                    'JS-LICENSE.txt'),
                    'version': version,
                    'timestamp': date.today(),
                    'copyright_year': datetime.now().year,
                    'copyright_holder': 'MyCompany',
                    'license_url': 'http://example.com/license'
                }
            }):

            # run collecstatic
            call_command('collectstatic', interactive=False, dry_run=False,
                clear=False, verbosity=0)

            # minified file created
            self.file_path = os.path.join(
                settings.STATIC_ROOT, settings.REQUIRE_BASE_URL,
                settings.REQUIRE_STANDALONE_MODULES['app']['out']
            )
            self.assertTrue(os.path.exists(self.file_path))

            # verify header
            with codecs.open(self.file_path, 'rb', encoding='utf-8') as output_file:
                lines = output_file.readlines()[:6]

                self.assertEqual(lines[0],
                    '/*! Copyright MyCompany {} - v{} ({})\n'.format(
                    datetime.now().year,
                    expectedVersion,
                    date.today()))

                self.assertEqual(lines[-2],
                    ' * For a list of these libraries and their licenses,'
                    ' visit http://example.com/license.\n')

    def test_basic(self):
        """
        :py:class:`~require_license.storage.LicenseHeaderMixin` adds a license
        header to the minified JS module.
        """
        version = '1.0.1'
        self.assertHeaderEqual(version, expectedVersion=version)

    def test_fqVersionAttribute(self):
        """
        Use fully-qualified path to an existing attribute containing the
        version number.
        """
        version = 'require_license.version'
        from require_license import version as expectedVersion
        self.assertHeaderEqual(version, expectedVersion)
