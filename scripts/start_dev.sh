#!/usr/bin/env bash

set -e

DEFAULT_MODULE_NAME=app.main

MODULE_NAME=${MODULE_NAME:-$DEFAULT_MODULE_NAME}
VARIABLE_NAME=${VARIABLE_NAME:-app}
export APP_MODULE=${APP_MODULE:-"$MODULE_NAME:$VARIABLE_NAME"}
export PYTHONPATH=${PYTHONPATH}:app/

HOST=${HOST:-0.0.0.0}
PORT=${PORT:-8000}

# Start Uvicorn with live reload
uvicorn --reload --proxy-headers --host $HOST --port $PORT "$APP_MODULE"