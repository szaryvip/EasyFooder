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

# SSH connection here, print something if no key is installed
RESULT=`ssh -o StrictHostKeyChecking=no -i "$1" "azureuser@52.157.157.162" 2>&1 < scripts/vm/restart.sh`

if [[ ! -z `echo "$RESULT" | grep "not accessible"` ]]
then
	echo "The provided path to an SSH key is incorrect. Please verify your input."
	exit 1
elif [[ ! -z `echo "$RESULT" | grep "connection refused"` ]]
then
	echo "Unable to connect to the virtual machine. Check if it's running and if the provided key is correct."
	exit 1
else
	# Connection should have went well
	echo "Restart procedures have been executed on the VM. If the server is up now, this means a success."
	echo "Please see logs on the host in case anything went wrong."
fi

