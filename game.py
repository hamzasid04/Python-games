#Name: Hamza Siddiqui
#UCID: 30183881
#Tutorial 10

EMPTY = ""
LINE_ENDING = ""
NEW_LINE = "\n"
SPACE = " "
SIZE = 9

'Version 2'

#Playuer can choose one of the 7 options
def menu():
    print("Choices for starting biospheres:")
    print("(1) Empty")
    print("(2) Single critter")
    print("(3) Single birth")
    print("(4) Simple birth")
    print("(5) Edgey testing")
    print("(6) It's a complex world")
    print("(7) Enter in a file that contains your desired biosphere:")
    print("")

    
    playerSelection = input("Selection: ")

    while (playerSelection not in ("1", "2", "3", "4","5","6","7")):
            print("Please select one of the options")
            playerSelection = input("Please select one of the following options: ")

    if (playerSelection == "1"):
        world = oneEmpty()
        #print("IT WORKS")

    elif (playerSelection == "2"):
        world = twoSingleCritter()

    elif (playerSelection == "3"):
        world = threeSingleBirth()
        
    elif (playerSelection == "4"):
        world = fourthSimpleBirth()
        
    elif (playerSelection == "5"):
        world = fifthCreateListEdgeCases()
        
    elif (playerSelection == "6"):
        world = sixthComplexCases()

    elif (playerSelection == "7"):
        world = fileRead()

    return world

# code below is responsible to integrate and run the rules
def applyingTheRules(world,oldWorld,newWorld,turn,fileValid):
    #oldWorld = []
    #fileValid = True
    #world =[]
    
    while (fileValid == True):
        #currentColumn = 0
        #currentRow = 0
        
            
        #while (world[currentColumn] != LINE_ENDING):
            #It will continue checking a column to the row as long as the space isnt encountered.

        #BIRTH

        oldWorld,newWorld,turn = rulesOfBirthAndDeath(world)


                    
                    


                    
                #currentColumn = currentColumn + 1
                    #incrementing +1 to row as it is indneted in accordance to while stement responsible for going to new line

    
