secretFile = open("secretFile.txt", "r")

print(secretFile.readline())
print(secretFile.readline())
print(secretFile.readline())

secretFile.close()