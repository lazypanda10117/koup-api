FROM postgres:10.5-alpine

LABEL maintainer="lazypanda10117"
LABEL org.label-schema.schema-version="1.0"
LABEL org.label-schema.name="postgres"
LABEL org.label-schema.vcs-url="https://github.com/lazypanda10117/koup-api"
LABEL org.label-schema.vendor="Jeffrey Kam"


## Use custom init script.
COPY initdb.sh /docker-entrypoint-initdb.d/initdb.sh
RUN chmod u+x /docker-entrypoint-initdb.d/initdb.sh
