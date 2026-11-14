#!/bin/sh
set -eu

mkdir -p media/cnn_images media/gans_images
python manage.py migrate --noinput
python manage.py collectstatic --noinput
exec "$@"
