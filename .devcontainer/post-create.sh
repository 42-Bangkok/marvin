#! /bin/bash

PRE='export $(cat '
POST='/.env | xargs)'
CMD=$PRE$1$POST
echo $CMD >> ~/.bashrc

sudo apt update && sudo apt install -y postgresql-client redis-tools
uv sync