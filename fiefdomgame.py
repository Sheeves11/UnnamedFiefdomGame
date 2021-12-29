import os
import time
import random
from classes import *

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
userFiefCount = 0

#hourly production values
#these should be changed to match the values in fiefdombackend.py
goldOutput = 100
defenderOutput = 3

#initial screen clear
os.system("clear")

#create some default objects that we'll write over later
attackFief = Fiefdom()
userFief = Fiefdom()

#this begins the main game loop
#------------------------------------------------------------------------------
while (loop):
    
    #The login page takes a username, puts it into memory, and sends you to the
    #stronghold page. It also contains a small intro snippet
    #TO DO:
    # - Add password encryption
    if screen == "login":
        os.system("clear")
        print(textColor.WARNING + '''
 _    _                                      _   ______ _       __    _                    _____                      
| |  | |                                    | | |  ____(_)     / _|  | |                  / ____|                     
| |  | |_ __  _ __   __ _ _ __ ___   ___  __| | | |__   _  ___| |_ __| | ___  _ __ ___   | |  __  __ _ _ __ ___   ___ 
| |  | | '_ \| '_ \ / _` | '_ ` _ \ / _ \/ _` | |  __| | |/ _ \  _/ _` |/ _ \| '_ ` _ \  | | |_ |/ _` | '_ ` _ \ / _ 
| |__| | | | | | | | (_| | | | | | |  __/ (_| | | |    | |  __/ || (_| | (_) | | | | | | | |__| | (_| | | | | | |  __/
 \____/|_| |_|_| |_|\__,_|_| |_| |_|\___|\__,_| |_|    |_|\___|_| \__,_|\___/|_| |_| |_|  \_____|\__,_|_| |_| |_|\___|
                                                                                                                       
~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~          
        ''' + textColor.RESET + '''
                                                  ,--,  ,.-.
                                   ,                   \,       '-,-`,'-.' | ._
                                  /|           \    ,   |\         }  )/  / `-,',
                                  [ ,          |\  /|   | |        /  \|  |/`  ,`
                                  | |       ,.`  `,` `, | |  _,...(   (      .',
                                  \  \  __ ,-` `  ,  , `/ |,'      Y     (   /_L|
                                   \  \_\,``,   ` , ,  /  |         )         _,/
                                    \  '  `  ,_ _`_,-,<._.<        /         /
                                     ', `>.,`  `  `   ,., |_      |         /
                                       \/`  `,   `   ,`  | /__,.-`    _,   `|
                                   -,-..\  _  \  `  /  ,  / `._) _,-\`       |
                                    \_,,.) /\    ` /  / ) (-,, ``    ,        |
                                   ,` )  | \_\       '-`  |  `(               |
                                  /  /```(   , --, ,' \   |`<`    ,            |
                                 /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
                           ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
                          (-, \           ) \ ('_.-._)/ /,`    /
                          | /  `          `/    V   V, /`     /
                       ,--\(        ,     <_/`       ||      /
                      (   ,``-     \/|         \-A.A-`|     /
                     ,>,_ )_,..(    )\          -,,_-`  _--`
                    (_ \|`   _,/_  /  \_            ,--`
                     \( `   <.,../`     `-.._   _,-`    ''' + textColor.WARNING + '''

~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~                                                                                                                       
        ''')
        print(textColor.RESET + '''
                Welcome to the Unnamed Fiefdom Game!

                This is a python programming project and multiplayer war game based on the classic
                BBS door games of the 80s and 90s. In much the same way, this system uses a central
                server to host the game to multiple users, who access it using a terminal emulator.

                See more info at github.com/Sheeves11/UnnamedFiefdomGame ''')
        print('\n')
        userFief = Fiefdom()        
        username = input("                Enter your username (Note that passwords are not encrypted (yet): ")
        currentUsername = username
        
        #if "username.txt" does not exist, create it. The file only contains a name and password for now.
        try:
            usernameFile = username + ".txt"
            with open(usernameFile, 'x') as f:
                f.write(username + '\n')
                os.system('clear')
                header()
                print('\n\n')
                print('Welcome! To create your account, please enter your password. \nIf this was a mistake, refresh the page!')
                print('\nUsername: ' + username)
                password = "default"
                password = input('Enter your password: ')
                f.write(password)
                print('Creating new account...')
                time.sleep(1)
                print('Logging in as: ' + username)
                time.sleep(1)
                screen = 'stronghold'
        except:
            with open(usernameFile, 'r') as f:
                temp1 = f.readline().strip()
                truePass = f.readline().strip()
                os.system('clear')
                header()
                
                print('\n\nWelcome back, ' + str(username))
                userPass = input('Enter your password: ')
                
                if str(userPass) == str(truePass):
                    print('Password is correct')
                    time.sleep(1)
                    print("Logging in as: " + username)
                    time.sleep(1)
                    screen = 'stronghold'
                else:
                    print('Access denied')
                    time.sleep(2)
                    screen = 'login'

