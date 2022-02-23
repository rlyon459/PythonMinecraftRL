from mcpi.minecraft import Minecraft
mc = Minecraft.create()

toDoList = open("/home/pi/hello_world/toDoFile.txt", "r")

for line in toDoList:
    mc.postToChat(line)