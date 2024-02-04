#Name: Hamza Siddiqui
#UCID: 30183881
#Tutorial 10


"""
Version of the program: Python 3.10.7

This is a game in which the goal of the player is to fertilize the pot fpor the vine to grow and lead player to paradise
"""


CHEESE = "Cheese"
BALLOFSTRING = "Ball of string"

#function purpose is to introduce the player
def introduction(alreadyDroppedBall):
    print("Welcome to this game. Here in the living room you can find a pot,\n a ball of string, stairs leading up to attic and a dark entranceway leading to the bedroom.\n When this pot in fertilised, a vine will grow leading you to paradise.\n There are 3 rooms: Living room, attic, and bedroom.\n There is a mouse in the bedroom that can't come out unless the cat\n watching over it's mouse hole leaves the room.")
    alreadyDroppedBall = False
    return alreadyDroppedBall


#function here is to have the user enter living room, it presents the user to pick up the ball if user doesnt have one only once. This room leads to the bedroom and the attic as well as the ability to view if pot is dry or not 
def livingRoom(InventoryForBall,InventoryForCheese,potIsBeingFertilized, alreadyDroppedBall):

    print("You are currently in the living room.")

    if (InventoryForBall == BALLOFSTRING or alreadyDroppedBall == True ):
        print("Press (A) to go to attic by the stairs going up")
        print("Press (B) to go to Bedroom through dark entranceway")
        print("Press (V) to view pot")
    else:
        print("Press (A) to go to attic by the stairs going up")
        print("Press (B) to go to Bedroom through dark entranceway")
        print("Press (P) to pick up ball of string")
        print("Press (V) to view pot")


    playerSelection = str(input("Please select one of the following options:"))

    if (InventoryForBall == BALLOFSTRING or alreadyDroppedBall == True ):
        while (playerSelection not in ("a", "A", "b", "B", "v", "V")):
            print("Please enter one of 'A', 'B', or 'V' ")
            playerSelection = str(input("Please select one of the following options: "))
    else:
        while (playerSelection not in ("a", "A", "b", "B", "p", "P", "v", "V")):
            print("Please enter one of 'A', 'B', 'P', or 'V' ")
            playerSelection = str(input("Please select one of the following options: "))


    if (playerSelection == "A" or playerSelection == "a"):
        playerSelection = attic(InventoryForBall,InventoryForCheese,alreadyDroppedBall)
    elif(playerSelection == "B" or playerSelection == "b"):
        playerSelection = bedroom(InventoryForBall,InventoryForCheese,potIsBeingFertilized,alreadyDroppedBall)
    elif(playerSelection == "P" or playerSelection == "p" and InventoryForBall != BALLOFSTRING):
        InventoryForBall,playerSelection = pickedUpBallofString(alreadyDroppedBall)
    elif(playerSelection == "v" or playerSelection == "V"):
        if (potIsBeingFertilized != "Yes"):
            print("Pot is dry")
            playerSelection = livingRoom(InventoryForBall,InventoryForCheese,potIsBeingFertilized,alreadyDroppedBall)
        else:
            print("Congradulations!! Pot is fertilized and vine is growing. Hop on and it will take you to paradise!!")

        

    return playerSelection, InventoryForBall,InventoryForCheese

#the attic is where the player can drop the ball thrugh the hole on the floor and pick up cheese.
def attic(InventoryForBall,InventoryForCheese,alreadyDroppedBall):

    print("You are in the attic. Here there is:  A tiny hole in the floor, an unlimited \nsupply of cheese, and stairs going down vto living room ")

    print("Press (C) to pick up cheese (it's unlimited)")
    print("Press (L) to go back down to living room")
    print("Press (H) to aproach hole on the floor")
    print("Press (I) to view Inventory")

    
    playerSelection = str(input("Please select one of the following options: "))

    while (playerSelection not in ("c", "C", "l", "L", "h", "H", "i", "I")):
            print("Please enter one of 'C', 'L', 'H', or 'I' ")
            playerSelection = str(input("Please select one of the following options: "))

    if (playerSelection == "c" or playerSelection == "C"):
        InventoryForCheese = -1
        InventoryForCheese,playerSelection = pickedUpCheese(InventoryForBall,alreadyDroppedBall)
  
    elif (playerSelection == "l" or playerSelection == "L"):
        playerSelection = livingRoom(InventoryForBall,InventoryForCheese,potIsBeingFertilized,alreadyDroppedBall)
        
    elif (playerSelection == "h" or playerSelection == "H"):
        print("There is a hole on the floor, you can see the bedroom where the cat is watching \n over the mousehole\n")
        playerSelection, alreadyDroppedBall = droppingItemsThroughFloor(InventoryForCheese,InventoryForBall)

    elif (playerSelection == "i" or playerSelection == "I"):
        print("Current Inventory: ", end="")
        if (InventoryForCheese != CHEESE):
            print("", end="")
        else:
            print("Cheese, ", end="")

        if(InventoryForBall != BALLOFSTRING):
            print("")
        else:
            print("Ball of string")
        
        playerSelection = attic(InventoryForBall,InventoryForCheese,alreadyDroppedBall)
    
    return InventoryForBall,InventoryForCheese, playerSelection, alreadyDroppedBall\

#bedroom is the place that will allow the user to play with the cat with the ball of string as well as feed the mouse once cat leaves the room

