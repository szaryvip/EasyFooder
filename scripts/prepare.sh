#!/bin/bash

# The following script handles the creation of a virtual environment along with an installation of required packages.

set -e

VENV="venv"

# Removing old venv
if [ -d "./$VENV" ]
then
	read -p "Old $VENV directory will be deleted. Proceed? (y/n) " -n 1 -r
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
	
	# Install python3.9- packages
	if [[ -z `dpkg -l | grep $PYTHON-dev` || -z `dpkg -l | grep $PYTHON-venv` ]]
	then
		echo "Note that $PYTHON-dev and $PYTHON-venv packages need to be installed - root privileges needed for that."
		sudo apt install -y $PYTHON-dev $PYTHON-venv
	fi
else
	# python3 is 3.9
	
	PYTHON="python3"
fi

# Check if system requirements satisfied
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

echo "Creating virtual environment..."
`$PYTHON -m venv ./$VENV`

echo "Installing required packages..."
# Wheel needs to be installed before all other requirements
$VENV/bin/python3 -m pip install wheel
$VENV/bin/python3 -m pip install -r requirements.txt

echo "Preparation complete."
