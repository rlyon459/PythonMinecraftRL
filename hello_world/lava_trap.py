import mcpi.minecraft as minecraft
import mcpi.block as block
from time import sleep

mc = minecraft.Minecraft.create()
mc.postToChat("welcome to theLAVATrap")

sleep(3)
pos = mc.player.getTilePos()
mc.setBlocks(pos.x - 5, pos.y - 2, pos.z - 5,
             pos.x + 5, pos.y - 2, pos.z + 5,
             block.STONE.id)
mc.setBlocks(pos.x - 5, pos.y - 1, pos.z - 5,
             pos.x + 5, pos.y - 1, pos.z + 5,
             block.LAVA.id)

mc.setBlock(pos.x, pos.y - 1, pos.z, block.DIAMOND_BLOCK.id)
