from mcpi.Minecraft import Minecraft
mc = Minecraft.create()
 answer = input("create a crater? Y/N")
 #Add an if statement here
 
 pos = mc.player.getPos()
 mc.setBlocks(pos.x + 1, pos.y + 1, pos.z + 1, pos.x - 1, pos.y - 1, pos.z - 1, 0)
 mc.postToChat("Boom!")