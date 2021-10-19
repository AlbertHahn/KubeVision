FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

RUN pip install --upgrade pip
RUN pip install flask
RUN pip install numpy
RUN pip install cv2
RUN pip install PIL
RUN pip install os
RUN pip install pickle

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
