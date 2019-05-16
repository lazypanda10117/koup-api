[![Codacy Badge](https://api.codacy.com/project/badge/Grade/7c63178850504375b6ba0dac6314ac0c)](https://app.codacy.com/app/jeffreykam0415/koup-api?utm_source=github.com&utm_medium=referral&utm_content=lazypanda10117/koup-api&utm_campaign=Badge_Grade_Dashboard)
# API for Koup (@stevenw47) [![Build Status](https://travis-ci.org/lazypanda10117/koup-api.svg?branch=master)](https://travis-ci.org/lazypanda10117/koup-api)

\
Demo Link: [https://koup-api.herokuapp.com/](https://koup-api.herokuapp.com/)

\
__What is Koup?__ 

It is a replica of the boardgame Coup.

\
\
__Brief Description of API:__

GraphQL Endpoint
```bash
/graphql
```
More details in [documentation](./docs/GraphQL_API.md)
\
\
\
Setup Endpoint (For Setting Up the Service)
```bash
/setup
```
\
\
Housekeeping Endpoints (For Purging Expired Rooms)
```bash
# Clear rooms that has last_updated time over 'minutes'

/housekeeping/purge/<int: minutes>
```
```bash
# Dynamically clear rooms that has last_updated time over the max_idle_minutes defined by the room

/housekeeping/purge/dynamic
```
