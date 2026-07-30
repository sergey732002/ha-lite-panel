#!/usr/bin/with-contenv bashio

echo "======================================"
echo "Starting HA Lite Panel"
echo "======================================"

mkdir -p /panels
mkdir -p /static
mkdir -p /templates

exec python3 /app.py