#!/usr/bin/env bash
if [ -d ./migrations ]
then
    echo "Building with Existing Migrations"
    $(make prod-update)
else
    echo "Building from Scratch"
    $(make prod-init)
fi