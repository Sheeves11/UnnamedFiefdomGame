#!/usr/bin/env python

from globals import *
import bcrypt
from getpass import getpass
from menu_devtest import *
from menu_sandbox import *
from menu_viewMapAndSurroundings import *
from menu_more import *
from menu_upgradesAndCustomizations import *
from menu_hire import *
from menu_garrison import *
from menu_fiefBuildings import *
from menu_combatAndThievery import *
from menu_fiefCommands import *

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
#   [fiefdomgame.py]:
#           login
#           stronghold
#           fiefdoms
#           playerStrongholds
#           ownedFiefDetails
#           enemyFiefDetails
#           enemyStrongholdDetails
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
#           upgradeFiefMenu
#           upgradeAttack
#           upgradeFarm
#           upgradeDefense
#           changeStrongholdColor
#           setStrongholdMessage
#   menu_hire.py:
#           hireAndRecruit
#           thieves
#           mercs
#   menu_garrison.py:
#           garrison
#           garrisonSorter
#   menu_combatAndThievery
#           thiefPage
#           battle
#   menu_fiefCommands.py:
#           withdrawGold
#           withdrawForces
#           deploy
#   menu_fiefBuildings.py:
#           WIP
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
                userPass = getpass('    Enter your password: ')

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

                            password = getpass('\n\n\n    Please choose your password: ')
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
        print('    Message: ' + userStronghold.strongholdMessage)
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
        print('    {2}: View Player Strongholds')
        print('    {3}: Hire and Recruit')
        print('    {4}: Upgrade and Customize')
        print('    {5}: Look Around')
        print('    {6}: World Map')
        print('    {7}: Message Board')
        print('    {8}: More')
        print('    --------------------------------------------------------')
        print('')
        command = input("    Enter your command: ")

        if command == '1':
            currentPage = 1
            screen = "fiefdoms"

        if command == '2':
            screen = 'playerStrongholds'

        if command == '3':
            screen = 'hireAndRecruit'

        if command == '4':
            screen = 'upgradeStronghold'
        
        if command == '5':
            screen = 'viewSurroundings'
            USER_STRONGHOLD = True
            STRONGHOLD = True

        if command == '6':
            screen = 'viewMapYourStronghold'

        if command == '7':
            screen = 'messageBoard'

        if command == '8':
            screen = 'moreCommands'
        
        #The following command is for testing only!
        if command == 'devtest' or command == 'dt':
            screen = 'devTest'


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
                        screen = 'ownedFiefDetails'
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
                        screen = 'ownedFiefDetails'
                    if str(attackStronghold.home) == 'True':
                        screen = 'stronghold'
                    if str(attackStronghold.ruler) != str(userStronghold.ruler):
                        screen = "enemyStrongholdDetails"

            except:
                print ('    the file open broke')

        os.system('clear')


#The ownedFiefDetails page gets called when a user tries to view their own Fiefdom
#From this page, they'll be able to add and withdraw troops, make upgrades,
#etc
#
#To Do
# - make it prettier
# - add some sort of upgrade system for defenses
#------------------------------------------------------------------------------

    if screen == "ownedFiefDetails":
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
        print('    {1}: Return to Stronghold        {9}: Resource Outposts') 
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
            screen = 'withdrawForces'

        if command == "5":
            screen = 'withdrawGold'

        if command == '6':
            screen = 'upgradeFiefMenu'

        if command == '7':
            screen = 'viewSurroundings'
            STRONGHOLD = False

        if command == '8':
            screen = 'viewMapCurrentFief'

        if command == '9':
            screen = 'outposts'

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
        print('    Your scouts return early in the morning, bringing back reports of the enemy stronghold.')
        print('    ' + attackStronghold.name + ' looks to have ' + str(attackStronghold.defenders) + ' fighters and their coffers contain ' + str(attackStronghold.gold) + ' gold.')
        print('    -------------------------------------------------------------------------')      
        print('    The enemy has a message posted on the path near the gate.')
        print('    It reads:  { ' + attackStronghold.strongholdMessage + ' }' )
        print('    -------------------------------------------------------------------------')
        print("    \n\n")

        art_stronghold(attackStronghold.biome, attackStronghold.color)

        print("    \n\n")
        print("    Avalible Commands:")
        print('    -------------------------------------')
        print('    {1}: Return to Stronghold')
        print('    {2}: View Player Strongholds')
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
            screen = "playerStrongholds"

        if command == "3":
            screen = "thiefPage"

        if command == "4":
            screen = "viewSurroundings"
            STRONGHOLD = True
            USER_STRONGHOLD = False
            
        if command == "5":
            screen = "viewMapEnemyStronghold"


#------------------------------------------------------------------------------
#This is a list of external menus (from other files)
#------------------------------------------------------------------------------
    screen = MoreMenu(screen, userStronghold)
    screen = UpgradesAndCustomizations(screen, userStronghold)
    screen = FiefCommandsMenu(screen, userStronghold)
    screen = FiefBuildingsMenu(screen, userStronghold)
    screen = HireMenu(screen, userStronghold)
    screen = GarrisonMenu(screen, userStronghold)
    screen = ViewMapAndSurroundings(screen, userStronghold, attackStronghold)
    screen = CombatAndThieveryMenu(screen, userStronghold, attackStronghold)
    screen = SandboxMenu(screen)
    screen = DevTestMenu(screen, userStronghold)

#eof