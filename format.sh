#!/bin/sh
isort -rc .
autoflake -ri --remove-all-unused-imports --remove-unused-variables .
autopep8 -aari .
