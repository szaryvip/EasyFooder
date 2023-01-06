#!/bin/bash

cd src/Django/EasyFooder
coverage run manage.py test
coverage report -m