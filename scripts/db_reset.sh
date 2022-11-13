sudo -u postgres psql -c "DROP TABLE test_app_teacher"

cd ./src/Django/EasyFooder
python3 manage.py migrate --fake test_app zero

python3 manage.py makemigrations
python3 manage.py migrate
