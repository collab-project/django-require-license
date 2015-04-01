#!/usr/bin/env python
# Copyright Collab 2015

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "require_license.tests.settings")

    from django.core.management import execute_from_command_line

    sys.argv.insert(1, 'test')

    execute_from_command_line(sys.argv)
