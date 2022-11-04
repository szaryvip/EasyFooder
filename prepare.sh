#!/bin/bash

# The following script handles the creation of a virtual environment along with an installation of required packages.

set -e

VENV="venv"

# Removing old venv
if [ -d "./$VENV" ]
then
	read -p "Old ./$VENV directory will be deleted. Proceed? (y/n) " -n 1 -r
	if [[ $REPLY =~ ^[Yy]$ ]]
	then
		rm -r ./$VENV
		echo
	else
		echo
		exit 1
	fi
fi

if [ `python3 --version | cut -d ' ' -f 2 | cut -d '.' -f 2` -lt 9 ]
then
	# python3 is not greater or equal than 3.9
	
	if [ -z `which python3.9` ]
	then
		echo "ERROR: No Python3.9 installation found. Install Python3.9 and make it accessible by either python3 or python3.9 alias."
		exit 1
	fi
	
	PYTHON="python3.9"
else
	# python3 is 3.9
	
	PYTHON="python3"
fi

if [[ -z `dpkg -l | grep $PYTHON-dev` || -z `dpkg -l | grep $PYTHON-venv` ]]
then
	echo "Note that $PYTHON-dev and $PYTHON-venv packages need to be installed - root privileges needed for that."
	sudo apt install -y $PYTHON-dev $PYTHON-venv
fi

echo "Creating virtual environment..."
`$PYTHON -m venv ./$VENV`

echo "Installing required packages..."
venv/bin/python3 -m pip install -r requirements.txt

echo "Preparation complete."
