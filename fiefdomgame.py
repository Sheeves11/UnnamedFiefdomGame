#!/usr/bin/env python

import os
import time
import random
import bcrypt
from classes import *
from worldmap import *
from os.path import exists
from art import *
from tests.sandbox import *

'''

Welcome to the Unnamed Fiefdom Game!

This game was designed and written by
Mike Quain of the University of Arkansas

More info can be found at
github.com/Sheeves11/UnnamedFiefdomGame

'''

#global variables
loop = True
screen = "login"
currentUsername = 'default'
tempName = {}

#fiefdom page variables
LINES_PER_PAGE = 10  #SET THIS TO 30 OR SOMETHING LATER! 10 IS FOR TESTING!
currentPage = 1
userStrongholdCount = 0


#hourly production values
#these should be changed to match the values in fiefdombackend.py
goldOutput = 100
defenderOutput = 3

#initial screen clear
os.system("clear")

#create some default objects that we'll write over later
attackFief = Fiefdom()
userStronghold = Stronghold()
attackStronghold = Stronghold()
serverMap = Map()
testMap = TestMap() #This is for users to have fun messing with the map generator
firstMapRead = True
newUserAccount = False

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

        userStronghold = Stronghold()
        username = input("                Enter your username: ")
        currentUsername = username

        userPath = ('users/' + username + '.txt')
        
        if exists(userPath) == True:
            
            usernameFile = "users/" + username + ".txt"
            with open(usernameFile, 'r') as f:
                os.system('clear')
                header()
                
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
            #if "username.txt" does not exist, create it. The file only contains a name and password for now.
            newUser = input('\n                New user detected. Make a new account? (y/n): ')
            
            if newUser == 'y':
                try:
                    usernameFile = "users/" + username + ".txt"
                    with open(usernameFile, 'x') as f:
                        f.write(username + '\n')
                        os.system('clear')
                        header()
                
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

        header()
        print("\n")
        print('     ' + textColor.WARNING + username + "'s Stronghold" + textColor.RESET)
        print("\n")

        userStronghold.name = username
        userStronghold.read()
        userStronghold.ruler = username
        userStronghold.defenders = str(userStronghold.defenders)
        userStronghold.write()

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
            SilentlyGenerateWorld(serverMap)
        if  newUserAccount:
            serverMap.name = 'serverMap'
            serverMap.read()
            SilentlyPlaceStrongholdInWorldMap(userStronghold, serverMap)
            # userStronghold.write()
            serverMap.read()
            newUserAccount = False

        print('     On a hilltop overlooking endless rolling fields, you see the only home you have ever known.')
        print('     The Fiefdom is home to ' + textColor.WARNING +  str(userStronghold.defenders) + textColor.RESET + ' highly skilled warriors, and dozens of loyal citizens.')
        print('     You also employ the services of ' + textColor.WARNING +  str(userStronghold.thieves) + textColor.RESET + ' well-trained thieves.')
        print('\n     Grow your forces to overcome the enemy. Do not let your citizens down')
        print('\n     Within your coffers, you have ' + textColor.WARNING + str(userStronghold.gold) + textColor.RESET + ' gold.')
        print('     ' + 'Production: ' + str(productionCalc) + ' gold and ' + str((int(defenderOutput) * int(attackFief.defenderMod))) + ' soldiers per hour.')
        print('     Your army of ' + textColor.WARNING + str(userStronghold.attType) + textColor.RESET + ' stands ready.')
        print('\n')

        art_stronghold(userStronghold.biome, userStronghold.color)

        print("     Avalible Commands:")
        print('     -------------------------------------------------------')
        print('     {1}: View Nearby Fiefdoms        {9}: Hire Thieves')
        print('     {2}: Hire Mercenaries            {10}: View World Map')
        print('     {3}: Upgrade Attack              {11}: Stronghold Color')
        print('     {4}: Garrison Soldiers')
        print('     {5}: About')
        print('     {6}: Upcoming Features')
        print('     {7}: Message Board')
        print('     {8}: View Past Winners')
        print('     --------------------------------------------------------')
        print('\n')
        command = input("     Enter your command: ")

        if command == '1':
            currentPage = 1
            screen = "fiefdoms"

        if command == '2':
            screen = 'mercs'

        if command == '3':
            screen = 'upgradeFiefAtt'

        if command == '4':
            screen = 'garrison'

        if command == '5':
            screen = 'about'

        if command == '6':
            screen = 'features'

        if command == '7':
            screen = 'board'

        if command == '8':
            screen = 'pastWinners'

        if command == '9':
            screen = 'thieves'

        if command == '10':
            screen = 'viewMapYourStronghold'

        if command == '11':
            screen = 'changeStrongholdColor'
        
        #The following command is for testing only!
        if command == 'devtest' or command == 'dt':
            screen = 'devTest'

#This is the screen for the message board.
#----------------------------------------------------------------------------------
    if screen == "board":
        os.system("clear")

        header()

        print('\n    Welcome to the message board! Keep it friendly :)')
        print('\n    --------------------------------------------------------------------------------------\n')

        #print off recent messages
        #dump the last 30 lines of chatlog.log to the screen
        with open('chatlog.log', "r") as logfile:
            lines = logfile.readlines()
            last_lines = lines[-30:]
            last_lines = [line[:-1] for line in last_lines]
            for i in last_lines:
                print ('    ' + i)

        print('\n    --------------------------------------------------------------------------------------\n\n')
        tempMessage = input("    Type your message here or type \"leave\" to visit your stronghold:\n\n    ")
        if tempMessage == 'leave':
            screen = 'stronghold'

        elif tempMessage == 'truncate chat':
            log = open("chatlog.log", "r+")
            log.truncate(0)
            log.close()
        else:
            #add tempMessage to the chat log
            with open('chatlog.log', 'a') as log:
                log.write(userStronghold.name + ': ' + str(tempMessage) + '\n')

            #refresh this page
            screen = 'board'

# This is the screen for displaying past winners. Update it whenever we have a new winner
#----------------------------------------------------------------------------------
    if screen == "pastWinners":
        os.system("clear")
        header()
        print('\n    These are your honorable past winners of Unnamed Fiefdom Game')
        print('\n    --------------------------------------------------------------------------------------\n')
        print('\n    Pre-Release (12/20/21): Steelwing\n')
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        tempInput = input('    Press Enter To Return To Stronghold\n    ')
        screen = 'stronghold'




#This is the screen for purchacing soldiers
#----------------------------------------------------------------------------------
    if screen == "thieves":
        #define the cost of a soldier here
        thiefCost = 1000

        os.system("clear")
        header()

        print('''
            
            
            
        As in all cities, your stronghold is home to a number of seedy characters who frequent the criminal underbelly
        of society. For a price, they will be loyal to you.
        
        Thieves do not contribute to your gold production, but they can infilitrate other player strongholds
        and return with stolen gold.
        ''')

        print('\n\n\n        You currently have ' + str(userStronghold.thieves) + ' thieves and ' +  str(userStronghold.gold) + ' gold.')

        print('        You can hire thieves for ' + str(thiefCost) + ' gold each')

        upgradeInput = input('\n        Enter the number of thieves you would like to hire: ')

        try:
            int(upgradeInput)
        except:
            upgradeInput = '0'

        if int(upgradeInput) == 0:
            print("        No changes were made!")

        elif int(upgradeInput) < 0:
            print("        You can't hire a negative number of thieves")

        elif (int(upgradeInput) * thiefCost) <=  int(userStronghold.gold):
            userStronghold.thieves = str(int(userStronghold.thieves) + int(upgradeInput))
            userStronghold.gold = str(int(userStronghold.gold) - (thiefCost * int(upgradeInput)))
            userStronghold.write()
            userStronghold.read()

        else:
            print("        You need more gold first!")

        print("\n\n\n\n\n\n\n\n\n")

        print("        Avalible Commands:")
        print('        -------------------------------------')
        print('        {1}: Return to Stronghold')
        print('        {2}: View Nearby Fiefdoms')
        print('        -------------------------------------')
        print('\n')
        command = input("        Enter your command: ")

        if command == "1":
            screen = "stronghold"
        if command == "2":
            currentPage = 1
            screen = "fiefdoms"


