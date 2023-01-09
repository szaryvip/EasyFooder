#!/bin/bash

cd src/Django/EasyFooder

# https://coverage.readthedocs.io/en/7.0.2/config.html
# https://adamj.eu/tech/2019/04/30/getting-a-django-application-to-100-percent-coverage/

coverage erase
coverage run --rcfile=EasyFooder/.coverargc manage.py test
coverage report --rcfile=EasyFooder/.coverargc

# sleep 3
# rm .coverage
