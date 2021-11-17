import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
mc.postToChat("Psalm Rules AND so does Ricky")

pos = mc.player.getPos()
x, y, z = mc.player.getPos()
mc.player.setPos(0, 100, 0)