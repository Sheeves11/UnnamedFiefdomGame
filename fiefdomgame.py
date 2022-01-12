#!/usr/bin/env python

from globals import *
import bcrypt
from menu_devtest import *
from menu_sandbox import *
from menu_viewMapAndSurroundings import *
from menu_more import *
from menu_upgradesAndCustomizations import *
from menu_hire import *

'''

Welcome to the Unnamed Fiefdom Game!

This game was designed and written by
Mike Quain of the University of Arkansas

More info can be found at
github.com/Sheeves11/UnnamedFiefdomGame

'''

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#                           New Menu Organization
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#   menu_more.py:
#           moreCommands
#           messageBoard
#           pastWinners
#           about
#           features
#   menu_sandbox.py:
#           sandboxMenu
#           sbTestMap
#           sbCreateFief
#           sbPlotTestFiefs
#           sbViewMap
#   menu_viewMapAndSurroundings.py:
#           viewMapYourStronghold
#           viewMapEnemyStronghold
#           viewMapCurrentFief
#           viewSurroundings
#   menu_devtest.py:
#           devTest
#           devTestCreateDefaults
#           devTestWorldMap
#           devTestFiefPlacement
#           devTestPlotAllFiefs
#           devTestPlotAllStrongholds
#           devTestGenerateWorld
#           devTestAddGold
#           devTestWorldMapDiagnostics
#           devTestRiverTool
#   menu_upgradesAndCustomizations.py:
#           upgradeStronghold
#           upgradeAttack
#           upgradeFarm
#           upgradeDefense
#           changeStrongholdColor
#   menu_hire.py:
#           hireAndRecruit
#           thieves
#           mercs
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

#initial screen clear
os.system("clear")

#global variables
loop = True
screen = "login"
userStronghold = Stronghold()
attackStronghold = Stronghold()

#this begins the main game loop
#------------------------------------------------------------------------------
while (loop):
    #The login page takes a username, puts it into memory, and sends you to the
    #stronghold page. It also contains a small intro snippet
    #TO DO:
    # - Add password encryption
    if screen == "login":
        os.system("clear")

        art_titleScreen()

        print(textColor.RESET + '''
                Welcome to the Unnamed Fiefdom Game!

                This is a python programming project and multiplayer war game based on the classic
                BBS door games of the 80s and 90s. In much the same way, this system uses a central
                server to host the game to multiple users, who access it using a terminal emulator.

                See more info at github.com/Sheeves11/UnnamedFiefdomGame ''')
        print('\n')

        # userStronghold = Stronghold()
        username = input("                Enter your username: ")
        currentUsername = username

        userPath = ('users/' + username + '.txt')
        
        if exists(userPath) == True:
            
            usernameFile = "users/" + username + ".txt"
            with open(usernameFile, 'r') as f:
                os.system('clear')
                header(username)
                
                temp1 = f.readline().strip()
                hashed = f.readline().strip()
                
                print('\n\n    Welcome back, ' + str(username))
                userPass = input('    Enter your password: ')

                if bcrypt.checkpw(userPass, hashed):
                    print('    Password is correct')
                    time.sleep(.5)
                    print("    Logging in as: " + username)
                    time.sleep(.5)
                    screen = 'stronghold'
                else:
                    print('    Access denied')
                    time.sleep(.5)
                    screen = 'login'

        else:
            if CheckLegalUsername(username):
                #if "username.txt" does not exist, create it. The file only contains a name and password for now.
                newUser = input('\n                New user detected. Make a new account? (y/n): ')
                
                if newUser == 'y':
                    try:
                        usernameFile = "users/" + username + ".txt"
                        with open(usernameFile, 'x') as f:
                            f.write(username + '\n')
                            os.system('clear')
                            header(userStronghold.name)
                    
                            print('\n\n')
                            print(textColor.WARNING + '    WELCOME NEW PLAYER' + textColor.RESET)
                            print('    -------------------------------------------------------------------------------------------------------------')
                            print('\n    Creating new account for ' + str(username) + '!')
                            password = "default"
                            email = "default"

                            password = input('\n\n\n    Please choose your password: ')
                            email = input('\n    Please enter your email address: ')

                            salt = bcrypt.gensalt()
                            hashed = bcrypt.hashpw(password, salt)
                    
                            print('\n\n')
                    
                            f.write(hashed + '\n')
                            f.write(email)
                            print('    Creating new account...')
                            time.sleep(.5)
                            print('    Logging in as: ' + username)
                            time.sleep(.5)

                            newUserAccount = True

                            screen = 'stronghold'
                    except:
                        pass
            

                else:
                    screen = "login"
            else:
                if username.strip() == "":
                    print("                Error, name can't be blank!")
                else:
                    print("                Error, name can't be " + str(username) + "!")
                time.sleep(1)
                screen = "login"