#This is the screen for purchacing soldiers
#----------------------------------------------------------------------------------
    if screen == "mercs":
        #define the cost of a soldier here
        mercCost = 10

        os.system("clear")
        header()

        print('You currently have ' + str(userStronghold.defenders) + ' soldiers and ' +  str(userStronghold.gold) + ' gold.')

        print('You can hire mercinaries for ' + str(mercCost) + ' gold each?')

        upgradeInput = input('\nHow many mercinaries would you like to hire?\n')

        try:
            int(upgradeInput)
        except:
            upgradeInput = '0'

        if int(upgradeInput) == 0:
            print("No changes were made!")

        elif int(upgradeInput) < 0:
            print("You can't hire a negative number of soldiers")

        elif (int(upgradeInput) * mercCost) <=  int(userStronghold.gold):
            userStronghold.defenders = str(int(userStronghold.defenders) + int(upgradeInput))
            userStronghold.gold = str(int(userStronghold.gold) - (mercCost * int(upgradeInput)))
            userStronghold.write()
            userStronghold.read()

        else:
            print("You need more gold first!")

        print("\n\n\n\n\n\n\n\n\n")

        print("Avalible Commands:")
        print('-------------------------------------')
        print('{1}: Return to Stronghold')
        print('{2}: View Nearby Fiefdoms')
        print('-------------------------------------')
        print('\n')
        command = input("Enter your command: ")

        if command == "1":
            screen = "stronghold"
        if command == "2":
            currentPage = 1
            screen = "fiefdoms"

#This is the screen for viewing users owned fiefs and for garrisoning soldiers
#----------------------------------------------------------------------------------
    if screen == "garrison":
        os.system("clear")

        header()

        userStrongholdCount = 0

        print('\n    Fiefs under your rule: \n')
        for filename in os.listdir('fiefs'):
            with open(os.path.join('fiefs', filename), 'r') as f:

                tempName = filename[:-4]
                tempName = Fiefdom()
                tempName.name = filename[:-4]
                tempName.read()

                if tempName.home != "True" and tempName.ruler == userStronghold.name:
                    userStrongholdCount = userStrongholdCount + 1
                    print (textColor.CYAN + tempName.name + ' || Ruled by: ' + tempName.ruler + ' || Defenders: ' +
                            tempName.defenders + textColor.RESET + ' || Gold: ' + tempName.gold)

        print('\n\n\n\n\n\n\n\n\n\n')
        print("     Avalible Commands:")
        print('     -------------------------------------')
        print('     {1}: Select Soldiers to Garrison')
        print('     {2}: Return to Stronghold')
        print('     {3}: View Nearby Fiefdoms')
        print('     -------------------------------------')
        print('\n')
        command = input("     Enter your command: ")

        if command == "1":
            screen = "garrisonSorter"

        if command == "2":
            screen = "stronghold"

        if command == "3":
            currentPage = 1
            screen = "fiefdoms"

#This is the screen for distributing a user's soldiers evenly among fiefs they control
#----------------------------------------------------------------------------------
    if screen == "garrisonSorter":
        os.system("clear")

        header()

        print("\n\n")
        print('Currently Ruled Fiefs: ' + str(userStrongholdCount))
        print('Current Number of Soldiers in Stronghold: ' + str(userStronghold.defenders))
        print('\n')
        time.sleep(1)
        if userStrongholdCount == 0:
            print('You control no fiefs you can distribute to! \n')
            time.sleep(2)
            screen = "garrison"
        else:
            withdrawNum = input('Enter the number of soldiers you would like to evenly distrubute among these ' + str(userStrongholdCount) + ' fiefs: ')
            time.sleep(1)

            try:
                int(withdrawNum)
            except:
                withdrawNum = '0'

            if int(withdrawNum) < 0:
                os.system("clear")
                print("You cannot distribute a negative number of soldiers. \n\nThat doesn't even make sense.")
                time.sleep(2)
                screen = 'garrison'

            elif int(withdrawNum) == 0:
                os.system("clear")
                print("Cancelling request...")
                time.sleep(1)
                screen = 'garrison'

            elif int(userStronghold.defenders) < int(withdrawNum):
                os.system("clear")
                print("You do not have enough soldiers for that.")
                time.sleep(2)
                screen = 'garrison'

            elif int(withdrawNum) < userStrongholdCount:
                os.system("clear")
                print("You have more fiefs than soldiers you want to distribute!")
                time.sleep(2)
                screen = 'garrison'

            else:
                print('Garrisoning ' + str(withdrawNum) + ' soldiers across ' + str(userStrongholdCount) + ' Fiefs...')

                time.sleep(1)

                benchedSoldiers = int(withdrawNum) % userStrongholdCount
                outgoingSoldierGroups = round((int(withdrawNum) - benchedSoldiers)/userStrongholdCount)

                if benchedSoldiers > 0:
                    print(str(benchedSoldiers) + ' soldiers were held back to make even groups of ' + str(outgoingSoldierGroups) + '.')

                print('\n')

                for filename in os.listdir('fiefs'):
                    with open(os.path.join('fiefs', filename), 'r') as f:

                        tempName = filename[:-4]
                        tempName = Fiefdom()
                        tempName.name = filename[:-4]
                        tempName.read()

                        homeStatus = " "

                        if tempName.home != "True" and tempName.ruler == userStronghold.name:
                            print(tempName.name + ' had ' + str(tempName.defenders) + ' soldier(s).')
                            time.sleep(0.3)
                            tempName.defenders = str(int(tempName.defenders) + outgoingSoldierGroups)
                            tempName.write()
                            tempName.read()
                            print(tempName.name + ' now has ' + str(tempName.defenders) + ' soldiers! \n')
                            time.sleep(0.3)

                userStronghold.defenders = int(userStronghold.defenders) - int(withdrawNum) + benchedSoldiers
                userStronghold.write()
                userStronghold.read()
                print('\nNumber of Soldiers Remaining in Stronghold: ' + str(userStronghold.defenders))

                print("\n\n\n\n\n\n\n\n\n")

                print("Avalible Commands:")
                print('-------------------------------------')
                print('{1}: Return to Stronghold')
                print('{2}: View Nearby Fiefdoms')
                print('-------------------------------------')
                print('\n')
                command = input("Enter your command: ")

                if command == "1":
                    screen = "stronghold"
                if command == "2":
                    currentPage = 1
                    screen = "fiefdoms"

