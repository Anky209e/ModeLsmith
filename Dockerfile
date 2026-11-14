FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libsndfile1 libjpeg-dev zlib1g-dev libpng-dev tk-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

RUN groupadd --gid 1000 appuser \
    && useradd --uid 1000 --gid appuser --create-home appuser
COPY --chown=appuser:appuser . /app
# Keep entrypoints outside the development source bind mount.
COPY entrypoint-dev.sh entrypoint-prod.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint-dev.sh /usr/local/bin/entrypoint-prod.sh \
    && mkdir -p /app/media/cnn_images /app/media/gans_images /app/models /app/static /app/runtime \
    && chown -R appuser:appuser /app/media /app/static /app/runtime
USER appuser
EXPOSE 8000
ENTRYPOINT ["/usr/local/bin/entrypoint-prod.sh"]
CMD ["gunicorn", "modelsmith.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "1", "--timeout", "120", "--access-logfile", "-", "--error-logfile", "-"]
