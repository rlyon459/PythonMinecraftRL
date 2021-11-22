from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

height = 2
blockType = 1
# Spire sides: should be same as height
sideHeight = height
mc.setBlocks(x + 1, y, z + 1, x + 3, y + sideHeight -1, z + 3, blockType)
# Spire point: should be two times the height
pointHeight = 4
mc.setBlocks(x + 2, y, z + 2, x + 2, y + pointHeight - 1, z + 2, blockType)
#Spire base: should be half the height
baseHeight = 1
mc.setBlocks(x, y, z, x + 4, y + baseHeight - 1, z + 4, blockType)