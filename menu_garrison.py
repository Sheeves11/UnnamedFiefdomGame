from globals import *

#This document contains screens for:
#   garrison
#   garrisonSorter

def GarrisonMenu(screen, userStronghold):
#This is the screen for viewing users owned fiefs and for garrisoning soldiers
#----------------------------------------------------------------------------------
    if screen == "garrison":
        os.system("clear")

        header(userStronghold.name)

        userFiefCount = 0

        print('\n    Fiefs under your rule:')
        print("    ------------------------------------------------------------------\n")
        for filename in os.listdir('fiefs'):
            with open(os.path.join('fiefs', filename), 'r') as f:

                tempName = filename[:-4]
                tempName = Fiefdom()
                tempName.name = filename[:-4]
                tempName.read()

                if tempName.home != "True" and tempName.ruler == userStronghold.name:
                    userFiefCount = userFiefCount + 1
                    print ('    ' + textColor.CYAN + tempName.name + ' || Ruled by: ' + tempName.ruler + ' || Defenders: ' +
                            tempName.defenders + textColor.RESET + ' || Gold: ' + tempName.gold)

        print('\n')
        print("    Avalible Commands:")
        print('    -------------------------------------')
        print('    {1}: Return to Stronghold')
        print('    {2}: View Fiefdoms')
        print('    {3}: Distribute Soldiers')
        print('    -------------------------------------')
        print('')
        command = input("    Enter your command: ")

        if command == "1":
            return "stronghold"

        if command == "2":
            return "fiefdoms"

        if command == "3":
            currentPage = 1
            return "garrisonSorter"

#This is the screen for distributing a user's soldiers evenly among fiefs they control
#----------------------------------------------------------------------------------
    if screen == "garrisonSorter":
        os.system("clear")

        header(userStronghold.name)

        print("\n\n")
        print('    Currently Ruled Fiefs: ' + str(userFiefCount))
        print('    Current Number of Soldiers in Stronghold: ' + str(userStronghold.defenders))
        print('\n')
        time.sleep(1)
        if userFiefCount == 0:
            print('    You control no fiefs you can distribute to! \n')
            time.sleep(2)
            return "garrison"
        else:
            withdrawNum = input('    Enter the number of soldiers you would like to evenly distrubute among these ' + str(userFiefCount) + ' fiefs: ')
            time.sleep(1)

            try:
                int(withdrawNum)
            except:
                withdrawNum = '0'

            if int(withdrawNum) < 0:
                os.system("clear")
                print("    You cannot distribute a negative number of soldiers. \n\nThat doesn't even make sense.")
                time.sleep(2)
                return 'garrison'

            elif int(withdrawNum) == 0:
                os.system("clear")
                print("    Cancelling request...")
                time.sleep(1)
                return 'garrison'

            elif int(userStronghold.defenders) < int(withdrawNum):
                os.system("clear")
                print("    You do not have enough soldiers for that.")
                time.sleep(2)
                return 'garrison'

            elif int(withdrawNum) < userFiefCount:
                os.system("clear")
                print("    You have more fiefs than soldiers you want to distribute!")
                time.sleep(2)
                return 'garrison'

            else:
                print('    Garrisoning ' + str(withdrawNum) + ' soldiers across ' + str(userFiefCount) + ' Fiefs...')

                time.sleep(1)

                benchedSoldiers = int(withdrawNum) % userFiefCount
                outgoingSoldierGroups = round((int(withdrawNum) - benchedSoldiers)/userFiefCount)

                if benchedSoldiers > 0:
                    print('    ' + str(benchedSoldiers) + ' soldiers were held back to make even groups of ' + str(outgoingSoldierGroups) + '.')

                print('\n')

                for filename in os.listdir('fiefs'):
                    with open(os.path.join('fiefs', filename), 'r') as f:

                        tempName = filename[:-4]
                        tempName = Fiefdom()
                        tempName.name = filename[:-4]
                        tempName.read()

                        homeStatus = " "

                        if tempName.home != "True" and tempName.ruler == userStronghold.name:
                            print('    ' + tempName.name + ' had ' + str(tempName.defenders) + ' soldier(s).')
                            time.sleep(0.3)
                            tempName.defenders = str(int(tempName.defenders) + outgoingSoldierGroups)
                            tempName.write()
                            tempName.read()
                            print('    ' + tempName.name + ' now has ' + str(tempName.defenders) + ' soldiers! \n')
                            time.sleep(0.3)

                userStronghold.defenders = int(userStronghold.defenders) - int(withdrawNum) + benchedSoldiers
                userStronghold.write()
                userStronghold.read()
                print('\n    Number of Soldiers Remaining in Stronghold: ' + str(userStronghold.defenders))

                print("\n\n\n\n\n\n\n\n\n")

        tempInput = input('    Press Enter to Continue')
        return 'garrison'

    return screen