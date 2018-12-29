#!/usr/bin/env sh
set -e

psql -v ON_ERROR_STOP=1 \
  --username "$POSTGRES_USER" \
  --dbname "$POSTGRES_DB" <<-EOSQL
  CREATE USER robot WITH ENCRYPTED PASSWORD '$ROBOT_PASS';
  CREATE DATABASE elevate;
  GRANT ALL PRIVILEGES ON DATABASE elevate TO robot;
EOSQL

set +e
