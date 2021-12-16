from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

def placeMelon(x, y, z):
    pos = mc.player.getPos()
    mc.setBlock(x, y - 1, z, 103)
    time.sleep(10)

for i in range(6):
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
    placeMelon(x, y, z)