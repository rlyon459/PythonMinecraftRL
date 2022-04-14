from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getPos()
startx = pos.x
starty = pos.y
startz = pos.z

print('x= ', startx,'y= ', starty,'z= ', startz)

mc.setBlocks(startx - 50, starty - 9, startz + 1, startx + 50, starty + 10, startz + 81, 638)