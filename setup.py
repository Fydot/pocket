#!/usr/bin/python
# coding: utf-8
from setuptools import setup, find_packages


setup(name='pocket',
      version='0.4.2',
      author='huangdiandian',
      author_email='ifidot@gmail.com',
      description='pocket',
      license='PRIVATE',
      packages=find_packages(),
      install_requires=[
          'ujson',
          'redis',
      ],)
