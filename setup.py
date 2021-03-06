#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='EmbASP',
      version='6.0.0',
      description='EmbASP',
      long_description=open('README.md').read(),
      author='Department of Mathematics and Computer Science, University of Calabria',
      license='MIT',
      author_email='embasp@mat.unical.it',
      url='https://www.mat.unical.it/calimeri/projects/embasp/',
      packages=find_packages(exclude=["*.test", "*.test.*", "test.*", "test"]),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
      ],
)