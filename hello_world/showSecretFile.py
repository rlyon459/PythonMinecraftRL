secretFile = open("/home/pi/hello_world/toDoFile.txt", "r")

print(secretFile.read())
secretFile.close()