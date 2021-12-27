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

#hourly production values
#these should be changed to match the values in fiefdombackend.py
goldOutput = 100
defenderOutput = 3

#initial screen clear
os.system("clear")

#create some default objects that we'll write over later
attackFife = Fifedom()
userFife = Fifedom()

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
        userFife = Fifedom()        
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
#into the userFife object.
#
#Each player gets a "home" stronghold that can't be overrun. This page displays the stats
#for that stronghold.
#
#TO DO:
# - Flesh this out a little more. Make it prettier.
# - Add a list of owned Fifedoms that aren't the home stronghold
#------------------------------------------------------------------------------
    if screen == "stronghold":
        os.system("clear")

        header()
        print("\n")
        print('     ' + textColor.WARNING + username + "'s Stronghold" + textColor.RESET)
        print("\n")
        
        userFife.name = username
        userFife.read()
        userFife.ruler = username
        userFife.defenders = str(userFife.defenders)
        userFife.write()

        productionCalc = 0
        maxProductionSoldiers = (int(userFife.goldMod) * 500)
        if int(userFife.defenders) > maxProductionSoldiers:
            productionCalc = ((goldOutput * int(userFife.goldMod)) + (int(maxProductionSoldiers) * int(userFife.goldMod)))

        else: 
            productionCalc = ((goldOutput * int(userFife.goldMod)) + (int(userFife.defenders) * int(userFife.goldMod)))

        if userFife.home != 'True':
            userFife.home = 'True'
            userFife.write()

        print('     On a hilltop overlooking endless rolling fields, you see the only home you have ever known.')
        print('     The Fiefdom is home to ' + textColor.WARNING +  str(userFife.defenders) + textColor.RESET + ' highly skilled warriors, and dozens of loyal citizens.')
        print('\n     Do not let them down')
        print('\n     Within your coffers, you have ' + textColor.WARNING + str(userFife.gold) + textColor.RESET + ' gold.')
        print('     ' + 'Production: ' + str(productionCalc) + ' gold and ' + str((int(defenderOutput) * int(attackFife.defenderMod))) + ' soldiers per hour.')
        print('     Your army of ' + textColor.WARNING + str(userFife.attType) + textColor.RESET + ' stands ready.')
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
        print('     {4}: About')
        print('     {5}: Upcoming Features')
        print('     {6}: Message Board')
        print('     {7}: View Past Winners')
        print('     -------------------------------------')
        print('\n')
        command = input("     Enter your command: ")
        
        if command == '1':
            screen = 'attack'

        if command == '2':
            screen = 'mercs'
            
        if command == '3':
            screen = 'upgradeFifeAtt'

        if command == '4':
            screen = 'about'
            
        if command == '5':
            screen = 'features'

        if command == '6':
            screen = 'board'
            
        if command == '7':
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
                log.write(userFife.name + ': ' + str(tempMessage) + '\n')

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
        print('You currently have ' + userFife.defenders + ' soldiers and ' +  userFife.gold + ' gold.')
        print('You can hire mercinaries for ' + str(mercCost) + ' gold each?')

        upgradeInput = input('\nHow many mercinaries would you like to hire?\n')

        if int(upgradeInput) == 0:
            print("No changes were made!")

        elif int(upgradeInput) < 0:
            print("You can't hire a negative number of soldiers")

        elif (int(upgradeInput) * mercCost) <=  int(userFife.gold): 
            userFife.defenders = str(int(userFife.defenders) + int(upgradeInput))
            userFife.gold = str(int(userFife.gold) - (mercCost * int(upgradeInput)))
            userFife.write()
            userFife.read()

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

