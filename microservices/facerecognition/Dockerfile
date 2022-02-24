# Use the Python3.7.2 image
FROM python:3.7.2-stretch

# Set the working directory to /app
WORKDIR /app
# Copy the current directory contents into the container at /app 
ADD . /app

# Update and install libraries for OpenCV
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
# Install the dependencies
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

# Add Metadata ENV for stdout and stdin of python processes
# Exposing Port 5000 for the websocketserver
ENV PYTHONUNBUFFERED 1
EXPOSE 5000

# Start the container with gunicorn geventwebsocket workers and bind it to port 5000 use run.py as entrypoint.
CMD ["gunicorn" , "-k" ,"geventwebsocket.gunicorn.workers.GeventWebSocketWorker", "-w", "3" , "--bind" , ":5000" , "run:app"]
