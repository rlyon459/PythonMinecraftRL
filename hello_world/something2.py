from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getPos()

mc.setBlock(pos.x + 2, pos.y + 1, pos.z, 8)