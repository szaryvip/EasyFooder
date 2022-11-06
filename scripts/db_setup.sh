#!/bin/bash

# The following script handles basic database configuration.

set -e

ENV_PATH="src/Django/EasyFooder/EasyFooder/.env"

read -s -p 'Please input new password for "postgres" user: ' -r
PASS=$REPLY

echo
echo "To access postgres settings, root privileges will be needed."
sudo su postgres <<HERE

psql
ALTER USER postgres WITH PASSWORD '$PASS';

HERE

echo "Changed password."

if [ -f $ENV_PATH ]
then
	read -p "Use existing .env file? (y/n) " -n 1 -r
	echo
	if [[ $REPLY =~ ^[Yy]$ ]]
	then
		sed "s/DB_PASSWORD=.*/DB_PASSWORD=$PASS/" $ENV_PATH > $ENV_PATH
		echo "Database setup complete."
		exit 0
	fi
fi

REPLY=""
while [ -z $REPLY ]
do
	read -p "Please provide a path to the .env file (content be copied to the destination location): " -r
	echo
	if [ ! -f "$REPLY" ]
	then
		echo "Path incorrect, try again."
		REPLY=""
	fi
done

cp $REPLY $ENV_PATH
sed "s/DB_PASSWORD=.*/DB_PASSWORD=$PASS/" $ENV_PATH > $ENV_PATH
echo "Database setup complete."

