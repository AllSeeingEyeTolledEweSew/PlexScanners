#!/usr/bin/env python

from __future__ import with_statement

from setuptools import setup, find_packages

with open("README") as readme:
    documentation = readme.read()

setup(
    name="PlexScanners",
    version="0.1.0",
    description="Plex's Scanners, repackaged for pypi.",
    long_description=documentation,
    author="AllSeeingEyeTolledEweSew",
    author_email="allseeingeyetolledewesew@protonmail.com",
    url="http://github.com/AllSeeingEyeTolledEweSew/PlexScanners",
    use_2to3=True,
    packages=[
        "plex.scanners.Common",
        "plex.scanners.Common.mp4file",
        "plex.scanners.Movies",
        "plex.scanners.Music",
        "plex.scanners.Photos",
        "plex.scanners.Series",
    ],
    install_requires=[
        "mutagen>=1.24",
        "titlecase>=0.2",
    ],
)
