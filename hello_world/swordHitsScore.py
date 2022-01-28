from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

name = ""
scoreboard = {}

while True:
    # Get the player's name
    name = input("what is your name?")
    
    # Break loop if name is exit
    if name == "exit":
        break
    mc.postToChat("Go!")
    
    #wait 60 seconds
    time.sleep(10)
    
    #get the list of block hits
    blockHits = mc.events.pollBlockHits()
    
    #display the length of the block hits list to chat
    blockHitsLength = len(blockHits)
    mc.postToChat("Your score is " + str(blockHitsLength))
    
    # Add the player to the scoreboard
    scoreboard[name] = blockHitsLength
    
    # Display the scoreboard
    print(scoreboard)