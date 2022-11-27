#!/bin/bash


sudo -u postgres -i psql -c "DROP TABLE test_app_teacher"
sudo -u postgres -i psql -c "DROP TABLE test_app_meal_tag"
sudo -u postgres -i psql -c "DROP TABLE test_app_order"
sudo -u postgres -i psql -c "DROP TABLE test_app_meal"
sudo -u postgres -i psql -c "DROP TABLE test_app_tag"
sudo -u postgres -i psql -c "DROP TABLE test_app_user"

rm ./src/Django/EasyFooder/test_app/migrations/0*

cd ./src/Django/EasyFooder

python3 manage.py makemigrations
python3 manage.py migrate --fake test_app zero
python3 manage.py migrate
