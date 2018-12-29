#!/usr/bin/env bash
i="0"
while [ $i -lt 50 ]
do
if  $(nc -z ${DB_HOST} ${DB_PORT}) ; then
    echo "Connected To Database"
    sleep 5
    gunicorn -b 0.0.0.0:$GUNICORN_PORT app:app
    exit 0
fi
let i+=1
done