# birth of the critter
def birth(world):
# BIRTH
    print(world)
    currentRow = 0
    fileValid = False
    while (currentRow <= 9):
        #print("THIS IS ROW")
        currentColumn = 0
        while (currentColumn <= 9):
            #print("THIS IS THE COLUMN")

            counter = 0
            right = currentColumn + 1
            left = currentColumn - 1
            top = currentRow + 1
            bottom = currentRow - 1
            #TOP LEFT
            if (world[0][0] == " "):
            
                if( right <= SIZE and right >= 0):
                    if (world[right][currentRow] =="*"):
                        counter = counter+1
                if (bottom <= SIZE and bottom >= 0):
                    if (world[currentColumn][bottom] == "*"):
                        counter = counter+1
                if (right <= SIZE and right >= 0 and bottom <= SIZE and bottom >= 0):
                    if (world[right][bottom] == "*"):
                        counter = counter + 1

                if (counter == 3):
                    world[currentColumn][currentRow] = "*" 
            # MIDDLE VERY LEFT
            if (world[0][currentRow] == " "):
                if( right <= SIZE and right >= 0):
                    if (world[right][currentRow] =="*"):
                        counter = counter+1
                if (top <= SIZE and top >= 0):
                    if (world[currentColumn][top] == "*"):
                        counter = counter+1
                if (bottom <= SIZE and bottom >= 0):
                    if (world[currentColumn][bottom] == "*"):
                        counter = counter+1
                if (right <= SIZE and right >= 0 and top <= SIZE and top >=0):
                    if (world[right][top] == "*"):
                        counter = counter +1
                if (right <= SIZE and right >= 0 and bottom <= SIZE and bottom >= 0):
                    if (world[right][bottom] == "*"):
                        counter = counter + 1

                if (counter == 3):
                    world[currentColumn][currentRow] = "*" 

            #BOTTOM LEFT

            if (world[0][9] == " "):


                if( right <= SIZE and right >= 0):
                    if (world[right][currentRow] =="*"):
                        counter = counter+1
                if (top <= SIZE and top >= 0):
                    if (world[currentColumn][top] == "*"):
                        counter = counter+1
                if (right <= SIZE and right >= 0 and top <= SIZE and top >=0):
                    if (world[right][top] == "*"):
                        counter = counter +1

                if (counter == 3):
                    world[currentColumn][currentRow] = "*" 

            #TOP RIGHT

            if (world[9][0]):
                if (left <= SIZE and left >= 0):
                    if (world[left][currentRow] == "*"):
                        counter = counter+1
                if (bottom <= SIZE and bottom >= 0):
                    if (world[currentColumn][bottom] == "*"):
                        counter = counter+1
                if (left <= SIZE and left >= 0 and bottom <= SIZE and left >= 0):
                    if (world[left][bottom] == "*"):
                        counter = counter + 1

                if (counter == 3):
                    world[currentColumn][currentRow] = "*" 

            #MIDDLE VERY RIGHT

            if (world[9][currentRow]):
                if (left <= SIZE and left >= 0):
                    if (world[left][currentRow] == "*"):
                        counter = counter+1
                if (top <= SIZE and top >= 0):
                    if (world[currentColumn][top] == "*"):
                        counter = counter+1
                if (bottom <= SIZE and bottom >= 0):
                    
                    if (world[currentColumn][bottom] == "*"):
                        counter = counter+1
                if (top <= SIZE and top >= 0 and left <= SIZE and left >= 0):
                    if (world[left][top] == "*"):
                        counter = counter +1
                if (left <= SIZE and left >= 0 and bottom <= SIZE and left >= 0):
                    if (world[left][bottom] == "*"):
                        counter = counter + 1
                        

                if (counter == 3):
                    world[currentColumn][currentRow] = "*"

            #BOTTOM RIGHT

            if (world[9][9] == " "):
            
                if (left <= SIZE and left >= 0):
                    if (world[left][currentRow] == "*"):
                        counter = counter+1
                if (top <= SIZE and top >= 0):
                    
                    if (world[currentColumn][top] == "*"):
                        counter = counter+1
                if (top <= SIZE and top >= 0 and left <= SIZE and left >= 0):
                    if (world[left][top] == "*"):
                        counter = counter +1

                if (counter == 3):
                    world[currentColumn][currentRow] = "*" 

            #MIDDLE TOP

            if (world[currentColumn][0]):
                if( right <= SIZE and right >= 0):
                    if (world[right][currentRow] =="*"):
                        counter = counter+1
                if (left <= SIZE and left >= 0):
                    if (world[left][currentRow] == "*"):
                        counter = counter+1
                if (bottom <= SIZE and bottom >= 0):
                    
                    if (world[currentColumn][bottom] == "*"):
                        counter = counter+1
                if (right <= SIZE and right >= 0 and bottom <= SIZE and bottom >= 0):
                    if (world[right][bottom] == "*"):
                        counter = counter + 1
                if (left <= SIZE and left >= 0 and bottom <= SIZE and left >= 0):
                    if (world[left][bottom] == "*"):
                        counter = counter + 1

                if (counter == 3):
                    world[currentColumn][currentRow] = "*" 

            #MIDDLE BOTTOM
            if (world[currentColumn][9]):
                if( right <= SIZE and right >= 0):
                    if (world[right][currentRow] =="*"):
                        counter = counter+1
                if (left <= SIZE and left >= 0):
                    if (world[left][currentRow] == "*"):
                        counter = counter+1
                if (top <= SIZE and top >= 0):
                    
                    if (world[currentColumn][top] == "*"):
                        counter = counter+1
                
                if (right <= SIZE and right >= 0 and top <= SIZE and top >=0):
                    if (world[right][top] == "*"):
                        counter = counter +1
                if (top <= SIZE and top >= 0 and left <= SIZE and left >= 0):
                    if (world[left][top] == "*"):
                        counter = counter +1

                if (counter == 3):
                    world[currentColumn][currentRow] = "*" 

            #MIDDLE OF LIST
            if (world[currentColumn][currentRow] == "*"):
                if( right <= SIZE and right >= 0):
                    if (world[right][currentRow] =="*"):
                        counter = counter+1
                if (left <= SIZE and left >= 0):
                    if (world[left][currentRow] == "*"):
                        counter = counter+1
                if (top <= SIZE and top >= 0):
                    
                    if (world[currentColumn][top] == "*"):
                        counter = counter+1
                if (bottom <= SIZE and bottom >= 0):
                    
                    if (world[currentColumn][bottom] == "*"):
                        counter = counter+1
                if (right <= SIZE and right >= 0 and top <= SIZE and top >=0):
                    if (world[right][top] == "*"):
                        counter = counter +1
                if (top <= SIZE and top >= 0 and left <= SIZE and left >= 0):
                    if (world[left][top] == "*"):
                        counter = counter +1
                if (right <= SIZE and right >= 0 and bottom <= SIZE and bottom >= 0):
                    if (world[right][bottom] == "*"):
                        counter = counter + 1
                if (left <= SIZE and left >= 0 and bottom <= SIZE and left >= 0):
                    if (world[left][bottom] == "*"):
                        counter = counter + 1

                if (counter == 3):
                    world[currentColumn][currentRow] = "*" 

            



                
                
            
            currentColumn = currentColumn + 1
        currentRow = currentRow + 1

        if(len(world) == 81):
            fileValid = False

    return fileValid