#This is the screen for updating a user's attack power.
#----------------------------------------------------------------------------------
    if screen == "upgradeFifeAtt":
        os.system("clear")

        header()
        
        attTypeNext = 'undefined'
        attUpgradeCost = 0
        
        if userFife.attLevel == str('0'):
            attTypeNext = 'Angry Villagers with Sharpened Pitchforks'
            attUpgradeCost = 500
                       
        if userFife.attLevel == str('1'):
            attTypeNext = 'Semi-trained Longbow Archers'
            attUpgradeCost = 1500
        
        if userFife.attLevel == str('2'):
            attTypeNext = 'Military Recruits'
            attUpgradeCost = 3000
        
        if userFife.attLevel == str('3'):
            attTypeNext = 'Fairly Well-trained Archers with Flaming Arrows'
            attUpgradeCost = 5000
        
        if userFife.attLevel == str('4'):
            attTypeNext = 'Drunks with Trebuchets'
            attUpgradeCost = 10000
        
        if userFife.attLevel == str('5'):
            attTypeNext = 'Scientists who are Experiementing with Biological Warfare'
            attUpgradeCost = 20000

        if userFife.attLevel == str('6'):
            attTypeNext = 'Peasents with Guns'
            attUpgradeCost = 40000
        
        if userFife.attLevel == str('7'):
            print('\n\n')
            print('     Your current army is made of ' + userFife.attType)
            print('     This is currently the highest attack level!')
            print('\n\n\n\n\n\n\n\n\n\n')
            command = input("     Press Enter")
            screen = "stronghold"

        else:
            print('\n\n')
            print('     Your current army is made of ' + userFife.attType)
            print('     Would you like to upgrade to ' + attTypeNext + ' for ' + str(attUpgradeCost) + ' gold?')

            upgradeInput = input('\n\n     Confirm Upgrade (y/n?): ')

            if upgradeInput == 'y' and int(userFife.gold) >= attUpgradeCost:
                print("     Upgrade Complete!")
                userFife.attType = attTypeNext
                userFife.attLevel = str(int(userFife.attLevel) + 1)
                userFife.gold = str(int(userFife.gold) - attUpgradeCost)
                userFife.write()
                userFife.read()


            elif upgradeInput == 'y' and int(userFife.gold) < attUpgradeCost:
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
        
        if attackFife.goldMod == str('1'):
            farmTypeNext = 'Watering Cans'
            farmUpgradeCost = 500
                
        if attackFife.goldMod == str('2'):
            farmTypeNext = 'Wheelbarrows'
            farmUpgradeCost = 1500
               
        if attackFife.goldMod == str('3'):
            farmTypeNext = 'Fertilizer'
            farmUpgradeCost = 5000
       
        if attackFife.goldMod == str('4'):
            farmTypeNext = 'Horse Plows'
            farmUpgradeCost = 10000

        if attackFife.goldMod == str('5'):
            farmTypeNext = 'Crop Rotation'
            farmUpgradeCost = 20000

        if attackFife.goldMod == str('6'):
            farmTypeNext = 'Artificial Selection'
            farmUpgradeCost = 40000

        print('\n    Your fiefdom\'s gold output is currently: ' + str((int(attackFife.goldMod) * goldOutput)) + ' per hour.')
        print('    Would you like to upgrade to ' + farmTypeNext + ' for ' + str(farmUpgradeCost) + ' gold?')


        upgradeInput = input('\n    y/n: ')

        if upgradeInput == 'y' and int(userFife.gold) >= farmUpgradeCost:
            print("\n    Upgrade Complete!")
            attackFife.farmType = farmTypeNext
            attackFife.goldMod = str(int(attackFife.goldMod) + 1)
            userFife.gold = str(int(userFife.gold) - farmUpgradeCost)
            attackFife.write()
            attackFife.read()
            userFife.write()
            userFife.read()
            screen = 'attack'

        elif upgradeInput == 'y' and int(userFife.gold) < farmUpgradeCost:
            print("\n    You need more gold first!")

        elif upgradeInput == 'n':
            print("\n    No changes made.")

        print('\n\n\n\n\n\n\n\n\n\n')
        command = input("     Press Enter ")
        screen = 'attack' 







