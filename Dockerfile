# Use an official Python runtime as a parent image
FROM python:3.7-alpine3.7

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
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt
RUN pip3 install --upgrade pip pipenv gunicorn
RUN apk del reqs
# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World
ENV FLASK_ENV=production GUNICORN_PORT=3000 ENDPOINT=http://0.0.0.0:3000

# Run app.py when the container launches
CMD ["python", "app.py"]
