#!/bin/bash
sudo pip3 install poetry
cd /home/ec2-user/service-analytics
source ./.venv/bin/activate
poetry install --no-dev
