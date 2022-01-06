# Use the Python3.7.2 image
FROM python:3.7.2-stretch

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app 
ADD . /app

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

# Install the dependencies
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

# run the command to start uWSGI
#CMD ["uwsgi", "app.ini"]

ENV PYTHONUNBUFFERED 1

EXPOSE 5000

RUN ["chmod", "+x", "/app/entry.sh"]

ENTRYPOINT [ "./entry.sh" ]