#This is the screen for updating a fief's defenses. Note: there are two screens
#like this. One for fiefs and one for player strongholds.
#----------------------------------------------------------------------------------
    if screen == "upgradeFifeDef":
        os.system("clear")

        header()
        
        defTypeNext = 'undefined'
        defUpgradeCost = 0
        
        if attackFife.defLevel == str('0'):
            defTypeNext = 'Wooden Fences'
            defUpgradeCost = 500
                
        if attackFife.defLevel == str('1'):
            defTypeNext = 'Really Deep Ditches'
            defUpgradeCost = 1500
               
        if attackFife.defLevel == str('2'):
            defTypeNext = 'Tall Towers'
            defUpgradeCost = 5000
       
        if attackFife.defLevel == str('3'):
            defTypeNext = 'In a Lake'
            defUpgradeCost = 10000

        if attackFife.defLevel == str('4'):
            defTypeNext = 'On Top of a Mountain'
            defUpgradeCost = 20000

        if attackFife.defLevel == str('5'):
            defTypeNext = 'Boiling Oil'
            defUpgradeCost = 40000

        print('Your current defense style is: ' + attackFife.defType)
        print('Would you like to upgrade to ' + defTypeNext + ' for ' + str(defUpgradeCost) + ' gold?')


        upgradeInput = input('y/n?')

        if upgradeInput == 'y' and int(userFife.gold) >= defUpgradeCost:
            print("Upgrade Complete!")
            attackFife.defType = defTypeNext
            attackFife.defLevel = str(int(attackFife.defLevel) + 1)
            userFife.gold = str(int(userFife.gold) - defUpgradeCost)
            attackFife.write()
            attackFife.read()
            userFife.write()
            userFife.read()


        elif upgradeInput == 'y' and int(userFife.gold) < defUpgradeCost:
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

#The attack page contains a list of fifedoms generated from the /fifes directory
#
#To Do
# - add some sort of "next page" function so that the printout won't scroll
#   off the page as more players join.
# - add some sort of sorting on the list. 
#-------------------------------------------------------------------------------
    if screen == "attack":
        os.system("clear")
        
        header()
        
        print("\n")
        print("Nearby Fiefdoms: ")
        print("------------------------------------------------------------------\n")
        
        for filename in os.listdir('fifes'):
            with open(os.path.join('fifes', filename), 'r') as f:
                
                tempName = filename[:-4]
                tempName = Fifedom()
                tempName.name = filename[:-4]
                tempName.read()
                
                homeStatus = " "

                if tempName.home == "True" and tempName.ruler != userFife.name:
                    homeStatus = "Home Stronghold"
                    print (textColor.WARNING + 'The Stronghold of ' +  tempName.name + ' || Defenders: ' + 
                            tempName.defenders + textColor.RESET + ' || Gold: ' + tempName.gold)

                if tempName.home != 'True' and tempName.ruler != userFife.name:
                    print (textColor.YELLOW + tempName.name + ' || Ruled by: ' + tempName.ruler + ' || Defenders: ' + 
                            tempName.defenders + textColor.RESET + ' || Gold: ' + tempName.gold)
                
                if tempName.home == "True" and tempName.ruler == userFife.name: 
                    print (textColor.GREEN + 'The Stronghold of ' + tempName.name + ' || Defenders: ' + 
                            tempName.defenders + textColor.RESET + ' || Gold: ' + tempName.gold)
                
                if tempName.home != "True" and tempName.ruler == userFife.name: 
                    print (textColor.CYAN + tempName.name + ' || Ruled by: ' + tempName.ruler + ' || Defenders: ' + 
                            tempName.defenders + textColor.RESET + ' || Gold: ' + tempName.gold)
                
        print("\nAvalible Commands:")
        print('-------------------------------------')
        print('{1}: Return to stronghold')
        print('{Enter fiefdom name or stronghold owner}: View Fiefdom Details') 
        print('-------------------------------------')
        print('\n')
        command = input("Enter your command: ")
        
        if str(command) == '1':
            screen = "stronghold"
        
        if str(command) != '1':
            #search for file to open. If there, initialize it and load data
            #then, switch to a details screen

            fileFife = 'fifes/' + command + '.txt'
            print (fileFife + 'loading is happening')
            try:
                with open(fileFife, 'r') as f:
                    attackFife.name = f.readline().strip()
                    attackFife.read()
                    
                    if str(attackFife.ruler) == str(userFife.ruler):
                        screen = 'homeDetails'
                    if str(attackFife.home) == 'True':
                        screen = 'stronghold'
                    if str(attackFife.ruler) != str(userFife.ruler):
                        screen = "details"

            except:
                print ('the file open broke')

        os.system('clear')

