# Copyright Collab 2015-2019
# See LICENSE for details.

from setuptools import setup, find_packages

from require_license import version

test_deps = [
    "tox",
    "coverage",
    "flake8"
]

setup(
    name="django-require-license",
    version=version,
    license="MIT",
    description="License header for django-require projects.",
    author="Thijs Triemstra",
    author_email="info@collab.nl",
    url="https://github.com/collab-project/django-require-license",
    packages=find_packages(),
    install_requires=[
        "django-require"
    ],
    tests_require=test_deps,
    extras_require={
        'docs': [
            'sphinx>=1.5.1'
        ],
        'test': test_deps
    },
    keywords="django requirejs plugin require.js",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 1.8",
        "Framework :: Django :: 1.9",
        "Framework :: Django :: 1.10",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
    ],
)
