FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libsndfile1 \
    libjpeg-dev \
    zlib1g-dev \
    libpng-dev \
    tk-dev \
    git \
    curl \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app

# Ensure folders exist
RUN mkdir -p /app/media /app/models

# Ensure entrypoints are executable
RUN chmod +x /app/entrypoint.sh || true
RUN chmod +x /app/entrypoint-prod.sh || true

# Non-root user for safety
RUN groupadd -r appuser && useradd -r -g appuser appuser || true
RUN chown -R appuser:appuser /app
USER appuser

EXPOSE 8000
ENV PORT=8000

# change entrypoint for production or development abhi dev ka h
ENV ENTRYPOINT_PATH=/app/entrypoint-prod.sh
ENTRYPOINT ["sh", "-c", "exec $ENTRYPOINT_PATH \"$@\""]