#The homeDetails page gets called when a user tries to view their own Fifedom
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
        attackFife.read()
        
        productionCalc = 0

        maxProductionSoldiers = (int(attackFife.goldMod) * 500)

        if int(attackFife.defenders) > maxProductionSoldiers:
            productionCalc = ((goldOutput * int(attackFife.goldMod)) + (int(maxProductionSoldiers) * int(attackFife.goldMod)))

        else: 
            productionCalc = ((goldOutput * int(attackFife.goldMod)) + (int(attackFife.defenders) * int(attackFife.goldMod)))
    
        print("\n")
        print('     You rule the fiefdom of ' + attackFife.name)
        print('\n')
        print('     Status Report:')
        print('\n     ' + 'Defenders: ' + attackFife.defenders + '\n     Gold: ' + attackFife.gold + ' gold.')
        print('     ' + 'Defensive Strategy: ' + attackFife.defType)
        print('     ' + 'Production: ' + str(productionCalc) + ' gold and ' + str(defenderOutput * int(attackFife.defenderMod))
                + ' soldiers per hour.')
        print("\n")

        if attackFife.defLevel == str(0):
            art1()

        if attackFife.defLevel == str(1):
            art2()
        
        if attackFife.defLevel == str(2):
            art3()

        if attackFife.defLevel == str(3):
            art4()

        if attackFife.defLevel == str(4):
            art5()
            
        if attackFife.defLevel == str(5):
            art6()
                        
        if attackFife.defLevel == str(6):
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
            screen = 'upgradeFifeDef'

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
        print('Now viewing the Fiefdom of ' + attackFife.name)
        print('\n')
        time.sleep(0)
        print(attackFife.name + ' has ' + attackFife.gold + ' gold.')
        time.sleep(1)
        print('\n')

        print('Sending ' + str(attackFife.gold) + ' gold back home')
        time.sleep(1)
        userFife.gold = str(int(userFife.gold) + int(attackFife.gold))
        attackFife.gold = str(0)
        attackFife.write()
        attackFife.read()
        userFife.write()
        userFife.read()

        screen = "attack"

