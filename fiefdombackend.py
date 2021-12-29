import time
import os
import random
from classes import *

#global variables for quick game balance adjustments
goldPer = 100
defendersPer = 3
#interval in seconds
interval = 3600



#this is the backend to the Untitled Fiefdom Game. This is run alongside the user sessions.
#the purpose of the backend is to increment gold, worker, and soldier totals.

#the fiefdom class holds variables that define a player's stats


os.system('clear')

loop = True

currentFief = Fiefdom()

while (loop):
    
    print('\n\n\n--------------------------------------------------------')
    print('Incrementing soldier totals')
    print('--------------------------------------------------------\n')
  
    for filename in os.listdir('fiefs'):
            with open(os.path.join('fiefs', filename), 'r') as f:
                
                tempName = filename[:-4]
                tempName = Fiefdom()
                tempName.name = filename[:-4]
                tempName.defenderMod = '0'
                tempName.defenderMod = '0' 
                tempName.read()
                
                productionCalc = 0
                maxProductionSoldiers = (int(tempName.goldMod) * 500)
                if int(tempName.defenders) > maxProductionSoldiers:
                    productionCalc = ((goldPer * int(tempName.goldMod)) + (int(maxProductionSoldiers) * int(tempName.goldMod)))

                else:
                    productionCalc = ((goldPer * int(tempName.goldMod)) + (int(tempName.defenders) * int(tempName.goldMod)))
                
                
                print(str(tempName.name + ' currently has ' + str(tempName.defenders) + ' defenders.'))
                if tempName.ruler != 'Unclaimed':
                    tempName.defenders = str(int(tempName.defenders) + (defendersPer * int(tempName.defenderMod)))
                    tempName.gold = str(int(tempName.gold) + int(productionCalc))
                    tempName.write()
    
    

    time.sleep(interval)
