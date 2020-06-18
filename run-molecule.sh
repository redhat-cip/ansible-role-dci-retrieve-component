#! /bin/bash

set -x

source /etc/os-release

cat /etc/os-release

DRIVER_ARGS=""


if [[ $ID == "centos" ]] && (( $VERSION_ID > 7)); then
    DRIVER_ARGS="--driver=podman"
    echo "Using podman driver"
fi

molecule test ${DRIVER_ARGS}
