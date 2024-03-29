#!/bin/bash


psql -h 52.157.157.162 -U postgres -c "DROP TABLE \"Meals_meal_tag\""
psql -h 52.157.157.162 -U postgres -c "DROP TABLE \"Meals_order\""
psql -h 52.157.157.162 -U postgres -c "DROP TABLE \"Meals_meal\""
psql -h 52.157.157.162 -U postgres -c "DROP TABLE \"Meals_tag\""

# sudo -u postgres -i psql -c "DROP TABLE \"Meals_meal_tag"

cd ./src/Django/EasyFooder
python3 manage.py migrate --fake Users zero
python3 manage.py migrate --fake Meals zero

find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

python3 manage.py makemigrations

python3 manage.py migrate --fake-initial