#The deploy screen allows players to deploy defenders to a Fifedom that they 
#currently control.
#
#To Do
# - add a "withdraw" page for pulling troops out of a Fifedom
# - verify that the player has the troops avalible for deployment
# - prevent negative numbers
#------------------------------------------------------------------------------
    if screen == 'deploy':
        os.system("clear")
        
        header()
        
        print("\n\n")
        print('Now viewing the Fiefdom of ' + attackFife.name)
        print('\n\n')
        time.sleep(1)
        print(attackFife.name + ' has ' + attackFife.defenders + ' fighters.')
        time.sleep(1)
        print('You have ' + str(userFife.defenders) + ' ready to deploy.\n\n')
        deployNum = input('Enter the number of soldiers you would like to deploy: ')
        time.sleep(1)

        print(deployNum + ' : deploynum || userFife.defenders : ' + userFife.defenders)
        
        if int(deployNum) < 0:
            os.system("clear")
            print("You cannot deploy a negative number of soldiers. \n\nThat doesn't even make sense.")
            time.sleep(2)
            screen = 'homeDetails'

        if (int(userFife.defenders) < int(deployNum)) and int(deployNum) > 0:
            os.system("clear")
            print("You do not have enough soldiers for that")
            time.sleep(2)
            screen = 'homeDetails'

        if (int(userFife.defenders) >= int(deployNum)) and int(deployNum) > 0:
            print('Deploying ' + str(deployNum) + ' soldiers to ' + str(attackFife.name))
        
            attackFife.defenders = str(int(attackFife.defenders) + int(deployNum))
            attackFife.write()
            attackFife.read()

            userFife.defenders = str(int(userFife.defenders) - int(deployNum))
            userFife.write()
            userFife.read()
            attackFife.read()

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
        print('Now viewing the Fiefdom of ' + attackFife.name)
        print('\n\n')
        time.sleep(1)
        print(attackFife.name + ' has ' + attackFife.defenders + ' fighters.')
        time.sleep(1)
        print('\n')
        withdrawNum = input('Enter the number of soldiers you would like to return home: ')
        time.sleep(1)
        
        if int(withdrawNum) < 0:
            os.system("clear")
            print("You cannot send home a negative number of soldiers. \n\nThat doesn't even make sense.")
            time.sleep(2)
            screen = 'homeDetails'

        if (int(attackFife.defenders) < int(withdrawNum)) and int(withdrawNum) > 0:
            os.system("clear")
            print("You do not have enough soldiers for that")
            time.sleep(2)
            screen = 'homeDetails'

        if (int(attackFife.defenders) >= int(withdrawNum)) and int(withdrawNum) > 0:
            print('Returning ' + str(withdrawNum) + ' soldiers back home')
        
            attackFife.defenders = str(int(attackFife.defenders) - int(withdrawNum))
            attackFife.write()
            attackFife.read()

            userFife.defenders = str(int(userFife.defenders) + int(withdrawNum))
            userFife.write()
            userFife.read()

            print("\n\n\n\n\n\n\n\n\n")

            print("Avalible Commands:")
            print('-------------------------------------')
            print('{1}: Return to stronghold')
            print('-------------------------------------')
            print('\n')
            command = input("Enter your command: ")
        
            if command == "1":
                screen = "stronghold"

#This is the details page for enemy fifedoms
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
        print('Now viewing the fiefdom of ' + attackFife.name)
        print('This fiefdom is ruled by ' + attackFife.ruler)
        print('-------------------------------------------------------------------------')
        print('\nYour scouts return early in the morning, bringing back reports of the enemy fiefdom.')
        print(attackFife.name + ' looks to have ' + attackFife.defenders + ' fighters.')
        print('Defense Type: ' + attackFife.defType)
        print('-------------------------------------------------------------------------')
        
        print("\n\n")
        
        if attackFife.defLevel == str(0):
            art1()

        if attackFife.defLevel == str(1):
            art2()
        
        if attackFife.defLevel == str(2):
            art3()

        if attackFife.defLevel == str(3):
            art4()

        if attackFife.defLevel == str(4):
            art5()
            
        if attackFife.defLevel == str(5):
            art6()
                        
        if attackFife.defLevel == str(6):
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