#This is the screen for updating a user's attack power.
#----------------------------------------------------------------------------------
    if screen == "upgradeFiefAtt":
        os.system("clear")
        header()

        attTypeNext = 'undefined'
        attUpgradeCost = 0

        if userStronghold.attLevel == str('0'):
            attTypeNext = 'Angry Villagers with Sharpened Pitchforks'
            attUpgradeCost = 500

        if userStronghold.attLevel == str('1'):
            attTypeNext = 'Semi-trained Longbow Archers'
            attUpgradeCost = 3500

        if userStronghold.attLevel == str('2'):
            attTypeNext = 'Military Recruits'
            attUpgradeCost = 10000

        if userStronghold.attLevel == str('3'):
            attTypeNext = 'Fairly Well-trained Archers with Flaming Arrows'
            attUpgradeCost = 45000

        if userStronghold.attLevel == str('4'):
            attTypeNext = 'Drunks with Trebuchets'
            attUpgradeCost = 75000

        if userStronghold.attLevel == str('5'):
            attTypeNext = 'Scientists who are Experiementing with Biological Warfare'
            attUpgradeCost = 200000

        if userStronghold.attLevel == str('6'):
            attTypeNext = 'Peasents with Guns'
            attUpgradeCost = 400000

        if userStronghold.attLevel == str('7'):
            print('\n\n')
            print('     Your current army is made of ' + userStronghold.attType)
            print('     This is currently the highest attack level!')
            print('\n\n\n\n\n\n\n\n\n\n')
            command = input("     Press Enter")

        else:
            print('\n\n')
            print('     Your current army is made of ' + userStronghold.attType)
            print('     Would you like to upgrade to ' + attTypeNext + ' for ' + str(attUpgradeCost) + ' gold?')

            upgradeInput = input('\n\n     Confirm Upgrade (y/n?): ')

            if upgradeInput == 'y' and int(userStronghold.gold) >= attUpgradeCost:
                print("     Upgrade Complete!")
                userStronghold.attType = attTypeNext
                userStronghold.attLevel = str(int(userStronghold.attLevel) + 1)
                userStronghold.gold = str(int(userStronghold.gold) - attUpgradeCost)
                userStronghold.write()
                userStronghold.read()

            elif upgradeInput == 'y' and int(userStronghold.gold) < attUpgradeCost:

                print('\n')
                print("     You need more gold first!\n\n\n\n")

            elif upgradeInput == 'n':
                print('\n')
                print("     No changes made.")

            print('\n\n\n\n\n\n\n\n\n\n')
            command = input("     Press Enter")

        screen = "stronghold"

#This is the screen for updating a fief's farm/gold production.
#----------------------------------------------------------------------------------
    if screen == "farm":
        #these variables define the next upgrade level and the cost of that level
        farmTypeNext = 'undefined'
        farmUpgradeCost = 0
        os.system("clear")
        header()

        if attackFief.goldMod == str('1'):
            farmTypeNext = 'Watering Cans'
            farmUpgradeCost = 500

        if attackFief.goldMod == str('2'):
            farmTypeNext = 'Wheelbarrows'
            farmUpgradeCost = 2000

        if attackFief.goldMod == str('3'):
            farmTypeNext = 'Fertilizer'
            farmUpgradeCost = 5000

        if attackFief.goldMod == str('4'):
            farmTypeNext = 'Horse Plows'
            farmUpgradeCost = 10000

        if attackFief.goldMod == str('5'):
            farmTypeNext = 'Crop Rotation'
            farmUpgradeCost = 20000

        if attackFief.goldMod == str('6'):
            farmTypeNext = 'Artificial Selection'
            farmUpgradeCost = 40000

        if attackFief.goldMod == str('7'):
            print('\n    Your fiefdom\'s gold output is currently: ' + str((int(attackFief.goldMod) * goldOutput)) + ' per hour.')
            print('   This is currently the highest gold output!')

            print('\n\n\n\n\n\n\n\n\n\n')
            command = input("     Press Enter ")

        else:
            print('\n    Your fiefdom\'s gold output is currently: ' + str((int(attackFief.goldMod) * goldOutput)) + ' per hour.')
            print('    Would you like to upgrade to ' + farmTypeNext + ' for ' + str(farmUpgradeCost) + ' gold?')

            upgradeInput = input('\n    y/n: ')

            if upgradeInput == 'y' and int(userStronghold.gold) >= farmUpgradeCost:
                print("\n    Upgrade Complete!")
                attackFief.farmType = farmTypeNext
                attackFief.goldMod = str(int(attackFief.goldMod) + 1)
                userStronghold.gold = str(int(userStronghold.gold) - farmUpgradeCost)
                attackFief.write()
                attackFief.read()
                userStronghold.write()
                userStronghold.read()
                currentPage = 1
                screen = "fiefdoms"

            elif upgradeInput == 'y' and int(userStronghold.gold) < farmUpgradeCost:
                print("\n    You need more gold first!")

            elif upgradeInput == 'n':
                print("\n    No changes made.")

            print('\n\n\n\n\n\n\n\n\n\n')
            command = input("     Press Enter ")

        currentPage = 1
        screen = "homeDetails"

#This is the screen for updating a fief's defenses. Note: there are two screens
#like this. One for fiefs and one for player strongholds.
#----------------------------------------------------------------------------------
    if screen == "upgradeFiefDef":
        os.system("clear")

        header()

        defTypeNext = 'undefined'
        defUpgradeCost = 0

        if attackFief.defLevel == str('0'):
            defTypeNext = 'Wooden Fences'
            defUpgradeCost = 500

        if attackFief.defLevel == str('1'):
            defTypeNext = 'Really Deep Ditches'
            defUpgradeCost = 2500

        if attackFief.defLevel == str('2'):
            defTypeNext = 'Tall Towers'
            defUpgradeCost = 5000

        if attackFief.defLevel == str('3'):
            defTypeNext = 'In a Lake'
            defUpgradeCost = 10000

        if attackFief.defLevel == str('4'):
            defTypeNext = 'On Top of a Mountain'
            defUpgradeCost = 20000

        if attackFief.defLevel == str('5'):
            defTypeNext = 'Boiling Oil'
            defUpgradeCost = 50000

        if attackFief.defLevel == str('6'):
            print('     Your current defense style is: ' + attackFief.defType)
            print('     This is currently the best defense style!')
            print('\n\n\n\n\n\n\n\n\n\n')
            command = input("     Press Enter ")
        else:
            print('    Your current defense style is: ' + attackFief.defType)
            print('    Would you like to upgrade to ' + defTypeNext + ' for ' + str(defUpgradeCost) + ' gold?')

            upgradeInput = input('    (y/n): ')

            if upgradeInput == 'y' and int(userStronghold.gold) >= defUpgradeCost:
                print("    Upgrade Complete!")
                attackFief.defType = defTypeNext
                attackFief.defLevel = str(int(attackFief.defLevel) + 1)
                userStronghold.gold = str(int(userStronghold.gold) - defUpgradeCost)
                attackFief.write()
                attackFief.read()
                userStronghold.write()
                userStronghold.read()

            elif upgradeInput == 'y' and int(userStronghold.gold) < defUpgradeCost:

                print("    You need more gold first!")

            elif upgradeInput == 'n':
                print("    No changes made.")

            print('\n\n\n\n\n\n\n\n\n\n')
            command = input("     Press Enter ")

        currentPage = 1
        screen = "homeDetails"

