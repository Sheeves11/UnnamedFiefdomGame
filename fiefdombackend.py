import time
import os
import random

#global variables for quick game balance adjustments
goldPer = 100
defendersPer = 3
#interval in seconds
interval = 3600



#from fiefdomgame.py import Fifedom as Fiefdom

#this is the backend to the Untitled Fiefdom Game. This is run alongside the user sessions.
#the purpose of the backend is to increment gold, worker, and soldier totals.

#the fifedom class holds variables that define a player's stats

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
    goldMod = 0
    defenderMod = 0

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
                f.write(str(self.goldMod) + '\n')
                f.write(str(self.defenderMod) + '\n')
                f.write(str(self.farmType) + '\n')
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
                f.write(str(self.goldMod) + '\n')
                f.write(str(self.defenderMod) + '\n')
                f.write(str(self.farmType) + '\n')
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
                self.goldMod = f.readline().strip()
                self.defenderMod = f.readline().strip()
                self.farmType = f.readline().strip()
        except:
            self.write()
            print('file read fail, creating new fife file for current user')



os.system('clear')

loop = True

currentFife = Fifedom()

while (loop):
    
    print('\n\n\n--------------------------------------------------------')
    print('Incrementing soldier totals')
    print('--------------------------------------------------------\n')
  
    for filename in os.listdir('fifes'):
            with open(os.path.join('fifes', filename), 'r') as f:
                
                tempName = filename[:-4]
                tempName = Fifedom()
                tempName.name = filename[:-4]
                tempName.defenderMod = '0'
                tempName.defenderMod = '0' 
                tempName.read()
                
                productionCalc = 0
                maxProductionSoldiers = (int(tempName.goldMod) * 500)
                    if int(tempName.defenders) > maxProductionSoldiers:
                        productionCalc = ((goldOutput * int(tempName.goldMod)) + (int(maxProductionSoldiers) * int(tempName.goldMod)))

                    else: 
                        productionCalc = ((goldOutput * int(tempName.goldMod)) + (int(tempName.defenders) * int(tempName.goldMod)))
                
                
                print(str(tempName.name + ' currently has ' + str(tempName.defenders) + ' defenders.'))
                if tempName.ruler != 'Unclaimed':
                    tempName.defenders = str(int(tempName.defenders) + (defendersPer * int(tempName.defenderMod)))
                    tempName.gold = str(int(tempName.gold) + int(productionCalc))
                    tempName.write()
    
    

    time.sleep(interval)
