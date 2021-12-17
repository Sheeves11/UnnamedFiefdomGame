import os
import time
import random
import classes

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
       
