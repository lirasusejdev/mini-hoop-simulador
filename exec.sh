#!/bin/bash
container=$1
shift
docker exec -it $container "$@"