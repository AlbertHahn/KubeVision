# Use the Python3.7.2 image
FROM python:slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app 
ADD . /app

# Install the dependencies
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED 1

EXPOSE 5001

# run the command to start uWSGI
CMD ["gunicorn", "-w", "1", "-b" , ":5001" ,"run:app"]
