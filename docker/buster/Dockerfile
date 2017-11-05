FROM python:2.7

MAINTAINER Vítor Brandão <vitor@noiselabs.io>

RUN pip install future && \
    pip install python-dateutil --upgrade && \
    pip install pytz --upgrade && \
    pip install docopt && \
    pip install gitpython && \
    pip install pyquery && \
    pip install git+https://github.com/dariosky/buster.git

ENV GHOST_LOCAL_ADDRESS web
ENV GHOST_LOCAL_PORT 80
ENV LIVE_URL http://www.example.com

ENV BUSTER_STATIC_DIR /var/tmp/buster
VOLUME $BUSTER_STATIC_DIR

COPY entrypoint.py /usr/local/bin/
ENTRYPOINT ["/usr/local/bin/entrypoint.py"]