#The "battle" page simulates a battle between two fifedoms. This is currently the most
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
        if attackFife.home == 'True':
            os.system('clear')
            print('You are unable to claim a player\'s home stronghold')
            time.sleep(3)
            screen = 'stronghold'

        #this is where the battle logic happens!
        if attackFife.home == 'False':
            print('\n\nThis battle is between ' + attackFife.name + ' and ' + userFife.name)
            print('\n\nSimulating Battle...')
            time.sleep(1)
            print('\n...\n')
            time.sleep(1)

            attackers = int(userFife.defenders)
            defenders = int(attackFife.defenders)
            
            defenseLosses = 0
            attackLosses = 0
            attackMod = int(userFife.attLevel)
            defenseMod = int(attackFife.defLevel)
            
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
            print(userFife.ruler + ' lost ' + str(attackLosses) + ' soldiers')
            print(attackFife.ruler + ' lost ' + str(defenseLosses) + ' soldiers')
            print('\n')
            print('------------------------------------------------------------------------------')
            print('------------------------------------------------------------------------------')
            print('\n\n')

            #if the current player wins
            if attackers > defenders:
                print('After a hard fought battle, your weary forces remain standing')
                print('You are the new ruler of ' + attackFife.name)
                
                attackFife.defenders = defenders
                attackFife.ruler = userFife.ruler
                attackFife.write()

                userFife.defenders = attackers
                userFife.write()
                
                userFife.gold = str(int(userFife.gold) + int(attackFife.gold))
                print('You now have a total of ' + str(userFife.gold) + ' gold!')
                attackFife.gold = str('0')

                userFife.write()
                attackFife.write()


            #if the other player wins
            if attackers <= defenders:
                print('Although your soldiers fought valiantly, they were unable to overcome ' + attackFife.ruler + '\'s forces')
                print('Your forces, now many fewer in number, begin the long march home.')

                attackFife.defenders = defenders
                attackFife.write()

                userFife.defenders = attackers
                userFife.write()

            
            time.sleep(2)
            nothing = input('Continue:')
            screen = 'attack'

#This is a "secret" page that you can use to create default fifedoms
#to seed your installation with land that can be taken. 
#
#It should be taken out if you ever open this game up to many players
#----------------------------------------------------------------------------------
    if screen == "createDefaults":

        os.system("clear")
        print('Seeding the world with default fiefdoms')
            
        names = ['Razor Hills', 'Forest of Fado', 'Emerald Cove', 'Stormgrove', 'Aegirs Hall', 'Ashen Grove', 'Bellhollow', 'Howling Plains', 'Jade Hill', 'Knoblands', 'Kestrel Keep', 'Direbrook', 'Greystone']
        for x in names:
            currentFife = Fifedom()
            currentFife.name = x
            currentFife.defenders = random.randint(10, 100)
            currentFife.gold = random.randint(500, 3100)
            currentFife.write()

        time.sleep(2)
        print('Seeding Complete')

        screen = 'stronghold'

#This is another "secret" page that can be used to add funds for testing purposes
#
#It should be taken out if you ever open this game up to many players
#----------------------------------------------------------------------------------
    if screen == "devTestAddGold":

        os.system("clear")
        print('Adding Funds!...')

        userFife.gold = str(int(userFife.gold) + 1000000)

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
        
        if userFife.defLevel == str('0'):
            defTypeNext = 'Wooden Fences'
            defUpgradeCost = 500
                
        if userFife.defLevel == str('1'):
            defTypeNext = 'Really Deep Ditches'
            defUpgradeCost = 1500
               
        if userFife.defLevel == str('2'):
            defTypeNext = 'Ditch Spikes'
            defUpgradeCost = 5000
       
        if userFife.defLevel == str('3'):
            defTypeNext = 'Moat'
            defUpgradeCost = 10000

        if userFife.defLevel == str('4'):
            defTypeNext = 'Alligators in the Moat'
            defUpgradeCost = 20000

        if userFife.defLevel == str('5'):
            defTypeNext = 'Drawbridge'
            defUpgradeCost = 40000

        print('Your current defense style is: ' + userFife.defType)
        print('Would you like to upgrade to ' + defTypeNext + ' for ' + str(defUpgradeCost) + ' gold?')

        upgradeInput = input('y/n?')

        if upgradeInput == 'y' and int(userFife.gold) >= defUpgradeCost:
            print("Upgrade Complete!")
            userFife.defType = defTypeNext
            userFife.defLevel = str(int(userFife.defLevel) + 1)
            userFife.gold = str(int(userFife.gold) - defUpgradeCost)
            userFife.write()
            userFife.read()

        elif upgradeInput == 'y' and int(userFife.gold) < defUpgradeCost:
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
