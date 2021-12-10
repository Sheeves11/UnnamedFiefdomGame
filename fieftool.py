import os
import time
import random

'''
Welcome to the Unnamed Fiefdom Game!
This game was designed and written by
Mike Quain of the University of Arkansas
More info can be found at
github.com/Sheeves11/UnnamedFiefdomGame

fieftool.py is a tool for adding new fiefs to the game. Just enter the name of the fiefdom and hit enter. You're done!
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
-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=--=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-
                                             UNNAMED FIEFDOM GAME
-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=--=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-'''
    + textColor.WARNING + '\n                          Announcement: Season 1 will begin on December 20th, 2021!'
    + textColor.RESET)

#the fifedom class holds variables that define a player's stats
class Fifedom:
    name = 'Default Fiefdom'
    ruler = 'Unclaimed'
    home = False
    defenders = 100
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
        print('Welcome to the fief creation tool.')
        newFife = input('Enter the name of your new fief: ')
        currentFife = Fifedom()
        currentFife.name = newFife
        currentFife.defenders = random.randint(10, 100)
        currentFife.gold = random.randint(500, 3100)
        currentFife.write()
        print('Fief write complete.')
        throwAway = input('Press Enter to Continue')
        screen = 'login'
       
