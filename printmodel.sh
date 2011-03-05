#!/bin/bash

python manage.py printmodel 2> $(date +'%Y-%m-%d').dat
