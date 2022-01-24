from globals import *
from armies import *

def BattalionMenu(screen, userStronghold, STRONGHOLD, USER_STRONGHOLD):
    currentBattalion = 0
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
        print('    {C}: Create Battalion')
        print('    ' + CYAN + '{Enter a number above to view that battalion}: ' + RESET)
        print('    ------------------------------------------------------')
        print('')
        command = input("    Enter your command: ")

        command = str(command.lower())

        if str(command) == 'r':
            return "stronghold"
        elif str(command) == 'c':
            return CreateNewBattalion(userStronghold)
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
        print('    ------------------------------------------------------')
        print('')
        command = input("    Enter your command: ")

        if str(command) == '1':
            return "battalions"
        else:
            return "battalions"

    return screen