#!/bin/bash

DOCKER_BUILD_PATH="resources/docker"
DOCKERFILES_PATH="$DOCKER_BUILD_PATH/dockerfiles/python3"
IMAGE_NAME="nommon-base-py3"
NAME="nommon-base-py3-$LOGNAME"
DOCKERFILE_NAME="DockerFileNommonBasePy3"
is_number="^[0-9]+"
port="$2"

if [[ $1 == '-i' ]]
then
    docker rmi -f "$IMAGE_NAME"
    docker build -t "$IMAGE_NAME" -f "$DOCKERFILES_PATH/$DOCKERFILE_NAME" $DOCKER_BUILD_PATH
elif [[ $1 == '-r' ]]
then
    if ! [[ $port =~ $is_number ]]
    then
            port=8888
    fi
    docker run --name="$NAME" --hostname=$NAME --volume="$(pwd):/opt/shared" -p "$port:8888" -it $IMAGE_NAME
elif [[ $1 == '-s' ]]
then
    docker stop "$NAME"
elif [[ $1 == '-d' ]]
then
    docker rm "$NAME"
else
    docker start -i "$NAME"
fi