#This is the about page for the game. Keep it updated
#------------------------------------------------------------------------------
    if screen == "about":
        os.system("clear")

        header()
        print('\n\n')

        print('''


      Intro:

      Unnamed Fiefdom Game is a python programming project by Mike Quain (mquain@uark.edu)
      The goal was to take on a project that was big enough to be challenging, but small enough to stay interesting.
      This game looks simple, but it taught me the basics of reading and writing to a database, data persistance,
      and multi-user tools.


      How to play:

      Your goal is to control as many fiefdoms as you can manage without spreading your army too thin and leaving
      yourself open to attack! Your home stronghold will never fall, but any conquered fiefdoms can be taken by
      opposing players. Make sure you can defend the territory you claim!

      Each claimed fiefdom will generate gold per hour depending on the number of soldiers you have! That gold can 
      be spent on defense and attack upgrades as well as additional soldiers or thieves.

      Upgrade your conqured fiefdoms to keep them safe! Be careful though. Any upgraded fiefdom can still be taken,
      and your upgrades will be transfered to the new ruler.

      Additional Info is avalible at github.com/Sheeves11/UntitledFiefdomGame

        ''')

        print('\n\n\n\n\n')
        print("      Avalible Commands:")
        print('      -------------------------------------')
        print('      {1}: Return to Stronghold')
        print('      {2}: Check Out the Map Generator')
        print('      -------------------------------------')
        print('\n')
        command = input("      Enter your command: ")

        if command == "1":
            screen = "stronghold"
        if command == "2":
            screen = "sandboxMenu"

#This is the features page for the game. Keep it updated
#------------------------------------------------------------------------------
    if screen == "features":
        os.system("clear")

        header()
        print('\n\n')

        print('''


      Current Status:

      The game is currently in the the pre-release stage of development and new features are being added on a
      daily basis! Make sure you check back often to see what's new!

      Upcoming Features:

      {Weather Events} - Weather events and patterns will affect your fiefdom's performance. Rain could cost you
                         your advantage in battle, or a drought could hurt your gold production! Something as
                         simple as waiting for a clear sunset could give you the advantage in an attack where
                         the sun is in your opponent's eyes.

      {Market Investments} - Invest your gold in the markets! Prices will rise and fall as the season moves along.
                             Ride the charts on your way to the top.

      Thanks for playing! Submit your suggestions github.com/Sheeves11/UntitledFiefdomGame

        ''')

        print('\n\n\n\n\n')
        print("      Avalible Commands:")
        print('      -------------------------------------')
        print('      {1}: Return to Stronghold')
        print('      -------------------------------------')
        print('\n')
        command = input("      Enter your command: ")

        if command == "1":
            screen = "stronghold"

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
        header()

        fiefdomCount = 0
        fiefdomMargin = 0

        print("\n")
        print("Nearby Fiefdoms: ")
        print("------------------------------------------------------------------\n")

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
                        print (textColor.YELLOW + tempName.name + ' || Ruled by: ' + tempName.ruler + ' || Defenders: ' +
                                tempName.defenders + textColor.RESET + ' || Gold: ' + tempName.gold)

                    if tempName.home != "True" and tempName.ruler == userStronghold.name:
                        print (textColor.CYAN + tempName.name + ' || Ruled by: ' + tempName.ruler + ' || Defenders: ' +
                                tempName.defenders + textColor.RESET + ' || Gold: ' + tempName.gold)

        if fiefdomMargin > LINES_PER_PAGE or currentPage > 1:
            print('\n/// Page ' + str(currentPage) + ' ///')
        print("\nAvalible Commands:")
        print('-------------------------------------')
        print('{1}: Return to Stronghold')
        print('{2}: Garrison Soldiers')
        print('{3}: View Nearby Strongholds')
        if fiefdomMargin > LINES_PER_PAGE:
            print('{4}: Next Page')

        if currentPage > 1:
            print('{5}: Previous Page')

        print('{Enter fiefdom name}: View Fiefdom Details')
        print('-------------------------------------')
        print('\n')
        command = input("Enter your command: ")
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
            print (fileFief + 'loading is happening')
            try:
                with open(fileFief, 'r') as f:
                    attackFief.name = f.readline().strip()
                    attackFief.read()

                    if str(attackFief.ruler) == str(userStronghold.ruler):
                        screen = 'homeDetails'
                    if str(attackFief.home) == 'True':
                        screen = 'stronghold'
                    if str(attackFief.ruler) != str(userStronghold.ruler):
                        screen = "details"

            except:
                print ('the file open broke')

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

        header()

        strongholdCount = 0
        strongholdMargin = 0

        print("\n")
        print("Nearby Strongholds: ")
        print("------------------------------------------------------------------\n")

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
                        print (textColor.WARNING + 'The Stronghold of ' +  tempName.name + ' || Defenders: ' +
                                tempName.defenders + textColor.RESET + ' || Gold: ' + tempName.gold)

                    if tempName.home == "True" and tempName.ruler == userStronghold.name:
                        print (textColor.GREEN + 'The Stronghold of ' + tempName.name + ' || Defenders: ' +
                                tempName.defenders + textColor.RESET + ' || Gold: ' + tempName.gold)

        if strongholdMargin > LINES_PER_PAGE or currentPage > 1:
            print('/// Page ' + str(currentPage) + ' ///\n')
        print("\nAvalible Commands:")
        print('-------------------------------------')
        print('{1}: Return to Stronghold')
        print('{2}: Garrison Soldiers')
        print('{3}: View Nearby Fiefdoms')
        if strongholdMargin > LINES_PER_PAGE:
            print('{4}: Next Page')

        if currentPage > 1:
            print('{5}: Previous Page')

        print('{Enter stronghold owner name}: View Stronghold Details')
        print('-------------------------------------')
        print('\n')
        command = input("Enter your command: ")
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
            print (fileFief + 'loading is happening')
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
                print ('the file open broke')

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
        header()
        attackFief.read()

        productionCalc = 0

        maxProductionSoldiers = (int(attackFief.goldMod) * 500)

        if int(attackFief.defenders) > maxProductionSoldiers:
            productionCalc = ((goldOutput * int(attackFief.goldMod)) + (int(maxProductionSoldiers) * int(attackFief.goldMod)))

        else:
            productionCalc = ((goldOutput * int(attackFief.goldMod)) + (int(attackFief.defenders) * int(attackFief.goldMod)))

        print("\n")
        print('     You rule the fiefdom of ' + attackFief.name)
        print('\n')
        print('     Status Report:')
        print('\n     ' + 'Defenders: ' + attackFief.defenders + '\n     Gold: ' + attackFief.gold + ' gold.')
        print('     ' + 'Defensive Strategy: ' + attackFief.defType)
        print('     ' + 'Production: ' + str(productionCalc) + ' gold and ' + str(defenderOutput * int(attackFief.defenderMod))
                + ' soldiers per hour.')
        print("\n")

        if attackFief.biome == str('^'):
            art_forest()
        
        if attackFief.biome == str('M'):
            art_mountain()
        
        if attackFief.biome == str('#'):
            art_plains()

        if attackFief.defLevel == str(0):
            art_fief0(attackFief.biome)

        if attackFief.defLevel == str(1):
            art_fief1(attackFief.biome)

        if attackFief.defLevel == str(2):
            art_fief2(attackFief.biome)

        if attackFief.defLevel == str(3):
            art_fief3(attackFief.biome)

        if attackFief.defLevel == str(4):
            art_fief4(attackFief.biome)

        if attackFief.defLevel == str(5):
            art_fief5(attackFief.biome)

        if attackFief.defLevel == str(6):
            art_fief6(attackFief.biome)


        if attackFief.goldMod == str(1):
            art_farm0()

        if attackFief.goldMod == str(2):
            art_farm1()

        if attackFief.goldMod == str(3):
            art_farm2()

        if attackFief.goldMod == str(4):
            art_farm3()

        if attackFief.goldMod == str(5):
            art_farm4()

        if attackFief.goldMod == str(6):
            art_farm5()

        if attackFief.goldMod == str(7):
            art_farm6()


        print('\n')
        print("     Avalible Commands:")
        print('     -------------------------------------------------------')
        print('     {1}: Return to Stronghold       {9}:View Location')
        print('     {2}: View Nearby Fiefdoms')
        print('     {3}: Deploy Additional Forces')
        print('     {4}: Withdraw Forces')
        print('     {5}: Withdraw Gold')
        print('     {6}: Upgrade Defenses')
        print('     {7}: Upgrade Farms')
        print('     {8}: Upgrade Training')
        print('     -------------------------------------------------------')
        print('\n')
        command = input("     Enter your command: ")

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
            screen = 'upgradeFiefDef'

        if command == '7':
            screen = 'farm'

        if command == '9':
            screen = 'viewMapCurrentFief'

