from mcpi.minecraft import Minecraft
mc = Minecraft.create()


buildX = 111.1
buildY = 27.8
buildZ = 12.0
width = 10
height = 5
length = 6

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
inside = buildX < x < buildX + width and buildY < y < buildY + height and buildZ < z < buildZ + length
mc.postToChat("inside" + str(inside))