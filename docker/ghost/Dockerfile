FROM ghost:1.16

MAINTAINER Vítor Brandão <vitor@noiselabs.io>

ENV GHOST_BASE_DATABASE_HOST=db

RUN set -x \
    && apt-get update && apt-get install -y --no-install-recommends build-essential python2.7 rsync sudo \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN npm install -g nodemon@latest

COPY ghost ${GHOST_INSTALL}/content
RUN rsync -a --delete ${GHOST_INSTALL}/current/content/themes/casper ${GHOST_INSTALL}/content/themes/
COPY config/config.development.json ${GHOST_INSTALL}/config.development.json
COPY config/config.production.json ${GHOST_INSTALL}/config.production.json

RUN mkdir /opt/ghost-base
COPY docker/bin/* /opt/ghost-base/
