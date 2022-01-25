from mcpi.minecraft import Minecraft
mc = Minecraft.create()


import random
import time

# Get the player position

#set the x, y, and z on the same line using tuple

while True:
    x += random.uniform(-0.2, 0.2)
    #change the z variable by a random float
    z +=
    y = mc.getHeight(x, z)
    
    mc.player.setPos(x, y, z)
    time.sleep(0.1)