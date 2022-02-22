secretFile = open("/home/pi/hello_world/secretFile.txt", "r")

print(secretFile.readline())
print(secretFile.readline())
print(secretFile.readline())

secretFile.close()