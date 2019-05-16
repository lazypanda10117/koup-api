[![Codacy Badge](https://api.codacy.com/project/badge/Grade/7c63178850504375b6ba0dac6314ac0c)](https://app.codacy.com/app/jeffreykam0415/koup-api?utm_source=github.com&utm_medium=referral&utm_content=lazypanda10117/koup-api&utm_campaign=Badge_Grade_Dashboard)
[![Build Status](https://travis-ci.org/lazypanda10117/koup-api.svg?branch=master)](https://travis-ci.org/lazypanda10117/koup-api)

# GraphQL API for Koup 

__What is Koup?__ 

It is a replica of the boardgame Coup. Rules can be found [here](https://upload.snakesandlattes.com/rules/c/CoupTheResistance.pdf)

\
__Some Notes about Koup__: 

The corresponding front-end of Koup is created by [@stevenw47](https://github.com/stevenw47/) and can be found here at [https://github.com/stevenw47/koup](https://github.com/stevenw47/koup). To get the whole Koup app up and running, you will need to build both the front-end from [@stevenw47](https://github.com/stevenw47/)'s repo and the back-end from this repo.

\
__Koup Demo!__ 

  - Koup API Demo: [https://koup-api.herokuapp.com/](https://koup-api.herokuapp.com/)
  - Koup App Demo (Front-end with API calls): [https://stevenw47.github.io/koup/#/](https://stevenw47.github.io/koup/#/)

\
\
__Brief Description of the API:__

GraphQL Endpoint
```bash
/graphql
```
More details in [GraphQL Endpoint documentation](./docs/GraphQL_API.md)

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