#death of the critter by lonliness
def deathLonely(world):
# DEATH
    #print(world)
    currentRow = 0
    fileValid = False
    while (currentRow <= 9):
        #print("THIS IS ROW FOR DEATH by lonliness")
        currentColumn = 0
        while (currentColumn <= 9):
            #print("THIS IS THE COLUMN FOR DEATH by loneliness")

            emptySpaces = 0
            spaceFilled = 0
            right = currentColumn + 1
            left = currentColumn - 1
            top = currentRow - 1
            bottom = currentRow + 1

        #WHEN TOO LONELY
            #TOP LEFT
            if (world[0][0] == "*"):
            
                if( right <= SIZE and right >= 0):
                    if (world[right][currentRow] ==" "):
                        emptySpaces = emptySpaces+1

                if (bottom <= SIZE and bottom >= 0):
                    
                    if (world[currentColumn][bottom] == " "):
                        emptySpaces = emptySpaces+1
                if (right <= SIZE and right >= 0 and bottom <= SIZE and bottom >= 0):
                    if (world[right][bottom] == " "):
                        emptySpaces = emptySpaces + 1

                if (emptySpaces <= 1):
                    world[currentColumn][currentRow] = " "
            # MIDDLE VERY LEFT
            if (world[0][currentRow] == "*"):
                if( right <= SIZE and right >= 0):
                    if (world[right][currentRow] ==" "):
                        emptySpaces = emptySpaces+1
                if (top <= SIZE and top >= 0):
                    
                    if (world[currentColumn][top] == " "):
                        emptySpaces = emptySpaces+1
                if (bottom <= SIZE and bottom >= 0):
                    
                    if (world[currentColumn][bottom] == " "):
                        emptySpaces = emptySpaces+1
                if (right <= SIZE and right >= 0 and top <= SIZE and top >=0):
                    if (world[right][top] == " "):
                        emptySpaces = emptySpaces +1
                if (right <= SIZE and right >= 0 and bottom <= SIZE and bottom >= 0):
                    if (world[right][bottom] == " "):
                        emptySpaces = emptySpaces + 1

                if (emptySpaces <= 1):
                    world[currentColumn][currentRow] = " "
                

            #BOTTOM LEFT

            if (world[0][9] == "*"):

                if( right <= SIZE and right >= 0):
                    if (world[right][currentRow] ==" "):
                        emptySpaces = emptySpaces+1

                if (top <= SIZE and top >= 0):
                    
                    if (world[currentColumn][top] == " "):
                        emptySpaces = emptySpaces+1

                if (right <= SIZE and right >= 0 and top <= SIZE and top >=0):
                    if (world[right][top] == " "):
                        emptySpaces = emptySpaces +1

                if (emptySpaces <= 1):
                    world[currentColumn][currentRow] = " "

            #TOP RIGHT

            if (world[9][0] == "*"):

                if (left <= SIZE and left >= 0):
                    if (world[left][currentRow] == " "):
                        emptySpaces = emptySpaces+1

                if (bottom <= SIZE and bottom >= 0):
                    
                    if (world[currentColumn][bottom] == " "):
                        emptySpaces = emptySpaces+1

                if (left <= SIZE and left >= 0 and bottom <= SIZE and left >= 0):
                    if (world[left][bottom] == " "):
                        emptySpaces = emptySpaces + 1

                if (emptySpaces <= 1):
                    world[currentColumn][currentRow] = " "

            #MIDDLE VERY RIGHT

            if (world[9][currentRow] == "*"):
                if (left <= SIZE and left >= 0):
                    if (world[left][currentRow] == " "):
                        emptySpaces = emptySpaces+1
                if (top <= SIZE and top >= 0):
                    
                    if (world[currentColumn][top] == " "):
                        emptySpaces = emptySpaces+1
                if (bottom <= SIZE and bottom >= 0):
                    
                    if (world[currentColumn][bottom] == " "):
                        emptySpaces = emptySpaces+1
                if (top <= SIZE and top >= 0 and left <= SIZE and left >= 0):
                    if (world[left][top] == " "):
                        emptySpaces = emptySpaces +1

                if (left <= SIZE and left >= 0 and bottom <= SIZE and left >= 0):
                    if (world[left][bottom] == " "):
                        emptySpaces = emptySpaces + 1

                if (emptySpaces <= 1):
                    world[currentColumn][currentRow] = " "

            #BOTTOM RIGHT

            if (world[9][9] == "*"):
            
                if (left <= SIZE and left >= 0):
                    if (world[left][currentRow] == " "):
                        emptySpaces = emptySpaces+1
                if (top <= SIZE and top >= 0):
                    
                    if (world[currentColumn][top] == " "):
                        emptySpaces = emptySpaces+1
                    

                if (top <= SIZE and top >= 0 and left <= SIZE and left >= 0):
                    if (world[left][top] == " "):
                        emptySpaces = emptySpaces +1



                if (emptySpaces <= 1):
                    world[currentColumn][currentRow] = " "

            #MIDDLE TOP

            if (world[currentColumn][0] == "*"):
                if( right <= SIZE and right >= 0):
                    if (world[right][currentRow] ==" "):
                        emptySpaces = emptySpaces+1
                if (left <= SIZE and left >= 0):
                    if (world[left][currentRow] == " "):
                        emptySpaces = emptySpaces+1

                if (bottom <= SIZE and bottom >= 0):
                    
                    if (world[currentColumn][bottom] == " "):
                        emptySpaces = emptySpaces+1

                if (right <= SIZE and right >= 0 and bottom <= SIZE and bottom >= 0):
                    if (world[right][bottom] == " "):
                        emptySpaces = emptySpaces + 1
                if (left <= SIZE and left >= 0 and bottom <= SIZE and left >= 0):
                    if (world[left][bottom] == " "):
                        emptySpaces = emptySpaces + 1

                if (emptySpaces <= 1):
                    world[currentColumn][currentRow] = " "
                        
                

            #MIDDLE BOTTOM
            if (world[currentColumn][9] == "*"):
                if( right <= SIZE and right >= 0):
                    if (world[right][currentRow] ==" "):
                        emptySpaces = emptySpaces+1
                if (left <= SIZE and left >= 0):
                    if (world[left][currentRow] == " "):
                        emptySpaces = emptySpaces+1
                if (top <= SIZE and top >= 0):
                    
                    if (world[currentColumn][top] == " "):
                        emptySpaces = emptySpaces+1

                if (right <= SIZE and right >= 0 and top <= SIZE and top >=0):
                    if (world[right][top] == " "):
                        emptySpaces = emptySpaces +1
                if (top <= SIZE and top >= 0 and left <= SIZE and left >= 0):
                    if (world[left][top] == " "):
                        emptySpaces = emptySpaces +1


                if (emptySpaces <= 1):
                    world[currentColumn][currentRow] = " "

            #MIDDLE OF LIST
            if (world[currentColumn][currentRow] == "*"):
                if( right <= SIZE and right >= 0):
                    if (world[right][currentRow] ==" "):
                        emptySpaces = emptySpaces+1
                if (left <= SIZE and left >= 0):
                    if (world[left][currentRow] == " "):
                        emptySpaces = emptySpaces+1
                if (top <= SIZE and top >= 0):
                    
                    if (world[currentColumn][top] == " "):
                        emptySpaces = emptySpaces+1
                if (bottom <= SIZE and bottom >= 0):
                    
                    if (world[currentColumn][bottom] == " "):
                        emptySpaces = emptySpaces+1
                if (right <= SIZE and right >= 0 and top <= SIZE and top >=0):
                    if (world[right][top] == " "):
                        emptySpaces = emptySpaces +1
                if (top <= SIZE and top >= 0 and left <= SIZE and left >= 0):
                    if (world[left][top] == " "):
                        emptySpaces = emptySpaces +1
                if (right <= SIZE and right >= 0 and bottom <= SIZE and bottom >= 0):
                    if (world[right][bottom] == " "):
                        emptySpaces = emptySpaces + 1
                if (left <= SIZE and left >= 0 and bottom <= SIZE and left >= 0):
                    if (world[left][bottom] == " "):
                        emptySpaces = emptySpaces + 1

                if (emptySpaces <= 1):
                    world[currentColumn][currentRow] = " "
            


                

            currentColumn = currentColumn + 1
        currentRow = currentRow + 1

        if(len(world) == 81):
            fileValid = False

    return fileValid


