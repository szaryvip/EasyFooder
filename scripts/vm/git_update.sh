#!/bin/bash

# The following script handles pulling changes from git repository
# and installing missing system & Python packages, as listed in
# requirements files.

cd EasyFooder

# Python packages
pip install -r requirements.txt

# System packages
sudo xargs apt install < requirements_system.txt -y
