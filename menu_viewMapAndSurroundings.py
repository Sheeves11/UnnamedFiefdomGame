from globals import *

#This document contains screens for:
#   viewMapYourStronghold
#   viewMapEnemyStronghold
#   viewMapCurrentFief
#   viewSurroundings

def ViewMapAndSurroundings(screen, userStronghold, attackStronghold, STRONGHOLD, USER_STRONGHOLD):
    global firstMapRead
    #This page prints the world map with your stronghold's location marked on it
    if screen == "viewMapYourStronghold":
        os.system("clear")
        headerSuperStripped()
        print('    --------------------------------------------------------------------------------------------------------------   ')
        print('                                                    W O R L D   M A P                                              ')

        serverMap.name = "serverMap"

        if firstMapRead:
            serverMap.read()
            firstMapRead = False

        PrintLegend()
        print('')
        #print('    ' + UNDERLINE + WARNING + 'World Map' + RESET + ':    [Current Location -  Row: ' + WARNING + str(userStronghold.yCoordinate) + RESET + '   Column: ' + WARNING + str(userStronghold.xCoordinate) + RESET + ']')
        WorldMapLocation(int(userStronghold.yCoordinate), int(userStronghold.xCoordinate), serverMap, userStronghold.name)
        print('')

        print("    Avalible Commands:")
        print('    -------------------------------------------------------')
        print('    {1}: Return to Stronghold')
        print('    {2}: Look at Surroundings')
        print('    {3}: View Temperature Map')
        print('    --------------------------------------------------------')
        print('')
        command = input("    Enter your command: ")

        if command == '1':
            screen = "stronghold"

        if command == '2':
            screen = 'viewSurroundings'
            USER_STRONGHOLD = True
            STRONGHOLD = True

        if command == '3':
            screen = "tempMap"

#This page prints the world map with your stronghold's location marked on it
    if screen == "viewMapEnemyStronghold":
        os.system("clear")
        headerSuperStripped()

        serverMap.name = "serverMap"

        if firstMapRead:
            serverMap.read()
            firstMapRead = False

        PrintLegend()
        print('')
        print('    ' + UNDERLINE + WARNING + 'World Map' + RESET + ':    [Current Location -  Row: ' + WARNING + str(attackStronghold.yCoordinate) + RESET + '   Column: ' + WARNING + str(attackStronghold.xCoordinate) + RESET + ']')
        WorldMapLocation(int(attackStronghold.yCoordinate), int(attackStronghold.xCoordinate), serverMap, userStronghold.name)
        print('')
        time.sleep(1)
        nothing = input('    Press Enter to Continue')

        return 'enemyStrongholdDetails'

#This page prints the world map with your stronghold's location marked on it
    if screen == "viewMapCurrentFief":
        os.system("clear")
        headerSuperStripped()

        serverMap.name = "serverMap"

        if firstMapRead:
            serverMap.read()
            firstMapRead = False

        PrintLegend()
        print('')
        print('    ' + UNDERLINE + WARNING + 'World Map' + RESET + ':    [Current Location -  Row: ' + WARNING + str(attackFief.yCoordinate) + RESET + '   Column: ' + WARNING + str(attackFief.xCoordinate) + RESET + ']')
        WorldMapLocation(int(attackFief.yCoordinate), int(attackFief.xCoordinate), serverMap, userStronghold.name)
        print('')
        time.sleep(1)
        nothing = input('    Press Enter to Continue')

        if str(attackFief.ruler) == str(userStronghold.ruler):
            return 'ownedFiefDetails'
        if str(attackFief.ruler) != str(userStronghold.ruler):
            return "enemyFiefDetails"

#This page prints the world map with your stronghold's location marked on it
    if screen == "viewSurroundings":
        os.system("clear")

        serverMap.name = "serverMap"
        serverMap.read()

        if STRONGHOLD:
            headerStripped()
            print('\n\n\n    ')
            print('    You stand atop the tallest tower in your stronghold and take a look around. This is what you see: \n\n\n')
            if USER_STRONGHOLD:
                ListSurroundings(serverMap.worldMap, userStronghold.xCoordinate, userStronghold.yCoordinate)
                print('')
                time.sleep(1)
                nothing = input('    Press Enter to Continue')
                return "stronghold"
            else:
                ListSurroundings(serverMap.worldMap, attackStronghold.xCoordinate, attackStronghold.yCoordinate)
                print('')
                time.sleep(1)
                nothing = input('    Press Enter to Continue')
                return "enemyStrongholdDetails"
        else:
            headerStripped()
            print('\n\n\n    ')
            print('    You stand atop the highest point in the fiefdom and take a look around. This is what you see: \n\n\n')
            ListSurroundings(serverMap.worldMap, attackFief.xCoordinate, attackFief.yCoordinate)
            print('')
            print('    In all:')
            if int(attackFief.adjacentWater) > 0:
                if int(attackFief.adjacentWater) == 1:
                    print('      There is one body of ' + textColor.BLUE + 'water' + textColor.RESET + ' nearby')
                elif int(attackFief.adjacentWater) > 1:
                    print('      There are ' + str(attackFief.adjacentWater) + ' bodies of ' + textColor.BLUE + 'water' + textColor.RESET + ' nearby')
            if int(attackFief.adjacentRivers) > 0:
                if int(attackFief.adjacentRivers) == 1:
                    print('      There is one ' + textColor.BLUE + 'river' + textColor.RESET + ' nearby')
                elif int(attackFief.adjacentRivers) > 1:
                    print('      There are ' + str(attackFief.adjacentRivers) + ' ' + textColor.BLUE + 'rivers' + textColor.RESET + ' nearby')
            if int(attackFief.adjacentPlains) > 0:
                if int(attackFief.adjacentPlains) == 1:
                    print('      There is one ' + textColor.YELLOW + 'plains' + textColor.RESET + ' nearby')
                elif int(attackFief.adjacentPlains) > 1:
                    print('      There are ' + str(attackFief.adjacentPlains) + ' ' + textColor.YELLOW + 'plains' + textColor.RESET + ' nearby')
            if int(attackFief.adjacentForests) > 0:
                if int(attackFief.adjacentForests) == 1:
                    print('      There is one ' + textColor.GREEN + 'forest' + textColor.RESET + ' nearby')
                elif int(attackFief.adjacentForests) > 1:
                    print('      There are ' + str(attackFief.adjacentForests) + ' ' + textColor.GREEN + 'forests' + textColor.RESET + ' nearby')
            if int(attackFief.adjacentMountains) > 0:
                if int(attackFief.adjacentMountains) == 1:
                    print('      There is one ' + textColor.DARK_GRAY + 'mountain' + textColor.RESET + ' nearby')
                elif int(attackFief.adjacentMountains) > 1:
                    print('      There are ' + str(attackFief.adjacentMountains) + ' ' + textColor.DARK_GRAY + 'mountains' + textColor.RESET + ' nearby')
            if str(attackFief.ruler) == str(userStronghold.ruler):
                print('')
                time.sleep(1)
                nothing = input('    Press Enter to Continue')
                return 'ownedFiefDetails'
            if str(attackFief.ruler) != str(userStronghold.ruler):
                print('')
                time.sleep(1)
                nothing = input('    Press Enter to Continue')
                return "enemyFiefDetails"

    return screen