#death of the critter by overcrowdedness
def deathOverCrowded(world):

# DEATH
    print(world)
    currentRow = 0
    fileValid = False
    while (currentRow <= 9):
        #print("THIS IS ROW FOR DEATH by overcrowding")
        currentColumn = 0
        while (currentColumn <= 9):
            #print("THIS IS THE COLUMN FOR DEATH by overcorwding")

            emptySpaces = 0
            spaceFilled = 0
            right = currentColumn + 1
            left = currentColumn - 1
            top = currentRow - 1
            bottom = currentRow + 1
            #WHEN OVERCROWDED
            #TOP LEFT
            if (world[0][0] == "*"):
            
                if( right <= SIZE and right >= 0):
                    if (world[right][currentRow] =="*"):
                        spaceFilled = spaceFilled+1

                if (bottom <= SIZE and bottom >= 0):
                    
                    if (world[currentColumn][bottom] == "*"):
                        spaceFilled = spaceFilled+1

                if (right <= SIZE and right >= 0 and bottom <= SIZE and bottom >= 0):
                    if (world[right][bottom] == "*"):
                        spaceFilled = spaceFilled + 1


                if (spaceFilled >= 4):
                    world[currentColumn][currentRow] = " "
            # MIDDLE VERY LEFT
            if (world[0][currentRow] == "*"):
                if( right <= SIZE and right >= 0):
                    if (world[right][currentRow] =="*"):
                        spaceFilled = spaceFilled+1
                if (top <= SIZE and top >= 0):
                    
                    if (world[currentColumn][top] == "*"):
                        spaceFilled = spaceFilled+1
                if (bottom <= SIZE and bottom >= 0):
                    
                    if (world[currentColumn][bottom] == "*"):
                        spaceFilled = spaceFilled+1
                if (right <= SIZE and right >= 0 and top <= SIZE and top >=0):
                    if (world[right][top] == "*"):
                        spaceFilled = spaceFilled +1
                if (right <= SIZE and right >= 0 and bottom <= SIZE and bottom >= 0):
                    if (world[right][bottom] == "*"):
                        spaceFilled = spaceFilled + 1


                if (spaceFilled >= 4):
                    world[currentColumn][currentRow] = " "

            #BOTTOM LEFT

            if (world[0][9] == "*"):

                if( right <= SIZE and right >= 0):
                    if (world[right][currentRow] =="*"):
                        spaceFilled = spaceFilled+1
                if (top <= SIZE and top >= 0):
                    
                    if (world[currentColumn][top] == "*"):
                        spaceFilled = spaceFilled+1


                if (right <= SIZE and right >= 0 and top <= SIZE and top >=0):
                    if (world[right][top] == "*"):
                        spaceFilled = spaceFilled +1
                

                if (spaceFilled >= 4):
                    world[currentColumn][currentRow] = " "

            #TOP RIGHT

            if (world[9][0] == "*"):

                if (left <= SIZE and left >= 0):
                    if (world[left][currentRow] == "*"):
                        spaceFilled = spaceFilled+1

                if (bottom <= SIZE and bottom >= 0):
                    
                    if (world[currentColumn][bottom] == "*"):
                        spaceFilled = spaceFilled+1

                if (left <= SIZE and left >= 0 and bottom <= SIZE and left >= 0):
                    if (world[left][bottom] == "*"):
                        spaceFilled = spaceFilled + 1

                if (spaceFilled >= 4):
                    world[currentColumn][currentRow] = " "

            #MIDDLE VERY RIGHT

            if (world[9][currentRow] == "*"):
            
                if (left <= SIZE and left >= 0):
                    if (world[left][currentRow] == "*"):
                        spaceFilled = spaceFilled+1
                if (top <= SIZE and top >= 0):
                    
                    if (world[currentColumn][top] == "*"):
                        spaceFilled = spaceFilled+1
                if (bottom <= SIZE and bottom >= 0):
                    
                    if (world[currentColumn][bottom] == "*"):
                        spaceFilled = spaceFilled+1
                if (top <= SIZE and top >= 0 and left <= SIZE and left >= 0):
                    if (world[left][top] == "*"):
                        spaceFilled = spaceFilled +1
                if (left <= SIZE and left >= 0 and bottom <= SIZE and left >= 0):
                    if (world[left][bottom] == "*"):
                        spaceFilled = spaceFilled + 1

                if (spaceFilled >= 4):
                    world[currentColumn][currentRow] = " "

            #BOTTOM RIGHT

            if (world[9][9] == "*"):
            
                if (left <= SIZE and left >= 0):
                    if (world[left][currentRow] == "*"):
                        spaceFilled = spaceFilled+1
                if (top <= SIZE and top >= 0):
                    
                    if (world[currentColumn][top] == "*"):
                        spaceFilled = spaceFilled+1
               
                if (top <= SIZE and top >= 0 and left <= SIZE and left >= 0):
                    if (world[left][top] == "*"):
                        spaceFilled = spaceFilled +1
               

                if (spaceFilled >= 4):
                    world[currentColumn][currentRow] = " "

            #MIDDLE TOP

            if (world[currentColumn][0] == "*"):
                if( right <= SIZE and right >= 0):
                    if (world[right][currentRow] =="*"):
                        spaceFilled = spaceFilled+1
                if (left <= SIZE and left >= 0):
                    if (world[left][currentRow] == "*"):
                        spaceFilled = spaceFilled+1
                if (bottom <= SIZE and bottom >= 0):
                    
                    if (world[currentColumn][bottom] == "*"):
                        spaceFilled = spaceFilled+1
        
                if (right <= SIZE and right >= 0 and bottom <= SIZE and bottom >= 0):
                    if (world[right][bottom] == "*"):
                        spaceFilled = spaceFilled + 1
                if (left <= SIZE and left >= 0 and bottom <= SIZE and left >= 0):
                    if (world[left][bottom] == "*"):
                        spaceFilled = spaceFilled + 1

                if (spaceFilled >= 4):
                    world[currentColumn][currentRow] = " "
                

            #MIDDLE BOTTOM
            if (world[currentColumn][9] == "*"):
                if( right <= SIZE and right >= 0):
                    if (world[right][currentRow] =="*"):
                        spaceFilled = spaceFilled+1
                if (left <= SIZE and left >= 0):
                    if (world[left][currentRow] == "*"):
                        spaceFilled = spaceFilled+1
                if (top <= SIZE and top >= 0):
                    
                    if (world[currentColumn][top] == "*"):
                        spaceFilled = spaceFilled+1
                if (right <= SIZE and right >= 0 and top <= SIZE and top >=0):
                    if (world[right][top] == "*"):
                        spaceFilled = spaceFilled +1
                if (top <= SIZE and top >= 0 and left <= SIZE and left >= 0):
                    if (world[left][top] == "*"):
                        spaceFilled = spaceFilled +1


                if (spaceFilled >= 4):
                    world[currentColumn][currentRow] = " "

            #MIDDLE OF LIST
            if (world[currentColumn][currentRow] == "*"):
                if( right <= SIZE and right >= 0):
                    if (world[right][currentRow] =="*"):
                        spaceFilled = spaceFilled+1
                if (left <= SIZE and left >= 0):
                    if (world[left][currentRow] == "*"):
                        spaceFilled = spaceFilled+1
                if (top <= SIZE and top >= 0):
                    
                    if (world[currentColumn][top] == "*"):
                        spaceFilled = spaceFilled+1
                if (bottom <= SIZE and bottom >= 0):
                    
                    if (world[currentColumn][bottom] == "*"):
                        spaceFilled = spaceFilled+1
                if (right <= SIZE and right >= 0 and top <= SIZE and top >=0):
                    if (world[right][top] == "*"):
                        spaceFilled = spaceFilled +1
                if (top <= SIZE and top >= 0 and left <= SIZE and left >= 0):
                    if (world[left][top] == "*"):
                        spaceFilled = spaceFilled +1
                if (right <= SIZE and right >= 0 and bottom <= SIZE and bottom >= 0):
                    if (world[right][bottom] == "*"):
                        spaceFilled = spaceFilled + 1
                if (left <= SIZE and left >= 0 and bottom <= SIZE and left >= 0):
                    if (world[left][bottom] == "*"):
                        spaceFilled = spaceFilled + 1

                if (spaceFilled >= 4):
                    world[currentColumn][currentRow] = " "

            



                
                

            currentColumn = currentColumn + 1
        currentRow = currentRow + 1

        if(len(world) == 81):
            fileValid = False

    return fileValid