#The withdraw gold screen allows players to withdraw gold from a ruled fiefdom
#
#To Do
# -
#
#------------------------------------------------------------------------------
    if screen == 'withdrawGold':
        os.system("clear")
        header()

        print("\n")
        print('Now viewing the Fiefdom of ' + attackFief.name)
        print('\n')
        time.sleep(0)
        print(attackFief.name + ' has ' + attackFief.gold + ' gold.')
        time.sleep(1)
        print('\n')

        print('Sending ' + str(attackFief.gold) + ' gold back home')
        time.sleep(1)
        userStronghold.gold = str(int(userStronghold.gold) + int(attackFief.gold))
        attackFief.gold = str(0)
        attackFief.write()
        attackFief.read()
        userStronghold.write()
        userStronghold.read()

        currentPage = 1
        screen = "fiefdoms"

#The deploy screen allows players to deploy defenders to a Fiefdom that they
#currently control.
#
#To Do
# - add a "withdraw" page for pulling troops out of a Fiefdom
# - verify that the player has the troops avalible for deployment
# - prevent negative numbers
#------------------------------------------------------------------------------
    if screen == 'deploy':
        os.system("clear")

        header()

        print("\n\n")
        print('Now viewing the Fiefdom of ' + attackFief.name)
        print('\n\n')
        time.sleep(1)
        print(attackFief.name + ' has ' + attackFief.defenders + ' fighters.')
        time.sleep(1)
        print('You have ' + str(userStronghold.defenders) + ' ready to deploy.\n\n')
        deployNum = input('Enter the number of soldiers you would like to deploy: ')
        time.sleep(1)

        #print(deployNum + ' : deploynum || userStronghold.defenders : ' + userStronghold.defenders) #SW: remove this?

        try:
            deployNum = int(deployNum)
        except:
            deployNum = 0

        if int(deployNum) < 0:
            os.system("clear")
            print("You cannot deploy a negative number of soldiers. \n\nThat doesn't even make sense.")
            time.sleep(2)
            screen = 'homeDetails'

        if (int(userStronghold.defenders) < int(deployNum)) and int(deployNum) > 0:
            os.system("clear")
            print("You do not have enough soldiers for that")
            time.sleep(2)
            screen = 'homeDetails'

        if deployNum == 0:
            screen = "homeDetails"

        if (int(userStronghold.defenders) >= int(deployNum)) and int(deployNum) > 0:
            print('Deploying ' + str(deployNum) + ' soldiers to ' + str(attackFief.name))

            attackFief.defenders = str(int(attackFief.defenders) + int(deployNum))
            attackFief.write()
            attackFief.read()

            userStronghold.defenders = str(int(userStronghold.defenders) - int(deployNum))
            userStronghold.write()
            userStronghold.read()
            attackFief.read()

            print("\n\n\n\n\n\n\n\n\n")

            print("Avalible Commands:")
            print('-------------------------------------')
            print('{1}: Return to Stronghold')
            print('{2}: View Nearby Fiefdoms')
            print('-------------------------------------')
            print('\n')
            command = input("Enter your command: ")

            if command == "1":
                screen = "stronghold"
            if command == "2":
                currentPage = 1
                screen = "fiefdoms"

        time.sleep(3)
#The withdraw screen allows players to withdraw forces from a ruled fiefdom
#
#To Do
# -
#
#------------------------------------------------------------------------------
    if screen == 'withdraw':
        os.system("clear")
        header()
        print("\n\n")
        print('Now viewing the Fiefdom of ' + attackFief.name)
        print('\n\n')
        time.sleep(0.5)
        print(attackFief.name + ' has ' + attackFief.defenders + ' fighters.')
        time.sleep(0.5)
        print('\n')

        withdrawNum = input('Enter the number of soldiers you would like to return home: ')
        time.sleep(1)
        try:
            withdrawNum = int(withdrawNum)
        except:
            withdrawNum = 0

        if int(withdrawNum) < 0:
            os.system("clear")
            print("You cannot send home a negative number of soldiers. \n\nThat doesn't even make sense.")
            time.sleep(2)
            screen = 'homeDetails'

        if (int(attackFief.defenders) < int(withdrawNum)) and int(withdrawNum) > 0:
            os.system("clear")
            print("You do not have enough soldiers for that")
            time.sleep(2)
            screen = 'homeDetails'

        if (int(attackFief.defenders) >= int(withdrawNum)) and int(withdrawNum) > 0:
            print('Returning ' + str(withdrawNum) + ' soldiers back home')

            attackFief.defenders = str(int(attackFief.defenders) - int(withdrawNum))
            attackFief.write()
            attackFief.read()

            userStronghold.defenders = str(int(userStronghold.defenders) + int(withdrawNum))
            userStronghold.write()
            userStronghold.read()

            print("\n\n\n\n\n\n\n\n\n")

            print("Avalible Commands:")
            print('-------------------------------------')
            print('{1}: Return to Stronghold')
            print('{2}: View Nearby Fiefdoms')
            print('-------------------------------------')
            print('\n')
            command = input("Enter your command: ")

            if command == "1":
                screen = "stronghold"
            if command == "2":
                currentPage = 1
                screen = "fiefdoms"

        if int(withdrawNum) == 0:
            print('No soldiers selected')
            screen = "homeDetails"

            attackFief.defenders = str(int(attackFief.defenders) - int(withdrawNum))
            attackFief.write()
            attackFief.read()

            userStronghold.defenders = str(int(userStronghold.defenders) + int(withdrawNum))
            userStronghold.write()
            userStronghold.read()

            print("\n\n\n\n\n\n\n\n\n")

            print("Avalible Commands:")
            print('-------------------------------------')
            print('{1}: Return to Stronghold')
            print('{2}: View Nearby Fiefdoms')
            print('-------------------------------------')
            print('\n')
            command = input("Enter your command: ")

            if command == "1":
                screen = "stronghold"
            if command == "2":
                currentPage = 1
                screen = "fiefdoms"

