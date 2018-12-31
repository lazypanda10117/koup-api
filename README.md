# API for Koup (@stevenw47)

Demo: https://koup-api.herokuapp.com/

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
