#!/usr/bin/env bash

export HOME=$(pwd)

mkdir -p ${HOME}/local_run/logs
export ENV=development
export HELIXA_APP_CONF=${HOME}/local_run/local_config.ini
export LOG_CONF=${HOME}/local_run/local_log_config.ini
export LOG_PATH=${HOME}/local_run/logs
export LOG_LEVEL=DEBUG

export GUNICORN_HOST="0.0.0.0"
export GUNICORN_PORT="5000"
export GUNICORN_APP_PATH="${HOME}/../farm_bo_api"
export GUNICORN_APP_MODULE="helixa_api.app:helixa_api_app"
export GUNICORN_WORKERS_NUMBER="1"
export GUNICORN_TIMEOUT="60"
export GUNICORN_BIND="${GUNICORN_HOST_HOST}:${GUNICORN_HOST_PORT}"

gunicorn --reload --capture-output --bind ${GUNICORN_HOST_BIND} --workers ${GUNICORN_HOST_WORKERS_NUMBER} --timeout ${GUNICORN_HOST_TIMEOUT} ${GUNICORN_HOST_APP_MODULE}
