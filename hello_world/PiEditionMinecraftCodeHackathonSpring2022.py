from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time
import random

mc.postToChat("Welcome to the MAZE by team camelCase.")
mc.postToChat("Destroy the gold block at the end of the maze to reveal the secret message.")

# print the player postion in the game:
pos = mc.player.getPos()
ogx = int(pos.x)
ogy = int(pos.y)
ogz = int(pos.z)
print('x= ', ogx,'y= ', ogy,'z= ', ogz)

#lapis lazuli structure
mc.setBlocks(ogx - 50, ogy - 9, ogz + 1, ogx + 50, ogy + 10, ogz + 81, 22)

#glowstone pattern
def sortPair(val1, val2):
    if val1 > val2:
        return val2, val1
    else:
        return val1, val2

x1, x2 = ogx - 50, ogx + 51
y1, y2 = ogy - 9, ogy + 11
z1, z2 = ogz + 1, ogz + 82

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

def buildJunction(x, y, z):
    #hollowing out space for tunnels
    #start tunnel
    mc.setBlocks(x - 1, y, z + 1, x + 1, y + 3, z + 1, 0)
    mc.setBlocks(x - 1, y + 1, z + 2, x + 1, y + 4, z + 2, 0)
    mc.setBlocks(x - 1, y + 2, z + 3, x + 1, y + 4, z + 7, 0)
    mc.setBlocks(x, y + 2, z + 8, x, y + 4, z + 9, 0)
    #question chamber
    mc.setBlocks(x - 2, y, z + 9, x + 2, y + 2, z + 9, 0)
    mc.setBlocks(x - 1, y, z + 10, x + 1, y + 1, z + 10, 0)
    #side passages
    mc.setBlocks(x + 3, y - 1, z + 9, x + 4, y + 1, z + 9, 0)
    mc.setBlocks(x - 3, y - 1, z + 9, x - 4, y + 1, z + 9, 0)
    
    mc.setBlocks(x + 4, y - 2, z + 8, x + 8, y, z + 10, 0)
    mc.setBlocks(x - 4, y - 2, z + 8, x - 8, y, z + 10, 0)
    
    mc.setBlocks(x + 8, y - 1, z + 8, x + 9, y + 1, z + 10, 0)
    mc.setBlocks(x - 8, y - 1, z + 8, x - 9, y + 1, z + 10, 0)
    
    mc.setBlocks(x + 9, y, z + 8, x + 11, y + 2, z + 10, 0)
    mc.setBlocks(x - 9, y, z + 8, x - 11, y + 2, z + 10, 0)
    
def buildDoomPit(x, y, z):
    #start tunnel
    mc.setBlocks(x - 1, y, z + 1, x + 1, y + 3, z + 1, 0)
    mc.setBlocks(x - 1, y + 1, z + 2, x + 1, y + 4, z + 2, 0)
    mc.setBlocks(x - 1, y + 2, z + 3, x + 1, y + 4, z + 7, 0)
    mc.setBlocks(x, y + 2, z + 8, x, y + 4, z + 10, 0)
    
    #pit of doom
    mc.setBlocks(x - 1, y + 1, z + 9, x + 1, -64, z + 11, 0)

def buildPuzzleHall(x, y, z):
    #start tunnel
    mc.setBlocks(x - 1, y, z, x + 1, y + 2, z + 11, 0)
    
    #diamond pedestal
    mc.setBlock(x, y - 1, z + 11, 57)
    
    #gold block
    mc.setBlock(x, y, z + 11, 41)

treasure_blocks = [16, 15, 14, 73, 74, 21, 57, 89, 89, 89, 89, 89]

def buildTreasureRoom(x, y, z):
    startx = x - 15
    starty = y - 2
    startz = z + 9
    
    for xxx in range(0, 31):
        for yyy in range(0, 20):
            for zzz in range(0, 32):
                i = random.randint(0,11)
                block = treasure_blocks[i]
                mc.setBlock(startx + xxx, starty + yyy, startz + zzz, block)
                zzz += 1
            yyy += 1
        xxx += 1
    
    mc.setBlocks(x - 14, y, z + 10, x + 14, y + 15, z + 38, 0)
    
xrn, yrn, zrn = ogx, ogy, ogz

buildJunction(xrn, yrn, zrn)

xrn -= 10
zrn += 10

buildJunction(xrn, yrn, zrn)

xrn += 10
zrn += 10

buildJunction(xrn, yrn, zrn)

xrn += 10
zrn += 10

buildJunction(xrn, yrn, zrn)

xrn -= 10
zrn += 10

buildJunction(xrn, yrn, zrn)

xrn += 10
zrn += 10

buildPuzzleHall(xrn, yrn, zrn)

zrn += 11

x_x, y_y, z_z = xrn, yrn, zrn

buildTreasureRoom(xrn, yrn, zrn)

xrn, yrn, zrn = ogx + 10, ogy, ogz + 10

buildDoomPit(xrn, yrn, zrn)

xrn -= 30
zrn += 10

buildDoomPit(xrn, yrn, zrn)

xrn += 10
zrn += 10

buildDoomPit(xrn, yrn, zrn)

xrn += 30
zrn += 10

buildDoomPit(xrn, yrn, zrn)

xrn -= 30
zrn += 10

buildDoomPit(xrn, yrn, zrn)

while True:
    gift = mc.getBlock(x_x, y_y, z_z)
    if gift == 0:
        mc.postToChat("Here is your secret ROT13 message:  'Cynpr na veba oybpx ba gur crqrfgny gb erirny gur frperg qbbe.'  Hint: Google 'ROT13 decoder'")
    elif gift == 42:
        mc.setBlocks(x_x + 1, y_y, z_z + 1, x_x + 1, y_y + 1, z_z + 50, 0)
        mc.setBlocks(x_x + 1, y_y, z_z + 50, x_x + 1, y_y + 100, z_z + 50, 0)
        mc.postToChat("Congratulations!  You made it through the maze and into the Cave of Wonders!")
        time.sleep(15)
        mc.setBlock(x_x, y_y, z_z, 41)
        mc.setBlocks(x_x + 1, y_y, z_z + 1, x_x + 1, y_y + 1, z_z + 9, 22)
        mc.setBlocks(x_x + 1, y_y, z_z + 50, x_x + 1, y_y + 100, z_z + 50, 0)