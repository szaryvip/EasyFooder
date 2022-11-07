#!/bin/bash

# The following script handles SSH connection to the Azure VM
# with a provided key file as well as fetching incoming changes
# from repository and restarting the server.

if [ -z "$1" ]
then
	echo "Please provide a path to the key file for SSH connection."
	exit 1
fi

echo "Connecting to the VM..."

ssh -o StrictHostKeyChecking=no -i "$1" "azureuser@52.157.157.162"
