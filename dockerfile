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
