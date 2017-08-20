#!/usr/bin/env bash

# Colors yo!
RED="\e[31m"
GREEN="\e[32m"
YELLOW="\e[33m"
RESET="\e[0m"

function usage {
    echo "Usage: ghost-start.sh <dev|prod>"
}

function setup_db {
    echo -e "Database host: ${YELLOW}${GHOST_BASE_DATABASE_HOST}${RESET}"
    ghost config database.connection.host "${GHOST_BASE_DATABASE_HOST}"
    echo -e "Database name: ${YELLOW}${MYSQL_DATABASE}${RESET}"
    ghost config database.connection.database ${MYSQL_DATABASE}
    ghost config database.connection.user ${MYSQL_USER}
    ghost config database.connection.password ${MYSQL_PASSWORD}
    ghost setup migrate
}

if [ $# -eq 0 ]; then
    usage
    exit 1
fi

env=${1}

if [ "dev" == "${env}" ]; then
    echo -e "Setting up Ghost in ${GREEN}Development${RESET} mode..."
    setup_db ${env}
    nodemon current/index.js --watch content/themes
elif [ "prod" == "${env}" ]; then
    echo -e "Setting up Ghost in ${GREEN}Production${RESET} mode..."
    setup_db ${env}
    ghost run
else
    usage
    exit 1
fi