#This is the details page for enemy Fiefdoms
#
#To Do
# - Make it prettier
# - In the future, add a way to obscure exact numbers?
# - Add ability to attempt spying to gain info on defenses and upgrades
#------------------------------------------------------------------------------
    if screen == "details":
        os.system("clear")
        header()

        print("\n\n")
        print('Now viewing the fiefdom of ' + attackFief.name)
        print('This fiefdom is ruled by ' + attackFief.ruler)
        print('-------------------------------------------------------------------------')
        print('\nYour scouts return early in the morning, bringing back reports of the enemy fiefdom.')
        print(attackFief.name + ' looks to have ' + str(attackFief.defenders) + ' fighters.')
        print('Defense Type: ' + attackFief.defType)
        print('-------------------------------------------------------------------------')

        print("\n\n")
        if attackFief.biome == str('^'):
            art_forest()
        
        if attackFief.biome == str('M'):
            art_mountain()
        
        if attackFief.biome == str('#'):
            art_plains()


        if attackFief.defLevel == str(0):
            art_fief0(attackFief.biome)

        if attackFief.defLevel == str(1):
            art_fief1(attackFief.biome)

        if attackFief.defLevel == str(2):
            art_fief2(attackFief.biome)

        if attackFief.defLevel == str(3):
            art_fief3(attackFief.biome)

        if attackFief.defLevel == str(4):
            art_fief4(attackFief.biome)

        if attackFief.defLevel == str(5):
            art_fief5(attackFief.biome)

        if attackFief.defLevel == str(6):
            art_fief6(attackFief.biome)


        if attackFief.goldMod == str(1):
            art_farm0()

        if attackFief.goldMod == str(2):
            art_farm1()

        if attackFief.goldMod == str(3):
            art_farm2()

        if attackFief.goldMod == str(4):
            art_farm3()

        if attackFief.goldMod == str(5):
            art_farm4()

        if attackFief.goldMod == str(6):
            art_farm5()

        if attackFief.goldMod == str(7):
            art_farm6()

        print("\n\n")

        print("Avalible Commands:")
        print('-------------------------------------')
        print('{1}: Return to Stronghold')
        print('{2}: View Nearby Fiefdoms')
        print('{3}: Attack')
        print('{4}: View Location')
        print('-------------------------------------')
        print('\n')

        command = input("Enter your command: ")

        if command == "1":
            screen = "stronghold"

        if command == "2":
            currentPage = 1
            screen = "fiefdoms"

        if command == "3":
            screen = 'battle'
        
        if command == "4":
            screen = 'viewMapCurrentFief'

#This is the details page for enemy Fiefdoms
#
#To Do
# - Make it prettier
# - In the future, add a way to obscure exact numbers?
# - Add ability to attempt spying to gain info on defenses and upgrades
#------------------------------------------------------------------------------
    if screen == "enemyStrongholdDetails":
        os.system("clear")
        header()
        attackStronghold.read()
        print("\n\n")
        print('Now viewing the stronghold of ' + attackStronghold.name)
        print('-------------------------------------------------------------------------')
        print('\nYour scouts return early in the morning, bringing back reports of the enemy fiefdom.')
        print(attackStronghold.name + ' looks to have ' + str(attackStronghold.defenders) + ' fighters.')
        print('Defense Type: ' + attackStronghold.defType)
        print('-------------------------------------------------------------------------')

        print("\n\n")

        #This whole section needs to be re-evaluated

        art_stronghold(attackStronghold.biome, attackStronghold.color)

        print("\n\n")

        print("Avalible Commands:")
        print('-------------------------------------')
        print('{1}: Return to Stronghold')
        print('{2}: View Nearby Fiefdoms')
        print('{3}: Send Thieves To Steal Gold')
        print('{4}: View Location')
        print('-------------------------------------')
        print('\n')

        command = input("Enter your command: ")

        if command == "1":
            screen = "stronghold"

        if command == "2":
            currentPage = 1
            screen = "fiefdoms"

        if command == "3":
            screen = "thiefPage"

        if command == "4":
            screen = "viewMapEnemyStronghold"


#This is the theif attack page, which you will see when trying
#to steal gold from another player
#
#------------------------------------------------------------------------------
    if screen == "thiefPage":
        os.system("clear")
        header()

        #this is where the battle logic happens!
        print('\n\n    ' + attackStronghold.name + '\'s Stronghold has ' + attackStronghold.defenders + ' soldiers keeping a watchful eye. You have ' + str(userStronghold.thieves) + ' who are ready for a heist.')
        print('    Rumor has it that their coffers hold ' + str(attackStronghold.gold) + ' gold pieces.')
        print('    Your thieves work best in groups of 3 per 100 soldiers. Too few and they lack manpower. Too many and they draw unwanted attention.')
        print('\n    ...\n')
        time.sleep(1)
        
        desiredAttackers = 0
        attackers = 0

        try:
            desiredAttackers = int(input('    Enter the number of thieves you would like to send on this mission: '))
        except:
            print('\n\n    That is not a valid option, sorry!')
            Attackers = 0

        if int(desiredAttackers) <= int(userStronghold.thieves)  and int(desiredAttackers) > 0:
#            print('desieredAttackers = ' + str(desiredAttackers))
            attackers = int(desiredAttackers)
        else:
            print('invalid number')
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



        tempInput = input('    Press Enter To Continue: ')
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
        header()

        #Idea: We're going to do a DnD style battle using D20s and modifiers.
        #roll(mod) is going to give the result of a roll plus modifiers and is
        #defined at the start of the file.

        #This if statement prevents players from attacking a player's home stronghold
        #Eventually this will be replaced with a formula that allows you to attack
        #for gold
        if attackFief.home == 'True':
            os.system('clear')
            print('You are unable to claim a player\'s home stronghold')
            time.sleep(3)
            screen = 'stronghold'

        #this is where the battle logic happens!
        if attackFief.home == 'False':
            print('\n\nThis battle is between ' + attackFief.name + ' and ' + userStronghold.name)
            print('\n\nSimulating Battle...')
            time.sleep(1)
            print('\n...\n')
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

            print('\n')
            print('------------------------------------------------------------------------------')
            print('-----------------------------Battle Results-----------------------------------')
            print('------------------------------------------------------------------------------')
            print('\n')
            print(userStronghold.ruler + ' lost ' + str(attackLosses) + ' soldiers')
            print(attackFief.ruler + ' lost ' + str(defenseLosses) + ' soldiers')
            print('\n')
            print('------------------------------------------------------------------------------')
            print('------------------------------------------------------------------------------')
            print('\n\n')

            #if the current player wins
            if attackers > defenders:
                print('After a hard fought battle, your weary forces remain standing')
                print('You are the new ruler of ' + attackFief.name)

                attackFief.defenders = defenders
                attackFief.ruler = userStronghold.ruler
                attackFief.write()

                userStronghold.defenders = attackers
                userStronghold.write()

                userStronghold.gold = str(int(userStronghold.gold) + int(attackFief.gold))
                print('You now have a total of ' + str(userStronghold.gold) + ' gold!')
                attackFief.gold = str('0')

                userStronghold.write()
                attackFief.write()

            #if the other player wins
            if attackers <= defenders:
                print('Although your soldiers fought valiantly, they were unable to overcome ' + attackFief.ruler + '\'s forces')
                print('Your forces, now many fewer in number, begin the long march home.')

                attackFief.defenders = defenders
                attackFief.write()

                userStronghold.defenders = attackers
                userStronghold.write()


            time.sleep(1)
            nothing = input('Continue:')
            currentPage = 1
            screen = "fiefdoms"

#This page prints the world map with your stronghold's location marked on it
    if screen == "viewMapYourStronghold":
        os.system("clear")
        serverMap.name = "serverMap"

        if firstMapRead:
            serverMap.read()
            firstMapRead = False

        print('Current Location -  Row: ' + str(userStronghold.yCoordinate) + ' Column: ' + str(userStronghold.xCoordinate))
        print('')
        PrintLegend()
        print('')
        print('World Map:')
        print('')
        WorldMapLocation(int(userStronghold.yCoordinate), int(userStronghold.xCoordinate), serverMap)
        print('')
        time.sleep(1)
        nothing = input('Continue:')

        screen = 'stronghold'

