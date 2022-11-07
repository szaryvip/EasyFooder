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
	read -p "Change password in existing .env file? (y/n) " -n 1 -r
	echo
	if [[ $REPLY =~ ^[Yy]$ ]]
	then
		sed "s/DB_PASSWORD=.*/DB_PASSWORD=$PASS/" $ENV_PATH > .tmp_env && mv .tmp_env $ENV_PATH
	else
		echo "OK. You may need to change the file manually."
	fi
else
	echo "Please follow https://easyfooder.atlassian.net/wiki/spaces/SD/pages/852518/Konfiguracja+bazy+danych to create .env file (this cannot be automated due to security reasons)."
fi

echo "Database setup complete."