#The stronghold screen is homebase for players. The page also writes the current username
#into the userStronghold object.
#
#Each player gets a "home" stronghold that can't be overrun. This page displays the stats
#for that stronghold.
#
#TO DO:
# - Flesh this out a little more. Make it prettier.
# - Add a list of owned Fiefdoms that aren't the home stronghold
#------------------------------------------------------------------------------
    if screen == "stronghold":
        os.system("clear")

        userStronghold.name = username
        userStronghold.read()
        userStronghold.ruler = username
        userStronghold.defenders = str(userStronghold.defenders)
        userStronghold.write()

        header(userStronghold.name)
        print("")
        print('    ' + textColor.WARNING + username + "'s Stronghold" + textColor.RESET)
        print("\n")



        productionCalc = 0
        maxProductionSoldiers = (int(userStronghold.goldMod) * 500)
        if int(userStronghold.defenders) > maxProductionSoldiers:
            productionCalc = ((goldOutput * int(userStronghold.goldMod)) + (int(maxProductionSoldiers) * int(userStronghold.goldMod)))

        else:
            productionCalc = ((goldOutput * int(userStronghold.goldMod)) + (int(userStronghold.defenders) * int(userStronghold.goldMod)))

        if userStronghold.home != 'True':
            userStronghold.home = 'True'
            userStronghold.write()

        #Check if anything needs to be initialized
        if FirstLaunch():
            serverMap.name = 'serverMap'
            SilentlyGenerateWorld(serverMap)
            # SilentlyPlaceStrongholdInWorldMap(userStronghold, serverMap)
            # serverMap.write()
            # userStronghold.write()
            serverMap.read()
            newUserAccount = False

        if  newUserAccount:
            serverMap.name = 'serverMap'
            serverMap.read()
            SilentlyPlaceStrongholdInWorldMap(userStronghold, serverMap)
            userStronghold.write()
            serverMap.read()
            newUserAccount = False

        print('    On a hilltop overlooking endless rolling fields, you see the only home you have ever known.')
        print('    The Fiefdom is home to ' + textColor.WARNING +  str(userStronghold.defenders) + textColor.RESET + ' highly skilled warriors, and dozens of loyal citizens.')
        print('    You also employ the services of ' + textColor.WARNING +  str(userStronghold.thieves) + textColor.RESET + ' well-trained thieves.')
        print('\n    Grow your forces to overcome the enemy. Do not let your citizens down')
        print('\n    Within your coffers, you have ' + textColor.WARNING + str(userStronghold.gold) + textColor.RESET + ' gold.')
        print('    ' + 'Production: ' + str(productionCalc) + ' gold and ' + str((int(defenderOutput) * int(attackFief.defenderMod))) + ' soldiers per hour.')
        print('    Your army of ' + textColor.WARNING + str(userStronghold.attType) + textColor.RESET + ' stands ready.')
        print('\n')

        userStronghold.read()
        art_stronghold(userStronghold.biome, userStronghold.color)

        print("    Avalible Commands:")
        print('    -------------------------------------------------------')
        print('    {1}: View Fiefdoms')
        print('    {2}: Hire and Recruit')
        print('    {3}: Upgrade and Customize')
        print('    {4}: Look Around')
        print('    {5}: World Map')
        print('    {6}: Message Board')
        print('    {7}: More')
        print('    --------------------------------------------------------')
        print('')
        command = input("    Enter your command: ")

        if command == '1':
            currentPage = 1
            screen = "fiefdoms"

        if command == '2':
            screen = 'hireAndRecruit'

        if command == '3':
            screen = 'upgradeStronghold'
        
        if command == '4':
            screen = 'viewSurroundings'
            USER_STRONGHOLD = True
            STRONGHOLD = True

        if command == '5':
            screen = 'viewMapYourStronghold'

        if command == '6':
            screen = 'messageBoard'

        if command == '7':
            screen = 'moreCommands'
        
        #The following command is for testing only!
        if command == 'devtest' or command == 'dt':
            screen = 'devTest'

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
            screen = "stronghold"

        if command == "2":
            screen = "fiefdoms"

        if command == "3":
            currentPage = 1
            screen = "garrisonSorter"

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
            screen = "garrison"
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
                screen = 'garrison'

            elif int(withdrawNum) == 0:
                os.system("clear")
                print("    Cancelling request...")
                time.sleep(1)
                screen = 'garrison'

            elif int(userStronghold.defenders) < int(withdrawNum):
                os.system("clear")
                print("    You do not have enough soldiers for that.")
                time.sleep(2)
                screen = 'garrison'

            elif int(withdrawNum) < userFiefCount:
                os.system("clear")
                print("    You have more fiefs than soldiers you want to distribute!")
                time.sleep(2)
                screen = 'garrison'

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
        screen = 'garrison'

