from os.path import exists
from classes import *
from worldmap import *
from passages import *
from art import *
#from tempMethods import *

#Most files should import this file.
#Doing so grants access to all the above imports as well.

#This file also contains the following global functions:
#   FirstLaunch, PrintFiefArt, HireUnit, ConstructOutpost

#========================================================================================================
#========================================================================================================
#========================================================================================================
#                                               Globals
#========================================================================================================
#========================================================================================================
#========================================================================================================

#=====================
#     Main File
#=====================
STRONGHOLD = True           #Used to differentiate strongholds/fiefs
USER_STRONGHOLD = True      #Used to differentiate attack/user strongholds
currentUsername = 'default'
attackFief = Fiefdom()
serverMap = Map()
testMap = TestMap() #This is for users to have fun messing with the map generator
firstMapRead = True
newUserAccount = False

#=====================
#   Fiefdom Pages
#=====================
LINES_PER_PAGE = 15         #The number of fiefs/strongholds that appear in the list
currentPage = 1             #Used to keep track of the page the user should be on
userFiefCount = 0           #Used to keep track of how many fiefs the user controls.

#=====================
#  Backend Variables
#=====================
GOLD_PER = 100
INTERVAL = 3600
defendersPer = 3

#=====================
#     Unit Costs
#=====================
UCOST_THIEF = 1000
UCOST_WARRIOR = 10    #Manage this for practical reasons (warrior costs 10, farmer costs 500. wat.)
UCOST_FARMER = 500
UCOST_VENDOR = 1500
UCOST_FISHER = 500
UCOST_SCAVENGER = 1000
UCOST_LUMBERJACK = 500
UCOST_HUNTER = 1000
UCOST_MINER = 500
UCOST_PROSPECTOR = 1500

#=====================
#   Base Unit Caps
#=====================
UCAP_THIEF = 50
UCAP_WARRIOR = 3000
#These are base caps per outpost. So if you have 8 plains around you, you can have 80 farmers. 
UCAP_FARMER = 10    
UCAP_VENDOR = 5
UCAP_FISHER = 10
UCAP_SCAVENGER = 5
UCAP_LUMBERJACK = 10
UCAP_HUNTER = 5
UCAP_MINER = 10
UCAP_PROSPECTOR = 5

#=====================
#    Unit Colors
#=====================
COLOR_THIEF = MAGENTA
COLOR_WARRIOR = LIGHT_GRAY
COLOR_FARMER = WARNING
COLOR_VENDOR = DARK_YELLOW
COLOR_FISHER = CYAN
COLOR_SCAVENGER = TEAL
COLOR_LUMBERJACK = GREEN
COLOR_HUNTER = DARK_GREEN
COLOR_MINER = RED
COLOR_PROSPECTOR = DARK_RED

#=====================
#   Outpost Costs
#=====================
#TODO - The costs here will probably need to be modified!
#   Values here are multiplied in cost based on the number of like-outposts constructed.
#   When constructing new outposts, the cost is equal to the current tier your
#   other outposts of the same kind are at. 

#Resource layout: [gold, food, wood, stone, ore]
OP_COST_T1_FARMLAND = 1000
OP_COST_T2_FARMLAND = 3000
OP_COST_T3_FARMLAND = 6000
OP_COST_T1_FISHERY = 1000
OP_COST_T2_FISHERY = 3000
OP_COST_T3_FISHERY = 6000
OP_COST_T1_LUMBERMILL = 1000
OP_COST_T2_LUMBERMILL = 3000
OP_COST_T3_LUMBERMILL = 6000
OP_COST_T1_MINE = 1000
OP_COST_T2_MINE = 3000
OP_COST_T3_MINE = 6000


OP_RCOST_T1_FARMLAND = [1000, 0, 0, 0, 0]
OP_RCOST_T2_FARMLAND = [1500, 0, 10, 10, 0]
OP_RCOST_T3_FARMLAND = [3000, 0, 20, 20, 0]
OP_RCOST_T1_FISHERY = [1000, 0, 0, 0, 0]
OP_RCOST_T2_FISHERY = [1500, 0, 10, 10, 0]
OP_RCOST_T3_FISHERY = [3000, 0, 20, 20, 0]
OP_RCOST_T1_LUMBERMILL = [1000, 0, 0, 0, 0]
OP_RCOST_T2_LUMBERMILL = [1500, 0, 10, 10, 0]
OP_RCOST_T3_LUMBERMILL = [3000, 0, 20, 20, 0]
OP_RCOST_T1_MINE = [1000, 0, 0, 0, 0]
OP_RCOST_T2_MINE = [1500, 0, 10, 10, 0]
OP_RCOST_T3_MINE = [3000, 0, 20, 20, 0]

