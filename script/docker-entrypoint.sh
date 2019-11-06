#!/bin/sh
set -e

echo "Waiting for Database to start...."
python3 manage.py shell << EOF
from django.db import connections
from django.db.utils import OperationalError

from time import sleep


RETRY_TIME = 30
SLEEP_TIME = 1

for c in connections.all():
    count = 1
    while True:
        try:
            print(f'Trying to connect to {c.alias}, retry count {count}.')
            c.ensure_connection()
        except OperationalError:
            print(f'Connect to db {c.alias} fail.')
            if count >= RETRY_TIME:
                print('Up to retry limit.')
                exit(1)

            sleep(SLEEP_TIME)
            count += 1
        else:
            print(f'Connect to db {c.alias} success.')
            break

    print()
EOF

echo "Collecting static files..."
python3 manage.py collectstatic --noinput

echo "Migrating Database"
python3 manage.py migrate

echo "Makeing log folder"
[[ -d ./log/archived ]] || mkdir -p ./log/archived

echo "Run crontab"
crond

exec "$@"
