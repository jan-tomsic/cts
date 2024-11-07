# Dockerized Flask API

This repository contains a simple Dockerized Flask application designed to respond to basic HTTP requests.

## Project Structure

- **cts.py**: Contains the Flask app with a `/ping` route.
- **wsgi.py**: Uses Waitress to serve the Flask app, handling configuration for host and port.
- **requirements.txt**: Lists the Python dependencies (Flask and Waitress).
- **Dockerfile**: Defines the Docker image, setting up a Python environment, installing dependencies, and starting the app with Waitress.
- **.github/workflows/docker.yml**: GitHub Actions workflow that builds and pushes the Docker image to the GitHub Container Registry.

## Getting Started

1. **Build and run the Docker container**

   ```bash
    docker build -t cts .
    docker run -p 8080:8080 cts

2. **Test the endpoint**

    ```bash
    curl http://localhost:8080/ping

## GitHub Actions Workflow
The workflow (docker.yml) will trigger on any push, performing the following steps:

1. Checkout the code.
2. Log in to GitHub Container Registry.
3. Build the Docker image, tag it, and push it to ghcr.io.
