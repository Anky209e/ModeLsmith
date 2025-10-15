#!/bin/sh
set -e

# Wait for any services (DB) if needed - simple sleep can be replaced with proper wait-for
echo "Starting entrypoint script..."

# Run migrations (safe for sqlite)
echo "Running migrations..."
python manage.py migrate --noinput || true

# Create media directories if missing
mkdir -p media

exec "$@"
