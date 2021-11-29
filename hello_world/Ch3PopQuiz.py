import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

width = 15
height = 10
depth = 10
blockType = 103

mc.setBlocks(x, y, z+1, x + width, y + height, z + depth + 1, blockType)
mc.setBlocks(x + 1, y + 1, z+2, x + width - 1, y + height - 1, z + depth, 0)