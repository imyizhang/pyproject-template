#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools


with open('README.md', mode='r', encoding='utf-8') as f:
    README = f.read()


setuptools.setup(
    name='pyproject',
    version='0.1.0',
    description='pyproject template',
    long_description=README,
    long_description_content_type='text/markdown',
    author='Yi Zhang',
    author_email='yizhang.dev@gmail.com',
    url='https://github.com/imyizhang/pyproject-template',
    download_url='https://github.com/imyizhang/pyproject-template',
    packages=setuptools.find_packages(exclude=['tests', 'docs']),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='pyproject template',
    license='MIT',
    python_requires='>=3.7',
    install_requires=[],
)
