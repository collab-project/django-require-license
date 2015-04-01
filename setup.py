# Copyright Collab 2015

from setuptools import setup

from require_license import version


setup(
    name = "django-require-license",
    version = version,
    license = "MIT",
    description = "License header for django-require projects.",
    author = "Thijs Triemstra",
    author_email = "info@collab.nl",
    url = "https://github.com/collab-project/django-require-license",
    packages = [
        "require_license"
    ],
    keywords='django requirejs plugin require.js',
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4"
    ],
)
