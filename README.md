# Fetch Backend Engineer Assessment

## Overview
https://github.com/fetch-rewards/receipt-processor-challenge
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
or
```bash
curl -X POST "http://127.0.0.1:5000/receipts/process" \
     -H "Content-Type: application/json" \
     --data-binary @receipt-processor-challenge-main/examples/morning-receipt.json
```
**Expected Response**:
```json
{
  "id": "e1108bb6-1f46-483e-8333-c2d03d75e107"
}
```
![image](https://github.com/user-attachments/assets/7d7a57e6-6aed-446a-8eac-550954ae9a02)


### 4. **Making a GET Request**

To retrieve the points for a given receipt ID, use the following GET request:

```bash
curl -X GET http://127.0.0.1:5000/receipts/e1108bb6-1f46-483e-8333-c2d03d75e107/points
```

**Expected Response**:
```json
{
  "points": 15
}
```
![image](https://github.com/user-attachments/assets/847fcc75-a91d-464d-961c-a82df6bb0570)

---

## Running in Docker

### 1. **Install Docker**

If you don't have Docker installed, you can download it. After installing, verify by running:

```bash
docker --version
```

You should see the Docker version information if it is installed properly.

### 2. **Dockerizing the Application**

To run the app in Docker, follow these steps:
Ensure that the Dockerfile is present in the project directory

In your project directory, run the following command to build the Docker image:

   ```bash
   docker build -t fetchbackendengineerassessment .
   ```

   This will create a Docker image with the tag `fetchbackendengineerassessment`.

### 3. **Running the Docker Container**

Once the image is built, you can run the container with the following command:

```bash
docker run -d -p 5000:5000 --name fetchbackendcontainer fetchbackendengineerassessment
```

This will start the application inside a Docker container.

### 4. **Making Requests to the Dockerized Application**

Once the container is running, you can use `curl` to make requests just like in the local setup shown above:

#### POST Request:

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
![PostDocker](https://github.com/user-attachments/assets/e601bc70-fb54-4108-b080-e696b36d56a4)

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
![GetDocker](https://github.com/user-attachments/assets/2088d153-ef83-4423-9f75-2ccd32ebd99d)

