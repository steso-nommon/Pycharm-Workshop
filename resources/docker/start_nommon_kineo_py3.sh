#!/bin/bash

DOCKER_BUILD_PATH="resources/docker"
DOCKERFILES_PATH="$DOCKER_BUILD_PATH/dockerfiles/python3"
BASE_IMAGE_NAME="nommon-base-py3"
BASE_IMAGE_DOCKERFILE="DockerFileNommonBasePy3"
IMAGE_NAME="nommon-kineo-py3"
NAME="nommon-kineo-py3-$LOGNAME"
DOCKERFILE_NAME="DockerFileNommonKineoPy3"
is_number="^[0-9]+"
port="$2"

if [[ $1 == '-i' ]]
then
    if [[ "$(docker images -q $BASE_IMAGE_NAME:latest 2> /dev/null)" == "" ]]; then
      docker build -t "$BASE_IMAGE_NAME" -f "$DOCKERFILES_PATH/$BASE_IMAGE_DOCKERFILE" $DOCKER_BUILD_PATH
    fi
    docker rmi -f "$IMAGE_NAME"
    docker build -t "$IMAGE_NAME" -f "$DOCKERFILES_PATH/$DOCKERFILE_NAME" $DOCKER_BUILD_PATH
elif [[ $1 == '-r' ]]
then
    if ! [[ $port =~ $is_number ]]
    then
            port=8888
    fi
    docker run --name="$NAME" --hostname=$NAME --volume="$(pwd):/opt/shared" -p $port:8888 -it $IMAGE_NAME
elif [[ $1 == '-s' ]]
then
    docker stop "$NAME"
elif [[ $1 == '-d' ]]
then
    docker rm "$NAME"
else
    docker start -i "$NAME"
fi
