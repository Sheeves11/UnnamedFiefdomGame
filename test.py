import os
import time
import random

#global variables
loop = True
screen = "login"
currentUsername = 'default'
tempName = {}

#initial screen clear
os.system("clear")

class Fifedom:
    name = 'Default Fifedom'
    ruler = 'Unclaimed'
    home = False
    defenders = 25
    workers = 25
    location = 1




    def write(self):
        fifeFile = 'fifes/' + self.name + '.txt'
#this part creates a file if it isn't made yet        
        try:
            with open(fifeFile, 'x') as f:

                f.write(self.name + '\n')
                f.write(self.ruler + '\n')
                f.write(str(self.home) + '\n')
                f.write(str(self.defenders) + '\n')
                f.write(str(self.workers) + '\n')
                f.write(str(self.location) + '\n')
        except:
            pass

#write the class variables down line by line in the text file
        try:
            with open(fifeFile, 'w') as f:
                f.write(self.name + '\n')
                f.write(self.ruler + '\n')
                f.write(str(self.home) + '\n')
                f.write(str(self.defenders) + '\n')
                f.write(str(self.workers) + '\n')
                f.write(str(self.location) + '\n')
        except:
            pass

#read class variables line by line
    def read(self):
        fifeFile = 'fifes/' + self.name + '.txt'
        try:
            with open(fifeFile, 'r') as f:
#                print('file opened successfully: ' + fifeFile)
                
                self.name = f.readline().strip()
#                print ('self.name =' + self.name)
                self.ruler = f.readline().strip()
                self.home = f.readline().strip()
                self.defenders = f.readline().strip()
        except:
            self.write()
            print('file read fail, creating new fife file for current user')
                    
#        print('ruler name in the system as: ' + self.ruler)


#defaut fief class
attackFife = Fifedom()
userFife = Fifedom()

#this begins the main game loop
#------------------------------------------------------------------------------
while (loop):
    if screen == "login":
        os.system("clear")

        print("Welcome to UNNAMED FIEFDOM GAME")
        print("\n\n")
        username = input("Enter your username: ")
        currentUsername = username

        try:
            usernameFile = username + ".txt"
            with open(usernameFile, 'x') as f:
                f.write(username)
                print('WRITING NEW USER FILE')
        except:
            time.sleep(1)
 


        print('\n\n')
        print("Logging in as: " + username)

        time.sleep(2)
        screen = "stronghold"


#------------------------------------------------------------------------------
    if screen == "stronghold":
        os.system("clear")

        print("UNNAMED FIEFDOM GAME")
        print("\n\n")
        print(username + "'s Stronghold")
        print("\n\n\n")
        
        userFife.name = username
        userFife.read()
        userFife.ruler = username
        userFife.defenders = str(userFife.defenders)
        userFife.write()

        if userFife.home != 'True':
            userFife.home = 'True'
            userFife.write()

        print('On a hilltop overlooking endless rolling fields, you see the only home you have ever known.')
        print('\n\nThe Fifedom is home to ' + str(userFife.defenders) + ' highly skilled warriors, and dozens of loyal citizens.')
        print('\nDo not let them down')
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
        print('{1}: View Nearby Fifedoms')
        print('-------------------------------------')
        print('\n')
        command = input("Enter your command: ")
        
        if command == "1":
            screen = "attack"

        if command == 'defaults':
            screen = 'createDefaults'


#-------------------------------------------------------------------------------
    if screen == "attack":
        os.system("clear")
        print("UNNAMED FIEFDOM GAME")
        print("\n")
        print("Nearby Fiefdoms: ")
        print("-------------------------------------------------------")
        print('\n')
        
        for filename in os.listdir('fifes'):
            with open(os.path.join('fifes', filename), 'r') as f:
                
                tempName = filename[:-4]
                tempName = Fifedom()
                tempName.name = filename[:-4]
                tempName.read()
                
                homeStatus = " "

                if tempName.home == "True":
                    homeStatus = "Home Stronghold"

                print ('Fifedom: ' + tempName.name + ' || Ruled by: ' + tempName.ruler)
                print ('Number of Warriors: ' + tempName.defenders + ' || ' + homeStatus)
                print ('\n')
                

        print("Avalible Commands:")
        print('-------------------------------------')
        print('{1}: Return to stronghold')
        print('{Stronghold Name}: View Fifedom Details') 
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
#                    print ('testing the file open: ')
#                    print (f.readline().strip())
                    attackFife.name = f.readline().strip()
#                    attackFife.ruler = f.readline().strip()

                    attackFife.read()
                    
                    screen = "details"


            except:
                print ('the file open broke')

        os.system('clear')


#------------------------------------------------------------------------------

    if screen == "details":
        os.system("clear")

        print("UNNAMED FIEFDOM GAME")
        print("\n\n")
        print('Now viewing the Fifedome of ' + attackFife.name)
        print('This Fifedome is ruled by ' + attackFife.ruler)
        
        
        
        
        time.sleep(2)
        print('\n\nYour scouts return early in the morning, bringing reports of the enemy Fifedom.')
        time.sleep(1)
        print(attackFife.name + ' looks to have ' + attackFife.defenders + ' fighters.')
        time.sleep(3)




        print("\n\n\n\n\n\n\n\n\n")



        print("Avalible Commands:")
        print('-------------------------------------')
        print('{1}: Return to stronghold')
        print('{2}: View nearby fifedoms')
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


