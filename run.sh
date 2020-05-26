#!/bin/sh
PORT=8888
docker run --rm -it -p $PORT:8000 -v "$(pwd)":/home cyclegans-demo