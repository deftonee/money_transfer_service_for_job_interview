#!/usr/bin/env sh

python manage.py migrate
python manage.py shell < init_db.py
python manage.py collectstatic --noinput
python manage.py runserver "$LISTEN_HOST":"$LISTEN_PORT" --noreload

