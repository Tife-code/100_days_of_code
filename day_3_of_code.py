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
 _________|___________| ;`-.o`"=._; ." ` '`.".` . "-._ /_______________|_______
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

print("Welcome to Treasure Island. \nYour mission is to find the treasure!")
response = input("Are you ready?(yes or no): ")
if response.lower() == "yes":
    print("Leet's Goooooo!")
    #the game begins
    game_choice1 = input("After walking 2miles, You have reached a cross road. Do you want to go left/right? ")
    if game_choice1.lower() == "left":
        print("You reached a lake.")
        game_choice2 = input("Do you want to swim / wait? ")
        if game_choice2.lower() == "wait":
            print("You waited for the boat! You're almost there!")
            game_choice3 = input("You've entered a castle with three doors. Your treasure awaits behind one of these doors. Which will you enter(Red, Blue and Yellow)? ")
            if game_choice3.lower() == "yellow":
                print("YOU WIN! you've found your treasure! Congratulations.")
            elif game_choice3.lower() == "red":
                print("ouch! you entered a room filled with booby traps")
            else:
                print("GEZZZZZZZ! you've been electrocuted!")
        else:
            print("Snap! Theres's a crocodile in here and it just snapped your head off")
                
    else:
        print("Oops! You just fell through the tunnel that exits Treasure Island. Come back soon!")

else:
    print("Please exit Treasure Island")