#combines the functions of birth and deaths into one whilst adding unchan ged list into oldWorld and updated list into newWorld
def rulesOfBirthAndDeath(world):
    turn = 0
    currentRow = 0
    currentColumn = 0
    oldWorld = []
    oldWorld = [
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "]
    ]

    while (currentRow >= 9 and currentRow <= 0):
        while (currentColumn >= 9 and currentColumn <=0): 
            oldWorld[currentRow].append(world[currentColumn])

            currentColumn = currentColumn + 1
                    
        currentRow = currentRow +1

    
    fileValid = birth(world)
    fileValid =  deathLonely(world)
    fileValid = deathOverCrowded(world)

    newWorld = []
    newWorld = [
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "]
    ]

    
    while (currentRow >= 9 and currentRow <= 0):
        while (wcurrentColumn >= 9 and currentColumn <=0): 
            newWorld[currentRow].append(world[currentColumn])

            currentColumn = currentColumn + 1
                    
        currentRow = currentRow +1
    
    turn = turn +1

    playerSelection = input("Press 'C' to continue playing the game OR Press 'Q' to quit: ")

    if (playerSelection == "C" or "c"):
        fileValid = True
    elif (playerSelection == "Q" or "q"):
        fileValid = False
    else:
       while (playerSelection not in ("C", "c", "Q", "q")):
            print("Please select one of the options")
            playerSelection = str(input("Please select one of the following options: "))

    
    


    return oldWorld,newWorld,turn,fileValid

