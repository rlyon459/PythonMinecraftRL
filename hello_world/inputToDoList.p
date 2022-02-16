toDoFile =

toDoList = ""

toDoItem = input("Enter a to-do List them:")

while toDoItem != "exit":
    toDoList = toDoList + toDoItem + "/n"
    toDoList = input("Enter a to-do List item:")
    
    
#write the to-do list to the file
# Close the file                                                                                                                                                                                                                                                                                                                                                                                                               