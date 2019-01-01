# GraphQL Endpoint

## Room Queries:

> Getting All Rooms
```graphql
query{
  allRooms{
    edges{
      node{
        ... fields ...
        players{
          ... fields ...
        }
      }
    }
  }
}
```


> Getting a Room with Room ID
```graphql
query{
  room(id:<string: room id>){
    room{
      ... fields ...
    }
  }
}
```


> Updating a Room
```graphql
mutation{
  updateRoom(input: {
    id: <string: room id>
    ... fields to change ...
  }){
    room{
      ... fields ...
    }
  }
}
```


> Deleting a Room
```graphql
query{
  deleteRoom(input: {
    id: <string: room id>
  }){
    room{
      ... fields ...
    }
  }
}
```


> Restarting a Room
```graphql
query{
  restartRoom(input: {
    key: <int: room key>
  }){
    room{
      ... fields ...
    }
  }
}
```


## Player Queries:

> Getting All Players
```graphql
query{
  allPlayers{
    edges{
      node{
        ... fields ...
      }
    }
  }
}
```


> Getting a Player with Player ID
```graphql
query{
  player(id:<string: player id>){
    player{
      ... fields ...
    }
  }
}
```


> Updating a Player
```graphql
mutation{
  updatePlayer(input: {
    id: <string: player id>
    ... fields to change ...
  }){
    player{
      ... fields ...
    }
  }
}
```


> Deleting a Player
```graphql
query{
  deletePlayer(input: {
    id: <string: player id>
  }){
    player{
      ... fields ...
    }
  }
}
```


> Player Creating a Room
```graphql
# All fields in input are optional

mutation{
  createRoom(input: {
    playerCap: <int>
    state: <int: 1=waiting, 2=running, 3=rejoining>
    swapping: <bool>
    maxIdleTime: <int>
  }){
    room{
      ... fields ...
    }
  }
}
```


> Player Starting a Room with Room Key (Automatically Creates the Player)
```graphql
mutation{
  startRoom(input:{
    roomKey:<int: corresponding to room key>
  }){
    room{
      ... fields ...
    }
  }
}
```


> Player Joining a Room with Room Key (Automatically Creates the Player)
```graphql
mutation{
  joinRoom(input:{
    roomKey:<int: corresponding to room key>
  }){
    player{
      ... fields ...
    }
  }
}
```


> Player Starting Swap Card
```graphql
mutation{
  swapStart(input:{
    id:<string: player id>
    numCards: <int>
  }){
    player{
      ... fields ...
    }
  }
}
```


> Player Ending Swap Card
```graphql
mutation{
  swapStart(input:{
    id:<string: player id>
    hand: <array[int]: card ids>
  }){
    player{
      ... fields ...
    }
  }
}
```


> Player Reveal Card (Put Card then Get Card)
```graphql
mutation{
  revealCard(input:{
    id:<string: player id>
    hand: <array[int]: card ids>
  }){
    player{
      ... fields ...
    }
  }
}
```


## Card Queries:

> Getting All Cards
```graphql
query{
  allCards{
    edges{
      node{
        ... fields ...
      }
    }
  }
}
```


> Getting a Card with Card ID
```graphql
query{
  card(id:<string: card id>){
    card{
      ... fields ...
    }
  }
}
```


> Updating a Card
```graphql
mutation{
  updateCard(input: {
    id: <string: card id>
    ... fields to change ...
  }){
    card{
      ... fields ...
    }
  }
}
```


> Deleting a Card
```graphql
query{
  deleteCard(input: {
    id: <string: card id>
  }){
    card{
      ... fields ...
    }
  }
}
```
