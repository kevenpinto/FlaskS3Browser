#! /bin/bash

cd /home/ec2-user/FlaskS3Browser
source venv/bin/activate
# virtualenv is now active.

waitress-serve --port=5000 --call flaskS3:create_app
