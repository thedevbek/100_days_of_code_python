print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("You are at a cross road. Where do you want to go? Type 'left' or 'right'\n").lower()

if direction == "left":
    wait = input("After taking the left path, you have found a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    if wait == "wait":
        door = input("You arrive at the island unharmed. There is a house with three doors. One red, one yellow, and one blue. Which color do you choose? Type 'red', 'yellow', or 'blue'\n").lower()
        if door == "red":
            print("You open the red door and are burned by fire. Game Over.")
        elif door == "blue":
            print("You open the blue door and are eaten by beasts. Game Over.")
        elif door == "yellow":
            print("You open the yellow door and find the treasure! You win!")
        else:
            print("You didn't choose a door. Game Over.")
    else:
        print("While trying to swim across the lake you were attacked by a trout. Game Over.")
else:
    print("After walking for a few steps you fall into a hole. Game Over.")
