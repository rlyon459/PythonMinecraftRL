from mcpi.minecraft import Minecraft
mc =  Minecraft.create()

x = 20
y = 50
z = 12

mc.player.setPos(x,y,z)
pos = mc.player.getPos()
mc.postToChat("Place an offering on the pedestal.")
gift = mc.getBlock(x, y, z)
if gift == 57:
    mc.setBlocks(x, y+1, z-1, x, y+2, z-1, 0)
else:
    mc.setBlock(pos.x, pos.y, pos.z, 10)