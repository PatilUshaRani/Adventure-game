def intro():
    print("Welcome to the Adventure Game!")
    print("You find yourself at the edge of a dark forest.")
    print("Do you want to enter the forest or go back to the village?")
    choice = input("Type 'forest' or 'village': ").lower()
    if choice == 'forest':
        forest_path()
    elif choice == 'village':
        village_path()
    else:
        print("Invalid choice. Try again.")
        intro()

def forest_path():
    print("\nYou enter the forest and hear strange noises.")
    print("You see a cave and a narrow trail leading deeper into the forest.")
    choice = input("Do you enter the 'cave' or follow the 'trail'? ").lower()
    if choice == 'cave':
        cave_adventure()
    elif choice == 'trail':
        trail_adventure()
    else:
        print("Invalid choice. Try again.")
        forest_path()

def village_path():
    print("\nYou return to the village and see people gathered at the square.")
    print("Do you want to 'join' the crowd or go to the 'tavern'?")
    choice = input("Type 'join' or 'tavern': ").lower()
    if choice == 'join':
        print("\nYou join the crowd and witness a festival beginning. You enjoy the rest of your day with music and food. The End!")
    elif choice == 'tavern':
        print("\nAt the tavern, you hear tales of a treasure in the forest. You decide to gather supplies and head out the next day. The adventure continues!")
    else:
        print("Invalid choice. Try again.")
        village_path()

def cave_adventure():
    print("\nInside the cave, you find glittering gems on the walls.")
    print("Suddenly, you hear a growl from deeper inside.")
    choice = input("Do you 'explore' further or 'run' out? ").lower()
    if choice == 'explore':
        print("\nYou bravely walk deeper and discover a sleeping dragon. You sneak past and find a chest of gold! You win!")
    elif choice == 'run':
        print("\nYou run out safely but miss the treasure. Maybe next time!")
    else:
        print("Invalid choice. Try again.")
        cave_adventure()

def trail_adventure():
    print("\nThe trail leads to a peaceful lake.")
    print("You see a boat and a path around the lake.")
    choice = input("Do you take the 'boat' or walk the 'path'? ").lower()
    if choice == 'boat':
        print("\nThe boat takes you to an island where you find a mysterious book of magic. You begin your journey as a wizard!")
    elif choice == 'path':
        print("\nYou walk around and enjoy the beauty of nature. You feel at peace. The End!")
    else:
        print("Invalid choice. Try again.")
        trail_adventure()

# Start the game
intro()
