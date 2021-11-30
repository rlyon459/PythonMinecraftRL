from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 10
y = 11
z = 12
melon = 103
block = mc.getBlock(x, y, z)

noMelon = # check the block is not a melon

mc.postToChat("you need to get some food:" + str(noMelon))
