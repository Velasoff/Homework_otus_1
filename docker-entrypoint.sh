#!/bin/bash
set -e

PORT=${2:-8000}

case "$1" in
    init)
        alembic upgrade head
        ;;
    api)
        exec uvicorn app.server:app --host 0.0.0.0 --port $PORT --forwarded-allow-ips '*'
        ;;
    start)
        alembic upgrade head
        gunicorn app.server:app -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 --workers=5
        ;;
    *)
        exec "$@"
        ;;
esac
