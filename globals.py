from os.path import exists
from classes import *
from worldmap import *
from passages import *
from art import *

#Most files should import this file.
#Doing so grants access to all the above imports as well.
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
UC_THIEF = 1000
UC_WARRIOR = 10    #Manage this for practical reasons
UC_FARMER = 500
UC_VENDOR = 1500
UC_FISHER = 500
UC_SCAVENGER = 1000
UC_LUMBERJACK = 500
UC_HUNTER = 1000
UC_MINER = 500
UC_PROSPECTOR = 1500

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

#========================================================================================================
#   printFiefArt
#   parameter: attackFief
#       Prints all the art for the passed fief. 
#========================================================================================================
def printFiefArt(attackFief):
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
#   parameters: userStronghold, unitType, unitBaseCost, unitCostModifier, unitCap, unitsOwned
#       Takes several parameters and rusn them through a default unit hiring interface.
#       With the addition of 8 new units, something like this was necessary to avoid redundant code.
#       Note: if any custom dialog needs to be added, just add checks for the unit type.
#========================================================================================================
def HireUnit(userStronghold, unitType, unitBaseCost, unitCostModifier, unitCap, unitsOwned):
    os.system("clear")
    header(userStronghold.name)
    spotsAvailable = unitCap - unitsOwned
    unitCost = unitBaseCost + int(unitBaseCost * unitCostModifier)
    print("    You currently have " + str(unitsOwned) + " " + unitType + " units hired.")
    time.sleep(0.5)
    if(spotsAvailable > 0 and unitType != "Warrior" and unitType != "Thief"):
        print("    You have room for " + str(spotsAvailable) + " more of these units.")
        time.sleep(0.5)
    else:
        print("    You don't have any more room for these units!")
        time.sleep(0.5)
        return
    print("     " + unitType + " units cost " + str(unitCost) + " gold each.")
    time.sleep(0.5)
    unitCount = input("    How many " + unitType + " units would you like to hire? : ")

    try:
        int(unitCount)
    except:
        unitCount = '0'

    if int(unitCount) == 0:
        print("    No changes were made!")

    elif int(unitCount) < 0:
        print("    You can't hire a negative number of " + unitType + " units!")

    elif (int(unitCount) * unitBaseCost) <=  int(userStronghold.gold):
        print("    Hiring " + str(unitCount) + unitType + " units...")
        #Increment the unit based on type:
        if unitType == "Warrior":
            userStronghold.defenders += unitCount
        elif unitType == "Thief":
            userStronghold.thieves += unitCount
        elif unitType == "Farmer":
            attackFief.op_farmlandPrimaryUnits += unitCount
        elif unitType == "Vendor":
            attackFief.op_farmlandSecondaryUnits += unitCount
        elif unitType == "Fisher":
            attackFief.op_fisheryPrimaryUnits += unitCount
        elif unitType == "Scavenger":
            attackFief.op_fisherySecondaryUnits += unitCount
        elif unitType == "Lumberjack":
            attackFief.op_lumberMillPrimaryUnits += unitCount
        elif unitType == "Hunter":
            attackFief.op_lumberMillSecondaryUnits += unitCount
        elif unitType == "Miner":
            attackFief.op_minePrimaryUnits += unitCount
        elif unitType == "Prospector":
            attackFief.op_mineSecondaryUnits += unitCount
        #Deduct gold
        userStronghold.gold = str(int(userStronghold.gold) - (unitCost * int(unitCount)))
        time.sleep(0.5)
        print("    Success! You now have " + str(unitsOwned) + " " + unitType + " units at this location!")
        userStronghold.write()
        userStronghold.read()

        attackFief.write()
        attackFief.read()
        time.sleep(0.5)
        nothing = input("    Press enter to continue ")

    else:
        print("    You need more gold first!")