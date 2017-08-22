#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(name='stormbot-yocto',
      version='1.0',
      description='yoctopuce plugin for stormbot',
      author='Paul Fariello',
      author_email='paul@fariello.eu',
      url='https://git.paulfariello.fr/Stormbot/stormbot-yocto',
      packages=find_packages(),
      install_requires=['stormbot', 'yoctopuce'],
      entry_points={'stormbot.plugins': ['yocto = stormbot_yocto:Yocto']},
      classifiers=['Environment :: Console',
                   'Intended Audience :: System Administrators',
                   'Operating System :: POSIX',
                   'Programming Language :: Python'])
