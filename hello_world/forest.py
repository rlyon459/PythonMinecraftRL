from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def growTree(x, y, z):
    mc.setBlocks(x, y, z, x, y + 3, z, 17)
    mc.setBlocks(x - 2, y + 4, z - 2, x + 2, y + 4, z + 2, 18)
    mc.setBlocks(x - 1, y + 5, z - 1, x + 1, y + 5, z + 1, 18)

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

for i in range(6):
    growTree(x + 1, y, z)
    
    x += 7