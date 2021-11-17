import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

while True:
    p = mc.player.getTilePos()
    mc.setBlock(p.x, p.y, p.z, block.DIAMOND_BLOCK)
    for hit in mc.events.pollBlockHits():
        mc.setBlock(hit.pos.x, hit.pos.y, hit.pos.z, block.DIAMOND_BLOCK)
   