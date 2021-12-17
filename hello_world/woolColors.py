def getWoolState(color):
    """take a color as a string and returns the wool block state for
        that color"""
    if color == "pink":
        blockState = 6
        
    elif # add elif statements for the other colors # Return the blockState here
    
    
colorstring = input("enter a block:")
state = getWoolState(colorString)

pos = mc.playergetTilePos()
mc.setBlock(pos.x, pos.y, pos.z, 35, state)wool