# OP_RCOST_CONSTRUCTION_FARMLAND = 1000
# OP_RCOST_CONSTRUCTION_FISHERY = 1000
# OP_RCOST_CONSTRUCTION_FOREST = 1000
# OP_RCOST_CONSTRUCTION_MINE = 1000


#=====================
#   Outpost Colors
#=====================
OP_COLOR_FARMLAND = DARK_YELLOW
OP_COLOR_FISHERY = BLUE
OP_COLOR_LUMBERMILL = DARK_GREEN
OP_COLOR_MINE = DARK_GRAY


#============
# TESTS
#============
RESOURCE_TEST_VALUES_1 = [10, 1, 2, 3, 4]
RESOURCE_TEST_VALUES_2 = [0, 1, 0, 1, 110]
RESOURCE_TEST_VALUES_3 = [10, 0, 0, 0, 0]
RESOURCE_TEST_VALUES_4 = [0, 0, 0, 0, 0]

#------------------------------------------------------------------------------
#   The following functions don't really have a proper home.
#------------------------------------------------------------------------------
def FirstLaunch():
    try:
        with open('settings.txt', 'r+') as settingsFile:
            # print('Opened settings.txt')
            line = settingsFile.readline().strip()
            if line.endswith('no'):
                # print('Settings.txt ends with no.')
                settingsFile.seek(0)
                # print('Attempting to write over line')
                settingsFile.write('Map Initialized: yes')
                # print('Wrote over the line!')
                settingsFile.close()
                return True
            else:
                # print('Settings did not end in no!')
                settingsFile.close()
                return False
    except:
        print('Error, something wrong with settings.txt!')
        return False

