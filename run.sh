#!/bin/sh
PORT=8888

# Interactive
# docker run --rm -it -p $PORT:8000 -v "$(pwd)":/home cyclegans-demo

# Daemonized (for server use)
docker run --rm -d -p $PORT:8000 -v "$(pwd)":/home cyclegans-demo