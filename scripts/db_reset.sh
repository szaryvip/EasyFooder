#!/bin/bash

# The following script resets migrations for test_app

# Go to proper directory
cd ./src/Django/EasyFooder/

# Create new migrations
python3 manage.py makemigrations

# Clear the migration history
python3 manage.py migrate --fake test_app zero

# Remove migration files
rm test_app/migrations/0*

# Create the initial migrations
python3 manage.py makemigrations

# Fake the initial migration
python3 manage.py migrate --fake-initial

# inspiration: https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html

# sudo -u postgres -i psql -c "DROP TABLE test_app_teacher"
# sudo -u postgres -i psql -c "DROP TABLE test_app_meal_tag"
# sudo -u postgres -i psql -c "DROP TABLE test_app_order"
# sudo -u postgres -i psql -c "DROP TABLE test_app_meal"
# sudo -u postgres -i psql -c "DROP TABLE test_app_tag"
# sudo -u postgres -i psql -c "DROP TABLE test_app_user"
