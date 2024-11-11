# Dockerized Flask API

This repository contains a simple Dockerized Flask application designed to respond to basic HTTP requests.

## Project Structure

- **cts.py**: Contains the Flask app with a `/ping` route.
- **wsgi.py**: Uses Waitress to serve the Flask app, handling configuration for host and port.
- **requirements.txt**: Lists the Python dependencies (Flask and Waitress).
- **Dockerfile**: Defines the Docker image, setting up a Python environment, installing dependencies, and starting the app with Waitress.
- **.github/workflows/cloudrun.yml**: GitHub Actions workflow that builds and pushes the Docker image to the GCR and deploys or updates Google Cloud Run.

## Getting Started

1. **Build and run the Docker container**

   ```bash
    docker build -t cts .
    docker run -p 8080:8080 cts

2. **Test the endpoint**

    ```bash
    curl http://localhost:8080/ping

## Environment Variables

The application requires the following environment variables to be set:

- **PORT**: The port on which the Flask app will run (default is `8080`).

You can set these variables in your Dockerfile or pass them when running the Docker container:

```bash
docker run -p 8080:8080 -e PORT=8080 cts
```

## GitHub Actions Workflow
The workflow (cloudrun.yml) will trigger on push to main branch, performing the following steps:

1. Checkout the code
2. Log in to Google Cloud and setup gcloud CLI
3. Build the Docker image, tag it, and push it to gcr.io
4. Deploy or Update Cloud Run with the latest image

The workflow (docker.yml) will trigger on every push, performing the following steps:

1. Checkout the code
2. Login to GHCR
3. Build the Docker image, tag it and push it to ghcr.io

## Requirements

Before running the GitHub Actions workflow, ensure you have the following:

- **GCP_CREDENTIALS**: A JSON file containing your Google Cloud service account key. This is required for authentication with Google Cloud.
- **GCP_PROJECT_ID**: Your Google Cloud project ID where the Cloud Run service will be deployed.

Make sure to add these as secrets in your GitHub repository settings:

1. Go to your repository on GitHub.
2. Click on `Settings` > `Secrets and variables` > `Actions` > `New repository secret`.
3. Add `GCP_CREDENTIALS` with the contents of your service account JSON file.
4. Add `GCP_PROJECT_ID` with your Google Cloud project ID.

## Required Google Cloud APIs

Ensure the following APIs are enabled in your Google Cloud project:

- **Cloud Run API**: Enables deploying and managing containerized applications.
- **Cloud Resource Manager API**: Provides methods for creating, reading, and updating project metadata.

You can enable these APIs via the Google Cloud Console or using the `gcloud` CLI:

```bash
gcloud services enable run.googleapis.com
gcloud services enable cloudresourcemanager.googleapis.com
```

