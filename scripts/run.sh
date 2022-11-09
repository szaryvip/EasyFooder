#!/bin/bash

set -e

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

# Check if system requirements changed
MISSING=""
while read line
do
	if [[ ! -z "$line" && -z `dpkg -l | grep "$line"` ]]
	then
		# This package is missing
		if [ -z "$MISSING" ]
		then
			MISSING="$line"
		else
			MISSING="$MISSING, $line"
		fi
	fi
done < requirements_system.txt

if [[ ! -z "$MISSING" ]]
then
	echo "One or more packages is missing."
	echo "The following packages will be installed: $MISSING."
	echo "Your credentials will be needed to run apt install."
	sudo xargs apt install -y < requirements_system.txt
	echo "Missing system packages installed."
fi

# Check if Python requirements changed
if [[ ! -z `pip3 freeze -r requirements.txt 2>&1 | grep "not installed"` ]]
then
	echo "Installing missing Python packages..."
	pip3 install -r requirements.txt
	echo "Missing Python packages installed."
fi

echo 'Running "makemigrations"...'
python3 src/Django/EasyFooder/manage.py makemigrations

echo 'Running "migrate"...'
python3 src/Django/EasyFooder/manage.py migrate

echo "Running Django server... Press Ctrl+C anytime to stop execution"
python3 src/Django/EasyFooder/manage.py runserver 0.0.0.0:8530

deactivate