#This page prints the world map with your stronghold's location marked on it
    if screen == "viewMapEnemyStronghold":
        os.system("clear")
        serverMap.name = "serverMap"

        if firstMapRead:
            serverMap.read()
            firstMapRead = False

        print('Current Location -  Row: ' + str(attackStronghold.yCoordinate) + ' Column: ' + str(attackStronghold.xCoordinate))
        print('')
        PrintLegend()
        print('')
        print('World Map:')
        print('')
        WorldMapLocation(int(attackStronghold.yCoordinate), int(attackStronghold.xCoordinate), serverMap)
        print('')
        time.sleep(1)
        nothing = input('Continue:')

        screen = 'enemyStrongholdDetails'

#This page prints the world map with your stronghold's location marked on it
    if screen == "viewMapCurrentFief":
        os.system("clear")
        serverMap.name = "serverMap"

        if firstMapRead:
            serverMap.read()
            firstMapRead = False

        print('Current Location -  Row: ' + str(attackFief.yCoordinate) + ' Column: ' + str(attackFief.xCoordinate))
        print('')
        PrintLegend()
        print('')
        print('World Map:')
        print('')
        WorldMapLocation(int(attackFief.yCoordinate), int(attackFief.xCoordinate), serverMap)
        print('')
        time.sleep(1)
        nothing = input('Continue:')

        if str(attackFief.ruler) == str(userStronghold.ruler):
            screen = 'homeDetails'
        if str(attackFief.ruler) != str(userStronghold.ruler):
            screen = "details"


#This page prints a menu for choosing your stronghold's color:
    if screen == "changeStrongholdColor":
        os.system("clear")

        print('\n\n\n\n\n')
        print("      Choose a Stronghold Color:")
        print('      -------------------------------------')
        print('''      {1}: Red       '''+textColor.RED+'''#'''+textColor.RESET+''' ''')
        print('''      {2}: Green     '''+textColor.GREEN+'''#'''+textColor.RESET+''' ''')
        print('''      {3}: Blue      '''+textColor.BLUE+'''#'''+textColor.RESET+''' ''')
        print('''      {4}: Yellow    '''+textColor.YELLOW+'''#'''+textColor.RESET+''' ''')
        print('''      {5}: Magenta   '''+textColor.MAGENTA+'''#'''+textColor.RESET+''' ''')
        print('''      {6}: Cyan      '''+textColor.CYAN+'''#'''+textColor.RESET+''' ''')
        print('''      {7}: White     '''+textColor.BOLD+'''#'''+textColor.RESET+''' ''')
        print('''      {8}: Gray      '''+textColor.DARK_GRAY+'''#'''+textColor.RESET+''' ''')
        print('      {9}: Leave color as is')
        print('      -------------------------------------')
        print('\n')
        command = input("      Enter your command: ")

        if command == "1":
            userStronghold.color = 'red'
        if command == "2":
            userStronghold.color = 'green'
        if command == "3":
            userStronghold.color = 'blue'
        if command == "4":
            userStronghold.color = 'yellow'
        if command == "5":
            userStronghold.color = 'magenta'
        if command == "6":
            userStronghold.color = 'cyan'
        if command == "7":
            userStronghold.color = 'white'
        if command == "8":
            userStronghold.color = 'gray'
        
        userStronghold.write()
        screen = "stronghold"


#This is the about page for the game. Keep it updated
#------------------------------------------------------------------------------
    if screen == "sandboxMenu":
        os.system("clear")

        header()
        print('\n\n')

        print('     Welcome to the Sandbox Menu, where uses can play with the map generator!')

        art_globe()

        print('\n\n\n\n\n')
        print("      Avalible Commands:")
        print('      -------------------------------------')
        print('      {1}: Return to Stronghold')
        print('      {2}: Generate a Test Map')
        print('      {3}: Create Custom Fiefs')
        print('      {4}: Add Fiefs to Test Map')
        print('      {5}: View Test Map')
        print('      -------------------------------------')
        print('\n')
        command = input("      Enter your command: ")

        if command == "1":
            screen = "stronghold"
        if command == "2":
            screen = "sbTestMap"
        if command == "3":
            screen = "sbCreateFief"
        if command == "4":
            screen = "sbPlotTestFiefs"
        if command == "5":
            screen = "sbViewMap"

#This is a page where users can generate maps of their own
#------------------------------------------------------------------------------
    if screen == "sbTestMap":
        os.system("clear")

        TestResetFiefCoordinates()

        testMap.name = 'testMap'
        testMap.seed = GenerateSeed()
        testMap.height = MAP_HEIGHT
        testMap.width = MAP_WIDTH
        testMap.worldMap = GenerateWorldMap(testMap.seed)
        SetBiomeCounts(testMap)
        testMap.write()
        
        print('World Map:')

        PrintColorMap(testMap.worldMap)

        print('\n Getting ready to generate rivers...')
        time.sleep(3)
        GenerateRivers(testMap)

        time.sleep(1)
        nothing = input('\nContinue:')

        screen = 'sandboxMenu'

#This is a page where users can view the maps they generate
#------------------------------------------------------------------------------
    if screen == "sbCreateFief":
        os.system("clear")
        print('    Welcome to the fief creation tool!')
        print('    Please be aware that other users may be able to see the fiefs you create!')
        newFief = input('\n    Enter the name of your new fief: ')
        testFief = TestFiefdom()
        testFief.name = newFief
        testFief.defenders = random.randint(10, 100)
        testFief.gold = random.randint(500, 3100)
        testFief.write()

        print('    ' + str(testFief.name) + ' has been created!')
        time.sleep(1)
        nothing = input('\nContinue:')

        screen = 'sandboxMenu'

#This is a page where users can add fiefs to their test map
#------------------------------------------------------------------------------
    if screen == "sbPlotTestFiefs":
        os.system("clear")

        testMap.name = 'testMap'
        testMap.read()
        
        TestPlotAllFiefs(testMap)

        time.sleep(1)
        nothing = input('\nContinue:')

        screen = 'sandboxMenu'

#This is a page where users can view the maps they generate
#------------------------------------------------------------------------------
    if screen == "sbViewMap":
        os.system("clear")
        
        testMap.name = 'testMap'
        testMap.read()
        
        print('Current Test Map:')

        PrintColorMap(testMap.worldMap)

        time.sleep(1)
        nothing = input('\nContinue:')

        screen = 'sandboxMenu'

#This is the new devtest menu with all the devtest commands sorted out and neat
#------------------------------------------------------------------------------
    if screen == "devTest":
        os.system("clear")

        header()
        print("\n")

        print('     Welcome to the dev test menu. This should only be used for testing purposes.')
        print('\n')
        
        art_devBricks()

        print("     Avalible Commands:")
        print('     -------------------------------------------------------')
        print('     {1}: Return to Stronghold')
        print('     {2}: Create Default Fiefs')
        print('     {3}: Generate World Map (Must do this before 4-6)')
        print('     {4}: Add Fief Tool')
        print('     {5}: Add all Fiefs Tool')
        print('     {6}: Add all Strongholds Tool')
        print('     {7}: Quick Generate World (DO NOT USE if 3-6 were used!)')
        print('     {8}: Add Gold Tool (for testing!)')
        print('     {9}: World Map Diagnostic (Only run after step 3 or 7)')
        print('     {10}: World Map River Tool')
        print('     --------------------------------------------------------')
        print('     Note: To quick generate a world, just hit 7. To go step ')
        print('           by step, start at 3 and proceed without using 7!  ')
        print('\n')
        command = input("     Enter your command: ")

        if command == '1':
            currentPage = 1
            screen = "stronghold"

        if command == '2':
            screen = 'devTestCreateDefaults'

        if command == '3':
            screen = 'devTestWorldMap'

        if command == '4':
            screen = 'devTestFiefPlacement'

        if command == '5':
            screen = 'devTestPlotAllFiefs'

        if command == '6':
            screen = 'devTestPlotAllStrongholds'

        if command == '7':
            screen = 'devTestGenerateWorld'

        if command == '8':
            screen = 'devTestAddGold'

        if command == '9':
            screen = 'devTestWorldMapDiagnostics'

        if command == '10':
            screen = 'devTestRiverTool'


