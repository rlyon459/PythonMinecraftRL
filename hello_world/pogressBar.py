from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

pos = mc.player.getTilePos()
x = pos.x + 1
y = pos.y
z = pos.z

blocks = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
barBlock = 22

count = 0
while count <= len(blocks):
    
    mc.setBlock(x, y, z, blocks[0])
    mc.setBlock(x, y + 1, z, blocks[1])
    mc.setBlock(x, y + 2, z, blocks[2])
    mc.setBlock(x, y + 3, z, blocks[3])
    mc.setBlock(x, y + 4, z, blocks[4])
    mc.setBlock(x, y + 5, z, blocks[5])
    mc.setBlock(x, y + 6, z, blocks[6])
    mc.setBlock(x, y + 7, z, blocks[7])
    mc.setBlock(x, y + 8, z, blocks[8])
    mc.setBlock(x, y + 9, z, blocks[9])
    
    count += 1
    
    blocks.remove(blocks[9])
    
    blocks.insert(0, barBlock)
    
    time.sleep(2)