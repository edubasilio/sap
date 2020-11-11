#!/bin/sh

echo "Waiting database start!"

while ! nc -z ${DATABASE_HOST} ${DATABASE_PORT}; do
    sleep 3
done

echo "Database started!"

exec "$@"
