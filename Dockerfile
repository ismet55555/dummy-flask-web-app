# Base Image
FROM python:3.8-slim-buster

# Install base OS tools and dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    openssh-server \
    vim \
    htop \
    wget \
    python3-venv \
    python3-pip

# Clearing out local repo of retrieved OS tools and dependencies
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Installing/Upgrading pip
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python3 get-pip.py

# Create the application directory
RUN mkdir -p /dummy-flask-web-app

# Copy all files in current directory into application directory (container)
COPY . /dummy-flask-web-app

# Define working directory
WORKDIR /dummy-flask-web-app

# Give execture permission to start-up script
RUN ["chmod", "+x", "/dummy-flask-web-app/start"]

# Run the start-up script
CMD [ "bash", "/dummy-flask-web-app/start" ]