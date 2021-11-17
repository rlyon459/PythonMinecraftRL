#Connect to Minecraft
#Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

#Set x, y, and z variables to represent coordinates
x = 10
y = 110
z = 12

#Change the players's position
mc.player.setTilePos(x, y, z)

#Wait 10 seconds
time.sleep(10)

#Set x, y, and z variables to represent coordinates
x = 20
y = 100
z = -5

#Change the players's position
mc.player.setTilePos(x, y, z)