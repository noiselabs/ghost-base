FROM python:2.7

MAINTAINER Vítor Brandão <vitor@noiselabs.io>

RUN pip install buster

ENV GHOST_LOCAL_ADDRESS web
ENV GHOST_LOCAL_PORT 80
ENV LIVE_URL http://www.example.com

ENV BUSTER_STATIC_DIR /var/tmp/buster
VOLUME $BUSTER_STATIC_DIR

COPY entrypoint.py /usr/local/bin/
ENTRYPOINT ["/usr/local/bin/entrypoint.py"]
