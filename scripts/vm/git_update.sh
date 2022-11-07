#!/bin/bash

# The following script handles pulling changes from git repository
# and installing missing system & Python packages, as listed in
# requirements files.

cd EasyFooder

# Pulling from git using deploy key configured as in here:
# https://dylancastillo.co/how-to-use-github-deploy-keys/
git pull

# System packages
sudo xargs apt install < requirements_system.txt -y

# Python packages
pip install -r requirements.txt
