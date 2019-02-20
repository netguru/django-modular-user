#!/usr/bin/env python3

from setuptools import setup

with open('README.md') as f:
	readme = f.read()

setup(
	name = "django-modular-user",
	version = "0.1.0",
	description = "Modular user model for Django",
	long_description = readme,
	author = "Aiakos Contributors",
	author_email = "aiakos@aiakosauth.com",
	url = "https://gitlab.com/aiakos/django-modular-user",
	keywords = "auth user oidc",
	install_requires = ['Django>=2.0,<2.99'],
	packages = ['django_modular_user'],
	zip_safe = True,
	license = 'MIT',
	classifiers = [
		'Development Status :: 4 - Beta',
		'Framework :: Django :: 2.0',
		'Framework :: Django :: 2.1',
		'Intended Audience :: Developers',
		'Intended Audience :: System Administrators',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.6',
		'Topic :: System :: Systems Administration :: Authentication/Directory',
	],
)