#The fiefdoms page contains a list of Fiefdoms generated from the /fiefs directory
#
#To Do
# - add some sort of "next page" function so that the printout won't scroll
#   off the page as more players join.
# - add some sort of sorting on the list.
# - SW: This needs to be updated, as I'm not sure what happens if your username is '1', for example.
#       As I started setting up the "caps doesn't matter" stuff, I ran into a problem.
#       The file and username schema would also need to be lowercase for this to work.
#       I will come back to this later.
#-------------------------------------------------------------------------------
    if screen == "fiefdoms":
        os.system("clear")
        header(userStronghold.name)

        fiefdomCount = 0
        fiefdomMargin = 0

        print("")
        print("    Nearby Fiefdoms: ")
        print("    ------------------------------------------------------------------\n")

        #loop through each file in the /fiefs/ directory and print off the details  of each fief in a list
        for filename in os.listdir('fiefs'):
            with open(os.path.join('fiefs', filename), 'r') as f:

                tempName = filename[:-4]
                tempName = Fiefdom()
                tempName.name = filename[:-4]
                tempName.read()
                fiefdomCount = fiefdomCount + 1
                fiefdomMargin = fiefdomCount - ((currentPage - 1) * LINES_PER_PAGE)

                if (fiefdomMargin <= LINES_PER_PAGE) and (fiefdomMargin > 0):
                    if tempName.home != 'True' and tempName.ruler != userStronghold.name:
                        print ('    ' + textColor.WARNING + tempName.name + ' || Ruled by: ' + tempName.ruler + ' || Defenders: ' +
                                tempName.defenders + textColor.RESET + ' || Gold: ' + tempName.gold)

                    if tempName.home != "True" and tempName.ruler == userStronghold.name:
                        print ('    ' + textColor.CYAN + tempName.name + ' || Ruled by: ' + tempName.ruler + ' || Defenders: ' +
                                tempName.defenders + textColor.RESET + ' || Gold: ' + tempName.gold)

        if fiefdomMargin > LINES_PER_PAGE or currentPage > 1:
            print('\n    /// ' + WARNING + 'Page ' + str(currentPage) + RESET + ' ///')
        print("\n    Avalible Commands:")
        print('    -------------------------------------')
        print('    {1}: Return to Stronghold')
        print('    {2}: Manage Your Fiefdoms')
        print('    {3}: View Player Strongholds')
        if fiefdomMargin > LINES_PER_PAGE:
            print('    {4}: Next Page')

        if currentPage > 1:
            print('    {5}: Previous Page')

        print('    {Enter fiefdom name}: View Fiefdom Details')
        print('    -------------------------------------')
        print('')
        command = input("    Enter your command: ")
        #command = command.lower() #This won't work until file-naming schema is changed!

        if str(command) == '1':
            screen = "stronghold"

        if str(command) == '2':
            screen = "garrison"

        if str(command) == '3':
            currentPage = 1
            screen = "playerStrongholds"

        if fiefdomMargin > LINES_PER_PAGE:
            if str(command) == '4':
                currentPage = currentPage + 1
                screen = "fiefdoms"

        if currentPage > 1: #SW: This statement is always true if previous if statement is true. This is probably ok though.
            if str(command) == '5':
                currentPage = currentPage - 1
                screen = "fiefdoms"

        if str(command) != '1':
            #search for file to open. If there, initialize it and load data
            #then, switch to a details screen

            fileFief = 'fiefs/' + command + '.txt'
            # print ('    ' + fileFief + 'loading is happening')
            try:
                with open(fileFief, 'r') as f:
                    attackFief.name = f.readline().strip()
                    attackFief.read()

                    if str(attackFief.ruler) == str(userStronghold.ruler):
                        screen = 'homeDetails'
                    if str(attackFief.home) == 'True':
                        screen = 'stronghold'
                    if str(attackFief.ruler) != str(userStronghold.ruler):
                        screen = "enemyFiefDetails"

            except:
                print ('    the file open broke')

        os.system('clear')

