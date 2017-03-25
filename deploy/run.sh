#!/bin/bash

cd /home/ian/tyler
source env/bin/activate
cd webapp
python manage.py runserver 0.0.0.0:8000
