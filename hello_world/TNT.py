from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

#crater
#mc.setBlocks(x - 50, y + 50, z - 50, x + 50, -63, z + 50, 0)

#tnt column
mc.setBlocks(x - 1, y - 1, z - 1, x + 1, y - 100, z + 1, 46, 1)

#tnt row
#mc.setBlocks(x - 1, y - 1, z - 1, x + 1, y + 1, z - 100, 46, 1)

#mc.setBlocks(x + 1, y - 1, z - 1, x + 100, y + 1, z + 1, 46, 1)
