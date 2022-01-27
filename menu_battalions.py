from globals import *
from armies import *

BatMenu = False
CurrentBattalion = 0

#   Not set up to handle Fiefs just yet!
def BattalionMenu(screen, userStronghold, STRONGHOLD, USER_STRONGHOLD):
    global CurrentBattalion
    global BatMenu
    
    xPos = 0
    yPos = 0
    if screen == "battalions":
        os.system("clear")
        header(userStronghold.name)

        serverArmies.read()

        battalions = serverArmies.GetBattalionObjects()
        count = 0

        yourBattalions = []

        print("\n    Battalions at Your Command:\n")
        for i in range(len(battalions)):
            if str(battalions[i].commander) == str(userStronghold.name):
                count = count + 1
                yourBattalions.append(battalions[i])
                leftNumber = str(CYAN + "    {" + str(count) + "}" + RESET).rjust(17, " ")
                location = GetLocation(serverMap, battalions[i].yPos, battalions[i].xPos)
                if location[0] == "":
                    print(str(leftNumber) + " " + str(battalions[i].MenuBar(userStronghold)))
                else:
                    print(str(leftNumber) + " " + str(battalions[i].MenuBarWithLocation(userStronghold, location[0])))

        print("\n    Avalible Commands:")
        print('    ------------------------------------------------------')
        print('    {R}: Return to Stronghold')
        if int(userStronghold.defenders) >= 100:
            print('    {C}: Create Battalion')
        print('    {V}: View World Map')
        print('    ' + CYAN + '{Enter a number above to view that battalion}: ' + RESET)
        print('    ------------------------------------------------------')
        print('')
        command = input("    Enter your command: ")

        command = str(command.lower())

        if int(userStronghold.defenders) >= 100:
            if str(command) == 'c':
                return CreateNewBattalion(userStronghold)

        if str(command) == 'r':
            return "stronghold"
        if str(command) == 'v':
            BatMenu = False
            xPos = int(userStronghold.xCoordinate)
            yPos = int(userStronghold.yCoordinate)
            screen = "battalionMap"
        elif IsPositiveIntEqualOrLessThan(command, count):
            CurrentBattalion = yourBattalions[int(command) - 1]
            screen = "commandBattalion"
        else:
            return "battalions"

    if screen == "commandBattalion":
        os.system("clear")
        if CurrentBattalion != 0:
            print(str(CurrentBattalion))
            CurrentBattalion = serverArmies.GetBattalion(CurrentBattalion.name)
        headerBattalion(CurrentBattalion, userStronghold, serverMap)
        GenerateMiniMap(serverMap, CurrentBattalion.yPos, CurrentBattalion.xPos)
        print(location[0])
        print("\n    Avalible Commands:")
        print('    ------------------------------------------------------')
        print('    {1}: Go Back')
        print('    {2}: Move Out')
        print('    {3}: View World Map')
        if location[0] != "":
            print('    {4}: Disband (' + LIME + 'Units and Inventory are added to this location' + RESET + ')')
        print('    ------------------------------------------------------')
        print('')
        command = input("    Enter your command: ")

        if str(command) == '1':
            return "battalions"
        elif str(command) == '2':
            screen = "battalionNavigation"
        elif str(command) == '3':
            BatMenu = True
            xPos = int(CurrentBattalion.xPos)
            yPos = int(CurrentBattalion.yPos)
            screen = "battalionMap"
        elif str(command) == '4':
            # DetermineLocation(location)
            
            if str(location[1]) == 'stronghold':
                userStronghold.defenders = int(userStronghold.defenders) + int(CurrentBattalion.numTroops)
                userStronghold.gold = int(userStronghold.gold) + int(CurrentBattalion.invGold)
                userStronghold.food = int(userStronghold.food) + int(CurrentBattalion.invFood)
                userStronghold.wood = int(userStronghold.wood) + int(CurrentBattalion.invWood)
                userStronghold.stone = int(userStronghold.stone) + int(CurrentBattalion.invStone)
                userStronghold.ore = int(userStronghold.ore) + int(CurrentBattalion.invOre)
                serverArmies.RemoveBattalion(CurrentBattalion)
                userStronghold.write()
                userStronghold.read()
            else:
                tempFief = Fiefdom()
                tempFief.name = str(location[2])
                tempFief.read()
                print(str(tempFief.name))
                tempFief.defenders = int(tempFief.defenders) + int(CurrentBattalion.numTroops)
                tempFief.gold = int(tempFief.gold) + int(CurrentBattalion.invGold)
                tempFief.food = int(tempFief.food) + int(CurrentBattalion.invFood)
                tempFief.wood = int(tempFief.wood) + int(CurrentBattalion.invWood)
                tempFief.stone = int(tempFief.stone) + int(CurrentBattalion.invStone)
                tempFief.ore = int(tempFief.ore) + int(CurrentBattalion.invOre)
                serverArmies.RemoveBattalion(CurrentBattalion)
                tempFief.write()
                tempFief.read()
            
            return "battalions"
        else:
            return "battalions"

    if screen == "battalionMap":
        os.system("clear")
        if BatMenu:
            headerBattalion(CurrentBattalion, userStronghold, serverMap)
        else:
            header(userStronghold.name)
        GenerateBattalionMap(serverMap, userStronghold, serverArmies, yPos, xPos)

        print("\n    Avalible Commands:")
        print('    ------------------------------------------------------')
        print('    {1}: Go Back')
        print('    {2}: List Fiefs and Strongholds')
        print('    ------------------------------------------------------')
        print('')
        command = input("    Enter your command: ")

        if str(command) == '1':
            if BatMenu:
                return "commandBattalion"
            else:
                return "battalions"
        elif str(command) == '2':
            screen = "battalionMap+"
        else:
            return "battalionMap"

    if screen == "battalionMap+":
        os.system("clear")
        if BatMenu:
            headerBattalion(CurrentBattalion, userStronghold, serverMap)
        else:
            header(userStronghold.name)
        GenerateBattalionMapWithLocations(serverMap, userStronghold, serverArmies, yPos, xPos)

        print("\n    Avalible Commands:")
        print('    ------------------------------------------------------')
        print('    {1}: Go Back')
        print('    {2}: List Battalions Only')
        print('    ------------------------------------------------------')
        print('')
        command = input("    Enter your command: ")

        if str(command) == '1':
            if BatMenu:
                return "commandBattalion"
            else:
                return "battalions"
        elif str(command) == '2':
            return "battalionMap"
        else:
            return "battalionMap+"

    if screen == "battalionNavigation":
        os.system("clear")
        headerBattalion(CurrentBattalion, userStronghold, serverMap)

        GenerateMiniMap(serverMap, CurrentBattalion.yPos, CurrentBattalion.xPos)
        
        print("\n    Directions:")
        print('    -------------')
        directions = AvailableDirections(CurrentBattalion)
        print('    -------------')
        print('')
        command = input("    Input which direction you would like to go, or hit enter to cancel: ")

        command = str(command.lower())
        
        if command in directions:
            MoveBattalion(userStronghold, CurrentBattalion, command)
            return "battalionNavigation"
        else:
            return "battalions"
        
        

    return screen