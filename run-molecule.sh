#! /bin/bash

set -x

source /etc/os-release

DRIVER_ARGS=""

if [[ $ID == "centos" ]] && (( $VERSION_ID > 7)); then
    DRIVER_ARGS="-d podman"
fi

molecule --debug test ${DRIVER_ARGS}
