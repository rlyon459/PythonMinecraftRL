from mcpi.minecraft import Minecraft
mc = Minecraf.create()
x = 10
y = 11
z = 12
gift = mc.getBlock(x, y, z,)
 #if gift is a diamond block
if gift == 57
    mc.setBlock(21, 21, 21,)

#else if gift is a sapling
elif mc.setBlock(22, 22, 22,)

else:
    mc.postToChat("Bring a gift to" + str(x) + "," + str(y) + "," + str(z))
    