#------------------------------------------------------------------------------

    if screen == "battle":
        os.system("clear")

        print("UNNAMED FIEFDOM GAME")
        print("\n\n")
        print('This battle is between ' + attackFife.name + ' and ' + userFife.name)
        
        print('\n\nSimulating Battle...\n\n')
        if attackFife.home == 'True':
            print('You are unable to claim a player\'s home stronghold')
            time.sleep(3)
            screen = 'stronghold'
        
        if attackFife.home == 'False':
            
            #battle logic time!
            
            #assign some temp variables
            playerWins = True
            
            print('\n\n\n\n\nThe two great fifedoms of ' + userFife.name + ' and ' + attackFife.name + ' prepare for battle!')
            time.sleep(2)

            print('\n\n' + userFife.name + ' fires the first volley of arrows, catching the defenders unaware.')
            time.sleep(1)
            print('\n\n...\n\n')
            time.sleep(1)

            casualties = 1
            maxCasualties = int(attackFife.defenders)
            casualties = random.randint(0, maxCasualties)


            userCasualties = 1
            userCasualties = random.randint(0, int(userFife.defenders))
           


            #make sure that the fife has at least one guy left
            if int(attackFife.defenders) <= 0:
                attackFife.defenders = 1
            
            attackFife.defenders = int(attackFife.defenders) - casualties
            
            #make sure they have a guy left
            if int(attackFife.defenders) <= 0:
                attackFife.defenders = 1

            attackFife.write()

            print('\n\n' + attackFife.name + ' suffers ' + str(casualties) + ' casulaties.')
            
            time.sleep(2)
            print('\n\n' + 'Stunned by your attack, the enemy charges')
            time.sleep(1)
            print('\n\n...\n\n')
            time.sleep(1)
            print('You suffer ' + str(userCasualties) + ' casualties')

            userFife.defenders = int(userFife.defenders) - userCasualties

            if int(attackFife.defenders) <= 0:
                userFife.defenders = 1

            userFife.write()





            if (int(attackFife.defenders) >= int(userFife.defenders)):
                playerWins = False


            if playerWins == True:
                #this happens if the user wins the fight            
                attackFife.ruler = userFife.name
                attackFife.write()

                print(userFife.name + ' is the winner!')
                time.sleep(1)
                print('\n----------------------------\n')
                print('Crushed by their loss, some of ' + attackFife.name + " \'s fighters join you.")
                
                defectors = 1
                defectors = int(attackFife.defenders) - random.randint(0, int(attackFife.defenders))
                attackFife.defenders = int(attackFife.defenders) - defectors
                attackFife.write()

                userFife.defenders = int(userFife.defenders) + defectors


                print('You gain ' + str(defectors) + ' somewhat loyal soldiers')

            
            if playerWins == False:
                #this happens if the player loses
                
                print(userFife.name + ' has been defeted')


            print("\n\n\n\n\n\n\n\n\n")
            print("Type leave to return to your stronghold: ")
            command = input("Enter your command: ")

            if command == "leave":
                screen = "stronghold"

            if command == "attack":
                screen = "attack"



#-------------------------------------------------------------------------------
#    if screen == "fifedomTest":
#
#        os.system("clear")
#        print('Welcome to the Fifedom read/write test')
#        
#        currentFifeName = input('Enter the name of your new Fifedom: ')
#        
#
#        os.system("clear")
#            
#        currentFife = Fifedom()
#        
#        currentFife.name = currentFifeName
#
#        currentFife.write()
#
#        currentFife.read()
#        print("UNNAMED FIEFDOM GAME")
#        print('\n')
#        print("-------------------------------------------------------")
#        print('\n')
#        print('Name: ' + currentFife.name)
#        print('Ruler: ' + currentFife.ruler)
#        print('Homebase: ' + str(currentFife.home))
#        print('Villagers: ' + str(currentFife.workers))
#        print('Location: ' + str(currentFife.location))
#        print('\n\n')
#
#
#        command = input('Enter your command: ')
#

#-------------------------------------------------------------------------------
#    if screen == "fifedom":
#
#        os.system("clear")
#        testfife = Fifedom()
#        testfife.read()
#        print("UNNAMED FIEFDOM GAME")
#        print('\n')
#        print("-------------------------------------------------------")
#        print('\n')
#        print('Name: ' + testfife.name)
#        print('Ruler: ' + testfife.ruler)
#        print('Homebase: ' + str(testfife.home))
#        print('Villagers: ' + str(testfife.workers))
#        print('Location: ' + str(testfife.location))
#        print('\n\n')
#        testfife.write()
#        print('\n\nAttempting test read')
#        testfife.read()
#        print('\n\nSetting Ruler Name')
#        testfife.ruler = 'Lars'
#        testfife.read()
#        testfife.write()
#        testfife.read()



#        print("-------------------------------------------------------")
#        print("Avalible Commands: logout, stronghold")
#        command = input("Enter your command: ")
#
#        if command == "logout":
#            screen = "login"
#
#        if command == "attack":
#            screen = "attack"
#        
#        if command == "stronghold":
#            screen = "stronghold"
#
#        if command == "fifedom":
#            screen = "fifedom"



#----------------------------------------------------------------------------------
 

    if screen == "createDefaults":

        os.system("clear")
        print('Seeding the world with default Fifedoms')
            
        names = ['Razor Hills', 'Forest of Fado', 'Emerald Cove', 'Stormgrove', 'Aegirs Hall', 'Ashen Grove', 'Bellhollow']
        for x in names:
            currentFife = Fifedom()
            currentFife.name = x
            currentFife.defenders = random.randint(10, 50)
            currentFife.write()

        time.sleep(2)
        print('Seeding Complete')

        screen = input("Enter your command: ")
