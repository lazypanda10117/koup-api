# Use an official Python runtime as a parent image
FROM python:3.6

LABEL maintainer="lazypanda10117"
LABEL org.label-schema.schema-version="1.0"
LABEL org.label-schema.name="koup-api"
LABEL org.label-schema.vcs-url="https://github.com/lazypanda10117/koup-api"
LABEL org.label-schema.vendor="Jeffrey Kam"

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN apk add --no-cache libpq
RUN apk add --no-cache --virtual reqs gcc musl-dev postgresql-dev
RUN pip3 install --upgrade pip pipenv gunicorn
RUN pipenv --python 3.7
RUN pipenv install --system --deploy
RUN apk del reqs

EXPOSE 3000

# Define environment variable
ENV FLASK_ENV=production GUNICORN_PORT=3000 ENDPOINT=http://0.0.0.0:3000

# Run app.py when the container launches
COPY ./scripts/start.sh .
CMD ["./start.sh"]