#The playerStrongholds page contains a list of player strongholds generated from the /strongholds directory
#
#To Do
# - add some sort of "next page" function so that the printout won't scroll
#   off the page as more players join.
# - add some sort of sorting on the list.
# - SW: This needs to be updated, as I'm not sure what happens if your username is '1', for example.
#       As I started setting up the "caps doesn't matter" stuff, I ran into a problem.
#       The file and username schema would also need to be lowercase for this to work.
#       I will come back to this later.
#-------------------------------------------------------------------------------
    if screen == "playerStrongholds":

        os.system("clear")

        header(userStronghold.name)

        strongholdCount = 0
        strongholdMargin = 0

        print("")
        print("    Nearby Strongholds: ")
        print("    ------------------------------------------------------------------\n")

        #loop through each file in the /fiefs/ directory and print off the details of each stronghold in a list
        for filename in os.listdir('strongholds'):
            with open(os.path.join('strongholds', filename), 'r') as f:

                tempName = filename[:-4]
                tempName = Stronghold()
                tempName.name = filename[:-4]
                tempName.read()
                strongholdCount = strongholdCount + 1
                strongholdMargin = strongholdCount - ((currentPage - 1) * LINES_PER_PAGE)
                homeStatus = " "

                if  (strongholdMargin <= LINES_PER_PAGE) and (strongholdMargin > 0):
                    if tempName.home == "True" and tempName.ruler != userStronghold.name:
                        homeStatus = "Home Stronghold"
                        print ('    ' + textColor.WARNING + 'The Stronghold of ' +  tempName.name + ' || Defenders: ' +
                                tempName.defenders + textColor.RESET + ' || Gold: ' + tempName.gold)

                    if tempName.home == "True" and tempName.ruler == userStronghold.name:
                        print ('    ' + textColor.GREEN + 'The Stronghold of ' + tempName.name + ' || Defenders: ' +
                                tempName.defenders + textColor.RESET + ' || Gold: ' + tempName.gold)

        if strongholdMargin > LINES_PER_PAGE or currentPage > 1:
            print('/// ' + WARNING + 'Page ' + str(currentPage) + RESET + ' ///\n')
        print("\n    Avalible Commands:")
        print('    -------------------------------------')
        print('    {1}: Return to Stronghold')
        print('    {2}: Manage Your Fiefdoms')
        print('    {3}: View Fiefdoms')
        if strongholdMargin > LINES_PER_PAGE:
            print('    {4}: Next Page')

        if currentPage > 1:
            print('    {5}: Previous Page')

        print('    {Enter stronghold owner name}: View Stronghold Details')
        print('    -------------------------------------')
        print('')
        command = input("    Enter your command: ")
        #command = command.lower() #This won't work until file-naming schema is changed!

        if str(command) == '1':
            screen = "stronghold"

        if str(command) == '2':
            screen = "garrison"

        if str(command) == '3':
            currentPage = 1
            screen = "fiefdoms"

        if strongholdMargin > LINES_PER_PAGE:
            if str(command) == '4':
                currentPage = currentPage + 1
                screen = "playerStrongholds"

        if currentPage > 1:
            if str(command) == '5':
                currentPage = currentPage - 1
                screen = "playerStrongholds"

        if str(command) != '1':
            #search for file to open. If there, initialize it and load data
            #then, switch to a details screen

            fileFief = 'strongholds/' + command + '.txt'
            # print ('    ' + fileFief + 'loading is happening')
            try:
                with open(fileFief, 'r') as f:
                    attackStronghold.name = f.readline().strip()
                    attackStronghold.read()

                    if str(attackStronghold.ruler) == str(userStronghold.ruler):
                        screen = 'homeDetails'
                    if str(attackStronghold.home) == 'True':
                        screen = 'stronghold'
                    if str(attackStronghold.ruler) != str(userStronghold.ruler):
                        screen = "enemyStrongholdDetails"

            except:
                print ('    the file open broke')

        os.system('clear')


