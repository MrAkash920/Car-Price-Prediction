# Car Price Prediction with Machine Learning

![GitHub contributors](https://img.shields.io/github/contributors/MrAkash920/Car-Price-Prediction)
![GitHub stars](https://img.shields.io/github/stars/MrAkash920/Car-Price-Prediction)
![GitHub forks](https://img.shields.io/github/forks/MrAkash920/Car-Price-Prediction)
![GitHub issues](https://img.shields.io/github/issues/MrAkash920/Car-Price-Prediction)
![GitHub license](https://img.shields.io/github/license/MrAkash920/Car-Price-Prediction)

Predict car prices with a Machine Learning model using Linear Regression. This project also utilizes Flask for creating a web application and Heroku for deployment.

## Table of Contents

- [Demo](#demo)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Demo

![Demo](demo.gif)

Check out the live demo [here](your-heroku-app-url).

## Features

- Train a Linear Regression model to predict car prices.
- Build a web application with Flask for easy user interaction.
- Deploy the app on Heroku for accessibility from anywhere.
- Clean and well-organized codebase for further development.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/MrAkash920/Car-Price-Prediction.git
   ```

2. Change the directory:

   ```bash
   cd Car-Price-Prediction
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Train the model:

   ```bash
   python train.py
   ```

2. Start the Flask app:

   ```bash
   python app.py
   ```

3. Open your web browser and go to `http://localhost:5000`.

4. Enter car details and get price predictions.


## Docker Containerization

You can run this application in a Docker container. Here are the steps to containerize and run the application using Docker:

## Prerequisites

- [Docker](https://www.docker.com/) installed on your system.

## Building the Docker Image

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/Car-Price-Prediction.git
   cd Car-Price-Prediction
   ```

2. Create a `Dockerfile` in the project directory if it doesn't exist.

   ```Dockerfile
   # Use the official Python image from the Docker Hub
   FROM python:3.9

   # Set the working directory in the container
   WORKDIR /app

   # Copy the requirements file into the container and install the dependencies
   COPY requirements.txt requirements.txt
   RUN pip install -r requirements.txt

   # Copy the current directory contents into the container at /app
   COPY . .

   # Expose the port your application will run on (usually 5000 for Flask)
   EXPOSE 5000

   # Define the command to run your application
   CMD ["python", "app.py"]
   ```

3. Create a `requirements.txt` file with the required dependencies.

   ```
   Flask==2.0.1
   Werkzeug==2.0.1
   scikit-learn==0.24.2
   numpy==1.21.2
   pandas==1.3.3
   joblib==1.0.1
   ```

4. Build the Docker image from the project directory:

   ```bash
   docker build -t car-price-prediction .
   ```

## Running the Docker Container

5. Run the Docker container:

   ```bash
   docker run -p 5000:5000 car-price-prediction
   ```

6. Access the application in your web browser at [http://localhost:5000](http://localhost:5000).

## Stopping the Container

7. To stop the container, press `Ctrl+C` in the terminal where it's running.

## Cleaning Up

8. If you want to remove the container, use the following command:

   ```bash
   docker rm -f $(docker ps -aq)
   ```

## Note

- Make sure you have Docker installed and running on your system before following these steps.


## Docker Hub

[Docker Hub](https://hub.docker.com/repositories/singhakashcu)


## Contributing

Contributions are welcome! Fork the project, create your feature branch, and submit a pull request.