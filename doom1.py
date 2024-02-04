#Name: Hamza Siddiqui
#UCID: 30183881
#Tutorial 10

"""
Version of the program: Python 3.10.7

This is a game that enables the player to slect a certain combination of the silver and golden lock
from the kitchen and pantry to be able to unlock the inner door of the house 
"""



NO_SELECTION = 5


goldLockStatus = "center"
silverLockStatus = "left"

playerSelection = "entrance"
victory = "FALSE"
while (victory =="FALSE"):
    #This section of code is where player will start and return to when the player presses "n". This part refers to the "entrance" to the house
    #It allows player to pick from the 3 options to go to the kitchen, pantry or open door
    while (playerSelection == "entrance"):
        print("You are in the entrance right now. The door that you came from has dissapeared.\n" "Your goal is to unlock the inner door of the house which is locked.\n" "In front of you is the inner door that leads to the rest of the house. \n To your left is the pantry. To your right is the kitchen.\n" "You must set the locks in the pantry and kitchen to the correct positions to \n unlock inner door ")


        print("Room actions:")
        print("(l)eft to pantry")
        print("(r)ight to kitchen")
        print("(o)pen door")

        playerSelection = str(input("Please select the following options: "))
#If player mistypes and chooses an option other than what is listed, it will prompt the user again to select the correct option
        while (playerSelection not in ("l", "L", "r", "R", "o", "O")):
            print("Please enter one of 'l', 'r', or 'o' ")
            playerSelection = str(input("Please select the following options: "))
#Player will arrive at pantry and will be able to select the lock postion when chosen from one of the options listed below
#If correct option isnt chosen then it will prompt the user to select the correct option again
        while ((playerSelection == "l") or (playerSelection == "L")):
            print("You are in pantry. The silver lock position is to the", silverLockStatus)

            print("Press (l) to turn the silver lock to the left position")
            print("Press (r) to turn the silver lock to the right position")
            print("Press (c) to turn the silver lock to the center position")
            print("Press (n) to not change it and return to entranceway")
            silverLockSelection = str(input("Select one of the options: "))


            if ((silverLockSelection == "R") or (silverLockSelection == "r")):
                print ("Silver lock position is to the right and is unlocked!")
                silverLockStatus = "right"
            elif ((silverLockSelection == "L") or (silverLockSelection == "l")):
                print("Silver lock position at left")
                
                silverLockStatus = "left"
            elif((silverLockSelection == "C") or (silverLockSelection == "c")):
                print("Silver lock position at center")
                silverLockStatus = "center"
            elif((silverLockSelection == "N") or (silverLockSelection == "n")):
                playerSelection = "entrance"
            else :
                print("Please enter one of 'l', 'r', 'n' or 'C' ")
#Player will arrive at kitchen and will be able to select the lock postion when chosen from one of the options listed below.
#If correct option isnt chosen then it will prompt the user to select the correct option again
        while((playerSelection == "r") or (playerSelection == "R")):
            print("You are in the kitchen. The gold lock position is at the", goldLockStatus)

            print("Press (l) to turn the gold lock to the left position")
            print("Press (r) to turn the gold lock to the right position")
            print("Press (c) to turn the gold lock to the center position")
            print("Press (n) to not change it and return to entranceway")
            goldLockSelection = str(input("Select one of the options: "))


            if ((goldLockSelection == "L") or (goldLockSelection == "l")):
                print ("Gold lock is to the left and is unlocked!")
                goldLockStatus = "left"
            elif ((goldLockSelection == "R") or (goldLockSelection == "r")):
                print("Gold lock posititon at right")
                goldLockStatus = "right"
            elif((goldLockSelection == "C") or (goldLockSelection == "c")):
                print("Gold lock position at center")
                goldLockStatus = "center"
            elif((goldLockSelection == "N") or (goldLockSelection == "n")):
                playerSelection = "entrance"
            else :
                print("Please enter one of 'l', 'r', 'n' or 'c' ")
#If goldlock is at left postion nand silver lock at right postion, then player has won and game will congradulate or else it will repeat the game until player finds the right combination of locks
        while((playerSelection == "o") or (playerSelection == "O")):

            if ((goldLockStatus == "left") and (silverLockStatus == "right")  ):
                print("Congratulations!! Inner door has finally been unlocked")
                playerSelection = NO_SELECTION
                victory ="TRUE"
            else:
                print("Inner door is still locked, keep trying by adjusting the locks")
                playerSelection = "entrance"
                victory = "FALSE"
    
    
    

