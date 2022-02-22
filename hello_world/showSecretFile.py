secretFile = open("/home/pi/hello_world/secretFile.txt", "r")

print(secretFile.read())
secretFile.close()