#displayes before and after effect in a specific format
#AUTHOR OF CODE BELOW IS DR. JAMES TAM
def display(turn,oldWorld,newWorld):
    # Displays a row at a time of each list
    print("Turn #%d" %turn)
    print("BEFORE\t\t\tAFTER")
    for r in range (0,SIZE,1):

        # Row of dashes before each row of old and new list
        # (Dashes for old list)
        for i in range (0, SIZE+1, 1): 
            print("%s" %(" -"), end="")
        print("#\t",end="")
        # (Dashes for new list)
        for i in range (0, SIZE+1, 1): 
            print("%s" %(" -"), end="")
        print()

        # Display one row of old world list
        for c in range (0,SIZE+1,1):
            # Display: A vertical bar and then element (old list) 
            print("|%s" %(oldWorld[r][c]), end = "")
        # Separate the lists with a number sign and a tab
        print("", end = "#\t")    

        # Display one row of new world list
        for c in range (0,SIZE+1,1):
            # Display: A vertical bar and then element (new list) 
            print("|%s" %(newWorld[r][c]), end = "")
        print("|")

    # Row of dashes after end of last row (old world list)
    for i in range (0, SIZE+1, 1): 
        print("%s" %(" -"), end="")
    print("#\t",end="")

    # Row of dashes after end of each row (new world list)
    for i in range (0, SIZE+1, 1): 
        print("%s" %(" -"), end="")
    print()
    


    

