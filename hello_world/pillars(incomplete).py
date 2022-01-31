from mcpi.minecraft import Minecraft
mc = Minecraft.create()
def setPillar(x, y, z, height):
    """ creates a pillar . Args set position and height of pillar"""
    stairBlock = 156
    block = 155
    #pillar top
    mc.setBlocks(x - 1, y + height, z - 1, x + 1, y + height, z + 1, block, 1)
    mc.setBlock(