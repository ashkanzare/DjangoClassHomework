FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN /usr/local/bin/python -m pip install -r requirements.txt
ADD . /code/