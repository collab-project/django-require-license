# Copyright Collab 2013-2015

"""
Custom static files storage for the :py:mod:`require_license` application.
"""

from __future__ import unicode_literals

import os
import codecs

from django.conf import settings
from django.utils.encoding import smart_bytes

from django.contrib.staticfiles.storage import StaticFilesStorage

from require.storage import OptimizedFilesMixin

from require_license import version


class LicenseHeaderMixin(OptimizedFilesMixin):
    """
    Static files `post_process` mixin that prepends the content of a license
    text file to compiled file(s).
    """
    def post_process(self, *args, **kwargs):
        for item in super(LicenseHeaderMixin, self).post_process(
            *args, **kwargs):
            yield item

        for module_file, config in list(settings.REQUIRE_LICENSE_HEADERS.items()):
            # path to license header file
            license_path = os.path.join(
                self.location,
                config.get('license_file'))

            # use local version if 'version' key is missing
            if 'version' not in config:
                config.update({'version': version})

            # inject header
            with open(license_path, 'r') as header:
                license_header = header.read().format(**config)

            # prepend license header to content
            module_path = self.path(module_file)
            with codecs.open(module_path, 'rb', encoding='utf-8') as input_file:
                content = '{header}\n{data}'.format(
                    header=license_header,
                    data=input_file.read())

            if kwargs['dry_run'] == False:
                # overwrite updated content to file
                with open(module_path, 'wb') as output_file:
                    output_file.write(smart_bytes(content))


class OptimizedStaticFilesStorage(LicenseHeaderMixin, StaticFilesStorage):
    pass
