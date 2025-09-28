PWD=$(pwd)
SERVERDIR="${PWD}/server"

mkdir bepinex
mkdir server

sudo add-apt-repository -y multiverse 
sudo apt update
echo steam steam/question select "I AGREE" | sudo debconf-set-selections
sudo apt install steamcmd unzip
steamcmd +force_install_dir "${SERVERDIR}" +login anonymous +app_update 3930080 validate +quit
wget -O "./bepinex/BepInEx_linux_x64_5.4.23.3.zip" "https://github.com/BepInEx/BepInEx/releases/download/v5.4.23.3/BepInEx_linux_x64_5.4.23.3.zip"

cp -r ./server/linux64/* ./server -f
unzip -o "./bepinex/BepInEx_linux_x64_5.4.23.3.zip" -d "./bepinex/"

rm "./bepinex/BepInEx_linux_x64_5.4.23.3.zip"

cp -a "./bepinex/." "./server/" -f
cp -a "./mods/." "./server/BepInEx/" -f

mkdir ./server/replays

python3 ./DedicatedServerConfig.py

chmod +x ./server/run_bepinex.sh
