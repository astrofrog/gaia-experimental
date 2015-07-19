#!/usr/bin/env python

from __future__ import print_function

from setuptools import setup, find_packages

entry_points = """
[glue.plugins]
gaia_viewer=glue_gaia:setup
"""

setup(name='glue-gaia',
      version="0.1.dev0",
      description = "Experimental GAIA plugin for glue",
      author='Thomas Robitaille',
      author_email='thomas.robitaille@gmail.com',
      url='http://glueviz.org',
      classifiers=[
          'Intended Audience :: Science/Research',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Topic :: Scientific/Engineering :: Visualization',
          'License :: OSI Approved :: BSD License'
          ],
      packages = find_packages(),
      package_data={'': ['*.ui'], '': ['*.png']},
      entry_points=entry_points
    )