def CheckLegalUsername(username):
    illegalUserNames = ['', ' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
    if username.strip() == "":
        return False
    for i in range(len(illegalUserNames)):
        if username == illegalUserNames[i]:
            return False
    return True

def GrabGlobalColors():
    global COLOR_THIEF
    global COLOR_WARRIOR
    global COLOR_FARMER
    global COLOR_VENDOR
    global COLOR_FISHER
    global COLOR_SCAVENGER
    global COLOR_LUMBERJACK 
    global COLOR_HUNTER
    global COLOR_MINER
    global COLOR_PROSPECTOR
    global OP_COLOR_FARMLAND
    global OP_COLOR_FISHERY
    global OP_COLOR_LUMBERMILL
    global OP_COLOR_MINE


#========================================================================================================
#   PrintFiefArt
#   parameter: attackFief
#       Prints all the art for the passed fief. 
#========================================================================================================
def PrintFiefArt(attackFief):
    #Print Biome Banner:
    if attackFief.biome == str('^'):
            art_forest()
        
    elif attackFief.biome == str('M'):
        art_mountain()
    
    elif attackFief.biome == str('#'):
        art_plains()

    #Print Fief Graphic:
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

    #Print Farm Graphic
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

#========================================================================================================
#   HireUnit
#   parameters: userStronghold, unitType, unitBaseCost, unitCostModifier, unitCap, unitsOwned, color, 
#               flavorText
#       Takes several parameters and rusn them through a default unit hiring interface.
#       With the addition of 8 new units, something like this was necessary to avoid redundant code.
#       Note: if any custom dialog needs to be added, just add checks for the unit type.
#========================================================================================================
def HireUnit(userStronghold, unitType, unitBaseCost, unitCostModifier, unitCap, unitsOwned, color, flavorText):
    os.system("clear")
    header(userStronghold.name)
    if flavorText.strip() != "":
        print(flavorText)
    spotsAvailable = int(unitCap) - int(unitsOwned)
    unitCost = int(unitBaseCost) + int(float(unitBaseCost) * float(unitCostModifier))
    print("    You currently have " + textColor.WARNING + str(unitsOwned) + color + " " + unitType + textColor.RESET + " units hired.\n")
    time.sleep(0.5)
    if(spotsAvailable > 0):
        print("    You have room for " + textColor.WARNING + str(spotsAvailable) + textColor.RESET + " more of these units.\n")
        time.sleep(0.5)
    else:
        print("    You don't have any more room for these units!\n")
        time.sleep(0.5)
        return
    print("    " + color + unitType + textColor.RESET + " units cost " + textColor.WARNING + str(unitCost) + textColor.RESET + " gold each.\n")
    time.sleep(0.5)
    unitCount = input("    How many " + color + unitType + textColor.RESET + " units would you like to hire? : ")

    try:
        int(unitCount)
    except:
        unitCount = '0'

    if int(unitCount) == 0:
        print("    No changes were made!\n")

    elif int(unitCount) < 0:
        print("    You can't hire a negative number of " + color + unitType + textColor.RESET + " units!\n")

    elif int(unitCount) > int(spotsAvailable):
        print("    Can't hire " + textColor.WARNING + str(unitCount) + textColor.RESET + " units, only have room for " + textColor.WARNING + str(spotsAvailable) + textColor.RESET + " more!\n")
        time.sleep(1)
        return

    elif (int(unitCount) * unitBaseCost) <=  int(userStronghold.gold):
        print("\n    Hiring " + textColor.WARNING + str(unitCount) + color +  " " + unitType + textColor.RESET + " units...")
        #Increment the unit based on type:
        if unitType == "Warrior":
            userStronghold.defenders = int(userStronghold.defenders) + int(unitCount)
        elif unitType == "Thief":
            userStronghold.thieves = int(userStronghold.thieves) + int(unitCount)
        elif unitType == "Farmer":
            attackFief.op_farmlandPrimaryUnits = int(attackFief.op_farmlandPrimaryUnits) + int(unitCount)
        elif unitType == "Vendor":
            attackFief.op_farmlandSecondaryUnits = int(attackFief.op_farmlandSecondaryUnits) + int(unitCount)
        elif unitType == "Fisher":
            attackFief.op_fisheryPrimaryUnits = int(attackFief.op_fisheryPrimaryUnits) + int(unitCount)
        elif unitType == "Scavenger":
            attackFief.op_fisherySecondaryUnits = int(attackFief.op_fisherySecondaryUnits) + int(unitCount)
        elif unitType == "Lumberjack":
            attackFief.op_lumberMillPrimaryUnits = int(attackFief.op_lumberMillPrimaryUnits) + int(unitCount)
        elif unitType == "Hunter":
            attackFief.op_lumberMillSecondaryUnits = int(attackFief.op_lumberMillSecondaryUnits) + int(unitCount)
        elif unitType == "Miner":
            attackFief.op_minePrimaryUnits = int(attackFief.op_minePrimaryUnits) + int(unitCount)
        elif unitType == "Prospector":
            attackFief.op_mineSecondaryUnits = int(attackFief.op_mineSecondaryUnits) + int(unitCount)
        #Deduct gold
        userStronghold.gold = str(int(userStronghold.gold) - (unitCost * int(unitCount)))
        time.sleep(0.5)
        print("\n    Success! You now have " + textColor.WARNING + str(int(unitsOwned) + int(unitCount)) + color + " " + unitType + textColor.RESET + " units at this fief!\n")
        userStronghold.write()
        userStronghold.read()

        attackFief.write()
        attackFief.read()
        time.sleep(0.5)
        nothing = input("    Press enter to continue ")

    else:
        print("    You need more gold first!\n")

#========================================================================================================
#   ConstructOutpost
#   parameters: userStronghold, outpostType, tier, numberBuilt, spotsAvailable, cost, color, flavorText
#       Takes some parameters and walks user through a cookie-cutter outpost construction menu
#========================================================================================================
def ConstructOutpost(userStronghold, outpostType, tier, numberBuilt, spotsAvailable, cost, color, flavorText):
    os.system("clear")
    header(userStronghold.name)

    listening = True

    if flavorText.strip() != "":
        print(flavorText)

    if int(userStronghold.gold) < int(cost):
        print("    You don't have enough gold to build any " + color + str(outpostType) + textColor.RESET + " outposts!\n")
        time.sleep(1)
        return
    else:
        if int(numberBuilt) > 0:
            print("    You currently have " + textColor.WARNING + str(numberBuilt) + color + " " + str(outpostType) + textColor.RESET + " outposts constructed.\n")
            time.sleep(0.5)
            print("    Your " + color + str(outpostType) + textColor.RESET + " outposts are at rank " + textColor.MAGENTA + str(int(tier) + 1) + textColor.RESET + ".\n")
            time.sleep(0.5)
            if int(tier) > 0:
                print("    Note that outposts must be constructed at the same rank as other outposts of the same type.")
        else:
            print("    You don't have any " + color + str(outpostType) + textColor.RESET + " outposts built yet.\n")
            time.sleep(0.5)

        #If you have reached this point, there has to be at least 1 spot available to build this outpost.
        if spotsAvailable == 1:
            print("    You have one spot left for a " + color + str(outpostType) + textColor.RESET + " outpost.\n")
            time.sleep(0.5)
            if AnswerYes("    Would you like to construct a " + color + str(outpostType) + textColor.RESET + " outpost for " + textColor.WARNING + str(cost) + textColor.RESET + " gold?"):
                print("\n    Constructing a new " + color + str(outpostType) + textColor.RESET + "...")
                time.sleep(1)

                userStronghold.gold = int(userStronghold.gold) - int(cost)

                userStronghold.write()
                userStronghold.read()

                if outpostType == "Farmland":
                    attackFief.op_farmlandNumBuilt = str(int(attackFief.op_farmlandNumBuilt) + 1)
                elif outpostType == "Fishery":
                    attackFief.op_fisheryNumBuilt = str(int(attackFief.op_fisheryNumBuilt) + 1)
                elif outpostType == "Lumber Mill":
                    attackFief.op_lumberMillNumBuilt = str(int(attackFief.op_lumberMillNumBuilt) + 1)
                elif outpostType == "Mine":
                    attackFief.op_mineNumBuilt = str(int(attackFief.op_mineNumBuilt) + 1)

                attackFief.write()
                attackFief.read()

                print("\n    Success!")
                time.sleep(0.5)
                nothing = input("\n    Press enter to continue ")

                return

            else:
                print("\n    Cancelling request...\n")
                time.sleep(1)
                return
        else:
            print("    You have room for " + textColor.WARNING + str(spotsAvailable) + textColor.RESET + " more " + color + str(outpostType) + textColor.RESET + " outposts.\n")
            time.sleep(0.5)
            print("    At rank " + textColor.MAGENTA + str(int(tier) + 1) + textColor.RESET + ", constructing a new " + color + str(outpostType) + textColor.RESET + " outpost will cost " + textColor.WARNING + str(cost) + textColor.RESET + " gold per outpost.\n")
            time.sleep(0.5)

            while listening:
                buildNum = input("    How many " + color + str(outpostType) + textColor.RESET + " outposts would you like to build? : ")
                try:
                    int(buildNum)

                    if int(buildNum) < 0:
                        pass
                
                    elif int(buildNum) == 0:
                        print("    Cancelling request...\n")
                        time.sleep(1)
                        return
                    
                    elif int(buildNum) > int(spotsAvailable):
                        print("    You only have " + textColor.WARNING + str(spotsAvailable) + textColor.RESET + " spots remaining!\n")
                        time.sleep(0.5)

                    elif int(userStronghold.gold) < int(int(buildNum) * int(cost)):
                        print("    You don't have enough gold to build " + textColor.WARNING + str(buildNum) + color + " " + str(outpostType) + textColor.RESET + " outposts!\n")
                        time.sleep(0.5)
                    
                    else:
                        print("\n    Constructing " + textColor.WARNING + str(buildNum) + color + " " + str(outpostType) + textColor.RESET + " outposts...")
                        time.sleep(1)

                        userStronghold.gold = int(userStronghold.gold) - (int(cost) * int(buildNum))

                        userStronghold.write()
                        userStronghold.read()

                        if outpostType == "Farmland":
                            attackFief.op_farmlandNumBuilt = str(int(attackFief.op_farmlandNumBuilt) + int(buildNum))
                        elif outpostType == "Fishery":
                            attackFief.op_fisheryNumBuilt = str(int(attackFief.op_fisheryNumBuilt) + int(buildNum))
                        elif outpostType == "Lumber Mill":
                            attackFief.op_lumberMillNumBuilt = str(int(attackFief.op_lumberMillNumBuilt) + int(buildNum))
                        elif outpostType == "Mine":
                            attackFief.op_mineNumBuilt = str(int(attackFief.op_mineNumBuilt) + int(buildNum))

                        attackFief.write()
                        attackFief.read()

                        print("\n    Construction of " + textColor.WARNING + str(buildNum) + color + " " + str(outpostType) + textColor.RESET + " outposts was successful!\n")
                        time.sleep(0.5)
                        nothing = input("    Press enter to continue ")
                        return

                except:
                    print("    Error with input, please try again.\n")
                    time.sleep(0.5)

                
#========================================================================================================
#   UpgradeOutpost
#   parameters: userStronghold, outpostType, tier, numberBuilt, cost, flavorText
#       Takes some parameters and walks user through a cookie-cutter outpost construction menu
#========================================================================================================
def UpgradeOutpost(userStronghold, outpostType, tier, numberBuilt, cost, color, flavorText):
    os.system("clear")
    header(userStronghold.name)

    if flavorText.strip() != "":
        print(flavorText)

    if tier >= 2:
        print("    Your outposts are at the max rank!\n")
        time.sleep(1)
        return
    elif int(userStronghold.gold) < int(cost):
        print("    You don't have enough gold to upgrade your " + color + str(outpostType) + textColor.RESET + " outposts!\n")
        time.sleep(1)
        return
    else:
        print("    You currently have " + textColor.WARNING + str(numberBuilt) + color + " " + str(outpostType) + textColor.RESET + " outposts constructed.\n")
        time.sleep(0.5)
        print("    Your " + color + str(outpostType) + textColor.RESET + " outposts are at rank " + textColor.MAGENTA + str(int(tier) + 1) + textColor.RESET + ".\n")
        time.sleep(0.5)
        print("    Note that you must upgrade all constructed outposts of the same type at the same time!\n")
        time.sleep(0.5)

        if AnswerYes("    Would you like to upgrade all of your " + color + str(outpostType) + textColor.RESET + " outposts for " + textColor.WARNING + str(cost) + textColor.RESET + " gold?"):
            print("\n    Upgrading " + color + str(outpostType)  + textColor.RESET + " outposts...\n")
            time.sleep(1)

            userStronghold.gold = int(userStronghold.gold) - int(cost)

            userStronghold.write()
            userStronghold.read()

            if outpostType == "Farmland":
                attackFief.op_farmlandTier = str(int(attackFief.op_farmlandTier) + 1)
            elif outpostType == "Fishery":
                attackFief.op_fisheryTier = str(int(attackFief.op_fisheryTier) + 1)
            elif outpostType == "Lumber Mill":
                attackFief.op_lumberMillTier = str(int(attackFief.op_lumberMillTier) + 1)
            elif outpostType == "Mine":
                attackFief.op_mineTier = str(int(attackFief.op_mineTier) + 1)

            attackFief.write()
            attackFief.read()

            print("\n    Success!")
            time.sleep(0.5)
            nothing = input("\n    Press enter to continue ")

            return

        else:
            print("\n    Cancelling request...")
            time.sleep(1)
            return
        
#========================================================================================================
#   PrintResourceCost
#   parameters: leadStatement, cost, endStatement
#       Takes a few parameters and organizes them into a print statement. 
#========================================================================================================
def PrintResourceCost(leadStatement, cost, endStatement):
    #cost = [gold, food, wood, stone, ore]
    sentence = []
    sentence.append(str(leadStatement))
    sentence.append(WARNING + " [" + RESET)
    if int(cost[0]) != 0:
        sentence.append(str(" " + DARK_YELLOW + str(cost[0]) + " gold " + RESET))
    if int(cost[1]) != 0:
        sentence.append(str(" " + DARK_RED + str(cost[1]) + " food " + RESET))
    if int(cost[2]) != 0:
        sentence.append(str(" " + DARK_GREEN + str(cost[2]) + " wood " + RESET))
    if int(cost[3]) != 0:
        sentence.append(str(" " + DARK_GRAY + str(cost[3]) + " stone " + RESET))
    if int(cost[4]) != 0:
        sentence.append(str(" " + DARK_MAGENTA + str(cost[4]) + " ore " + RESET))
    sentence.append(WARNING + "] " + RESET)
    sentence.append(str(endStatement))
    print(*sentence, sep="")

#========================================================================================================
#   HaveEnoughResources
#   parameters: station, cost
#   returns: True if you have enough resources at the passed station.
#========================================================================================================
def HaveEnoughResources(station, cost):
    #cost = [gold, food, wood, stone, ore]
    if int(station.gold) >= cost[0]:
        pass
    else:
        return False
    if int(station.food) >= int(cost[1]):
        pass
    else:
        return False
    if int(station.wood) >= int(cost[2]):
        pass
    else:
        return False
    if int(station.stone) >= int(cost[3]):
        pass
    else:
        return False
    if int(station.ore) >= int(cost[4]):
        pass
    else:
        return False

    return True


