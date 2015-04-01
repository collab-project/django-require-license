# Copyright Collab 2015

import os
from datetime import datetime, date

DEBUG = True

SITE_ID = 1

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

TEST_ROOT = os.path.dirname(__file__)

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'require_license'
]

SECRET_KEY = 'top_secret'

MEDIA_ROOT = os.path.join(TEST_ROOT, 'media')

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware'
)

# =============================================================================
# STATIC FILES
# =============================================================================

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: ``/home/media/media.lawrence.com/static/``
STATIC_ROOT = os.path.abspath(os.path.join(TEST_ROOT, 'static'))

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.abspath(os.path.join(TEST_ROOT, 'resources')),
)

# URL prefix for static files.
# Example: ``/static/`` or ``http://mysite.static/``
STATIC_URL = '/static/'

# The file storage engine to use when collecting static files with the
# `collectstatic` management command.
# Default: :py:class:`django.contrib.staticfiles.storage.StaticFilesStorage`
# Require.js: :py:class:`require.storage.OptimizedStaticFilesStorage`
# django-require-license: :py:class:`require_license.storage.OptimizedStaticFilesStorage`
STATICFILES_STORAGE = 'require_license.storage.OptimizedStaticFilesStorage'

# =============================================================================
# REQUIREJS
# =============================================================================

# The baseUrl to pass to the r.js optimizer.
REQUIRE_BASE_URL = 'js'

# The name of the build profile for the site, relative to REQUIRE_BASE_URL.
# Leave blank to use the built-in default build profile.
REQUIRE_BUILD_PROFILE = 'app.build.js'

# The name of the require.js script used by your project, relative to
# REQUIRE_BASE_URL.
REQUIRE_JS = os.path.join(REQUIRE_BASE_URL, 'libs', 'require.js')

# Whether to run django-require in debug mode.
REQUIRE_DEBUG = DEBUG

# A dictionary of standalone modules to build with almond.js.
REQUIRE_STANDALONE_MODULES = {
    'app': {
        # Where to output the built module, relative to REQUIRE_BASE_URL.
        'out': 'app.min.js',

        # A build profile used to build this standalone module.
        'build_profile': REQUIRE_BUILD_PROFILE,
    }
}

# A dictionary of output files that need a license header with configs.
REQUIRE_LICENSE_HEADERS = {
    os.path.join(REQUIRE_BASE_URL, 'app.min.js'): {
        'license_file': os.path.join(REQUIRE_BASE_URL, 'JS-LICENSE.txt'),
        'timestamp': date.today(),
        'copyright_year': datetime.now().year,
        'copyright_holder': 'MyCompany',
        'license_url': 'http://example.com/license'
    }
}

# A tuple of files to exclude from the compilation result of r.js.
REQUIRE_EXCLUDE = ('build.txt',
    os.path.join(REQUIRE_BASE_URL, REQUIRE_BUILD_PROFILE),
)

# The execution environment in which to run r.js: auto, node or rhino.
# auto will autodetect the environment and make use of node if available
# and rhino if not. It can also be a path to a custom class that subclasses
# require.environments.Environment and defines some "args" function that
# returns a list with the command arguments to execute.
REQUIRE_ENVIRONMENT = "auto"

# =============================================================================
# LOGGING
# =============================================================================

# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

LOG_HANDLER = 'null'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)-6s %(name)-15s - %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(asctime)s %(levelname)-6s %(name)-15s - %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        }
    },
    'loggers': {
        'require_license': {
            'handlers': [LOG_HANDLER],
            'level': 'DEBUG'
        },
        'celery': {
            'handlers': [LOG_HANDLER],
            'level': 'DEBUG'
        },
    }
}
