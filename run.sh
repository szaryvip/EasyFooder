#!/bin/bash

VENV="venv"

if [ ! -d "./$VENV" ]
then
	echo "Virtual environment not found. Please run prepare.sh first to configure."
	exit 1
fi

source ./$VENV/bin/activate

if [[ ! `which python3` =~ .*"$VENV".* ]]
then
	echo "Unable to activate virtual environment"
	exit 1
fi

# Venv activated

# TODO check if requirements.txt changed

echo "Running Django server... Press Ctrl+C anytime to stop execution"
python3 src/Django/EasyFooder/manage.py runserver &
SERVER_PID=$!

# On exit (ctrl-c), kill server and deactivate venv
trap "kill $SERVER_PID; deactivate" EXIT

# Give the server a moment and then open a webpage
sleep 3

echo "Opening webpage..."
python3 -m webbrowser http://127.0.0.1:8000/test_app

# Wait for ctrl-c signal
while true
do
	sleep 2
done
