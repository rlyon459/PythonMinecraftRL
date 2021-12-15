from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    userInput = input("enter a command:")
    if userInput == "exit":
        break
    mc.postToChat(userInput)
mc.postToChat("loop exited")