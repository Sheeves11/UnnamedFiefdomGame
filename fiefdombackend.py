from globals import *

#Globals merged and moved to globals.py

#this is the backend to the Untitled Fiefdom Game. This is run alongside the user sessions.
#the purpose of the backend is to increment gold, worker, and soldier totals.

#the fiefdom class holds variables that define a player's stats


os.system('clear')

loop = True

currentFief = Fiefdom()

while (loop):
    
    print('\n\n\n--------------------------------------------------------')
    print('Incrementing totals')
    print('--------------------------------------------------------\n')

    #=====================
    #    Update Market
    #=====================
    serverMarket.ListGoods()
    serverMarket.DecrementMerchandiseShelfLife(3600)
    serverMarket.CheckRestock()
  
    for filename in os.listdir('fiefs'):
            with open(os.path.join('fiefs', filename), 'r') as f:
                
#                print('Incrementing Fiefdom Totals:\n')

                tempName = filename[:-4]
                tempName = Fiefdom()
                tempName.name = filename[:-4]
                tempName.defenderMod = '0'
                tempName.defenderMod = '0' 
                tempName.read()
                
                # print(" Incrementing " + str(tempName.name) + "'s Resources. Currently at: " + GetStationResources(tempName))
                #=====================
                # Increment Resources
                #=====================
                if tempName.ruler != 'Unclaimed':
                    # Increment Gold (only from outposts, and also this is temporary)
                    goldPerHour = tempName.GetSecondaryPer("farmland")
                    tempName.gold = int(tempName.gold) + int(goldPerHour)

                    # Increment Food:
                    foodPerHour = tempName.GetPrimaryPer("farmland") + tempName.GetPrimaryPer("fishery") + tempName.GetSecondaryPer("lumberMill")
                    tempName.food = int(tempName.food) + int(foodPerHour)
                    
                    # Increment Wood:
                    woodPerHour = tempName.GetPrimaryPer("lumberMill")
                    tempName.wood = int(tempName.wood) + int(woodPerHour)

                    # Increment Stone:
                    stonePerHour = tempName.GetPrimaryPer("mine")
                    tempName.stone = int(tempName.stone) + int(stonePerHour)

                    # Increment Ore:
                    orePerHour = tempName.GetSecondaryPer("mine")
                    tempName.ore = int(tempName.ore) + int(orePerHour)

                    # Increment Random:
                    Scavenge(tempName)  #This function grabs random resources based on the number of scavengers at this fief.

                productionCalc = 0
                maxProductionSoldiers = (int(tempName.defLevel) + 1) * int(MAX_PRODUCTION_SOLDIERS_CONSTANT) #Now scales by defense level
                if int(tempName.defenders) > int(maxProductionSoldiers):
                    productionCalc = ((GOLD_PER * int(tempName.goldMod)) + (int(maxProductionSoldiers) * int(tempName.goldMod)))

                else:
                    productionCalc = ((GOLD_PER * int(tempName.goldMod)) + (int(tempName.defenders) * int(tempName.goldMod)))
                
                if tempName.ruler != 'Unclaimed':
                    tempName.defenders = str(int(tempName.defenders) + (defendersPer * int(tempName.defenderMod)))
                    tempName.gold = str(int(tempName.gold) + int(productionCalc))
                    tempName.write()
                    # print(str('the fiefdom of ' + tempName.name + ' now has ' + str(tempName.defenders) + ' defenders.'))

                print(" Incremented " + str(tempName.name) + "'s Resources. Now at: " + GetStationResources(tempName))

    for filename in os.listdir('strongholds'):
            with open(os.path.join('strongholds', filename), 'r') as f:
                
#                print('Incrementing Player Stronghold Totals:\n')

                tempName = filename[:-4]
                tempName = Stronghold()
                tempName.name = filename[:-4]
                tempName.defenderMod = '0'
                tempName.defenderMod = '0' 
                tempName.read()
                
                productionCalc = 0
                maxProductionSoldiers = (int(tempName.goldMod) * 500)
                if int(tempName.defenders) > maxProductionSoldiers:
                    productionCalc = ((GOLD_PER * int(tempName.goldMod)) + (int(maxProductionSoldiers) * int(tempName.goldMod)))

                else:
                    productionCalc = ((GOLD_PER * int(tempName.goldMod)) + (int(tempName.defenders) * int(tempName.goldMod)))
                
                if tempName.ruler != 'Unclaimed':
                    tempName.defenders = str(int(tempName.defenders) + (defendersPer * int(tempName.defenderMod)))
                    tempName.gold = str(int(tempName.gold) + int(productionCalc))
                    tempName.write()
                    print('the stronghold of ' + str(tempName.name + ' currently has ' + str(tempName.defenders) + ' defenders.'))
    

    time.sleep(INTERVAL)
