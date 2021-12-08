from mcpi.minecraft import Minecraft
mc =  Minecraft.create()

x = 114
y = 2.0
z = 42

mc.player.setPos(x,y,z + 1)
pos = mc.player.getPos()
mc.postToChat("Place an offering on the pedestal.")
gift = mc.getBlock(x, y, z)
if gift != 0:
    if gift == 57:
        mc.setBlocks(x-1, y, z-1, x-1, y+1, z-1, 0)
    else:
        mc.setBlock(pos.x, pos.y, pos.z, 10)