#!/bin/bash

sudo apt-get update && sudo apt-get upgrade

sudo apt install nginx

sudo apt install gunicorn

sudo apt install python3-pip

pip install -r requirements.txt