#The stronghold screen is homebase for players. The page also writes the current username
#into the userFief object.
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
        
        userFief.name = username
        userFief.read()
        userFief.ruler = username
        userFief.defenders = str(userFief.defenders)
        userFief.write()

        productionCalc = 0
        maxProductionSoldiers = (int(userFief.goldMod) * 500)
        if int(userFief.defenders) > maxProductionSoldiers:
            productionCalc = ((goldOutput * int(userFief.goldMod)) + (int(maxProductionSoldiers) * int(userFief.goldMod)))

        else: 
            productionCalc = ((goldOutput * int(userFief.goldMod)) + (int(userFief.defenders) * int(userFief.goldMod)))

        if userFief.home != 'True':
            userFief.home = 'True'
            userFief.write()

        print('     On a hilltop overlooking endless rolling fields, you see the only home you have ever known.')
        print('     The Fiefdom is home to ' + textColor.WARNING +  str(userFief.defenders) + textColor.RESET + ' highly skilled warriors, and dozens of loyal citizens.')
        print('\n     Do not let them down')
        print('\n     Within your coffers, you have ' + textColor.WARNING + str(userFief.gold) + textColor.RESET + ' gold.')
        print('     ' + 'Production: ' + str(productionCalc) + ' gold and ' + str((int(defenderOutput) * int(attackFief.defenderMod))) + ' soldiers per hour.')
        print('     Your army of ' + textColor.WARNING + str(userFief.attType) + textColor.RESET + ' stands ready.')
        print('\n')
        print('''
                                            |>>>                        |>>>
                                            |                           |
                                        _  _|_  _                   _  _|_  _
                                       | |_| |_| |                 | |_| |_| |
                                       \  .      /                 \ .    .  /
                                        \    ,  /                   \    .  /
                                         | .   |_   _   _   _   _   _| ,   |
                                         |    .| |_| |_| |_| |_| |_| |  .  |
                                         | ,   | .    .     .      . |    .|
                                         |   . |  .     . .   .  ,   |.    |
                             ___----_____| .   |.   ,  _______   .   |   , |---~_____
                        _---~            |     |  .   /+++++++\    . | .   |         ~---_
                                         |.    | .    |+++++++| .    |   . |              ~-_
                                      __ |   . |   ,  |+++++++|.  . _|__   |                 ~-_
                             ____--`~    '--~~__ .    |++++ __|----~    ~`---,              ___^~-__
                        -~--~                   ~---__|,--~'                  ~~----_____-~'   `~----~

                ''')

        print("     Avalible Commands:")
        print('     -------------------------------------')
        print('     {1}: View Nearby Fiefdoms')
        print('     {2}: Hire Mercenaries')
        #print('{3}: Upgrade Defense')
        print('     {3}: Upgrade Attack')
        print('     {4}: Garrison Soldiers')
        print('     {5}: About')
        print('     {6}: Upcoming Features')
        print('     {7}: Message Board')
        print('     {8}: View Past Winners')
        print('     -------------------------------------')
        print('\n')
        command = input("     Enter your command: ")
        
        if command == '1':
            screen = 'attack'

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

        if command == 'defaults':
            screen = 'createDefaults'

        if command == 'bigmoney':
            screen = 'devTestAddGold'

#This is the screen for the message board.
#----------------------------------------------------------------------------------
    if screen == "board":
        os.system("clear")

        header()

        print('\n    Welcome to the message board! Keep it friendly :)')
        print('\n    --------------------------------------------------------------------------------------\n')

        #print off recent messages
        #dump the last 16 lines of log.txt to the screen
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
                log.write(userFief.name + ': ' + str(tempMessage) + '\n')

            #refresh this page
            screen = 'stronghold'
            
