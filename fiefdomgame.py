import os
import time
import random


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

#initial screen clear
os.system("clear")

#header() should be called on every page
def header():
    print('''
|----------------------------------------------------------------------------------|
|------------------------------UNNAMED FIEFDOM GAME--------------------------------|
|----------------------------------------------------------------------------------|
    ''')

#this is the d20 roll function
def roll(mod):
    d20 = random.randint(1, 20)
    return d20 + mod

#define some text colors
class textColor:
    RED = '\033[91m'
    GREEN = '\033[92m'
    RESET = '\033[0m'
    DIM = '\033[2m'
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    WARNING = '\033[93m'
    YELLOW = '\033[33m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



#the fifedom class holds variables that define a player's stats
class Fifedom:
    name = 'Default Fiefdom'
    ruler = 'Unclaimed'
    home = False
    defenders = 25
    gold = 500
    defLevel = 0
    defType = "Open Camp"
    attLevel = 0
    attType = "Angry Mob"

    #take the current fifedom and write it to the /fifes directory
    def write(self):
        fifeFile = 'fifes/' + self.name + '.txt'
        
        #this part creates a file if it isn't made yet        
        try:
            with open(fifeFile, 'x') as f:

                f.write(self.name + '\n')
                f.write(self.ruler + '\n')
                f.write(str(self.home) + '\n')
                f.write(str(self.defenders) + '\n')
                f.write(str(self.gold) + '\n')
                f.write(str(self.defLevel) + '\n')
                f.write(str(self.defType) + '\n')
                f.write(str(self.attLevel) + '\n')
                f.write(str(self.attType) + '\n')
        except:
            pass

        #write the class variables down line by line in the text file
        try:
            with open(fifeFile, 'w') as f:
                f.write(self.name + '\n')
                f.write(self.ruler + '\n')
                f.write(str(self.home) + '\n')
                f.write(str(self.defenders) + '\n')
                f.write(str(self.gold) + '\n')
                f.write(str(self.defLevel) + '\n')
                f.write(str(self.defType) + '\n')
                f.write(str(self.attLevel) + '\n')
                f.write(str(self.attType) + '\n')
        except:
            pass

    #read class variables line by line
    def read(self):
        fifeFile = 'fifes/' + self.name + '.txt'
        try:
            with open(fifeFile, 'r') as f:
                self.name = f.readline().strip()
                self.ruler = f.readline().strip()
                self.home = f.readline().strip()
                self.defenders = f.readline().strip()
                self.gold = f.readline().strip()
                self.defLevel = f.readline().strip()
                self.defType = f.readline().strip()
                self.attLevel = f.readline().strip()
                self.attType = f.readline().strip()

        except:
            self.write()
            #print('file read fail, creating new fife file for current user')
                    


#create some default objects that we'll write over later
attackFife = Fifedom()
userFife = Fifedom()

