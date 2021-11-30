from mcpi.minecraft import Minecraft
mc = Minecraft.create()

buildX = 91.3
buildY = 24.0
buildZ = -11.6
width = 10
height = 5
length = 6
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

inside = buildX < x < buildX + width and buildY < y < buildY + width and buildZ < z < buildZ + width
mc.postToChat("im inside the bulding" + str(inside))
