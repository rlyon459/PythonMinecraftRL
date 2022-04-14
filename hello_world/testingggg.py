from mcpi.minecraft import Minecraft
mc = Minecraft.create()

mc.postToChat("Hello from Python")

# print the player postion in the game:
pos = mc.player.getPos()
ogx = int(pos.x)
ogy = int(pos.y)
ogz = int(pos.z)
print('x= ', ogx,'y= ', ogy,'z= ', ogz)

#glowstone pattern
def sortPair(val1, val2):
    if val1 > val2:
        return val2, val1
    else:
        return val1, val2

#x1, x2 = ogx - 50, ogx + 51
#y1, y2 = ogy - 9, ogy + 11
#z1, z2 = ogz + 1, ogz + 82

x1, x2 = ogx - 3, ogx + 3 #test
y1, y2 = ogy - 2, ogy + 3 #test
z1, z2 = ogz, ogz + 10 #test

x1, x2 = sortPair(x1, x2)
y1, y2 = sortPair(y1, y2)
z1, z2 = sortPair(z1, z2)
 
width = x2 - x1
height = y2 - y1
length = z2 - z1

for yy in range(height//2):
    for zz in range(length//2):
        for xx in range(width//2):
            mc.setBlock(x1 + xx * 2, y1 + yy * 2, z1 + zz * 2, 89)
            xx += 1
        zz += 1
    yy += 1

