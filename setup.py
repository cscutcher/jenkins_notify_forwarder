# -*- coding: utf-8 -*-
"""
Setup for ttm_cli
"""
from setuptools import setup, find_packages
setup(
    name='jenkins_notify_forwarder',
    description='Forwards jenkins scm notifications to multiple jenkins instances',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'Requests',
        'gunicorn',
    ],
    entry_points={
    },
    author='Chris Scutcher',
    author_email='cscutche@cisco.com',
    url='https://stash-eng-gpk1.cisco.com/stash/projects/EXP/repos/ttm_cli',
)