# This is the screen for displaying past winners. Update whenever we have a new winner
#----------------------------------------------------------------------------------
    if screen == "pastWinners":
        os.system("clear")

        header()

        print('\n    These are your honorable past winners of Unnamed Fiefdom Game')
        print('\n    --------------------------------------------------------------------------------------\n')
        print('\n    Pre-Release (12/20/21): Steelwing\n')
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        tempInput = input('    Press Enter To Return To Stronghold\n    ')
        screen = 'board'
 
#This is the screen for purchacing soldiers
#----------------------------------------------------------------------------------
    if screen == "mercs":
        os.system("clear")

        header()
        
        mercCost = 10
        print('You currently have ' + userFief.defenders + ' soldiers and ' +  userFief.gold + ' gold.')
        print('You can hire mercinaries for ' + str(mercCost) + ' gold each?')

        upgradeInput = input('\nHow many mercinaries would you like to hire?\n')

        if int(upgradeInput) == 0:
            print("No changes were made!")

        elif int(upgradeInput) < 0:
            print("You can't hire a negative number of soldiers")

        elif (int(upgradeInput) * mercCost) <=  int(userFief.gold): 
            userFief.defenders = str(int(userFief.defenders) + int(upgradeInput))
            userFief.gold = str(int(userFief.gold) - (mercCost * int(upgradeInput)))
            userFief.write()
            userFief.read()

        else:
            print("You need more gold first!")

        print('\n\n\n\n\n\n\n\n\n\n')
        print("     Avalible Commands:")
        print('     -------------------------------------')
        print('     {1}: Return to Stronghold')
        print('     -------------------------------------')
        print('\n')
        command = input("     Enter your command: ")
        
        if command == "1":
            screen = "stronghold"

#This is the screen for viewing users owned fiefs and for garrisoning soldiers
#----------------------------------------------------------------------------------
    if screen == "garrison":
        os.system("clear")

        header()

        userFiefCount = 0

        print('\n    Fiefs under your rule: \n')
        for filename in os.listdir('fiefs'):
            with open(os.path.join('fiefs', filename), 'r') as f:
                
                tempName = filename[:-4]
                tempName = Fiefdom()
                tempName.name = filename[:-4]
                tempName.read()
                
                homeStatus = " "
                
                if tempName.home != "True" and tempName.ruler == userFief.name: 
                    userFiefCount = userFiefCount + 1
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
            screen = "attack"

#This is the screen for distributing a user's soldiers evenly among fiefs they control
#----------------------------------------------------------------------------------
    if screen == "garrisonSorter":
        os.system("clear")

        header()

        print("\n\n")
        print('Currently Ruled Fiefs: ' + str(userFiefCount))
        print('\n')
        print('Current Number of Soldiers in Stronghold: ' + str(userFief.defenders))
        print('\n\n')
        time.sleep(1)
        if userFiefCount == 0:
            print('You control no fiefs you can distribute to! \n')
            time.sleep(1)
            screen = "garrison"
        else:
            withdrawNum = input('Enter the number of soldiers you would like to evenly distrubute among these ' + str(userFiefCount) + ' fiefs: ')
            time.sleep(1)
        
            if int(withdrawNum) < 0:
                os.system("clear")
                print("You cannot distribute a negative number of soldiers. \n\nThat doesn't even make sense.")
                time.sleep(2)
                screen = 'garrison'

            if (int(userFief.defenders) < int(withdrawNum)) and int(withdrawNum) > 0:
                os.system("clear")
                print("You do not have enough soldiers for that.")
                time.sleep(2)
                screen = 'garrison'

            if (int(userFief.defenders) >= int(withdrawNum)) and int(withdrawNum) > 0 and int(withdrawNum) < userFiefCount:
                os.system("clear")
                print("You have more fiefs than soldiers you want to distribute!")
                time.sleep(2)
                screen = 'garrison'

            if (int(userFief.defenders) >= int(withdrawNum)) and int(withdrawNum) > 0:
                print('Garrisoning ' + str(withdrawNum) + ' soldiers across ' + str(userFiefCount) + ' Fiefs...')
            
                time.sleep(1)

                benchedSoldiers = int(withdrawNum) % userFiefCount
                outgoingSoldierGroups = (int(withdrawNum) - benchedSoldiers)/userFiefCount

                print(str(benchedSoldiers) + ' soldiers were held back to make even groups of ' + str(outgoingSoldierGroups) + '.')

                for filename in os.listdir('fiefs'):
                    with open(os.path.join('fiefs', filename), 'r') as f:
                
                        tempName = filename[:-4]
                        tempName = Fiefdom()
                        tempName.name = filename[:-4]
                        tempName.read()
                
                        homeStatus = " "
                
                        if tempName.home != "True" and tempName.ruler == userFief.name:
                            print(tempName.name + ' had ' + str(tempName.defenders) + ' soldiers. \n')
                            tempName.defenders = str(int(tempName.defenders) + outgoingSoldierGroups)
                            tempName.write()
                            tempName.read()
                            print(tempName.name + ' now has ' + str(tempName.defenders) + ' soldiers! \n')

                userFief.defenders = int(userFief.defenders) - int(withdrawNum) + benchedSoldiers
                userFief.write()
                userFief.read()


                print("\n\n\n\n\n\n\n\n\n")

                print("Avalible Commands:")
                print('-------------------------------------')
                print('{1}: Return to stronghold')
                print('-------------------------------------')
                print('\n')
                command = input("Enter your command: ")
        
                if command == "1":
                    screen = "stronghold"

