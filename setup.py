#!/usr/bin/env python3
# coding=utf-8

'''
    python distribute file
'''

# from __future__ import (absolute_import, division, print_function,
#                         unicode_literals, with_statement)

from setuptools import setup, find_packages


def requirements_file_to_list(fn='requirements.txt'):
    '''
        read a requirements file and create a list that can be used in setup.
    '''
    with open(fn, 'r') as f:
        return [x.rstrip() for x in list(f) if x and not x.startswith('#')]


setup(
    name='twitter-amnesia',
    version='1.0.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=requirements_file_to_list(),
    py_modules=['main'],
    entry_points={
        'console_scripts': [
            'twitter-amnesia = twitter_amnesia:main',
        ]
    },
    author='Carlos Miguel Ferreira',
    author_email='carlosmf.pt@gmail.com',
    maintainer='Carlos Miguel Ferreira',
    maintainer_email='carlosmf.pt@gmail.com',
    description='A twitter service used to delete tweets not protected by a custom tag and older than a specific date.',
    long_description=open('README.md').read(),
    keywords=['Twitter', 'Management'],
    license='GPLv3',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
    ]
)
