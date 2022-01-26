from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

#wait 60 seconds
time.sleep(60)

#get the list of block hits
blockHits = mc.events.pollBlockHits()

#display the length of the block hits list to chat
blockHitsLength = len(blockHits)
mc.postToChat("Your score is " + str(blockHitsLength))