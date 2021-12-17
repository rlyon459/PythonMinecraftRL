from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def melon():
    """ Returns the value of the melon block """
    return 103

def water():
    return 8

def lava():
    return 11

def tnt():
    return 46

def flower():
    return 38

def diamondBlock():
    return 57

block = melon()
pos = mc.player.getTilePos()
mc.setBlock(pos.x, pos.y, pos.z, block)