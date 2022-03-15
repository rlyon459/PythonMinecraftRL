from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import shelve

def buildStructure(x, y, z, structure):
    xStart = x
    zStart = z
    for row in structure:
        for column in row:
            for block in column:
                mc.setBlock(x + 1, y, z, block)
                z += 1
            x += 1
            z = zStart
        y += 1
        x = xStart

# Open and load the structure file
structureDictionary = shelve.open("structuresFile.db")
structureName = input("Enter the structure's name: ")

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

buildStructure(x, y, z, structureDictionary[structureName])
structureDictionary.close()