#This is the screen for updating a user's attack power.
#----------------------------------------------------------------------------------
    if screen == "upgradeFiefAtt":
        os.system("clear")

        header()
        
        attTypeNext = 'undefined'
        attUpgradeCost = 0
        
        if userFief.attLevel == str('0'):
            attTypeNext = 'Angry Villagers with Sharpened Pitchforks'
            attUpgradeCost = 500
                       
        if userFief.attLevel == str('1'):
            attTypeNext = 'Semi-trained Longbow Archers'
            attUpgradeCost = 1500
        
        if userFief.attLevel == str('2'):
            attTypeNext = 'Military Recruits'
            attUpgradeCost = 3000
        
        if userFief.attLevel == str('3'):
            attTypeNext = 'Fairly Well-trained Archers with Flaming Arrows'
            attUpgradeCost = 5000
        
        if userFief.attLevel == str('4'):
            attTypeNext = 'Drunks with Trebuchets'
            attUpgradeCost = 10000
        
        if userFief.attLevel == str('5'):
            attTypeNext = 'Scientists who are Experiementing with Biological Warfare'
            attUpgradeCost = 20000

        if userFief.attLevel == str('6'):
            attTypeNext = 'Peasents with Guns'
            attUpgradeCost = 40000
        
        if userFief.attLevel == str('7'):
            print('\n\n')
            print('     Your current army is made of ' + userFief.attType)
            print('     This is currently the highest attack level!')
            print('\n\n\n\n\n\n\n\n\n\n')
            command = input("     Press Enter")

        else:
            print('\n\n')
            print('     Your current army is made of ' + userFief.attType)
            print('     Would you like to upgrade to ' + attTypeNext + ' for ' + str(attUpgradeCost) + ' gold?')

            upgradeInput = input('\n\n     Confirm Upgrade (y/n?): ')

            if upgradeInput == 'y' and int(userFief.gold) >= attUpgradeCost:
                print("     Upgrade Complete!")
                userFief.attType = attTypeNext
                userFief.attLevel = str(int(userFief.attLevel) + 1)
                userFief.gold = str(int(userFief.gold) - attUpgradeCost)
                userFief.write()
                userFief.read()


            elif upgradeInput == 'y' and int(userFief.gold) < attUpgradeCost:
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
        os.system("clear")

        header()
        
        farmTypeNext = 'undefined'
        farmUpgradeCost = 0
        
        if attackFief.goldMod == str('1'):
            farmTypeNext = 'Watering Cans'
            farmUpgradeCost = 500
                
        if attackFief.goldMod == str('2'):
            farmTypeNext = 'Wheelbarrows'
            farmUpgradeCost = 1500
               
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

            if upgradeInput == 'y' and int(userFief.gold) >= farmUpgradeCost:
                print("\n    Upgrade Complete!")
                attackFief.farmType = farmTypeNext
                attackFief.goldMod = str(int(attackFief.goldMod) + 1)
                userFief.gold = str(int(userFief.gold) - farmUpgradeCost)
                attackFief.write()
                attackFief.read()
                userFief.write()
                userFief.read()
                screen = 'attack'

            elif upgradeInput == 'y' and int(userFief.gold) < farmUpgradeCost:
                print("\n    You need more gold first!")

            elif upgradeInput == 'n':
                print("\n    No changes made.")

            print('\n\n\n\n\n\n\n\n\n\n')
            command = input("     Press Enter ")

        screen = 'attack' 







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
            defUpgradeCost = 1500
               
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
            defUpgradeCost = 40000

        if attackFief.defLevel == str('6'):
            print('     Your current defense style is: ' + attackFief.defType)
            print('     This is currently the best defense style!')
            print('\n\n\n\n\n\n\n\n\n\n')
            command = input("     Press Enter ")
        else:
            print('Your current defense style is: ' + attackFief.defType)
            print('Would you like to upgrade to ' + defTypeNext + ' for ' + str(defUpgradeCost) + ' gold?')


            upgradeInput = input('y/n?')

            if upgradeInput == 'y' and int(userFief.gold) >= defUpgradeCost:
                print("Upgrade Complete!")
                attackFief.defType = defTypeNext
                attackFief.defLevel = str(int(attackFief.defLevel) + 1)
                userFief.gold = str(int(userFief.gold) - defUpgradeCost)
                attackFief.write()
                attackFief.read()
                userFief.write()
                userFief.read()


            elif upgradeInput == 'y' and int(userFief.gold) < defUpgradeCost:
                print("You need more gold first!")

            elif upgradeInput == 'n':
                print("No changes made.")

            print('\n\n\n\n\n\n\n\n\n\n')
            command = input("     Press Enter ")
        
        screen = "attack"
            
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

      Each claimed fiefdom will generate 100 gold per hour. That gold can be spent on defense and attack upgrades
      as well as additional soldiers.

      Upgrade your conqured fiefdoms to keep them safe! Be careful though. Any upgraded fiefdom can still be taken, 
      and your upgrades will be transfered to the new ruler.

      Additional Info is avalible at github.com/Sheeves11/UntitledFiefdomGame

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

