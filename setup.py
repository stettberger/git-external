#!/usr/bin/env python3

from setuptools import setup

setup(name='git-external',
      version="0.1",
      description='Provide an SVN external mechanism for Git.',
      author='Christian Dietrich',
      author_email='stettberger@dokucode.de',
      url='https://github.com/stettberger/git-external',
      classifiers=[
          "Intended Audience :: Developers",
          "Topic :: Software Development",
          "Environment :: Console",
          "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
          "Topic :: Software Development",
          "Topic :: Software Development :: Version Control"
      ],
      zip_safe=False,
      scripts=['bin/git-external']
)

