import json
import os
from glob import glob
from os import path

subdir = "missions"
abs_path_missions = os.path.abspath(subdir)


SERVER_MISSIONDIR = str(abs_path_missions)
SERVER_MODDED = "true"
SERVER_NAME = "SERVER NAME"
SERVER_PORT_ISOVERRIDE = "true"
SERVER_PORT_VALUE = "7777"
SERVER_QUERYPORT_ISOVERRIDE = "true"
SERVER_QUERYPORT_VALUE = "7778"
SERVER_PASSWORD = "SERVER PASSWORD"
SERVER_MAXPLAYERS = "16"
SERVER_NOPLAYERSTOPTIME = "30.0"
SERVER_ROTATIONTYPE = "0"

SERVER_MISSION_MAXTIME = "28800.0"

missions = [f for f in os.listdir("missions") if os.path.isdir(os.path.join("missions", f))]

missionRotation = []
for mission in missions:
    m = {"Key": {"Group":"User","Name":mission},"MaxTime":SERVER_MISSION_MAXTIME}
    missionRotation.append(m)
jsonRot = json.dumps(missionRotation)

file_path = path.relpath("ConfigTemplate.json")
file = open(file_path)
contents = file.read()
file.close()

contents = contents.replace('SERVER_MISSIONDIR', SERVER_MISSIONDIR)
contents = contents.replace('SERVER_MODDED', SERVER_MODDED)
contents = contents.replace('SERVER_NAME', SERVER_NAME)
contents = contents.replace('SERVER_PORT_ISOVERRIDE', SERVER_PORT_ISOVERRIDE)
contents = contents.replace('SERVER_PORT_VALUE', SERVER_PORT_VALUE)
contents = contents.replace('SERVER_QUERYPORT_ISOVERRIDE', SERVER_QUERYPORT_ISOVERRIDE)
contents = contents.replace('SERVER_QUERYPORT_VALUE', SERVER_QUERYPORT_VALUE)
contents = contents.replace('SERVER_PASSWORD', SERVER_PASSWORD)
contents = contents.replace('SERVER_MAXPLAYERS', SERVER_MAXPLAYERS)
contents = contents.replace('SERVER_NOPLAYERSTOPTIME', SERVER_NOPLAYERSTOPTIME)
contents = contents.replace('SERVER_ROTATIONTYPE', SERVER_ROTATIONTYPE)
contents = contents.replace('SERVER_MISSIONROTATION', ('"MissionRotation"' + ":" + str(missionRotation).replace("'",'"')))

file_path = path.relpath("server/DedicatedServerConfig.json")
outFile = open(file_path, "w")
for line in contents:
    outFile.write(line)
outFile.close()

file_path = path.relpath("server/run_bepinex.sh")
bepinexLaunchFile = open(file_path)
bepinexLaunchFileContents = bepinexLaunchFile.read()
bepinexLaunchFile.close()
bepinexLaunchFileContents = bepinexLaunchFileContents.replace('executable_name=""','executable_name="NuclearOptionServer.x86_64"')
outFile = open(file_path, "w")
for line in bepinexLaunchFileContents:
    outFile.write(line)
outFile.close()

replaysdir = "server/replays"
abs_path_replays = os.path.abspath(replaysdir)
print(abs_path_replays)

file_path = path.relpath("server/BepInEx/config/xyz.KopterBuzz.NOBlackBox.cfg")
file = open(file_path)
contents = file.read()
contents = contents.replace("SERVER_OUTPUTPATH",str(abs_path_replays + "/"))
file.close()
file = open(file_path,"w")
for line in contents:
    file.write(line)
file.close()


