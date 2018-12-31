# API for Koup (@stevenw47)

__What is Koup?__ 

It is a replica of boardgame Coup.

\
\
__Brief Description of API:__

GraphQL endpoint
```bash
/graphql
```
\
Setup endpoint (For Setting Up the Service)
```bash
/setup
```
\
Housekeeping endpoint (For Purging Expired Rooms)
```bash
# Clear rooms that has last_updated time over 'minutes'

/housekeeping/purge/<int: minutes>
```
```bash
# Dynamically clear rooms that has last_updated time over the max_idle_minutes defined by the room

/housekeeping/purge/dynamic
```
