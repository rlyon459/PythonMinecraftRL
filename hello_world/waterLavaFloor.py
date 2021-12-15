from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

pos = mc.player.getTilePos()
floorX = pos.x - 2
floorY = pos.y - 1
floorZ = pos.z - 2
width = 5
length = 5
block = 8
mc.setBlocks(floorX, floorY-1, floorZ,
             floorX + width, floorY-1, floorZ + length, 1)

mc.setBlocks(floorX, floorY, floorZ,
             floorX + width, floorY, floorZ + length, block)

while True:
    if block == 8:
        block = 11
    else:
        block = 8
    mc.setBlocks(floorX, floorY, floorZ,
                 floorX + width, floorY, floorZ + length, block)
    time.sleep(0.5)
