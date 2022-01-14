from globals import *

#This document contains screens for:
#   withdrawGold
#   withdrawForces
#   deploy

def FiefCommandsMenu(screen, userStronghold):
#The withdraw gold screen allows players to withdraw gold from a ruled fiefdom
#
#To Do
# -
#
#------------------------------------------------------------------------------
    if screen == "withdrawGold":
        os.system("clear")
        # header(userStronghold.name)
        headerFief(attackFief)

        print("\n")
        print('    Now viewing the Fiefdom of ' + attackFief.name)
        print('\n')
        time.sleep(0)
        print('    ' + attackFief.name + ' has ' + attackFief.gold + ' gold.')
        time.sleep(1)
        print('\n')
        if int(attackFief.gold) > 0:
            print('    Sending ' + str(attackFief.gold) + ' gold back home')
            time.sleep(1)
            userStronghold.gold = str(int(userStronghold.gold) + int(attackFief.gold))
            attackFief.gold = str(0)
            attackFief.write()
            attackFief.read()
            userStronghold.write()
            userStronghold.read()

        return "fiefdoms"

#The deploy screen allows players to deploy defenders to a Fiefdom that they
#currently control.
#
#To Do
# - add a "withdraw" page for pulling troops out of a Fiefdom
# - verify that the player has the troops avalible for deployment
# - prevent negative numbers
#------------------------------------------------------------------------------
    if screen == "deploy":
        os.system("clear")

        # header(userStronghold.name)
        headerFief(attackFief)

        print("\n\n")
        print('    Now viewing the Fiefdom of ' + attackFief.name)
        print('\n\n')
        time.sleep(1)
        print('    ' + attackFief.name + ' has ' + attackFief.defenders + ' fighters.')
        time.sleep(1)
        print('    You have ' + str(userStronghold.defenders) + ' ready to deploy.\n\n')
        deployNum = input('    Enter the number of soldiers you would like to deploy: ')
        time.sleep(1)

        #print(deployNum + ' : deploynum || userStronghold.defenders : ' + userStronghold.defenders) #SW: remove this?

        try:
            deployNum = int(deployNum)
        except:
            deployNum = 0

        if int(deployNum) < 0:
            os.system("clear")
            print("    You cannot deploy a negative number of soldiers. \n\nThat doesn't even make sense.")
            time.sleep(2)
            return 'ownedFiefDetails'

        if (int(userStronghold.defenders) < int(deployNum)) and int(deployNum) > 0:
            os.system("clear")
            header(userStronghold.name)
            print("    You do not have enough soldiers for that")
            time.sleep(2)
            return 'ownedFiefDetails'

        if deployNum == 0:
            return "ownedFiefDetails"

        if (int(userStronghold.defenders) >= int(deployNum)) and int(deployNum) > 0:
            print('    Deploying ' + str(deployNum) + ' soldiers to ' + str(attackFief.name))

            attackFief.defenders = str(int(attackFief.defenders) + int(deployNum))
            attackFief.write()
            attackFief.read()

            userStronghold.defenders = str(int(userStronghold.defenders) - int(deployNum))
            userStronghold.write()
            userStronghold.read()
            attackFief.read()
            print('')
            tempInput = input('    Press Enter to Continue')
            return 'ownedFiefDetails'

        time.sleep(1)
#The withdrawForces screen allows players to withdraw forces from a ruled fiefdom
#
#To Do
# -
#
#------------------------------------------------------------------------------
    if screen == "withdrawForces":
        os.system("clear")
        # header(userStronghold.name)
        headerFief(attackFief)
        print("\n\n")
        print('    Now viewing the Fiefdom of ' + attackFief.name)
        print('\n\n')
        time.sleep(0.5)
        print('    ' + attackFief.name + ' has ' + attackFief.defenders + ' fighters.')
        time.sleep(0.5)
        print('\n')

        withdrawNum = input('    Enter the number of soldiers you would like to return home: ')
        time.sleep(1)
        try:
            withdrawNum = int(withdrawNum)
        except:
            withdrawNum = 0

        if int(withdrawNum) < 0:
            os.system("clear")
            print("    You cannot send home a negative number of soldiers. \n\nThat doesn't even make sense.")
            time.sleep(1)
            return 'ownedFiefDetails'

        if (int(attackFief.defenders) < int(withdrawNum)) and int(withdrawNum) > 0:
            os.system("clear")
            print("    You do not have enough soldiers for that")
            time.sleep(1)
            return 'ownedFiefDetails'

        if (int(attackFief.defenders) >= int(withdrawNum)) and int(withdrawNum) > 0:
            print('    Returning ' + str(withdrawNum) + ' soldiers back home')

            attackFief.defenders = str(int(attackFief.defenders) - int(withdrawNum))
            attackFief.write()
            attackFief.read()

            userStronghold.defenders = str(int(userStronghold.defenders) + int(withdrawNum))
            userStronghold.write()
            userStronghold.read()

            tempInput = input('    Press Enter to Continue')
            return 'ownedFiefDetails'

        if int(withdrawNum) == 0:
            print('    No soldiers selected')
            time.sleep(1)
            return "ownedFiefDetails"

    return screen