#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# manage.py と同じ階層にいるので cd は不要
python manage.py collectstatic --no-input
python manage.py migrate