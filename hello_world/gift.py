from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = 58.7
y = 4.0
z = -10.3
gift = mc.getBlock(x, y, z,)
 #if gift is a diamond block
if gift == 57:
    mc.postToChat("thanks for the diamond")
#else if gift is a sapling
elif gift == 6:
    mc.postToChat("i guess tree saplings are as good as diamonds.....")
else:
    mc.postToChat("Bring a gift to " + str(x) + "," + str(y) + "," + str(z))
    