#The attack page contains a list of Fiefdoms generated from the /fiefs directory
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
    if screen == "attack":
        os.system("clear")
        
        header()
        
        print("\n")
        print("Nearby Fiefdoms: ")
        print("------------------------------------------------------------------\n")
        
        for filename in os.listdir('fiefs'):
            with open(os.path.join('fiefs', filename), 'r') as f:
                
                tempName = filename[:-4]
                tempName = Fiefdom()
                tempName.name = filename[:-4]
                tempName.read()
                
                homeStatus = " "

                if tempName.home == "True" and tempName.ruler != userFief.name:
                    homeStatus = "Home Stronghold"
                    print (textColor.WARNING + 'The Stronghold of ' +  tempName.name + ' || Defenders: ' + 
                            tempName.defenders + textColor.RESET + ' || Gold: ' + tempName.gold)

                if tempName.home != 'True' and tempName.ruler != userFief.name:
                    print (textColor.YELLOW + tempName.name + ' || Ruled by: ' + tempName.ruler + ' || Defenders: ' + 
                            tempName.defenders + textColor.RESET + ' || Gold: ' + tempName.gold)
                
                if tempName.home == "True" and tempName.ruler == userFief.name: 
                    print (textColor.GREEN + 'The Stronghold of ' + tempName.name + ' || Defenders: ' + 
                            tempName.defenders + textColor.RESET + ' || Gold: ' + tempName.gold)
                
                if tempName.home != "True" and tempName.ruler == userFief.name: 
                    print (textColor.CYAN + tempName.name + ' || Ruled by: ' + tempName.ruler + ' || Defenders: ' + 
                            tempName.defenders + textColor.RESET + ' || Gold: ' + tempName.gold)

        print("\nAvalible Commands:")
        print('-------------------------------------')
        print('{1}: Return to Stronghold')
        print('{2}: Garrison Soldiers')
        print('{Enter fiefdom name or stronghold owner}: View Fiefdom Details') 
        print('-------------------------------------')
        print('\n')
        command = input("Enter your command: ")
        #command = command.lower() #This won't work until file-naming schema is changed!

        if str(command) == '1':
            screen = "stronghold"

        if str(command) == '2':
            screen = "garrison"
        
        if str(command) != '1':
            #search for file to open. If there, initialize it and load data
            #then, switch to a details screen

            fileFief = 'fiefs/' + command + '.txt'
            print (fileFief + 'loading is happening')
            try:
                with open(fileFief, 'r') as f:
                    attackFief.name = f.readline().strip()
                    attackFief.read()
                    
                    if str(attackFief.ruler) == str(userFief.ruler):
                        screen = 'homeDetails'
                    if str(attackFief.home) == 'True':
                        screen = 'stronghold'
                    if str(attackFief.ruler) != str(userFief.ruler):
                        screen = "details"

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

        if attackFief.defLevel == str(0):
            art1()

        if attackFief.defLevel == str(1):
            art2()
        
        if attackFief.defLevel == str(2):
            art3()

        if attackFief.defLevel == str(3):
            art4()

        if attackFief.defLevel == str(4):
            art5()
            
        if attackFief.defLevel == str(5):
            art6()
                        
        if attackFief.defLevel == str(6):
            art7()
        
        
        print('\n')
        print("     Avalible Commands:")
        print('     -------------------------------------')
        print('     {1}: Return to stronghold')
        print('     {2}: View nearby fiefdoms')
        print('     {3}: Deploy additional forces')
        print('     {4}: Withdraw forces')
        print('     {5}: Withdraw gold')
        print('     {6}: Upgrade defenses')
        print('     {7}: Upgrade farms')
        print('     {8): Upgrade training')
        print('     -------------------------------------')
        print('\n')
        command = input("     Enter your command: ")

        if command == "1":
            screen = "stronghold"

        if command == "2":
            screen = "attack"

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
        userFief.gold = str(int(userFief.gold) + int(attackFief.gold))
        attackFief.gold = str(0)
        attackFief.write()
        attackFief.read()
        userFief.write()
        userFief.read()

        screen = "attack"

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
        print('You have ' + str(userFief.defenders) + ' ready to deploy.\n\n')
        deployNum = input('Enter the number of soldiers you would like to deploy: ')
        time.sleep(1)

        print(deployNum + ' : deploynum || userFief.defenders : ' + userFief.defenders)
        
        if int(deployNum) < 0:
            os.system("clear")
            print("You cannot deploy a negative number of soldiers. \n\nThat doesn't even make sense.")
            time.sleep(2)
            screen = 'homeDetails'

        if (int(userFief.defenders) < int(deployNum)) and int(deployNum) > 0:
            os.system("clear")
            print("You do not have enough soldiers for that")
            time.sleep(2)
            screen = 'homeDetails'

        if (int(userFief.defenders) >= int(deployNum)) and int(deployNum) > 0:
            print('Deploying ' + str(deployNum) + ' soldiers to ' + str(attackFief.name))
        
            attackFief.defenders = str(int(attackFief.defenders) + int(deployNum))
            attackFief.write()
            attackFief.read()

            userFief.defenders = str(int(userFief.defenders) - int(deployNum))
            userFief.write()
            userFief.read()
            attackFief.read()

            print("\n\n\n\n\n\n\n\n\n")

            print("Avalible Commands:")
            print('-------------------------------------')
            print('{1}: Return to stronghold')
            print('-------------------------------------')
            print('\n')
            command = input("Enter your command: ")
        
            if command == "1":
                screen = "stronghold"

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
        time.sleep(1)
        print(attackFief.name + ' has ' + attackFief.defenders + ' fighters.')
        time.sleep(1)
        print('\n')
        withdrawNum = input('Enter the number of soldiers you would like to return home: ')
        time.sleep(1)
        
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

            userFief.defenders = str(int(userFief.defenders) + int(withdrawNum))
            userFief.write()
            userFief.read()

            print("\n\n\n\n\n\n\n\n\n")

            print("Avalible Commands:")
            print('-------------------------------------')
            print('{1}: Return to stronghold')
            print('-------------------------------------')
            print('\n')
            command = input("Enter your command: ")
        
            if command == "1":
                screen = "stronghold"

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
        print(attackFief.name + ' looks to have ' + attackFief.defenders + ' fighters.')
        print('Defense Type: ' + attackFief.defType)
        print('-------------------------------------------------------------------------')
        
        print("\n\n")
        
        if attackFief.defLevel == str(0):
            art1()

        if attackFief.defLevel == str(1):
            art2()
        
        if attackFief.defLevel == str(2):
            art3()

        if attackFief.defLevel == str(3):
            art4()

        if attackFief.defLevel == str(4):
            art5()
            
        if attackFief.defLevel == str(5):
            art6()
                        
        if attackFief.defLevel == str(6):
            art7()

        print("\n\n")

        print("Avalible Commands:")
        print('-------------------------------------')
        print('{1}: Return to stronghold')
        print('{2}: View nearby fiefdoms')
        print('{3}: Attack')
        print('-------------------------------------')
        print('\n')
        
        command = input("Enter your command: ")
        
        if command == "1":
            screen = "stronghold"

        if command == "2":
            screen = "attack"

        if command == "3":
            screen = 'battle'

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
            print('\n\nThis battle is between ' + attackFief.name + ' and ' + userFief.name)
            print('\n\nSimulating Battle...')
            time.sleep(1)
            print('\n...\n')
            time.sleep(1)

            attackers = int(userFief.defenders)
            defenders = int(attackFief.defenders)
            
            defenseLosses = 0
            attackLosses = 0
            attackMod = int(userFief.attLevel)
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
            print(userFief.ruler + ' lost ' + str(attackLosses) + ' soldiers')
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
                attackFief.ruler = userFief.ruler
                attackFief.write()

                userFief.defenders = attackers
                userFief.write()
                
                userFief.gold = str(int(userFief.gold) + int(attackFief.gold))
                print('You now have a total of ' + str(userFief.gold) + ' gold!')
                attackFief.gold = str('0')

                userFief.write()
                attackFief.write()


            #if the other player wins
            if attackers <= defenders:
                print('Although your soldiers fought valiantly, they were unable to overcome ' + attackFief.ruler + '\'s forces')
                print('Your forces, now many fewer in number, begin the long march home.')

                attackFief.defenders = defenders
                attackFief.write()

                userFief.defenders = attackers
                userFief.write()

            
            time.sleep(2)
            nothing = input('Continue:')
            screen = 'attack'

