toDoFile = open("/home/pi/hello_world/toDoFile.txt", "a")

toDoList = ""

toDoItem = input("Enter a to-do list item: ")

while toDoItem != "exit":
    toDoList = toDoList + toDoItem + "\n"
    toDoItem = input("Enter a to-do list item: ")
    
toDoFile.write(toDoList)
toDoFile.close()