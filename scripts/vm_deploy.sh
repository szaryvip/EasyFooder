#!/bin/bash

# The following script handles SSH connection to the Azure VM
# with an installed key file as well as fetching incoming changes
# from repository and restarting the server.

# TODO remove this
echo "Script incomplete, do not run me"
exit 1

# SSH connection here, print something if no key is installed
# TODO

# Kill existing server instance
killall python3
killall postgres

# Fetch changes from github
scripts/vm/git_update.sh

# Run the server
scripts/run.sh

# Exit SSH
exit
