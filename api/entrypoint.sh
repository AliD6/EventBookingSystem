#!/bin/bash

python manage.py wait_for_db
python manage.py migrate
gunicorn --reload config.wsgi --bind 0.0.0.0:8000
