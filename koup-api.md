functions:

startroom

startgame

joinroom [room]

getplayers [room]



getroomstate [room]



shuffle : private function

getTopCards [room, num=1]

startswap [room] : getTopCards[room,2], setswapping[room, true]

endswap [cards, room] : returnCards[cards, room], setswapping[room, false]

returnCards [cards, room]

deleteRooms [pwd]



Universe:

id

foreign_key: room



Room:

id

player_cap

players: foreign key

cards

status

swapping

max_idle_time

last_update



Players:

id

hand: {card array}

