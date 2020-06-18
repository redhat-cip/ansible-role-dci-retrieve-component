#! /bin/bash

source /etc/os-release

DRIVER_ARGS=""

if [[ $DISTRO == "centos" ]] && (( $VERSION_ID > 7)); then
    DRIVER_ARGS="--driver=podman"
    echo "Using podman driver"
fi

molecule test ${DRIVER_ARGS}
