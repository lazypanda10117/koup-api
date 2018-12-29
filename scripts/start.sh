#!/usr/bin/env sh

for count in $(seq 1 100); do
  echo "Pinging database: attempt $count"

  if  $(nc -z ${DB_HOST} ${DB_PORT}) ; then
    echo "Database responded. Starting application..."
    sleep 5
    gunicorn -b 0.0.0.0:$GUNICORN_PORT app:app
    exit 0
  fi

  sleep 5
done

## Failed to connect after max attempts.
exit 1
