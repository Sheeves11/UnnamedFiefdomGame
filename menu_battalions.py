from globals import *
from armies import *

BatMenu = False

#   Not set up to handle Fiefs just yet!
def BattalionMenu(screen, userStronghold, STRONGHOLD, USER_STRONGHOLD):
    currentBattalion = 0
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
                if location == "":
                    print(str(leftNumber) + " " + str(battalions[i].MenuBar(userStronghold)))
                else:
                    print(str(leftNumber) + " " + str(battalions[i].MenuBarWithLocation(userStronghold, location)))

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
            currentBattalion = yourBattalions[int(command) - 1]
            screen = "commandBattalion"
        else:
            return "battalions"

    if screen == "commandBattalion":
        os.system("clear")
        headerBattalion(currentBattalion, userStronghold, serverMap)
        GenerateMiniMap(serverMap, currentBattalion.yPos, currentBattalion.xPos)

        print("\n    Avalible Commands:")
        print('    ------------------------------------------------------')
        print('    {1}: Go Back')
        print('    {2}: Move Out')
        print('    {3}: View World Map')
        if location != "":
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
            xPos = int(currentBattalion.xPos)
            yPos = int(currentBattalion.yPos)
            screen = "battalionMap"
        elif str(command) == '4':
            userStronghold.defenders = int(userStronghold.defenders) + int(currentBattalion.numTroops)
            userStronghold.gold = int(userStronghold.gold) + int(currentBattalion.invGold)
            userStronghold.food = int(userStronghold.food) + int(currentBattalion.invFood)
            userStronghold.wood = int(userStronghold.wood) + int(currentBattalion.invWood)
            userStronghold.stone = int(userStronghold.stone) + int(currentBattalion.invStone)
            userStronghold.ore = int(userStronghold.ore) + int(currentBattalion.invOre)
            serverArmies.RemoveBattalion(currentBattalion)
            userStronghold.write()
            userStronghold.read()
            return "battalions"
        else:
            return "battalions"

    if screen == "battalionMap":
        os.system("clear")
        if BatMenu:
            headerBattalion(currentBattalion, userStronghold, serverMap)
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
            screen = "battalionsMap+"
        else:
            return "battalionMap"

    if screen == "battalionMap+":
        os.system("clear")
        if BatMenu:
            headerBattalion(currentBattalion, userStronghold, serverMap)
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
            return "battalionsMap"
        else:
            return "battalionMap+"

    if screen == "battalionNavigation":
        os.system("clear")
        headerBattalion(currentBattalion, userStronghold, serverMap)

        GenerateMiniMap(serverMap, currentBattalion.yPos, currentBattalion.xPos)
        
        print("\n    Directions:")
        print('    -------------')
        if int(currentBattalion.xPos) > 0 and int(currentBattalion.xPos) < MAP_WIDTH and int(currentBattalion.yPos) > 0 and int(currentBattalion.yPos) < MAP_HEIGHT:
            directions = ['n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw']
            print('    {NW} {N} {NE}')
            print('    {W}       {E}')
            print('    {SW} {S} {SE}')
        elif int(currentBattalion.xPos) == 0 and int(currentBattalion.yPos) > 0 and int(currentBattalion.yPos) < MAP_HEIGHT:
            directions = ['n', 'ne', 'e', 'se', 's']
            print('    {X} {N} {NE}')
            print('    {X}      {E}')
            print('    {X} {S} {SE}')
        elif int(currentBattalion.xPos) == MAP_WIDTH and int(currentBattalion.yPos) > 0 and int(currentBattalion.yPos) < MAP_HEIGHT:
            directions = ['n', 's', 'sw', 'w', 'nw']
            print('    {NW} {N} {X}')
            print('    {W}      {X}')
            print('    {SW} {S} {X}')
        elif int(currentBattalion.xPos) > 0 and int(currentBattalion.xPos) < MAP_WIDTH and int(currentBattalion.yPos) == 0:
            directions = ['e', 'se', 's', 'sw', 'w']
            print('    {X}  {X}  {X}')
            print('    {W}       {E}')
            print('    {SW} {S} {SE}')
        elif int(currentBattalion.xPos) > 0 and int(currentBattalion.xPos) < MAP_WIDTH and int(currentBattalion.yPos) == MAP_HEIGHT:
            directions = ['n', 'ne', 'e', 'w', 'nw']
            print('    {NW} {N} {NE}')
            print('    {W}       {E}')
            print('    {X}  {X}  {X}')
        elif int(currentBattalion.xPos) == MAP_WIDTH and int(currentBattalion.yPos) == MAP_HEIGHT:
            directions = ['n', 'w', 'nw']
            print('    {NW} {N}  {X}')
            print('    {W}       {X}')
            print('    {X}  {X}  {X}')
        elif int(currentBattalion.xPos) == 0 and int(currentBattalion.yPos) == 0:
            directions = ['e', 'se', 's']
            print('    {X} {X}  {X}')
            print('    {X}      {E}')
            print('    {X} {S} {SE}')
        elif int(currentBattalion.xPos) == MAP_WIDTH and int(currentBattalion.yPos) == 0:
            directions = ['s', 'sw', 'w']
            print('    {X}  {X} {X}')
            print('    {W}      {X}')
            print('    {SW} {S} {X}')
        elif int(currentBattalion.xPos) == 0 and int(currentBattalion.yPos) == MAP_HEIGHT:
            directions = ['n', 'ne', 'e']
            print('    {X} {N} {NE}')
            print('    {X}      {E}')
            print('    {X} {X}  {X}')
        print('    -------------')
        print('')
        command = input("    Input which direction you would like to go, or hit enter to cancel: ")

        command = str(command.lower())
        
        if command in directions:
            MoveBattalion(userStronghold, currentBattalion, command)
        else:
            return "commandBattalion"
        
        

    return screen