#This is a "secret" page that you can use to create default Fiefdoms
#to seed your installation with land that can be taken.
#
#It should be taken out if you ever open this game up to many players
#----------------------------------------------------------------------------------
    if screen == "devTestCreateDefaults":
        os.system("clear")

        print('Seeding the world with default fiefdoms')

        names = ['Razor Hills', 'Forest of Fado', 'Emerald Cove', 'Stormgrove',
                'Dreadwall', 'Aegirs Hall', 'Ashen Grove', 'Bellhollow', 'Howling Plains',
                'Jade Hill', 'Knoblands', 'Kestrel Keep', 'Direbrook',
                'Greystone', 'Dusk Hollow', 'Ebonmarch', 'Eclipse', 'Midgar', 'Mordengaard']
        for x in names:
            currentFief = Fiefdom()
            currentFief.name = x
            currentFief.defenders = random.randint(10, 100)
            currentFief.gold = random.randint(500, 3100)
            currentFief.write()

        time.sleep(2)
        print('Seeding Complete')
        currentPage = 1
        screen = "fiefdoms"

#This is another "secret" page that can be used to add funds for testing purposes
#
#It should be taken out if you ever open this game up to many players
#----------------------------------------------------------------------------------
    if screen == "devTestAddGold":
        os.system("clear")

        print('Adding Funds!...')

        userStronghold.gold = str(int(userStronghold.gold) + 1000000)
        userStronghold.write()

        time.sleep(0.5)
        print('...Funds Added!')
        time.sleep(0.5)
        screen = 'devTest'

#This is a devtool for making the world map for a server
#
#It eventually needs to be accessed in another way
#----------------------------------------------------------------------------------
    if screen == "devTestWorldMap":
        os.system("clear")

        serverMap.name = 'serverMap'
        serverMap.seed = GenerateSeed()
        serverMap.height = MAP_HEIGHT
        serverMap.width = MAP_WIDTH
        serverMap.worldMap = GenerateWorldMap(serverMap.seed)
        SetBiomeCounts(serverMap)
        serverMap.write()

        print('\n')
        PrintColorMap(serverMap.worldMap)

        nothing = input('\nContinue:')

        screen = 'devTest'

#This is currently just a test page to see if fief placement in the world map works as intended
#----------------------------------------------------------------------------------
    if screen == "devTestFiefPlacement":

        os.system("clear")

        fief = Fiefdom()
        command = input('Enter a fief name to input: ')

        fileFief = 'fiefs/' + command + '.txt'
        try:
            with open(fileFief, 'r') as f:
                fief.name = f.readline().strip()
                fief.read()
        except:
            print ('No file found')

        PlaceFiefInWorldMap(fief, serverMap)

        nothing = input('Continue:')

        screen = 'devTest'

#This plots all fiefs on the server at once
#----------------------------------------------------------------------------------
    if screen == "devTestPlotAllFiefs":

        os.system("clear")

        PlotAllFiefs(serverMap)

        nothing = input('Continue:')

        screen = 'devTest'
        
#This plots all strongholds on the server at once
#----------------------------------------------------------------------------------
    if screen == "devTestPlotAllStrongholds":

        os.system("clear")
        PlotAllStrongholds(serverMap)

        nothing = input('Continue:')

        screen = 'devTest'


#This impelments all the map related functions in one go
#----------------------------------------------------------------------------------
    if screen == "devTestGenerateWorld":

        os.system("clear")
        serverMap.name = 'serverMap'
        serverMap.seed = GenerateSeed()
        serverMap.height = MAP_HEIGHT
        serverMap.width = MAP_WIDTH
        serverMap.worldMap = SilentlyGenerateWorldMap(serverMap.seed)
        SetBiomeCounts(serverMap)
        serverMap.write()

        os.system("clear")
        PlotAllFiefs(serverMap)

        os.system("clear")
        PlotAllStrongholds(serverMap)

        os.system("clear")
        print('World Generation Complete!')
        print('')
        PrintColorMap(serverMap.worldMap)

        nothing = input('Continue:')

        screen = 'devTest'

#This impelments all the map related functions in one go
#----------------------------------------------------------------------------------
    if screen == "devTestWorldMapDiagnostics":

        os.system("clear")

        serverMap.selfDiagnostic()
        # print('\n')
        # PrintLegend()
        print('\n')
        PrintColorMap(serverMap.worldMap)

        nothing = input('Continue:')

        screen = 'devTest'

#This allows you to add rivers to a map
#-----------------------------------------------------------------------------------
    if screen == "devTestRiverTool":
        os.system("clear")
        serverMap.read()
        GenerateRivers(serverMap)

        nothing = input('Continue:')
        
        screen = 'devTest'

    '''
#This screen is for upgrading your home stronghold's defenses
#Not currently in use
#------------------------------------------------------------------------------
    if screen == "upgradeDef":
        os.system("clear")

        header()

        defTypeNext = 'undefined'
        defUpgradeCost = 0

        if userStronghold.defLevel == str('0'):
            defTypeNext = 'Wooden Fences'
            defUpgradeCost = 500

        if userStronghold.defLevel == str('1'):
            defTypeNext = 'Really Deep Ditches'
            defUpgradeCost = 1500

        if userStronghold.defLevel == str('2'):
            defTypeNext = 'Ditch Spikes'
            defUpgradeCost = 5000

        if userStronghold.defLevel == str('3'):
            defTypeNext = 'Moat'
            defUpgradeCost = 10000

        if userStronghold.defLevel == str('4'):
            defTypeNext = 'Alligators in the Moat'
            defUpgradeCost = 20000

        if userStronghold.defLevel == str('5'):
            defTypeNext = 'Drawbridge'
            defUpgradeCost = 40000

        print('Your current defense style is: ' + userStronghold.defType)
        print('Would you like to upgrade to ' + defTypeNext + ' for ' + str(defUpgradeCost) + ' gold?')

        upgradeInput = input('y/n?')

        if upgradeInput == 'y' and int(userStronghold.gold) >= defUpgradeCost:
            print("Upgrade Complete!")
            userStronghold.defType = defTypeNext
            userStronghold.defLevel = str(int(userStronghold.defLevel) + 1)
            userStronghold.gold = str(int(userStronghold.gold) - defUpgradeCost)
            userStronghold.write()
            userStronghold.read()

        elif upgradeInput == 'y' and int(userStronghold.gold) < defUpgradeCost:
            print("You need more gold first!")

        elif upgradeInput == 'n':
            print("No changes made.")

        print('\n\n\n\n\n\n\n\n\n\n')
        print("Avalible Commands:")
        print('-------------------------------------')
        print('{1}: Return to Stronghold')
        print('-------------------------------------')
        print('\n')
        command = input("Enter your command: ")

        if command == "1":
            screen = "stronghold"
    '''