#this begins the main game loop
#------------------------------------------------------------------------------
while (loop):
    
    #The login page takes a username, puts it into memory, and sends you to the
    #stronghold page. It also contains a small intro snippet
    #TO DO:
    # - Add user authentication, preferably in a secure way
    if screen == "login":
        os.system("clear")
        header()
        print("\n\n")
        print('''
Welcome to the Unnamed Fiefdom Game!

This is a python programming project and multiplayer war game based on the classic
BBS door games of the 80s and 90s. In much the same way, this system uses a central
server to host the game to multiple users, who access it using a terminal emulator.

See more info at github.com/Sheeves11/UnnamedFiefdomGame
        ''')
        print('\n\n')
        userFife = Fifedom()        
        username = input("Enter your username\n(Note that usernames are not validated at the moment): ")
        currentUsername = username
        
        #if "username.txt" does not exist, create it. The file only contains a name for now.
        try:
            usernameFile = username + ".txt"
            with open(usernameFile, 'x') as f:
                f.write(username)
               # print('WRITING NEW USER FILE')
        except:
            time.sleep(1)
 
        print('\n\n')
        print("Logging in as: " + username)

        time.sleep(2)
        screen = "stronghold"

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
        print(textColor.WARNING + username + "'s Stronghold" + textColor.RESET)
        print("\n\n")
        
        userFife.name = username
        userFife.read()
        userFife.ruler = username
        userFife.defenders = str(userFife.defenders)
        userFife.write()

        if userFife.home != 'True':
            userFife.home = 'True'
            userFife.write()

        print('On a hilltop overlooking endless rolling fields, you see the only home you have ever known.')
        print('The Fiefdom is home to ' + str(userFife.defenders) + ' highly skilled warriors, and dozens of loyal citizens.')
        print('\nDo not let them down')
        print('\n\nWithin your coffers, you have ' + str(userFife.gold) + ' gold.')
        print('Defense type: ' + str(userFife.defType))
        print('Offensive type: ' + str(userFife.attType))
        print('\n\n\n\n')
        print('''\


       _   |~  _             
      [_]--'--[_]
      |'|""'""|'|           
      | | /^\ | |
   ---|_|_|I|_|_|---
         /   \ 

                ''')

        print("Avalible Commands:")
        print('-------------------------------------')
        print('{1}: View Nearby Fiefdoms')
        print('{2}: About')
        print('{3}: Upgrade Defense')
        print('{4}: Upgrade Attack')
        print('{5}: Hire Mercenaries')
        print('-------------------------------------')
        print('\n')
        command = input("Enter your command: ")
        
        if command == "1":
            screen = "attack"

        if command == 'defaults':
            screen = 'createDefaults'

        if command == '2':
            screen = 'about'

        if command == '3':
            screen = 'upgradeDef'

        if command == '4':
            screen = 'upgradeAtt'

        if command == '5':
            screen = 'mercs'



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

        elif (int(userFife.gold) // int(upgradeInput) > mercCost): 
            userFife.defenders = str(int(userFife.defenders) + int(upgradeInput))
            userFife.gold = str(int(userFife.gold) - (mercCost * int(upgradeInput)))
            userFife.write()
            userFife.read()

        else:
            print("You need more gold first!")


        print('\n\n\n\n\n\n\n\n\n\n')
        print("Avalible Commands:")
        print('-------------------------------------')
        print('{1}: Return to Stronghold')
        print('-------------------------------------')
        print('\n')
        command = input("Enter your command: ")
        
        if command == "1":
            screen = "stronghold"

            








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
            defTypeNext = 'Ditch Spikes'
            defUpgradeCost = 5000
       
        if attackFife.defLevel == str('3'):
            defTypeNext = 'Moat'
            defUpgradeCost = 10000

        if attackFife.defLevel == str('4'):
            defTypeNext = 'Alligators in the Moat'
            defUpgradeCost = 20000

        if attackFife.defLevel == str('5'):
            defTypeNext = 'Drawbridge'
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
        print("Avalible Commands:")
        print('-------------------------------------')
        print('{1}: Return to Stronghold')
        print('-------------------------------------')
        print('\n')
        command = input("Enter your command: ")
        
        if command == "1":
            screen = "stronghold"

            
            
#This screen is for upgrading your home stronghold's defenses
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



#This is the about page for the game. Keep it updated
#------------------------------------------------------------------------------
    if screen == "about":
        os.system("clear")

        header()
        print('\n\n\n\n\n\n\n\n\n')

        print('''
        
Intro:
        
Unnamed Fiefdom Game is a python programming project by Mike Quain (mquain@uark.edu)
The goal was to take on a project that was big enough to be challenging, but small enough to stay interesting.
This game looks simple, but it taught me the basics of reading and writing to a database, data persistance, and multi-user tools.

How to play:

Your goal is to control as many fiefdoms as you can manage without spreading your army too thin and leaving yourself open to attack!
Your home stronghold will never fall, but any conquered fifedoms can be taken by opposing players. Make sure you can defend the
territory you claim!

Your fiefdom consists of soldiers and workers. The workers earn income and the soldiers both fight and defend your fiefdoms.
Each worker produces 1 coin per hour. These coins will be used to purchace various upgrades and to recruit new fighters.

Additional Info is avalible at github.com/Sheeves11/UntitledFiefdomGame

        ''')

        print('\n\n\n\n\n\n\n\n\n\n')
        print("Avalible Commands:")
        print('-------------------------------------')
        print('{1}: Return to Stronghold')
        print('-------------------------------------')
        print('\n')
        command = input("Enter your command: ")
        
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
                    print (textColor.WARNING + 'The Stronghold of ' +  tempName.name + ' || Defenders: ' + tempName.defenders + textColor.RESET + ' || Gold: ' + tempName.gold)

                if tempName.home != 'True' and tempName.ruler != userFife.name:
                    print (textColor.YELLOW + tempName.name + ' || Ruled by: ' + tempName.ruler + ' || Defenders: ' + tempName.defenders + textColor.RESET + ' || Gold: ' + tempName.gold)
                
                if tempName.home == "True" and tempName.ruler == userFife.name: 
                    print (textColor.GREEN + 'The Stronghold of ' + tempName.name + ' || Defenders: ' + tempName.defenders + textColor.RESET + ' || Gold: ' + tempName.gold)
                
                if tempName.home != "True" and tempName.ruler == userFife.name: 
                    print (textColor.CYAN + tempName.name + ' || Ruled by: ' + tempName.ruler + ' || Defenders: ' + tempName.defenders + textColor.RESET + ' || Gold: ' + tempName.gold)
                
                #print (' ')

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
        
        print("\n")
        print('Now viewing the Fiefdom of ' + attackFife.name)
        print('You rule this fiefdom')
              
        time.sleep(1)
        print('\nStatus Report:')
        print(attackFife.name + ' has ' + attackFife.defenders + ' fighters.')
        print(attackFife.name + ' has ' + attackFife.gold + ' gold.')
        print(attackFife.name + ' has the following defense: ' + attackFife.defType)

        print("\n\n\n\n\n\n\n\n\n")

        print("Avalible Commands:")
        print('-------------------------------------')
        print('{1}: Return to stronghold')
        print('{2}: View nearby fiefdoms')
        print('{3}: Deploy additional forces')
        print('{4}: Withdraw forces')
        print('{5}: Withdraw gold')
        print('{6}: Upgrade Defenses')
        print('-------------------------------------')
        print('\n')
        command = input("Enter your command: ")

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
        time.sleep(1)
        print(attackFife.name + ' has ' + attackFife.gold + ' gold.')
        time.sleep(1)
        print('\n')
        withdrawNum = input('Enter the amount of gold you would like to return home: ')
        time.sleep(1)
        
        if int(withdrawNum) < 0:
            os.system("clear")
            print("You cannot send home a negative number of gold. \n\nThat doesn't even make sense.")
            time.sleep(2)
            screen = 'homeDetails'

        if (int(attackFife.gold) < int(withdrawNum)) and int(withdrawNum) > 0:
            os.system("clear")
            print("You do not have enough gold for that")
            time.sleep(2)
            screen = 'homeDetails'

        if (int(attackFife.gold) >= int(withdrawNum)) and int(withdrawNum) > 0:
            print('Sending ' + str(withdrawNum) + ' gold back home')
        
            attackFife.gold = str(int(attackFife.gold) - int(withdrawNum))
            attackFife.write()
            attackFife.read()

            userFife.gold = str(int(userFife.gold) + int(withdrawNum))
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
        print('Now viewing the Fiefdom of ' + attackFife.name)
        print('This Fiefdome is ruled by ' + attackFife.ruler)
        print('-------------------------------------------------------------------------')
        print('\nYour scouts return early in the morning, bringing back reports of the enemy fiefdom.')
        print(attackFife.name + ' looks to have ' + attackFife.defenders + ' fighters.')
        print('Defense Type: ' + attackFife.defType)
        print('-------------------------------------------------------------------------')
        print("\n\n\n\n\n\n\n\n\n")
        
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
            attackMod = 0
            defenseMod = 0
            
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

            #if the other player wins
            if attackers <= defenders:
                print('Although your soldiers fought valiantly, they were unable to overcome ' + attackFife.ruler + '\'s forces')
                print('Your forces, now many fewer in number, begin the long march home.')

                attackFife.defenders = defenders
                attackFife.write()

                userFife.defenders = attackers
                userFife.write()

            print("\n\n\n\n\n\n\n\n\n")
            print("Type leave to return to your stronghold: ")
            command = input("Enter your command: ")

            if command == "leave":
                screen = "stronghold"

            if command == "attack":
                screen = "attack"

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

        screen = input("Enter your command: ")
