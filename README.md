NOServerSetup - Linux server installation tools for Nuclear Option

How to use:

clone this repo to a linux machine

modify the "SERVER_" variables values to your liking

add the mods you want to the mods/plugins folder

by default I have NOBlackBox, JetFox RCON + AntiCheat, senti's SlingLoad Hook Exploit Fix.

also add default config for them if needed, to the mods/config folder

add the missions you want to the missions folder

run install.sh

it will download and install all dependencies required to run a NO server with BepInEx and generate a server config file 

then launch the server with:

cd ./server
./run_bepinex.sh