#The homeDetails page gets called when a user tries to view their own Fiefdom
#From this page, they'll be able to add and withdraw troops, make upgrades,
#etc
#
#To Do
# - make it prettier
# - add some sort of upgrade system for defenses
#------------------------------------------------------------------------------

    if screen == "homeDetails":
        os.system("clear")
        header(userStronghold.name)
        attackFief.read()

        productionCalc = 0

        maxProductionSoldiers = (int(attackFief.goldMod) * 500)

        if int(attackFief.defenders) > maxProductionSoldiers:
            productionCalc = ((goldOutput * int(attackFief.goldMod)) + (int(maxProductionSoldiers) * int(attackFief.goldMod)))

        else:
            productionCalc = ((goldOutput * int(attackFief.goldMod)) + (int(attackFief.defenders) * int(attackFief.goldMod)))

        if attackFief.biome == MOUNTAIN:
            currentBiome = 'Mountain'
        elif attackFief.biome == PLAINS:
            currentBiome = 'Plains'
        elif attackFief.biome == FOREST:
            currentBiome = 'Forest'

        print('')
        print('    You rule the fiefdom of ' + attackFief.name)
        print('')
        print('    Status Report:')
        print('    ')
        print('    Defenders: ' + attackFief.defenders)
        print('    Gold: ' + attackFief.gold)
        print('    Defensive Strategy: ' + attackFief.defType)
        print('    Biome: ' + currentBiome)
        print('    Production: ' + str(productionCalc) + ' gold and ' + str(defenderOutput * int(attackFief.defenderMod))
                + ' soldiers per hour.')
        print("\n")

        printFiefArt(attackFief)

        print('')
        print("    Avalible Commands:")
        print('    -------------------------------------------------------')
        print('    {1}: Return to Stronghold')
        print('    {2}: View Fiefdoms')
        print('    {3}: Deploy Additional Forces')
        print('    {4}: Withdraw Forces')
        print('    {5}: Withdraw Gold')
        print('    {6}: Upgrades')
        print('    {7}: Look Around')
        print('    {8}: World Map')
        print('    -------------------------------------------------------')
        print('')
        command = input("    Enter your command: ")

        if command == "1":
            screen = "stronghold"

        if command == "2":
            currentPage = 1
            screen = "fiefdoms"

        if command == "3":
            screen = 'deploy'

        if command == "4":
            screen = 'withdraw'

        if command == "5":
            screen = 'withdrawGold'

        if command == '6':
            screen = 'upgradeFiefMenu'

        if command == '7':
            screen = 'viewSurroundings'
            STRONGHOLD = False

        if command == '8':
            screen = 'viewMapCurrentFief'

#This is a menu for additional features
#----------------------------------------------------------------------------------
    if screen == "upgradeFiefMenu":
        os.system("clear")
        
        header(userStronghold.name)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print("    Avalible Commands:")
        print('    -------------------------------------------------------')
        print('    {1}: Go Back')
        print('    {2}: Upgrade Defenses')
        print('    {3}: Upgrade Farms')
        # print('    {4}: Upgrade Training')
        print('    --------------------------------------------------------')
        print('')
        command = input("    Enter your command: ")

        if command == '1':
            screen = 'homeDetails'

        if command == '2':
            screen = 'upgradeDefense'

        if command == '3':
            screen = 'upgradeFarm'

        if command == '4':
            screen = 'upgradeFiefMenu'

#The withdraw gold screen allows players to withdraw gold from a ruled fiefdom
#
#To Do
# -
#
#------------------------------------------------------------------------------
    if screen == "withdrawGold":
        os.system("clear")
        header(userStronghold.name)

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

        screen = "fiefdoms"

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

        header(userStronghold.name)

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
            screen = 'homeDetails'

        if (int(userStronghold.defenders) < int(deployNum)) and int(deployNum) > 0:
            os.system("clear")
            header(userStronghold.name)
            print("    You do not have enough soldiers for that")
            time.sleep(2)
            screen = 'homeDetails'

        if deployNum == 0:
            screen = "homeDetails"

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
            screen = 'homeDetails'

        time.sleep(1)
