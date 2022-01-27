from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Add locations to the dictionary
places = {'Diamond Ore': (-76, 17, -40), 'Random Place':(69, 69, 69)}

choice = ""
while choice != "exit":
    choice = input("Enter a location ('exit' to close): ")
    if choice in places:
        # Store the dictionary item's value using its key (choice)
        location = places[choice]
        # Store the values stored in the tuple in tyhe x, y, and z variables
        x, y, z = location[0], location[1], location[2]
        mc.player.setTilePos(x, y, z)