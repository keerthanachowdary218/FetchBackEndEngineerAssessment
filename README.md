# Fetch Backend Engineer Assessment

## Overview

This project involves setting up a receipt processing system using Python and Docker. The application allows users to send receipt data via a POST request and receive a unique receipt ID. Users can then retrieve point values associated with the receipt via a GET request.

## Running Locally (on Mac)

### 1. **Install Dependencies**

Ensure you have the following installed:

- Python (preferably 3.x)
- `curl` for making requests
- Docker (if you want to run in a containerized environment)

### 2. **Run the Application Locally**

1. Open a terminal and navigate to the project directory.

2. Run the application using the following command:
   ```bash
   python app.py
   ```

   This will start a local server on `http://127.0.0.1:5000`.

### 3. **Making a POST Request**

Once the application is running, open another terminal and navigate to the project folder. You can now make a POST request using `curl`:

```bash
curl -X POST "http://127.0.0.1:5000/receipts/process" \
    -H "Content-Type: application/json" \
    -d @receipt-processor-challenge-main/examples/morning-receipt.json
```

**Expected Response**:
```json
{
  "id": "a57f5e3c-4e64-43a8-a835-7d6b6c55a844"
}
```

### 4. **Making a GET Request**

To retrieve the points for a given receipt ID, use the following GET request:

```bash
curl -X GET http://127.0.0.1:5000/receipts/a57f5e3c-4e64-43a8-a835-7d6b6c55a844/points
```

**Expected Response**:
```json
{
  "points": 15
}
```

---

## Running in Docker

### 1. **Install Docker**

If you don't have Docker installed, you can download it from [Docker's official website](https://www.docker.com/). After installing, verify by running:

```bash
docker --version
```

You should see the Docker version information if it is installed properly.

### 2. **Dockerizing the Application**

To run the app in Docker, follow these steps:

1. **Create a Dockerfile** in the project directory:

   ```bash
   vim Dockerfile
   ```

2. **Write the following Dockerfile configuration**:

   ```Dockerfile
   FROM python:3.9-slim

   WORKDIR /app
   
   COPY requirements.txt requirements.txt
   RUN pip install --no-cache-dir -r requirements.txt
   
   COPY . .
   
   CMD ["python", "app.py"]
   
   EXPOSE 5000

   ```

3. **Build the Docker image**:

   In your project directory, run the following command to build the Docker image:

   ```bash
   docker build -t fetchbackendengineerassessment .
   ```

   This will create a Docker image with the tag `fetchbackendengineerassessment`.

### 3. **Running the Docker Container**

Once the image is built, you can run the container with the following command:

```bash
docker run -d -p 8080:5000 --name fetchbackendcontainer fetchbackendengineerassessment
```

This will start the application inside a Docker container and expose port `5000` inside the container to port `8080` on your machine.

### 4. **Making Requests to the Dockerized Application**

Once the container is running, you can use `curl` to make requests just like in the local setup:

#### POST Request:

```bash
curl -X POST "http://127.0.0.1:8080/receipts/process" \
    -H "Content-Type: application/json" \
    -d @receipt-processor-challenge-main/examples/morning-receipt.json
```

**Expected Response**:
```json
{
  "id": "a57f5e3c-4e64-43a8-a835-7d6b6c55a844"
}
```

#### GET Request:

```bash
curl -X GET http://127.0.0.1:8080/receipts/a57f5e3c-4e64-43a8-a835-7d6b6c55a844/points
```

**Expected Response**:
```json
{
  "points": 15
}
```