#The withdraw screen allows players to withdraw forces from a ruled fiefdom
#
#To Do
# -
#
#------------------------------------------------------------------------------
    if screen == "withdraw":
        os.system("clear")
        header(userStronghold.name)
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
            time.sleep(2)
            screen = 'homeDetails'

        if (int(attackFief.defenders) < int(withdrawNum)) and int(withdrawNum) > 0:
            os.system("clear")
            print("    You do not have enough soldiers for that")
            time.sleep(2)
            screen = 'homeDetails'

        if (int(attackFief.defenders) >= int(withdrawNum)) and int(withdrawNum) > 0:
            print('    Returning ' + str(withdrawNum) + ' soldiers back home')

            attackFief.defenders = str(int(attackFief.defenders) - int(withdrawNum))
            attackFief.write()
            attackFief.read()

            userStronghold.defenders = str(int(userStronghold.defenders) + int(withdrawNum))
            userStronghold.write()
            userStronghold.read()

            tempInput = input('    Press Enter to Continue')
            screen = 'homeDetails'

        if int(withdrawNum) == 0:
            print('    No soldiers selected')
            screen = "homeDetails"

            attackFief.defenders = str(int(attackFief.defenders) - int(withdrawNum))
            attackFief.write()
            attackFief.read()

            userStronghold.defenders = str(int(userStronghold.defenders) + int(withdrawNum))
            userStronghold.write()
            userStronghold.read()

            tempInput = input('    Press Enter to Continue')
            screen = 'homeDetails'

#This is the details page for enemy Fiefdoms
#
#To Do
# - Make it prettier
# - In the future, add a way to obscure exact numbers?
# - Add ability to attempt spying to gain info on defenses and upgrades
#------------------------------------------------------------------------------
    if screen == "enemyFiefDetails":
        os.system("clear")
        header(userStronghold.name)

        if attackFief.biome == MOUNTAIN:
            currentBiome = 'Mountain'
        elif attackFief.biome == PLAINS:
            currentBiome = 'Plains'
        elif attackFief.biome == FOREST:
            currentBiome = 'Forest'

        print("")
        print('    Now viewing the fiefdom of ' + attackFief.name)
        print('    This fiefdom is ruled by ' + attackFief.ruler)
        print('    -------------------------------------------------------------------------')
        print('    Your scouts return early in the morning, bringing back reports of the enemy fiefdom.')
        print('    ' + attackFief.name + ' looks to have ' + str(attackFief.defenders) + ' fighters.')
        print('    Defense Type: ' + attackFief.defType)
        print('    Biome: ' + currentBiome)
        print('    -------------------------------------------------------------------------')

        print("\n")
        
        printFiefArt(attackFief)

        print("")

        print("    Avalible Commands:")
        print('    -------------------------------------')
        print('    {1}: Return to Stronghold')
        print('    {2}: View Fiefdoms')
        print('    {3}: Attack')
        print('    {4}: Look Around')
        print('    {5}: World Map')
        print('    -------------------------------------')
        print('')

        command = input("    Enter your command: ")

        if command == "1":
            screen = "stronghold"

        if command == "2":
            currentPage = 1
            screen = "fiefdoms"

        if command == "3":
            screen = 'battle'
        
        if command == "4":
            screen = 'viewSurroundings'
            STRONGHOLD = False

        if command == "5":
            screen = 'viewMapCurrentFief'

