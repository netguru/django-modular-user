#!/usr/bin/env python3

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding = 'utf-8') as f:
	long_description = f.read()

setup(
	name = 'django-modular-user',
	version = '0.1.1',
	description = "Modular user model for Django",
	long_description = long_description,
	long_description_content_type = 'text/markdown',
	url = 'https://gitlab.com/aiakos/django-modular-user',
	author = "Aiakos Contributors",
	author_email = 'aiakos@aiakosauth.com',
	classifiers = [
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'Intended Audience :: System Administrators',
		'Topic :: System :: Systems Administration :: Authentication/Directory',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3 :: Only',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Framework :: Django',
		'Framework :: Django :: 2.0',
		'Framework :: Django :: 2.1',
	],
	keywords = "django user model auth email phone number",
	packages = ['django_modular_user'],
	zip_safe = True,
	install_requires = ['django>=2.0.0,<2.99'],
)
