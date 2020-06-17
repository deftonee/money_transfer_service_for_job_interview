FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV LISTEN_HOST "0.0.0.0"
ENV LISTEN_PORT "8000"

RUN mkdir /src
WORKDIR /src
COPY requirements.txt /src/
RUN pip install -r requirements.txt
COPY . /src/

ENTRYPOINT ["/src/run.sh"]
