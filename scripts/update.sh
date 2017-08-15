#!/usr/bin/env bash

# Colors yo!
GREEN="\e[32m"
RESET="\e[0m"

echo -en "${GREEN}Synchronzing the Casper theme...${RESET}"
docker-compose run dev rsync -a --delete current/content/themes/casper content/themes/
echo -e "${GREEN} Done.${RESET}"
