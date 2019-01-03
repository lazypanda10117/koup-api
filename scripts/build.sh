#!/usr/bin/env bash
if [[ -f .env ]];
then
    BUILD_TYPE=$(grep BUILD_TYPE .env | cut -d '=' -f 2-)
    BUILD_TYPE="${BUILD_TYPE// }"
else
    BUILD_TYPE=$(python3 ./scripts/build.py 1)
fi

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