def oneEmpty():
    world = []
    world = [
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "]
    ]
    #display()
    return(world)

    
    

def twoSingleCritter():
    world = []
    world = [
     ["*"," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "]
    ]
    return(world)

def threeSingleBirth():
    world = []
    world = [
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " ","*", " ", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "]
    ]
    return(world)
    world = birthsAndDeaths(world)

def fourthSimpleBirth():
    world = []
    world = [
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", "*","*", " ", " ", " ", " ", " ", " "],
     [" ","*", " ","*", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     ["*"," ", " "," ", " ", " ", " ", " ", " ", " "]
    ]
    return(world)
    world = birthsAndDeaths(world)
    return(world)

def fifthCreateListEdgeCases():
    world = []
    world = [
     ["*"," ", "*"," ", " ", " ", " ", " ", " ", "*"],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     ["*"," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", " ", " ", " ", " ", " "],
     ["*"," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", "*"],
     [" "," ", " "," ", " ", " ", " ", " ", "*", " "],
     ["*","*", " "," ", " ", " ", " ", " ", " ", "*"]
    ]
    #display()
    return(world)
    world = birthsAndDeaths(world)

def sixthComplexCases():
    world = []
    world = [
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", "*", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", "*", " ", " ", " ", " "],
     [" "," ", " ","*", "*", "*", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     ["*"," ", " "," ", " ", " ", " ", " ", " ", " "]
    ]
    return(world)
    world = 0
    world = birthsAndDeaths(world)
#reads file
def fileRead():
    fileValid = False
    oldWorld = []
    
    while (fileValid == False):
        try:

            fileName = input("Enter your file name: ")
            inputFile = open(fileName, "r")
            world = inputFile.readline()
        
            if (world == ""):
                print( fileName, "is am empty file. Please enter the file name: ")
                fileName = input("Enter your file name: ")
                inputFile = open(fileName, "n")
                fileValid = False
            else:
                fileValid = True

        except IOError:
                print("There has been a problem reading the file" , fileName )
                fileValid = False #cuz encountered an error thus will repeat the while loop
    birthsAndDeaths(world)

def start():
    world = []
    oldWorld = []
    newWorld = []
    turn = 0
    fileValid = True
    playerSelection = 0
    
    world = menu()
    fileValid = applyingTheRules(world,oldWorld,newWorld,turn,fileValid)
    display(turn,oldWorld,newWorld)
    

start()
    



    
    
