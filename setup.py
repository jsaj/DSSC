#!/usr/bin/env python

import codecs
import os
from distutils.core import setup

from setuptools import find_packages

setup_path = os.path.abspath(os.path.dirname(__file__))
with codecs.open(os.path.join(setup_path, 'README.rst'), encoding='utf-8-sig') as f:
    README = f.read()

setup(name='DSSC',
      version='0.1',
      url='https://github.com/jsaj/DSSC',
      maintainer='Juscelino S. A. Júnior',
      maintainer_email='j.jr.avelino@gmail.com',
      description='Implementation of approach to Cross-Project Defect Prediction with Dynamic Ensemble Selection methods',
      long_description=README,
      long_description_content_type="text/markdown",  # README.md is of type 'markdown'
      author='Juscelino S. A. Júnior',
      author_email='j.jr.avelino@gmail.com',
      license='BSD 3-clause "New" or "Revised License"',

      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
      ],
      install_requires=[
          'scikit-learn>=0.21.0',
          'numpy>=1.17.0',
          'scipy>=1.4.0',
      ],
      python_requires='>=3',      

      packages=find_packages())