#This is a "secret" page that you can use to create default Fiefdoms
#to seed your installation with land that can be taken. 
#
#It should be taken out if you ever open this game up to many players
#----------------------------------------------------------------------------------
    if screen == "createDefaults":

        os.system("clear")
        print('Seeding the world with default fiefdoms')
            
        names = ['Razor Hills', 'Forest of Fado', 'Emerald Cove', 'Stormgrove', 'Aegirs Hall', 'Ashen Grove', 'Bellhollow', 'Howling Plains', 'Jade Hill', 'Knoblands', 'Kestrel Keep', 'Direbrook', 'Greystone']
        for x in names:
            currentFief = Fiefdom()
            currentFief.name = x
            currentFief.defenders = random.randint(10, 100)
            currentFief.gold = random.randint(500, 3100)
            currentFief.write()

        time.sleep(2)
        print('Seeding Complete')

        screen = 'attack'

#This is another "secret" page that can be used to add funds for testing purposes
#
#It should be taken out if you ever open this game up to many players
#----------------------------------------------------------------------------------
    if screen == "devTestAddGold":

        os.system("clear")
        print('Adding Funds!...')

        userFief.gold = str(int(userFief.gold) + 1000000)
        userFief.write()
        
        time.sleep(2)
        print('...Funds Added!')

        screen = 'stronghold'

    '''            
#This screen is for upgrading your home stronghold's defenses
#Not currently in use
#------------------------------------------------------------------------------
    if screen == "upgradeDef":
        os.system("clear")

        header()
        
        defTypeNext = 'undefined'
        defUpgradeCost = 0
        
        if userFief.defLevel == str('0'):
            defTypeNext = 'Wooden Fences'
            defUpgradeCost = 500
                
        if userFief.defLevel == str('1'):
            defTypeNext = 'Really Deep Ditches'
            defUpgradeCost = 1500
               
        if userFief.defLevel == str('2'):
            defTypeNext = 'Ditch Spikes'
            defUpgradeCost = 5000
       
        if userFief.defLevel == str('3'):
            defTypeNext = 'Moat'
            defUpgradeCost = 10000

        if userFief.defLevel == str('4'):
            defTypeNext = 'Alligators in the Moat'
            defUpgradeCost = 20000

        if userFief.defLevel == str('5'):
            defTypeNext = 'Drawbridge'
            defUpgradeCost = 40000

        print('Your current defense style is: ' + userFief.defType)
        print('Would you like to upgrade to ' + defTypeNext + ' for ' + str(defUpgradeCost) + ' gold?')

        upgradeInput = input('y/n?')

        if upgradeInput == 'y' and int(userFief.gold) >= defUpgradeCost:
            print("Upgrade Complete!")
            userFief.defType = defTypeNext
            userFief.defLevel = str(int(userFief.defLevel) + 1)
            userFief.gold = str(int(userFief.gold) - defUpgradeCost)
            userFief.write()
            userFief.read()

        elif upgradeInput == 'y' and int(userFief.gold) < defUpgradeCost:
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
