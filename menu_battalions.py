from globals import *
from armies import *

def BattalionMenu(screen, userStronghold, STRONGHOLD, USER_STRONGHOLD):
    if screen == "battalions":
        os.system("clear")
        header(userStronghold.name)

        serverArmies.read()

        battalions = serverArmies.GetBattalions()
        count = 0

        print("\n    Your Battalions\n")
        for i in range(len(battalions)):
            if str(battalions[i].commander) == str(userStronghold.name):
                count = count + 1
                leftNumber = str(CYAN + "    {" + str(count) + "}" + RESET).rjust(17, " ")
                print(str(leftNumber) + " " + str(battalions[i].ListDetails))

        print("\n    Avalible Commands:")
        print('    ------------------------------------------------------')
        print('    {R}: Return to Stronghold')
        print('    {Enter a number above to view the offer}: ')
        print('    ------------------------------------------------------')
        print('')
        command = input("    Enter your command: ")

        command = str(command.lower())

        if str(command) == 'r':
            screen = "stronghold"
        else:
            screen = "market"

    return screen