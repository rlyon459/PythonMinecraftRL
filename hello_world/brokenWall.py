from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random

def brokenBlock():
    brokenBlocks = [48, 67, 4, 4, 4, 4]
    block = random.choice(brokenBlocks)
    return block

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

brokenWall = []
temporaryList = []
height, width = 5, 10

for i in range(height):
    for i in range(width):
        currentBlock = brokenBlock()
        temporaryList.append(currentBlock)
    brokenWall.append(temporaryList)
    temporaryList = []

for row in brokenWall:
    for block in row:
        mc.setBlock(x + 1, y, z, block)
        x += 1
    y += 1
    x = pos.x