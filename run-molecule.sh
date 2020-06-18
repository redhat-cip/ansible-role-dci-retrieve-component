#! /bin/bash

source /etc/os-release

DRIVER_ARGS=""

if [[ $DISTRO == "centos" ]] && (( $VERSION > 7)); then
    DRIVER_ARGS="--driver=podman"
fi

molecule test $DRIVER_ARGS
