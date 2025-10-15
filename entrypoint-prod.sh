#!/bin/sh
set -e 

echo "Starting production entrypoint..."

# Run migrations (safe for sqlite)
python manage.py migrate --noinput || true

# Collect static files
python manage.py collectstatic --noinput || true

# Ensure media dir exists
mkdir -p /app/media

exec "$@"