def bedroom(InventoryForBall,InventoryForCheese,potIsBeingFertilized,alreadyDroppedBall):
    
    print("You are in the bedroom. Here you can see a mouse inside mousehole, and a cat watching over the mousehole ")

    print("Press (L) to go back to living room")
    print("Press (I) to view Inventory")
    
    
    if (InventoryForBall == BALLOFSTRING):
        print("Press (P) to use the Ball of string to play with cat")
    else:
        print("Cat has left the room when you threw the ball of string from above")
        print("")
        print("The mouse has finally come out of his mousehole")
        print("Press (L) to return back to living room")

        if(InventoryForCheese == CHEESE):
            print("Press (F) to feed the mouse")
    

    playerSelection = str(input("Please select an option: "))

    if (playerSelection == "p" or playerSelection == "P"):
        print("Cat has breifly looked at you and is stubborn on watching over the moushole")
        playerSelection, potIsFertilized = bedroom(InventoryForBall,InventoryForCheese,potIsBeingFertilized,alreadyDroppedBall)
    elif(playerSelection == "L" or playerSelection == "l"):
        playerSelection = livingRoom(InventoryForBall,InventoryForCheese,potIsBeingFertilized,alreadyDroppedBall)
    elif((playerSelection == "f") or (playerSelection =="F")):
        print("Mouse has been fed , it has left to fertilize the vine plant and has now\n returned back to the room")
        InventoryForCheese = -1
        potIsFertilized, playerSelection = potIsBeingFertilized(InventoryForBall,InventoryForCheese,alreadyDroppedBall)
    elif (playerSelection == "i" or playerSelection == "I"):
        print("Current Inventory: ", end="")
        if (InventoryForCheese != CHEESE):
            print("", end="")
        else:
            print("Cheese, ", end="")

        if(InventoryForBall != BALLOFSTRING):
            print("")
        else:
            print("Ball of string")
    

        
        

    while (playerSelection not in ("p", "P", "L", "l", "f", "F","i", "I")):
            print("Please enter one of 'P', 'L', 'I', or 'F' ")
            playerSelection = str(input("Please select one of the following options: "))

    playerSelection, potIsFertilized = potIsBeingFertilized(InventoryForBall,InventoryForCheese,alreadyDroppedBall)
    
    

    return potIsFertilized,playerSelection,InventoryForCheese
        
    
#Side Functions

#function to fertilize the vine plant
def potIsBeingFertilized(InventoryForBall,InventoryForCheese,alreadyDroppedBall):
    potIsFertilized = -1
    potIsFertilized = "Yes"
    playerSelection = bedroom(InventoryForBall,InventoryForCheese,potIsBeingFertilized,alreadyDroppedBall)
    return potIsFertilized, playerSelection

#Allows user to have ball of string added to inventory     
def pickedUpBallofString(alreadyDroppedBall):
    InventoryForCheese = -1
    InventoryForBall = BALLOFSTRING
    print("Inventory: ", InventoryForBall, "has been added")
    playerSelection = livingRoom(InventoryForBall,InventoryForCheese,potIsBeingFertilized,alreadyDroppedBall)
    return InventoryForBall

#Allows user to pick up cheese
def pickedUpCheese(InventoryForBall,alreadyDroppedBall):
    print("You have picked up big slice of cheese")
    InventoryForCheese = CHEESE  
    print("Inventory: ",InventoryForCheese, "has been added")
    playerSelection = attic(InventoryForBall,InventoryForCheese,alreadyDroppedBall)
    return InventoryForCheese, playerSelection
    
#functions purpose is to drop items of cheese and ball of string through the floor and dispolay the respective responses        
def droppingItemsThroughFloor(InventoryForCheese,InventoryForBall):
    
    print("Drop the Item through the floor \n")
    
    if (InventoryForCheese == CHEESE):
        print("Drop (C)heese")     
    if (InventoryForBall == BALLOFSTRING):
        print("Drop (B)all of string")
    if((InventoryForCheese != CHEESE) and (InventoryForBall != BALLOFSTRING)):
        print("You do not have anything to throw down, go grab something ")
        playerSelection = attic(InventoryForBall,InventoryForCheese)

    print("Press (A) to go back to attic")
        


    playerSelection = str(input("Please select an option: "))

    if (playerSelection == "c" or playerSelection == "C"):
        print("Cheese is too big and can't fit through hole")
        InventoryForCheese = -1
    elif (playerSelection == "b" or playerSelection == "B"):
        print("Ball of string has successfully gone through the hole and had distracted the cat enough to leave the bedroom")
        InventoryForBall = -1
        alreadyDroppedBall = True
    elif (playerSelection == "a" or playerSelection == "A"):
        playerSelection = attic(InventoryForBall,InventoryForCheese,alreadyDroppedBall)


    while (playerSelection not in ("c", "C", "B", "b","a","A")):
        print("Please enter one of 'C' ,'B' or 'A'")
        playerSelection = str(input("Please select the following options: "))

    playerSelection = attic(InventoryForBall,InventoryForCheese,alreadyDroppedBall)

    return InventoryForBall, InventoryForCheese, playerSelection, alreadyDroppedBall
     
        
#calling function
def start():
    playerSelection = -1
    InventoryForBall = -1
    InventoryForCheese = -1
    potIsFertilized = -1
    alreadyDroppedBall = -1
    introduction(alreadyDroppedBall)
    playerSelection,InventoryForCheese,InventoryForBall, = livingRoom(InventoryForBall,InventoryForCheese,potIsBeingFertilized,alreadyDroppedBall)

start()
