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

# Venv activated, do sth
echo "Main file will run here. This is not configured yet. #TODO"

deactivate
