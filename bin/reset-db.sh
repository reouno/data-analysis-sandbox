#!/bin/sh
set -eux

# move to the directory
cd "$(dirname $0)"

# delete db
rm -f ../api_server/api_server/db.sqlite3

# migration
cd ../api_server && python manage.py migrate

# create seed data
python manage.py loaddata api_server/apps/custom_accounts/fixtures/fixtures.json

