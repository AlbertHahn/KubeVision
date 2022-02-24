#!/bin/sh
docker run -v opencv-data:/app/modules/opencv/images \
-p 5000:5000 \
albird/flask-opencv:latest \
gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 1 --bind 0.0.0.0:5000 run:app
