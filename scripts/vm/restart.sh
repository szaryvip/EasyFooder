#!/bin/bash

cd EasyFooder

# Kill existing server instance
killall python3
killall postgres

# Fetch changes from github
scripts/vm/git_update.sh 1>../update_log.txt 2>&1

# Run the server
scripts/run.sh 1>../run_log.txt 2>&1 &

