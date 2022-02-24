secretFile = open("/home/pi/hello_world/SecretFile.txt", "r")

print(secretFile.read())
secretFile.close()