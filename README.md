# ddbot
A bot, created for the Impressive Title server 'Dragon's Den' - a better solution for finding items that are dropped by enemies ingame.


### What is Dragon's Den?
Dragon's Den is an Impressive Title server that was released in 2012. Based off of original game, Impressive Title, it runs on the same engine and same technology created on Impressive Title's initial release - with some security modifications and plenty of content. 

### Why this bot?
The main premise of Dragon's Den is to hunt creatures and collect the items that they drop, usually to accessorize your character or give them stat boosts for hunting larger, more lucrative creatures. Dragon's Den currently runs on the operation of using a large list for players to search through manually, which I felt is too tedious. As a result, I created this bot! Which not only searches for where prey spawn in which location in the game, but also will find which item drop from which prey - or even return a list of items that drop from a specified prey! The bot also includes a few fun minigames.

### Can I use this?
Sure! If you want to use this for your own Impressive Title server, simply implement the following:

A settings.json file that contains a value of 'Key' with your Discord bot's API key.
Replace the droplist.json and and spawnlist.json with a .json formatted file of both a drop list and map spawn lists respectively.
