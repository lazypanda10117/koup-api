#!/usr/bin/env bash
BUILD_TYPE=$(python3 ./scripts/build.py)
if [[ ${BUILD_TYPE} = "Init" ]];
then
    echo "Build Type: ${BUILD_TYPE} "
    echo "Building from Scratch"
    $(make prod-init)
elif [[ ${BUILD_TYPE} = "Update" ]];
then
    echo "Build Type: ${BUILD_TYPE} "
    echo "Building from Existing Migration"
    $(make prod-update)
elif [[ ${BUILD_TYPE} = "Run" ]];
then
    echo "Build Type: ${BUILD_TYPE} "
    echo "Running Program"
    $(make prod-run)
else
    echo "Build Type: ${BUILD_TYPE} Does Not Exist. Resolving to Default Action"
    echo "Running Program"
    $(make prod-run)
fi