#This is the details page for enemy Strongholds
#
#To Do
# - Make it prettier
# - In the future, add a way to obscure exact numbers?
# - Add ability to attempt spying to gain info on defenses and upgrades
#------------------------------------------------------------------------------
    if screen == "enemyStrongholdDetails":
        os.system("clear")
        header(userStronghold.name)
        attackStronghold.read()
        print("")
        print('    Now viewing the stronghold of ' + attackStronghold.name)
        print('    -------------------------------------------------------------------------')
        print('    Your scouts return early in the morning, bringing back reports of the enemy fiefdom.')
        print('    ' + attackStronghold.name + ' looks to have ' + str(attackStronghold.defenders) + ' fighters.')
        print('    Their coffers contain ' + str(attackStronghold.gold) + ' gold.')
        print('    -------------------------------------------------------------------------')
        print("    \n\n")

        art_stronghold(attackStronghold.biome, attackStronghold.color)

        print("    \n\n")
        print("    Avalible Commands:")
        print('    -------------------------------------')
        print('    {1}: Return to Stronghold')
        print('    {2}: View Fiefdoms')
        print('    {3}: Send Thieves To Steal Gold')
        print('    {4}: Look Around')
        print('    {5}: World Map')
        print('    -------------------------------------')
        print('')

        command = input("    Enter your command: ")

        if command == "1":
            screen = "stronghold"

        if command == "2":
            currentPage = 1
            screen = "fiefdoms"

        if command == "3":
            screen = "thiefPage"

        if command == "4":
            screen = "viewSurroundings"
            STRONGHOLD = True
            USER_STRONGHOLD = False
            
        if command == "5":
            screen = "viewMapEnemyStronghold"


#This is the theif attack page, which you will see when trying
#to steal gold from another player
#
#------------------------------------------------------------------------------
    if screen == "thiefPage":
        os.system("clear")
        header(userStronghold.name)

        #this is where the battle logic happens!
        print('    \n\n')
        print('    ' + attackStronghold.name + '\'s Stronghold has ' + attackStronghold.defenders + ' soldiers keeping a watchful eye. You have ' + str(userStronghold.thieves) + ' who are ready for a heist.')
        print('    Rumor has it that their coffers hold ' + str(attackStronghold.gold) + ' gold pieces.')
        print('    Your thieves work best in groups of 3 per 100 soldiers. Too few and they lack manpower. Too many and they draw unwanted attention.')
        print('    ')
        print('        ...\n')
        time.sleep(1)
        
        desiredAttackers = 0
        attackers = 0

        if int(userStronghold.thieves) > 0:
            try:
                desiredAttackers = int(input('    Enter the number of thieves you would like to send on this mission: '))
            except:
                print('\n\n    That is not a valid option, sorry!')
                Attackers = 0

            if int(desiredAttackers) <= int(userStronghold.thieves)  and int(desiredAttackers) > 0:
    #            print('desieredAttackers = ' + str(desiredAttackers))
                attackers = int(desiredAttackers)
            else:
                print('    invalid number')
                attackers = 0
        

            goldToSteal = attackStronghold.gold

    #        print('Thieves Attacking: ' + str(attackers))
    #        print('Defending Stronghold: ' + attackStronghold.name)
    #        print('Attacking Stronghold: ' + str(userStronghold.name))
    #        print('Potential Gold To Be Stolen: ' + str(attackStronghold.gold))
    #        print('Defenders: ' + str(attackStronghold.defenders))
    #        print('\n\nThief Logic Time: ')
            
            thiefs = float(attackers)
            defs = float(attackStronghold.defenders)
            potentialGold = float(attackStronghold.gold)
            maxCarriedGold = 0
            
            ratio = float(thiefs / defs)

            chance = float(4.4 + (ratio * 4180) + (-61607 * (ratio * ratio)))

            maxCarriedGold = thiefs * (potentialGold // 10)
            maxCarriedGold = maxCarriedGold * (1 + thiefs // 2)

            
    #        print('Percent Chance of Success: ' + str(chance))
    #        print('Max Stolen Gold = ' + str(maxCarriedGold))
            
            if int(maxCarriedGold) > int(attackStronghold.gold):
                maxCarriedGold = int(attackStronghold.gold)
            
            randomNum = roll(0) * 5
    #        print('\nRandom Roll is: ' + str(randomNum))

            if int(randomNum) > int(chance) and int(attackers) > 0:
                
                print('    Despite their valient efforts, your thieves have been captured.\n    This mission is a failure.')
                
                userStronghold.thieves = int(userStronghold.thieves) - int(attackers)
                userStronghold.write()
                userStronghold.read()

                print('    You have ' + str(userStronghold.thieves) + ' thieves remaining.')

            elif int(randomNum) <= int(chance) and int(attackers) > 0:
                print('    Success! Your thieves return with pocketsfull of gold!\n    Your thieves managed to secure ' + str(maxCarriedGold) + ' gold for the stronghold!')
                
                userStronghold.gold = int(maxCarriedGold) + int(userStronghold.gold)
                userStronghold.write()
                userStronghold.read()

                attackStronghold.gold = int(attackStronghold.gold) - int(maxCarriedGold)
                attackStronghold.write()
                attackStronghold.read()

                print('    You now have ' + str(userStronghold.gold) + ' gold.')

            else:
                print('    Nothing Happened')
        
        else:
            print("    You don't have any thieves hired!")

        tempInput = input('    Press Enter To Continue')
        screen = "enemyStrongholdDetails"


#The "battle" page simulates a battle between two Fiefdoms. This is currently the most
#complicated page and could use some cleaning up.
#
#To Do
# - add a better system for determining winners and casualties. The current system
#   is almost entirely random, which is bad.
# - make it prettier
#
#------------------------------------------------------------------------------
    if screen == "battle":
        os.system("clear")
        header(userStronghold.name)

        #Idea: We're going to do a DnD style battle using D20s and modifiers.
        #roll(mod) is going to give the result of a roll plus modifiers and is
        #defined at the start of the file.

        #This if statement prevents players from attacking a player's home stronghold
        #Eventually this will be replaced with a formula that allows you to attack
        #for gold
        if attackFief.home == 'True':
            os.system('clear')
            print('    You are unable to claim a player\'s home stronghold')
            time.sleep(3)
            screen = 'stronghold'

        #this is where the battle logic happens!
        if attackFief.home == 'False':
            print('\n\n    This battle is between ' + attackFief.name + ' and ' + userStronghold.name)
            print('\n\n    Simulating Battle...')
            time.sleep(1)
            print('\n        ...\n')
            time.sleep(1)

            attackers = int(userStronghold.defenders)
            defenders = int(attackFief.defenders)

            defenseLosses = 0
            attackLosses = 0
            attackMod = int(userStronghold.attLevel)
            defenseMod = int(attackFief.defLevel)

            for i in range(3):

                for i in range(int(4)):
                    maxDeaths = attackers // 4

                    while (defenders > 1 and attackers > 1) and maxDeaths > 0 :
                        defense = roll(defenseMod)
                        attack = roll(attackMod)
                        maxDeaths = maxDeaths - 1
                        if attack > defense:
                            defenders = defenders - 1
                            defenseLosses = defenseLosses + 1
                        if attack <= defense:
                            attackers = attackers - 1
                            attackLosses = attackLosses + 1

            print('    \n')
            print('    ------------------------------------------------------------------------------')
            print('    -----------------------------Battle Results-----------------------------------')
            print('    ------------------------------------------------------------------------------')
            print('    \n')
            print('    ' + userStronghold.ruler + ' lost ' + str(attackLosses) + ' soldiers')
            print('    ' + attackFief.ruler + ' lost ' + str(defenseLosses) + ' soldiers')
            print('    \n')
            print('    ------------------------------------------------------------------------------')
            print('    ------------------------------------------------------------------------------')
            print('    \n\n')

            #if the current player wins
            if attackers > defenders:
                print('    After a hard fought battle, your weary forces remain standing')
                print('    You are the new ruler of ' + attackFief.name)

                attackFief.defenders = defenders
                attackFief.ruler = userStronghold.ruler
                attackFief.write()

                userStronghold.defenders = attackers
                userStronghold.write()

                userStronghold.gold = str(int(userStronghold.gold) + int(attackFief.gold))
                print('    You now have a total of ' + str(userStronghold.gold) + ' gold!')
                attackFief.gold = str('0')

                userStronghold.write()
                attackFief.write()

            #if the other player wins
            if attackers <= defenders:
                print('    Although your soldiers fought valiantly, they were unable to overcome ' + attackFief.ruler + '\'s forces')
                print('    Your forces, now many fewer in number, begin the long march home.')

                attackFief.defenders = defenders
                attackFief.write()

                userStronghold.defenders = attackers
                userStronghold.write()


            time.sleep(1)
            nothing = input('    Press Enter to Continue')
            currentPage = 1
            screen = "fiefdoms"


#This is a list of external pages from other files
#------------------------------------------------------------------------------
    screen = MoreMenu(screen, userStronghold)
    screen = UpgradesAndCustomizations(screen, userStronghold)
    screen = HireMenu(screen, userStronghold)
    screen = ViewMapAndSurroundings(screen, userStronghold, attackStronghold)
    screen = SandboxMenu(screen)
    screen = DevTestMenu(screen, userStronghold)

#eof

