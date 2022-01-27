from curses import COLOR_GREEN
from os.path import exists
from colors import *
from classes import *
from worldmap import *
from market import *
from passages import *
from art import *
from armies import *

#from tempMethods import *

#Most files should import this file.
#Doing so grants access to all the above imports as well.


#This file also contains the following global functions:
#   FirstLaunch, PrintFiefArt, HireUnit, ConstructOutpost, CreateFief, Log
#   And many others... maybe update this sometime.


#========================================================================================================
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#========================================================================================================
#                                          Global Variables
#========================================================================================================
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#========================================================================================================

#=====================
#     Main File
#=====================
STRONGHOLD = True           #Used to differentiate strongholds/fiefs
USER_STRONGHOLD = True      #Used to differentiate attack/user strongholds
currentUsername = 'default'
attackFief = Fiefdom()
serverMap = Map()
serverMarket = Market()
serverArmies = Armies()
testMap = TestMap() #This is for users to have fun messing with the map generator
firstMapRead = True
newUserAccount = False
DEFAULT_FIEFDOM_NUMBER = 8    #This is the number of fiefdoms to create when starting a new server

#=========================
#   System Announcement
#=========================
#I had to throw this one in the art file do to import issues
#ANNOUNCEMENT = "This is a test build"

#=====================
#   Fiefdom Pages
#=====================
LINES_PER_PAGE = 25         #The number of fiefs/strongholds that appear in the list
currentPage = 1             #Used to keep track of the page the user should be on
userFiefCount = 0           #Used to keep track of how many fiefs the user controls.
RESOURCE_SPACING = 90
FILL_SYMBOL = "-"

#=====================
#  Backend Variables
#=====================
# maxProductionSoldiers now scales by defenseLevel. 300/600/900/1200/1500/1800 (see constant)
GOLD_PER = 200
INTERVAL = 3600
# INTERVAL = 60
MAX_PRODUCTION_SOLDIERS_CONSTANT = 3000  #Nerfed to 300 down from 500. May not be necessary. // I'm raising this quite high after the removal of production upgrades -Sheeves
defendersPer = 5
MARKET_ITEM_THRESHOLD = 5
MAX_LISTING_AMOUNT = 10

#=====================
#      Others
#=====================
ILLEGAL_CHARACTERS = ["\\", "//", "`", "{", "}", "(", ")", "[", "]", "_", "*", "$", "#", "<", ">", "'"]
ILLEGAL_USERNAMES = ['', ' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', 'The Wandering Merchant']
BATTALION_NAME_CAP = 25

#=====================
#      Resources
#=====================
BIOME_RESOURCE_MIN = 5
BIOME_RESOURCE_MAX = 15
ADJACENT_RESOURCE_MIN = 2
ADJACENT_RESOURCE_MAX = 5
SCAV_RESOURCE_MAX = 3
STR_GOLD = str(C_GOLD + " Gold " + RESET)
STR_FOOD = str(C_FOOD + " Food " + RESET)
STR_WOOD = str(C_WOOD + " Wood " + RESET)
STR_STONE = str(C_STONE + " Stone " + RESET)
STR_ORE = str(C_ORE + " Ore " + RESET)

#=============================================
#      Starting Fiefdom Gold and Warriors
#=============================================
FIEFDOM_GOLD_MIN = 1266
FIEFDOM_GOLD_MAX = 3877
FIEFDOM_WARRIOR_MIN = 5
FIEFDOM_WARRIOR_MAX = 100

#=====================
#      Weather
#=====================
WEATHER_SYSTEM_MOD = 0         #think of this as a seasonal modifier for temperature
BASELINE_TEMP = 72              #this is the baseline for global temp calculations

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



#=================================================
#=================================================
#                Resource Costs
#=================================================
#=================================================

#=====================
#     Unit Costs
#=====================
UCOST_THIEF = [500, 0, 0, 0, 0]
UCOST_WARRIOR = [50, 0, 0, 0, 0]    #Manage this for practical reasons (warrior costs 10, farmer costs 500. wat.)
UCOST_FARMER = [125, 0, 0, 0, 0]
UCOST_VENDOR = [750, 0, 0, 0, 0]
UCOST_FISHER = [125, 0, 0, 0, 0]
UCOST_SCAVENGER = [250, 0, 0, 0, 0]
UCOST_LUMBERJACK = [125, 0, 0, 0, 0]
UCOST_HUNTER = [250, 0, 0, 0, 0]
UCOST_MINER = [125, 0, 0, 0, 0]
UCOST_PROSPECTOR = [375, 0, 0, 0, 0]

#=====================
#   Outpost Costs
#=====================
#   Resource layout: [gold, food, wood, stone, ore]
#   Values here are multiplied in cost based on the number of like-outposts constructed.
#   When constructing new outposts, the cost is equal to the current tier your
#   other outposts of the same kind are at. 
OP_RCOST_T1_FARMLAND = [500, 0, 0, 0, 0]
OP_RCOST_T2_FARMLAND = [750, 0, 10, 10, 0]
OP_RCOST_T3_FARMLAND = [1500, 0, 20, 20, 0]
OP_RCOST_T1_FISHERY = [500, 0, 0, 0, 0]
OP_RCOST_T2_FISHERY = [750, 0, 10, 10, 0]
OP_RCOST_T3_FISHERY = [1500, 0, 20, 20, 0]
OP_RCOST_T1_LUMBERMILL = [500, 0, 0, 0, 0]
OP_RCOST_T2_LUMBERMILL = [750, 0, 10, 10, 0]
OP_RCOST_T3_LUMBERMILL = [1500, 0, 20, 20, 0]
OP_RCOST_T1_MINE = [500, 0, 0, 0, 0]
OP_RCOST_T2_MINE = [750, 0, 10, 10, 0]
OP_RCOST_T3_MINE = [1500, 0, 20, 20, 0]

#===========================
#   Attack Upgrade Costs
#===========================
#   Resource layout: [gold, food, wood, stone, ore]
UPGRADE_ATTACK_T1 = [500, 0, 0, 0, 0]
UPGRADE_ATTACK_T2 = [3500, 0, 0, 0, 0]
UPGRADE_ATTACK_T3 = [5000, 0, 0, 0, 0]
UPGRADE_ATTACK_T4 = [10000, 0, 0, 0, 0]
UPGRADE_ATTACK_T5 = [20000, 0, 0, 0, 0]
UPGRADE_ATTACK_T6 = [40000, 0, 0, 0, 0]
UPGRADE_ATTACK_T7 = [80000, 0, 0, 0, 0]

#===========================
#   Defense Upgrade Costs
#===========================
#   Resource layout: [gold, food, wood, stone, ore]
UPGRADE_DEFENSE_T1 = [500, 0, 20, 0, 0]
UPGRADE_DEFENSE_T2 = [1000, 0, 20, 20, 0]
UPGRADE_DEFENSE_T3 = [3000, 0, 30, 30, 0]
UPGRADE_DEFENSE_T4 = [5000, 0, 30, 30, 0]
UPGRADE_DEFENSE_T5 = [8000, 0, 40, 40, 10]
UPGRADE_DEFENSE_T6 = [13000, 0, 50, 50, 20]


#=================================================
#=================================================
#                    Names
#=================================================
#=================================================

#===========================
#   Attack Upgrade Names
#===========================
NAME_ATTACK_T1 = str(WARNING + "Angry Villagers with Sharpened Pitchforks" + RESET)
NAME_ATTACK_T2 = str(WARNING + "Semi-trained Longbow Archers" + RESET)
NAME_ATTACK_T3 = str(WARNING + "Military Recruits" + RESET)
NAME_ATTACK_T4 = str(WARNING + "Fairly Well-trained Archers with Flaming Arrows" + RESET)
NAME_ATTACK_T5 = str(WARNING + "Drunks with Trebuchets") + RESET
NAME_ATTACK_T6 = str(WARNING + "Scientists who are Experiementing with Biological Warfare" + RESET)
NAME_ATTACK_T7 = str(WARNING + "Peasents with Guns" + RESET)

#===========================
#   Defense Upgrade Names
#===========================
NAME_DEFENSE_T1 = 'Wooden Fences'
NAME_DEFENSE_T2 = 'Deep Trenches'       #Was "Really Deep Ditches". Changed to keep consistency with others and trenches sounds cooler than ditches
NAME_DEFENSE_T3 = 'Tall Towers'
NAME_DEFENSE_T4 = 'Encompassing Canals' #Was "In a Lake. Changed becuase they're not actually in a lake biome.
NAME_DEFENSE_T5 = 'Stalwart Ramparts'   #Was "On a Mountain". Changed because they aren't required to be on a mountain.
NAME_DEFENSE_T6 = 'Unwavering Bastion'  #Was "Boiling Oil". Changed because boiling oil doesn't sound like a "final" defensive upgrade.


#========================================================================================================
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#========================================================================================================
#                                          Global Functions
#========================================================================================================
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#========================================================================================================

#========================================================================================================
#   Wait
#   parameter: username
#   returns: True/False
#       Prevents the use of certain usernames that may interfere with menu operations.
#========================================================================================================
def Wait():
    wait = input("\n    Press Enter to continue : ")

#========================================================================================================
#   FirstLaunch
#       Saves info in settings.txt so the game knows if the map has been initialized or not. 
#       Room to expand or add stuff here as needed.
#========================================================================================================
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

#========================================================================================================
#   CheckLegalUsername
#   parameter: username
#   returns: True/False
#       Prevents the use of certain usernames that may interfere with menu operations.
#========================================================================================================
def CheckLegalUsername(username):
    if len(username) < 18:
        if username.strip() == "":
            return False
        for i in range(len(ILLEGAL_USERNAMES)):
            if username == ILLEGAL_USERNAMES[i]:
                return False
        return True
    os.system('clear')
    return False


#========================================================================================================
#   AddRandomFief
#   parameter: newFief
#       Adds a random fief and initializes its resources
#========================================================================================================
def AddRandomFief(newFief):
    filenameTemp = newFief.name + '.txt'
    with open(os.path.join('fiefs', filenameTemp), 'r') as f:
        tempName = filenameTemp[:-4]
        tempName = Fiefdom()
        tempName.name = filenameTemp[:-4]
        tempName.read()
        SilentlyPlaceFiefInWorldMap(tempName, serverMap)

        tempName.gold = random.randint(FIEFDOM_GOLD_MIN, FIEFDOM_GOLD_MAX)
        tempName.defenders= random.randint(FIEFDOM_WARRIOR_MIN, FIEFDOM_WARRIOR_MAX)
        tempName.write()

        AddFiefStartingResources(tempName)


#========================================================================================================
#   [InitializeStartingFiefs]
#   Parameters: none
#       Initializes all the fiefs that should be there at the beginning of the game. 
#========================================================================================================
def InitializeStartingFiefs(firstLaunchFief):
    for i in range(DEFAULT_FIEFDOM_NUMBER):
        #Create Default Fiefs
        firstLaunchFief.name = str(CreateFief())
        
        serverMap.read()

        #Setting starting resources for this new random fiefdom
        AddRandomFief(firstLaunchFief)
        serverMap.read()

    #Set the fiefs starting resources
    InitializeAllStartingFiefResources()

#========================================================================================================
#   [InitializeAllStartingFiefResources]
#   Parameters: none
#   Initializes fiefs with starting resources based on their surroundings and the biome they're on
#========================================================================================================
def InitializeAllStartingFiefResources():
    for filename in os.listdir('fiefs'):
            with open(os.path.join('fiefs', filename), 'r') as f:
                tempName = filename[:-4]
                tempName = Fiefdom()
                tempName.name = filename[:-4]
                AddFiefStartingResources(tempName)

#========================================================================================================
#   [AddFiefStartingResources]
#   Parameters: fief
#       Sets the starting resources of a new fief based on surroundings
#========================================================================================================
def AddFiefStartingResources(fief):
    fief.read()
    if fief.biome == MOUNTAIN:
        fief.stone = int(fief.stone) + random.randint(BIOME_RESOURCE_MIN, BIOME_RESOURCE_MAX)
    elif fief.biome == FOREST:
        fief.wood = int(fief.wood) + random.randint(BIOME_RESOURCE_MIN, BIOME_RESOURCE_MAX)
    elif fief.biome == PLAINS:
        fief.food = int(fief.food) + random.randint(BIOME_RESOURCE_MIN, BIOME_RESOURCE_MAX)

    for i in range(int(fief.adjacentForests)):
        fief.wood = int(fief.wood) + random.randint(ADJACENT_RESOURCE_MIN, ADJACENT_RESOURCE_MAX)
    for i in range(int(fief.adjacentRivers)):
        fief.food = int(fief.food) + random.randint(ADJACENT_RESOURCE_MIN, ADJACENT_RESOURCE_MAX)
    for i in range(int(fief.adjacentWater)):
        fief.food = int(fief.food) + random.randint(ADJACENT_RESOURCE_MIN, ADJACENT_RESOURCE_MAX)
    for i in range(int(fief.adjacentPlains)):
        fief.food = int(fief.food) + random.randint(ADJACENT_RESOURCE_MIN, ADJACENT_RESOURCE_MAX)
    for i in range(int(fief.adjacentMountains)):
        fief.stone = int(fief.stone) + random.randint(ADJACENT_RESOURCE_MIN, ADJACENT_RESOURCE_MAX)
    fief.write()

#========================================================================================================
#   [GetFiefByName]
#   Parameters: name
#       Returns a fief class with the passed name
#========================================================================================================
def GetFiefByName(name):
    for filename in os.listdir('fiefs'):
            with open(os.path.join('fiefs', filename), 'r') as f:
                tempName = filename[:-4]
                tempName = Fiefdom()
                tempName.name = filename[:-4]
                tempName.read()
                if tempName.name == name:
                    return tempName

#========================================================================================================
#   [GetOwnedFiefList]
#   Parameters: username
#       Returns a list of fief classes owned by the passed username
#========================================================================================================
def GetOwnedFiefList(username):
    fiefList = []
    for filename in os.listdir('fiefs'):
            with open(os.path.join('fiefs', filename), 'r') as f:
                tempName = filename[:-4]
                tempName = Fiefdom()
                tempName.name = filename[:-4]
                tempName.read()
                if tempName.ruler == username:
                    fiefList.append(tempName)
    return fiefList


#========================================================================================================
#   [IsPositiveInteger]
#   parameters: integer
#   returns: True/False
#       Checks if passed integer is both positive and an integer.
#========================================================================================================
def IsPositiveInteger(integer):
    try:
        int(integer)
    except:
        return False
    if int(integer) <= 0:
        return False
    return True

#========================================================================================================
#   [IsPositiveIntEqualOrLessThan]
#   parameters: integer, amount
#   returns: True/False
#       Checks if passed integer is both positive and an integer and then if it is less than "amount"
#========================================================================================================
def IsPositiveIntEqualOrLessThan(integer, amount):
    if IsPositiveInteger(integer) == False:
        return False
    elif int(integer) > int(amount):
        return False
    else:
        return True

#========================================================================================================
#   GrabGlobalColors
#       This is a quick way to call all these globals into a function so they are properly linked.
#       Room to expand this function.
#========================================================================================================
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
    global C_GOLD
    global C_FOOD
    global C_WOOD
    global C_STONE
    global C_ORE


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

#========================================================================================================
#   PrintFiefInformation
#   parameter: userStronghold, fief
#       Prints all the details about a fief
#========================================================================================================
def PrintFiefInformation(userStronghold, fief):
    enemyFiefdomInfo = str('    ' + textColor.WARNING + fief.name + ' || Ruled by: ' + fief.ruler + ' || Defenders: ' + fief.defenders + textColor.RESET)
    ownedFiefdomInfo = str('    ' + textColor.CYAN + fief.name + ' || Ruled by: ' + fief.ruler + ' || Defenders: ' + fief.defenders + textColor.RESET)
    fiefdomResources = str(' | ' + textColor.YELLOW + fief.gold + textColor.RESET + ' ' + textColor.DARK_RED + fief.food + textColor.RESET + ' ' + textColor.DARK_GREEN + fief.wood + textColor.RESET + ' ' + textColor.DARK_GRAY + fief.stone + textColor.RESET + ' ' + textColor.DARK_MAGENTA + fief.ore + textColor.RESET + '')

    if fief.home != 'True' and fief.ruler != userStronghold.name:
        print(enemyFiefdomInfo.ljust(RESOURCE_SPACING, FILL_SYMBOL) + fiefdomResources)
    if fief.home != "True" and fief.ruler == userStronghold.name:
        print(ownedFiefdomInfo.ljust(RESOURCE_SPACING, FILL_SYMBOL) + fiefdomResources)

#========================================================================================================
#   PrintOwnedFiefInformation
#   parameter: fief
#       Prints all the details about a fief
#========================================================================================================
def PrintOwnedFiefInformation(fief):
    ownedFiefdomInfo = str('    ' + textColor.CYAN + fief.name + ' || Defenders: ' + fief.defenders + textColor.RESET)
    fiefdomResources = str(' | ' + textColor.YELLOW + fief.gold + textColor.RESET + ' ' + textColor.DARK_RED + fief.food + textColor.RESET + ' ' + textColor.DARK_GREEN + fief.wood + textColor.RESET + ' ' + textColor.DARK_GRAY + fief.stone + textColor.RESET + ' ' + textColor.DARK_MAGENTA + fief.ore + textColor.RESET + '')
    
    print(ownedFiefdomInfo.ljust(RESOURCE_SPACING, FILL_SYMBOL) + fiefdomResources)


#========================================================================================================
#   Scavenge
#   parameter: fief
#       Triggers each hour, gathering a random resource based on the number of scavengers at a fief.
#========================================================================================================
def Scavenge(fief):
    if int(fief.op_fisheryTier) == 0:
        pass
    else:
        if int(fief.op_fisheryTier) == 1:
            loot = [("gold", 3), ("food", 5), ("wood", 15), ("stone", 15), ("ore", 1)]
        elif int(fief.op_fisheryTier) == 2:
            loot = [("gold", 5), ("food", 5), ("wood", 10), ("stone", 10), ("ore", 5)]
        
        #Expand list to a loot table:
        lootTable = []
        for item, weight in loot:
            lootTable.extend([item]*weight)

        for i in range(int(fief.op_fisherySecondaryUnits)):
            #Choose a random item in the list:
            pickedLoot = random.choice(lootTable)

            if pickedLoot == "gold":
                fief.gold = int(fief.gold) + 100
            elif pickedLoot == "food":
                fief.food = int(fief.food) + random.randint(1, SCAV_RESOURCE_MAX)
            elif pickedLoot == "wood":
                fief.wood = int(fief.wood) + random.randint(1, SCAV_RESOURCE_MAX)
            elif pickedLoot == "stone":
                fief.stone = int(fief.stone) + random.randint(1, SCAV_RESOURCE_MAX)
            elif pickedLoot == "ore":
                fief.ore = int(fief.ore) + 1

        fief.write()
        fief.read()



#========================================================================================================
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#========================================================================================================
#                                    Resource Management Functions
#========================================================================================================
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#========================================================================================================

#========================================================================================================
#   VerifyResourceValuesAsInts
#   parameters: cost
#       Runs a resource cost through a series of tests to make sure there aren't any "" variables
#========================================================================================================
def VerifyResourceValuesAsInts(cost):
    try:
        int(cost[0])
    except:
        cost[0] = '0'
    try:
        int(cost[1])
    except:
        cost[1] = '0'
    try:
        int(cost[2])
    except:
        cost[2] = '0'
    try:
        int(cost[3])
    except:
        cost[3] = '0'
    try:
        int(cost[4])
    except:
        cost[4] = '0'

    return cost

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
#   GetResourceCost
#   parameters: cost, quantity
#       Takes a few parameters and organizes them into a print statement. 
#========================================================================================================
def GetResourceCost(cost, quantity):
    #cost = [gold, food, wood, stone, ore]
    cost = VerifyResourceValuesAsInts(cost)
    sentence = ""
    sentence += WARNING + " [" + RESET
    if int(cost[0]) != 0:
        sentence += str(" " + DARK_YELLOW + str(int(cost[0]) * quantity) + " gold " + RESET)
    if int(cost[1]) != 0:
        sentence += str(" " + DARK_RED + str(int(cost[1]) * quantity) + " food " + RESET)
    if int(cost[2]) != 0:
        sentence += str(" " + DARK_GREEN + str(int(cost[2]) * quantity) + " wood " + RESET)
    if int(cost[3]) != 0:
        sentence += str(" " + DARK_GRAY + str(int(cost[3]) * quantity) + " stone " + RESET)
    if int(cost[4]) != 0:
        sentence += str(" " + DARK_MAGENTA + str(int(cost[4]) * quantity) + " ore " + RESET)
    sentence += WARNING + "] " + RESET
    
    return sentence

#========================================================================================================
#   HaveEnoughResources
#   parameters: station, cost, quantity
#   returns: True if you have enough resources at the passed station.
#========================================================================================================
def HaveEnoughResources(station, cost, quantity):
    #cost = [gold, food, wood, stone, ore]
    cost = VerifyResourceValuesAsInts(cost)
    if int(station.gold) >= int(cost[0]) * int(quantity):
        pass
    else:
        return False
    if int(station.food) >= int(cost[1]) * int(quantity):
        pass
    else:
        return False
    if int(station.wood) >= int(cost[2]) * int(quantity):
        pass
    else:
        return False
    if int(station.stone) >= int(cost[3]) * int(quantity):
        pass
    else:
        return False
    if int(station.ore) >= int(cost[4]) * int(quantity):
        pass
    else:
        return False

    return True


#========================================================================================================
#   CheckResourceByType
#   parameters: station, type, quantity
#   returns: True if you have enough resources at the passed station.
#========================================================================================================
def CheckResourceByType(station, type, quantity):
    if type == "Gold":
        if int(station.gold) >= int(quantity):
            pass
        else:
            return False
    if type == "Food":
        if int(station.food) >= int(quantity):
            pass
        else:
            return False
    if type == "Wood":
        if int(station.wood) >= int(quantity):
            pass
        else:
            return False
    if type == "Stone":
        if int(station.stone) >= int(quantity):
            pass
        else:
            return False
    if type == "Ore":
        if int(station.ore) >= int(quantity):
            pass
        else:
            return False

    return True

#========================================================================================================
#   GetStationResources
#   parameters: station
#       Takes a station and prints its current resources
#========================================================================================================
def GetStationResources(station):
    #cost = [gold, food, wood, stone, ore]
    sentence = []
    sentence.append(WARNING + " [" + RESET)
    sentence.append(str(" " + DARK_YELLOW + str(station.gold) + " gold " + RESET))
    sentence.append(str(" " + DARK_RED + str(station.food) + " food " + RESET))
    sentence.append(str(" " + DARK_GREEN + str(station.wood) + " wood " + RESET))
    sentence.append(str(" " + DARK_GRAY + str(station.stone) + " stone " + RESET))
    sentence.append(str(" " + DARK_MAGENTA + str(station.ore) + " ore " + RESET))
    sentence.append(WARNING + "] " + RESET)
    return sentence[0] + sentence[1] + sentence[2] + sentence[3] + sentence[4] + sentence[5] + sentence[6]

#========================================================================================================
#   DeductResources
#   parameters: station, cost, quantity
#       Removes resources from station based on cost.
#       This should be checked with a HaveEnoughResources function before being called!
#       Just in case though, it will print a message if there aren't enough resources to be removed.
#========================================================================================================
def DeductResources(station, cost, quantity):
    #cost = [gold, food, wood, stone, ore]
    cost = VerifyResourceValuesAsInts(cost)
    if int(station.gold) >= int(cost[0]) * int(quantity):
        station.gold = str(int(station.gold) - int(cost[0]) * int(quantity))
    else:
        print(RED + "\nError, not enough gold!\n")
    if int(station.food) >= int(cost[1]) * int(quantity):
        station.food = str(int(station.food) - int(cost[1]) * int(quantity))
    else:
        print(RED + "\nError, not enough food!\n")
    if int(station.wood) >= int(cost[2]) * int(quantity):
        station.wood = str(int(station.wood) - int(cost[2]) * int(quantity))
    else:
        print(RED + "\nError, not enough wood!\n")
    if int(station.stone) >= int(cost[3]) * int(quantity):
        station.stone = str(int(station.stone) - int(cost[3]) * int(quantity))
    else:
        print(RED + "\nError, not enough stone!\n")
    if int(station.ore) >= int(cost[4]) * int(quantity):
        station.ore = str(int(station.ore) - int(cost[4]) * int(quantity))
    else:
        print(RED + "\nError, not enough ore!\n")


#========================================================================================================
#   StationHasSomeResources
#   parameters: station
#       Returns true if station has any resources (besides gold) at all. Returns false otherwise.
#========================================================================================================
def StationHasSomeResources(station):
    if int(station.food) > 0:
        return True
    if int(station.wood) > 0:
        return True
    if int(station.stone) > 0:
        return True
    if int(station.ore) > 0:
        return True
    
    return False



#========================================================================================================
#   DeductResourceByType
#   parameters: station, resource, quantity
#       Removes resources from station based on type.
#       This should be checked with a HaveEnoughResources function before being called!
#========================================================================================================
def DeductResourceByType(station, resource, quantity):
    if resource == "Gold":
        station.gold = str(int(station.gold) - int(quantity))
    if resource == "Food":
        station.food = str(int(station.food) - int(quantity))
    if resource == "Wood":
        station.wood = str(int(station.wood) - int(quantity))
    if resource == "Stone":
        station.stone = str(int(station.stone) - int(quantity))
    if resource == "Ore":
        station.ore = str(int(station.ore) - int(quantity))
    station.write()
    station.read()

#========================================================================================================
#   AddResourceByType
#   parameters: station, resource, quantity
#       Adds resources from station based on type.
#       This should be checked with a HaveEnoughResources function before being called!
#========================================================================================================
def AddResourceByType(station, resource, quantity):
    if resource == "Gold":
        station.gold = str(int(station.gold) + int(quantity))
    if resource == "Food":
        station.food = str(int(station.food) + int(quantity))
    if resource == "Wood":
        station.wood = str(int(station.wood) + int(quantity))
    if resource == "Stone":
        station.stone = str(int(station.stone) + int(quantity))
    if resource == "Ore":
        station.ore = str(int(station.ore) + int(quantity))
    

#========================================================================================================
#   TransferResource
#   parameters: fromStation, toStation, resource, quantity
#       Takes a specific resource, deducts it from the fromStation, and adds it to the toStation.
#========================================================================================================
def TransferResource(fromStation, toStation, resource, quantity):
    if resource == "gold":
        fromStation.gold = str(int(fromStation.gold) - int(quantity))
        toStation.gold = str(int(toStation.gold) + int(quantity))
    if resource == "food":
        fromStation.food = str(int(fromStation.food) - int(quantity))
        toStation.food = str(int(toStation.food) + int(quantity))
    if resource == "wood":
        fromStation.wood = str(int(fromStation.wood) - int(quantity))
        toStation.wood = str(int(toStation.wood) + int(quantity))
    if resource == "stone":
        fromStation.stone = str(int(fromStation.stone) - int(quantity))
        toStation.stone = str(int(toStation.stone) + int(quantity))
    if resource == "ore":
        fromStation.ore = str(int(fromStation.ore) - int(quantity))
        toStation.ore = str(int(toStation.ore) + int(quantity))
    fromStation.write()
    fromStation.read()
    toStation.write()
    toStation.read()

#========================================================================================================
#   SendResources
#   parameters: station
#========================================================================================================
def SendResources(station, userStronghold):
    if isinstance(station, Stronghold):
        ownedFiefs = GetOwnedFiefList(station.name)
        actions = []
        if len(ownedFiefs) == 0:
            print("    You don't own any fiefs to send resources to!\n")
            time.sleep(0.5)
            nothing = input("    Press enter to continue ")
            return
        else:
            waiting = True
            print("    Your stronghold currently has: " + GetStationResources(station) + "\n")
            time.sleep(0.5)
            print("    Fiefs under your rule:\n")
            time.sleep(0.5)
            for i in range(len(ownedFiefs)):
                PrintOwnedFiefInformation(ownedFiefs[i])
            print("")
            while waiting:
                fiefName = input("    Please type a fief name above to send resources to it (or hit enter to cancel) : ")
                if fiefName == "":
                    waiting = False
                    print("\n    Cancelling request...\n")
                    time.sleep(0.5)
                    nothing = input("    Press enter to continue ")
                    return
                else:
                    for i in range(len(ownedFiefs)):
                        if fiefName == str(ownedFiefs[i].name):
                            waiting = False
            toStation = GetFiefByName(fiefName)
            print("\n    Please select the resources you would like to send to " + str(toStation.name) + ". (Type " + textColor.GREEN + "\"A\"" + RESET + " to send all resources): \n")
            time.sleep(0.5)
            if int(station.gold) > 0:
                print("\n    | Stronghold Gold: " + C_GOLD + str(station.gold) + RESET + " | " + str(toStation.name) + " Gold: " + YELLOW + str(toStation.gold) + RESET + " |")
                time.sleep(0.5)
                amount = input("\n    How much gold would you like to send to " + str(toStation.name) + "? : ")
                if IsPositiveIntEqualOrLessThan(amount, station.gold):
                    TransferResource(station, toStation, "gold", amount)
                    actions.append("    Sent " + C_GOLD + str(amount) + RESET + " gold to " + str(toStation.name))

                if amount == "A" or amount == "a":
                    actions.append("    Sent " + C_GOLD + str(station.gold) + RESET + " gold to " + str(toStation.name))
                    TransferResource(station, toStation, "gold", int(station.gold))

            if int(station.food) > 0:
                print("\n    | Stronghold Food: " + C_FOOD + str(station.food) + RESET + " | " + str(toStation.name) + " Food: " + C_FOOD + str(toStation.food) + RESET + " |")
                time.sleep(0.5)
                amount = input("\n    How much food would you like to send to " + str(toStation.name) + "? : ")
                if IsPositiveIntEqualOrLessThan(amount, station.food):
                    TransferResource(station, toStation, "food", amount)
                    actions.append("    Sent " + C_FOOD + str(amount) + RESET + " food to " + str(toStation.name))

                if amount == "A" or amount == "a":
                    actions.append("    Sent " + C_FOOD + str(station.food) + RESET + " food to " + str(toStation.name))
                    TransferResource(station, toStation, "food", int(station.food))

            if int(station.wood) > 0:
                print("\n    | Stronghold Wood: " + C_WOOD + str(station.wood) + RESET + " | " + str(toStation.name) + " Wood: " + C_WOOD + str(toStation.wood) + RESET + " |")
                time.sleep(0.5)
                amount = input("\n    How much wood would you like to send to " + str(toStation.name) + "? : ")
                if IsPositiveIntEqualOrLessThan(amount, station.wood):
                    TransferResource(station, toStation, "wood", amount)
                    actions.append("    Sent " + C_WOOD + str(amount) + RESET + " wood to " + str(toStation.name))

                if amount == "A" or amount == "a":
                    actions.append("    Sent " + C_WOOD + str(station.wood) + RESET + " wood to your stronghold.")
                    TransferResource(station, toStation, "wood", int(station.wood))

            if int(station.stone) > 0:
                print("\n    | Stronghold Stone: " + C_STONE + str(station.stone) + RESET + " | " + str(toStation.name) + " Stone: " + C_STONE + str(toStation.stone) + RESET + " |")
                time.sleep(0.5)
                amount = input("\n    How much stone would you like to send to " + str(toStation.name) + "? : ")
                if IsPositiveIntEqualOrLessThan(amount, station.stone):
                    TransferResource(station, toStation, "stone", amount)
                    actions.append("    Sent " + C_STONE + str(amount) + RESET + " stone to " + str(toStation.name))

                if amount == "A" or amount == "a":
                    actions.append("    Sent " + C_STONE + str(station.stone) + RESET + " stone to your stronghold.")
                    TransferResource(station, toStation, "stone", int(station.stone))


            if int(station.ore) > 0:
                print("\n    | Stronghold Ore: " + C_ORE + str(station.ore) + RESET + " | " + str(toStation.name) + " Ore: " + C_ORE + str(toStation.ore) + RESET + " |")
                time.sleep(0.5)
                amount = input("\n    How much ore would you like to send to " + str(toStation.name) + "? : ")
                if IsPositiveIntEqualOrLessThan(amount, station.ore):
                    TransferResource(station, toStation, "ore", amount)
                    actions.append("    Sent " + C_ORE + str(amount) + RESET + " ore to " + str(toStation.name))

                if amount == "A" or amount == "a":
                    actions.append("    Sent " + C_ORE + str(station.ore) + RESET + " ore to your stronghold.")
                    TransferResource(station, toStation, "ore", int(station.ore))
            
            time.sleep(0.5)
            #Print actions taken
            print("")
            if int(len(actions)) > 0:
                for i in range(len(actions)):
                    print("   " + str(actions[i]) + "\n")
                
                print("    Finished!\n")
                time.sleep(0.5)
                nothing = input("    Press enter to continue ")
                return
            else:
                print("    No changes were made.\n")
                time.sleep(0.5)
                nothing = input("    Press enter to continue ")
                return
    else:
        ownedFiefs = GetOwnedFiefList(station.ruler)
        actions = []
        waiting = True
        stronghold = False
        print("    " + str(station.name) + " currently has: " + GetStationResources(station) + "\n")
        time.sleep(0.5)
        if len(ownedFiefs) > 1:
            print("    Other fiefs under your rule:\n")
            time.sleep(0.5)
            for i in range(len(ownedFiefs)):
                if str(ownedFiefs[i].name) != str(station.name):
                    PrintOwnedFiefInformation(ownedFiefs[i])
            print("")
            while waiting:
                fiefName = input("    Type the Fiefdom name you would like to send resources to. Type " + textColor.GREEN + "\"S\"" + RESET + " to send the resources to your home Stronghold (or hit enter to cancel): ")
                if fiefName == "":
                    waiting = False
                    print("\n    Cancelling request...\n")
                    time.sleep(0.5)
                    nothing = input("    Press enter to continue ")
                    return
                elif fiefName == "stronghold" or fiefName == "S" or fiefName == "s":
                    toStation = userStronghold
                    stronghold = True
                    waiting = False
                else:
                    for i in range(len(ownedFiefs)):
                        if fiefName == str(ownedFiefs[i].name) and fiefName != str(station.name):
                            waiting = False
                            toStation = GetFiefByName(fiefName)
        else:
            toStation = userStronghold
            stronghold = True
        if stronghold:
            print("\n    Please select the resources you would like to send to your stronghold (Type " + textColor.GREEN + "\"A\"" + RESET + " to send all resources): \n")
            time.sleep(0.5)
            if int(station.gold) > 0:
                print("\n    | " + str(station.name) + " Gold: " + C_GOLD + str(station.gold) + RESET + " | Stronghold Gold: " + YELLOW + str(toStation.gold) + RESET + " |")
                time.sleep(0.5)
                amount = input("\n    How much gold would you like to send to your stronghold? : ")
                if IsPositiveIntEqualOrLessThan(amount, station.gold):
                    TransferResource(station, toStation, "gold", amount)
                    actions.append("    Sent " + C_GOLD + str(amount) + RESET + " gold to your stronghold.")

                if amount == "A" or amount == "a":
                    actions.append("    Sent " + C_GOLD + str(station.gold) + RESET + " gold to your stronghold.")
                    TransferResource(station, toStation, "gold", int(station.gold))

            if int(station.food) > 0:
                print("\n    | " + str(station.name) + " Food: " + C_FOOD + str(station.food) + RESET + " | Stronghold Food: " + C_FOOD + str(toStation.food) + RESET + " |")
                time.sleep(0.5)
                amount = input("\n    How much food would you like to send to your stronghold? : ")
                if IsPositiveIntEqualOrLessThan(amount, station.food):
                    TransferResource(station, toStation, "food", amount)
                    actions.append("    Sent " + C_FOOD + str(amount) + RESET + " food to your stronghold.")

                if amount == "A" or amount == "a":
                    actions.append("    Sent " + C_FOOD + str(station.food) + RESET + " food to your stronghold.")
                    TransferResource(station, toStation, "food", int(station.food))

            if int(station.wood) > 0:
                print("\n    | " + str(station.name) + " Wood: " + C_WOOD + str(station.wood) + RESET + " | Stronghold Wood: " + C_WOOD + str(toStation.wood) + RESET + " |")
                time.sleep(0.5)
                amount = input("\n    How much wood would you like to send to your stronghold? : ")
                if IsPositiveIntEqualOrLessThan(amount, station.wood):
                    TransferResource(station, toStation, "wood", amount)
                    actions.append("    Sent " + C_WOOD + str(amount) + RESET + " wood to your stronghold.")

                if amount == "A" or amount == "a":
                    actions.append("    Sent " + C_WOOD + str(station.wood) + RESET + " wood to your stronghold.")
                    TransferResource(station, toStation, "wood", int(station.wood))

            if int(station.stone) > 0:
                print("\n    | " + str(station.name) + " Stone: " + C_STONE + str(station.stone) + RESET + " | Stronghold Stone: " + C_STONE + str(toStation.stone) + RESET + " |")
                time.sleep(0.5)
                amount = input("\n    How much stone would you like to send to your stronghold? : ")
                if IsPositiveIntEqualOrLessThan(amount, station.stone):
                    TransferResource(station, toStation, "stone", amount)
                    actions.append("    Sent " + C_STONE + str(amount) + RESET + " stone to your stronghold.")

                if amount == "A" or amount == "a":
                    actions.append("    Sent " + C_STONE + str(station.stone) + RESET + " stone to your stronghold.")
                    TransferResource(station, toStation, "stone", int(station.stone))

            if int(station.ore) > 0:
                print("\n    | " + str(station.name) + " Ore: " + C_ORE + str(station.ore) + RESET + " | Stronghold Ore: " + C_ORE + str(toStation.ore) + RESET + " |")
                time.sleep(0.5)
                amount = input("\n    How much ore would you like to send to your stronghold? : ")
                if IsPositiveIntEqualOrLessThan(amount, station.ore):
                    TransferResource(station, toStation, "ore", amount)
                    actions.append("    Sent " + C_ORE + str(amount) + RESET + " ore to your stronghold.")

                if amount == "A" or amount == "a":
                    actions.append("    Sent " + C_ORE + str(station.ore) + RESET + " ore to your stronghold.")
                    TransferResource(station, toStation, "ore", int(station.ore))

        elif isinstance(toStation, Fiefdom):
            print("\n    Please select the resources you would like to send from " + str(station.name) + " to " + str(toStation.name) + " (Type " + textColor.GREEN + "\"A\"" + RESET + " to send all resources): \n")
            time.sleep(0.5)
            if int(station.gold) > 0:
                print("\n    | " + str(station.name) + " Gold: " + C_GOLD + str(station.gold) + RESET + " | " + str(toStation.name) + " Gold: " + YELLOW + str(toStation.gold) + RESET + " |")
                time.sleep(0.5)
                amount = input("\n    How much gold would you like to send to " + str(toStation.name) + "? : ")
                if IsPositiveIntEqualOrLessThan(amount, station.gold):
                    TransferResource(station, toStation, "gold", amount)
                    actions.append("    Sent " + C_GOLD + str(amount) + RESET + " gold to " + str(toStation.name))

                if amount == "A" or amount == "a":
                    actions.append("    Sent " + C_GOLD + str(station.gold) + RESET + " gold to " + str(toStation.name))
                    TransferResource(station, toStation, "gold", int(station.gold))

            if int(station.food) > 0:
                print("\n    | " + str(station.name) + " Food: " + C_FOOD + str(station.food) + RESET + " | " + str(toStation.name) + " Food: " + C_FOOD + str(toStation.food) + RESET + " |")
                time.sleep(0.5)
                amount = input("\n    How much food would you like to send to " + str(toStation.name) + "? : ")
                if IsPositiveIntEqualOrLessThan(amount, station.food):
                    TransferResource(station, toStation, "food", amount)
                    actions.append("    Sent " + C_FOOD + str(amount) + RESET + " food to " + str(toStation.name))

                if amount == "A" or amount == "a":
                    actions.append("    Sent " + C_FOOD + str(station.food) + RESET + " food to " + str(toStation.name))
                    TransferResource(station, toStation, "food", int(station.food))

            if int(station.wood) > 0:
                print("\n    | " + str(station.name) + " Wood: " + C_WOOD + str(station.wood) + RESET + " | " + str(toStation.name) + " Wood: " + C_WOOD + str(toStation.wood) + RESET + " |")
                time.sleep(0.5)
                amount = input("\n    How much wood would you like to send to " + str(toStation.name) + "? : ")
                if IsPositiveIntEqualOrLessThan(amount, station.wood):
                    TransferResource(station, toStation, "wood", amount)
                    actions.append("    Sent " + C_WOOD + str(amount) + RESET + " wood to " + str(toStation.name))

                if amount == "A" or amount == "a":
                    actions.append("    Sent " + C_WOOD + str(station.wood) + RESET + " wood to " + str(toStation.name))
                    TransferResource(station, toStation, "wood", int(station.wood))

            if int(station.stone) > 0:
                print("\n    | " + str(station.name) + " Stone: " + C_STONE + str(station.stone) + RESET + " | " + str(toStation.name) + " Stone: " + C_STONE + str(toStation.stone) + RESET + " |")
                time.sleep(0.5)
                amount = input("\n    How much stone would you like to send to " + str(toStation.name) + "? : ")
                if IsPositiveIntEqualOrLessThan(amount, station.stone):
                    TransferResource(station, toStation, "stone", amount)
                    actions.append("    Sent " + C_STONE + str(amount) + RESET + " stone to " + str(toStation.name))

                if amount == "A" or amount == "a":
                    actions.append("    Sent " + C_STONE + str(station.stone) + RESET + " stone to " + str(toStation.name))
                    TransferResource(station, toStation, "stone", int(station.stone))

            if int(station.ore) > 0:
                print("\n    | " + str(station.name) + " Ore: " + C_ORE + str(station.ore) + RESET + " | " + str(toStation.name) + " Ore: " + C_ORE + str(toStation.ore) + RESET + " |")
                time.sleep(0.5)
                amount = input("\n    How much ore would you like to send to " + str(toStation.name) + "? : ")
                if IsPositiveIntEqualOrLessThan(amount, station.ore):
                    TransferResource(station, toStation, "ore", amount)
                    actions.append("    Sent " + C_ORE + str(amount) + RESET + " ore to " + str(toStation.name))

                if amount == "A" or amount == "a":
                    actions.append("    Sent " + C_ORE + str(station.ore) + RESET + " ore to " + str(toStation.name))
                    TransferResource(station, toStation, "ore", int(station.wood))
        
        time.sleep(0.5)
        #Print actions taken
        print("")
        if int(len(actions)) > 0:
            for i in range(len(actions)):
                print("   " + str(actions[i]) + "\n")
            
            print("    Finished!\n")
            time.sleep(0.5)
            nothing = input("    Press enter to continue ")
            return
        else:
            print("    No changes were made.\n")
            time.sleep(0.5)
            nothing = input("    Press enter to continue ")
            return




#========================================================================================================
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#========================================================================================================
#                                     Upgrades and Hire Functions
#========================================================================================================
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#========================================================================================================


#========================================================================================================
#   HireUnit
#   parameters: station, unitType, unitBaseCost, unitCostModifier, unitCap, unitsOwned, color, flavorText
#       Takes several parameters and rusn them through a default unit hiring interface.
#       With the addition of 8 new units, something like this was necessary to avoid redundant code.
#       Note: The cost modifier currently does nothing, may need to add it back into the loop somehow.
#========================================================================================================
def HireUnit(station, unitType, unitCost, unitCostModifier, unitCap, unitsOwned, color, flavorText):
    
    if flavorText.strip() != "":
        print(flavorText)
    spotsAvailable = int(unitCap) - int(unitsOwned)
    # unitCost = int(unitBaseCost) + int(float(unitBaseCost) * float(unitCostModifier))
    print("    You currently have " + textColor.WARNING + str(unitsOwned) + color + " " + unitType + textColor.RESET + " units hired.\n")
    time.sleep(0.5)
    if(spotsAvailable > 0):
        print("    You have room for " + textColor.WARNING + str(spotsAvailable) + textColor.RESET + " more of these units.\n")
        time.sleep(0.5)
    else:
        print("    You don't have any more room for these units!\n")
        time.sleep(0.5)
        nothing = input("    Press enter to continue ")
        return
    print("    " + color + unitType + textColor.RESET + " units cost " + GetResourceCost(unitCost, 1) + " each.\n")
    time.sleep(0.5)
    unitCount = input("    How many " + color + unitType + textColor.RESET + " units would you like to hire? : ")

    try:
        int(unitCount)
    except:
        unitCount = '0'

    if int(unitCount) == 0:
        print("\n    No changes were made!\n")
        time.sleep(0.5)
        nothing = input("    Press enter to continue ")
        return

    elif int(unitCount) < 0:
        print("\n    You can't hire a negative number of " + color + unitType + textColor.RESET + " units!\n")
        time.sleep(0.5)
        nothing = input("    Press enter to continue ")
        return

    elif int(unitCount) > int(spotsAvailable):
        print("\n    Can't hire " + textColor.WARNING + str(unitCount) + textColor.RESET + " units, only have room for " + textColor.WARNING + str(spotsAvailable) + textColor.RESET + " more!\n")
        time.sleep(0.5)
        nothing = input("    Press enter to continue ")
        return

    elif HaveEnoughResources(station, unitCost, unitCount):
        print("\n    Hiring " + textColor.WARNING + str(unitCount) + color +  " " + unitType + textColor.RESET + " units...")
        time.sleep(0.5)

        #Increment the unit based on type:
        if unitType == "Warrior":
            station.defenders = int(station.defenders) + int(unitCount)
        elif unitType == "Thief":
            station.thieves = int(station.thieves) + int(unitCount)
        elif unitType == "Farmer":
            station.op_farmlandPrimaryUnits = int(station.op_farmlandPrimaryUnits) + int(unitCount)
        elif unitType == "Vendor":
            station.op_farmlandSecondaryUnits = int(station.op_farmlandSecondaryUnits) + int(unitCount)
        elif unitType == "Fisher":
            station.op_fisheryPrimaryUnits = int(station.op_fisheryPrimaryUnits) + int(unitCount)
        elif unitType == "Scavenger":
            station.op_fisherySecondaryUnits = int(station.op_fisherySecondaryUnits) + int(unitCount)
        elif unitType == "Lumberjack":
            station.op_lumberMillPrimaryUnits = int(station.op_lumberMillPrimaryUnits) + int(unitCount)
        elif unitType == "Hunter":
            station.op_lumberMillSecondaryUnits = int(station.op_lumberMillSecondaryUnits) + int(unitCount)
        elif unitType == "Miner":
            station.op_minePrimaryUnits = int(station.op_minePrimaryUnits) + int(unitCount)
        elif unitType == "Prospector":
            station.op_mineSecondaryUnits = int(station.op_mineSecondaryUnits) + int(unitCount)
        #Deduct resources
        DeductResources(station, unitCost, unitCount)
        
        print("\n    Success! You now have " + textColor.WARNING + str(int(unitsOwned) + int(unitCount)) + color + " " + unitType + textColor.RESET + " units at this location!\n")
        station.write()
        station.read()
        time.sleep(0.5)

        print("    This location now has " + GetStationResources(station) + " remaining!")
        time.sleep(0.5)

        nothing = input("\n    Press enter to continue ")

    else:
        time.sleep(0.5)
        print("\n    You don't have the required resources!\n")
        nothing = input("    Press enter to continue ")
        return

#========================================================================================================
#   ConstructOutpost
#   parameters: station, outpostType, tier, numberBuilt, spotsAvailable, cost, color, flavorText
#       Takes some parameters and walks user through a cookie-cutter outpost construction menu
#========================================================================================================
def ConstructOutpost(station, outpostType, tier, numberBuilt, spotsAvailable, cost, color, flavorText):
    listening = True

    if flavorText.strip() != "":
        print(flavorText)

    if HaveEnoughResources(station, cost, 1) == False:
        print("    You don't have the resources to build any " + color + str(outpostType) + textColor.RESET + " outposts!\n")
        print("    It will cost " + GetResourceCost(cost, 1) + " to build another outpost.")
        nothing = input("\n    Press enter to continue ")
        return
    else:
        if int(numberBuilt) > 0:
            print("    You currently have " + textColor.WARNING + str(numberBuilt) + color + " " + str(outpostType) + textColor.RESET + " outposts constructed.\n")
            time.sleep(0.5)
            print("    Your " + color + str(outpostType) + textColor.RESET + " outposts are at rank " + textColor.MAGENTA + str(int(tier) + 1) + textColor.RESET + ".\n")
            time.sleep(0.5)
            if int(tier) > 0:
                print("    Note that outposts must be constructed at the same " + textColor.MAGENTA + "rank" + textColor.RESET + " as other outposts of the same type.\n")
        else:
            print("    You don't have any " + color + str(outpostType) + textColor.RESET + " outposts built yet.\n")
            time.sleep(0.5)

        #If you have reached this point, there has to be at least 1 spot available to build this outpost.
        if spotsAvailable == 1:
            print("    You have one spot left for a " + color + str(outpostType) + textColor.RESET + " outpost.\n")
            time.sleep(0.5)
            if AnswerYes("    Would you like to construct a " + color + str(outpostType) + textColor.RESET + " outpost for " + GetResourceCost(cost, 1) + " gold?"):
                print("\n    Constructing a new " + color + str(outpostType) + textColor.RESET + "...")
                time.sleep(1)

                DeductResources(station, cost, 1)

                if outpostType == "Farmland":
                    station.op_farmlandNumBuilt = str(int(station.op_farmlandNumBuilt) + 1)
                elif outpostType == "Fishery":
                    station.op_fisheryNumBuilt = str(int(station.op_fisheryNumBuilt) + 1)
                elif outpostType == "Lumber Mill":
                    station.op_lumberMillNumBuilt = str(int(station.op_lumberMillNumBuilt) + 1)
                elif outpostType == "Mine":
                    station.op_mineNumBuilt = str(int(station.op_mineNumBuilt) + 1)

                station.write()
                station.read()

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
            print("    At rank " + textColor.MAGENTA + str(int(tier) + 1) + textColor.RESET + ", constructing a new " + color + str(outpostType) + textColor.RESET + " outpost will cost " + GetResourceCost(cost, 1) + " per outpost.\n")
            time.sleep(0.5)

            while listening:
                buildNum = input("    How many " + color + str(outpostType) + textColor.RESET + " outposts would you like to build? : ")
                try:
                    int(buildNum)

                    if int(buildNum) < 0:
                        pass
                
                    elif int(buildNum) == 0:
                        print("\n    Cancelling request...\n")
                        time.sleep(1)
                        return
                    
                    elif int(buildNum) > int(spotsAvailable):
                        print("\n    You only have " + textColor.WARNING + str(spotsAvailable) + textColor.RESET + " spots remaining!\n")
                        time.sleep(0.5)
                        nothing = input("    Press enter to continue ")
                        return

                    elif HaveEnoughResources(station, cost, buildNum) == False:
                        print("\n    You don't have the resources to build " + textColor.WARNING + str(buildNum) + color + " " + str(outpostType) + textColor.RESET + " outposts!\n")
                        time.sleep(0.5)
                        nothing = input("    Press enter to continue ")
                        return
                    
                    else:
                        print("\n    Constructing " + textColor.WARNING + str(buildNum) + color + " " + str(outpostType) + textColor.RESET + " outposts...")
                        time.sleep(1)

                        DeductResources(station, cost, buildNum)

                        if outpostType == "Farmland":
                            station.op_farmlandNumBuilt = str(int(station.op_farmlandNumBuilt) + int(buildNum))
                        elif outpostType == "Fishery":
                            station.op_fisheryNumBuilt = str(int(station.op_fisheryNumBuilt) + int(buildNum))
                        elif outpostType == "Lumber Mill":
                            station.op_lumberMillNumBuilt = str(int(station.op_lumberMillNumBuilt) + int(buildNum))
                        elif outpostType == "Mine":
                            station.op_mineNumBuilt = str(int(station.op_mineNumBuilt) + int(buildNum))

                        station.write()
                        station.read()

                        print("\n    Construction of " + textColor.WARNING + str(buildNum) + color + " " + str(outpostType) + textColor.RESET + " outposts was successful!\n")
                        time.sleep(0.5)
                        nothing = input("    Press enter to continue ")
                        return

                except:
                    print("    Error with input, please try again.\n")
                    time.sleep(0.5)
                    nothing = input("    Press enter to continue ")
                    return

                
#========================================================================================================
#   UpgradeOutpost
#   parameters: station, outpostType, tier, numberBuilt, cost, flavorText
#       Takes some parameters and walks user through a cookie-cutter outpost construction menu
#========================================================================================================
def UpgradeOutpost(station, outpostType, tier, numberBuilt, cost, color, flavorText):
    if flavorText.strip() != "":
        print(flavorText)
    if tier >= 2:
        print("    Your outposts are at the max rank!\n")
        time.sleep(1)
        return
    elif HaveEnoughResources(station, cost, 1) == False:
        print("    You don't have enough resources to to upgrade your " + color + str(outpostType) + textColor.RESET + " outposts!\n")
        print("    This upgrade will cost " + GetResourceCost(cost, 1))

        nothing = input("\n    Press enter to continue ")
        return
    else:
        print("    You currently have " + textColor.WARNING + str(numberBuilt) + color + " " + str(outpostType) + textColor.RESET + " outposts constructed.\n")
        time.sleep(0.5)
        print("    Your " + color + str(outpostType) + textColor.RESET + " outposts are at rank " + textColor.MAGENTA + str(int(tier) + 1) + textColor.RESET + ".\n")
        time.sleep(0.5)
        print("    Note that you must upgrade all constructed outposts of the same type at the same time!\n")
        time.sleep(0.5)

        if AnswerYes("    Would you like to upgrade all of your " + color + str(outpostType) + textColor.RESET + " outposts for " + GetResourceCost(cost, 1) + "?"):
            print("\n    Upgrading " + color + str(outpostType)  + textColor.RESET + " outposts...\n")
            time.sleep(1)

            DeductResources(station, cost, 1)

            if outpostType == "Farmland":
                station.op_farmlandTier = str(int(station.op_farmlandTier) + 1)
            elif outpostType == "Fishery":
                station.op_fisheryTier = str(int(station.op_fisheryTier) + 1)
            elif outpostType == "Lumber Mill":
                station.op_lumberMillTier = str(int(station.op_lumberMillTier) + 1)
            elif outpostType == "Mine":
                station.op_mineTier = str(int(station.op_mineTier) + 1)

            station.write()
            station.read()

            print("    Success!")
            time.sleep(0.5)
            nothing = input("\n    Press enter to continue ")

            return

        else:
            print("\n    Cancelling request...")
            time.sleep(1)
            return
        



#--------------------------------------------------------------------------------------------------------------
#   [CreateFief]
#   Parameters: num
#   Creates a new fief file when called. It will pull names from the fieflist.py and check to see
#   if a fief has been created before doing so.
#--------------------------------------------------------------------------------------------------------------
def CreateFief():
    #print('\n\n    Creating New Fief')

    filename = "defaultfieflist.dat"
    fiefExists = True
    fiefName = "default"
    
    #while the random fief does not exist in the list of fief files
    while(fiefExists):
        lines = open(filename).read().splitlines()
        randomFief = random.choice(lines)
        #print('\n    ' + randomFief + ' chosen. Checking to see if it exists in fiefs/')
        
        userPath = ('fiefs/' + randomFief + '.txt')        
        if exists(userPath) == True:
            #print('\n    This fief already exists in the fiefs/ folder! Trying again')
            pass
        else:
            # print('\n    This fief is unique! Create it now')
            #ok now we need to create a new fief file with the default values

            currentFief = Fiefdom()
            currentFief.name = randomFief
            currentFief.defenders = random.randint(10, 100)
            currentFief.gold = random.randint(500, 3100)
            currentFief.write()
            print('    New Fief Created!')
            os.system("clear")
            
            try:
                map().read(serverMap)
            except:
                #print('(map().read(serverMap)      failed')
                pass

            #print('\n    ' + randomFief + ' is created')
            fiefName = randomFief
            fiefExists = False    
            return(randomFief)



    #tempInput = input('\n    Press Enter to Continue: ')





#========================================================================================================
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#========================================================================================================
#                                         Market Functions
#========================================================================================================
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#========================================================================================================

#==================================================================================
#   [CreateListing]
#   parameter: userStronghold
#       Guides user through menu to list a sale or offer
#==================================================================================
def CreateListing(userStronghold):
    os.system("clear")
    header(userStronghold.name)
    seller = str(WARNING + str(userStronghold.name) + RESET)
    transaction = str(CYAN + " [?] " + RESET)
    costAmount = str(WARNING + " (?) " + RESET)
    costType = str(GREEN + " (?) " + RESET)
    goodAmount = str(WARNING + " (?) " + RESET)
    goodType = str(CYAN + "(?)" + RESET)
    numListings = serverMarket.NumListings(userStronghold.name)

    #Check if the user has too many listings already
    if int(numListings) >= MAX_LISTING_AMOUNT:
        time.sleep(0.5)
        print("    You have too many listings! Maximum is " + str(MAX_LISTING_AMOUNT) + "!")
        nothing = input("    Press enter to continue.")
        return "market"

    listing = str("\n        " + seller + transaction + costAmount + costType + " [For] " + goodAmount + goodType)

    print("\n    Your Listing:")
    print(listing)

    print('')
    if int(numListings) > int(MAX_LISTING_AMOUNT) - 3:
        print("    " + RED + "Warning" + RESET + ": users may have 10 active listings at one time! You have " + WARNING + str(numListings) + RESET + " currently!")
    print("    Please select the kind of " + CYAN + "transaction " + RESET + "you want to make:")
    print('    -------------------------------------------------------')
    if int(userStronghold.gold) > 0:
        print('    {1}: Buy') 
    if StationHasSomeResources(userStronghold):
        print('    {2}: Sell')
        print('    {3}: Trade')
    print('    {4}: Cancel')
    print('    -------------------------------------------------------')
    print('')
    command = input("    Enter your command: ")
    picking = True
    while picking:
        if int(userStronghold.gold) > 0:
            if command == "1":
                transaction = str(GREEN + "  [Buying] " + RESET)
                tr = "buy"
                picking = False
        if StationHasSomeResources(userStronghold):
            if command == "2":
                transaction = str(CYAN + "  [Selling] " + RESET)
                tr = "sell"
                picking = False
            if command == "3":
                transaction = str(WARNING + "  [Trading] " + RESET)
                tr = "trade"
                picking = False
        if command == "4":
            return "market"

    #--------------------------------------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------------------------------
    #                                                   BUY
    #--------------------------------------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------------------------------
    if tr == "buy":
        os.system("clear")
        header(userStronghold.name)
        listing = str("\n        " + seller + transaction + costAmount + costType + " [For] " + goodAmount + goodType)
        print("\n    Your Listing:")
        print(listing)

        print('')
        print("    Please select the good you're" + WARNING + " BUYING" + RESET + ":")
        print('    -------------------------------------------------------')
        print('    {1}:' + STR_FOOD)
        print('    {2}:' + STR_WOOD)
        print('    {3}:' + STR_STONE)
        print('    {4}:' + STR_ORE)
        print('    {5}: Cancel')
        print('    -------------------------------------------------------')
        print('')
        picking = True
        while picking:
            command = input("    Select a good or cancel listing: ")
            if command == "1":
                costType = str(STR_FOOD)
                ct = "Food"
                picking = False
            elif command == "2":
                costType = str(STR_WOOD)
                ct = "Wood"
                picking = False
            elif command == "3":
                costType = str(STR_STONE)
                ct = "Stone"
                picking = False
            elif command == "4":
                costType = str(STR_ORE)
                ct = "Ore"
                picking = False
            elif command == "5":
                return "market"

        picking = True
        while picking:
            command = input("    How much" + costType + "are you wanting?: ")
            if IsPositiveInteger(command):    
                costAmount = str(WARNING + " " + str(command) + " " + RESET)
                ca = str(command)
                picking = False
            elif command == "cancel":
                return "market"
            else:
                print("    Positive integers only (or type cancel to exit): ")

        os.system("clear")
        header(userStronghold.name)
        listing = str("\n        " + seller + transaction + costAmount + costType + " [For] " + goodAmount + goodType)
        print("\n    Your Listing:")
        print(listing)
            
        picking = True
        while picking:
            command = input("\n\n    How much " + STR_GOLD + " are you offering?: ")
            if IsPositiveInteger(command):
                if CheckResourceByType(userStronghold, "Gold", command):
                    goodType = str(STR_GOLD)
                    gt = "Gold"
                    goodAmount = str(WARNING + " " + command + " " + RESET)
                    ga = str(command)
                    picking = False
                else:
                    print("    You don't have enough " + STR_GOLD + "!")
            elif command == "cancel":
                return "market"
            else:
                print("    Positive integers only (or type cancel to exit): ")

        os.system("clear")
        header(userStronghold.name)
        listing = str("\n        " + seller + transaction + costAmount + costType + " [For] " + goodAmount + goodType)
        print("\n    Your Listing:")
        print(listing)

        print('')
        print("    Please select how" + WARNING + " LONG" + RESET + " you want your listing to be up for:")
        print('    -------------------------------------------------------')
        print('    {1}: One Hour') 
        print('    {2}: Three Hours')
        print('    {3}: One Day')
        print('    {4}: Two Days')
        print('    {5}: Three Days')
        print('    {6}: Cancel')
        print('    -------------------------------------------------------')
        print('')
        picking = True
        while picking:
            command = input("    Input a time or cancel listing: ")
            if command == "1":
                shelfLife = "One Hour"
                sl = 3600
                picking = False
            elif command == "2":
                shelfLife = "Three Hours"
                sl = int(3600 * 3)
                picking = False
            elif command == "3":
                shelfLife = "One Day"
                sl = int(3600 * 24)
                picking = False
            elif command == "4":
                shelfLife = "Two Days"
                sl = int(3600 * 48)
                picking = False
            elif command == "5":
                shelfLife = "Three Days"
                sl = int(3600 * 72)
                picking = False
            elif command == "6":
                return "market"

        os.system("clear")
        header(userStronghold.name)
        listing = str("\n        " + seller + transaction + costAmount + costType + " [For] " + goodAmount + goodType)
        print("\n    Your Listing:")
        print(listing)

        time.sleep(0.5)
        print("\n    Your" + goodAmount + goodType + "will be returned after " + CYAN + shelfLife + RESET + " if no one accepts the offer.\n")
        time.sleep(0.5)
        if AnswerYes("    Finalize listing?"):
            serverMarket.AddGood(userStronghold.name, sl, gt, ga, ct, ca)
            serverMarket.write()
            DeductResourceByType(userStronghold, gt, ga)
            time.sleep(0.5)
            print("\n    Listing successful!")
            time.sleep(0.5)
            nothing = input("\n    Press enter to continue.")

        return "market"
    #--------------------------------------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------------------------------
    #                                                      SELL
    #--------------------------------------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------------------------------
    elif tr == "sell":
        os.system("clear")
        header(userStronghold.name)
        ct = "Gold"
        costType = str(STR_GOLD)
        listing = str("\n        " + seller + transaction + goodAmount + goodType + " [For] " + costAmount + costType)
        print("\n    Your Listing:")
        print(listing)

        print('')
        print("    Please select the good you're" + WARNING + " OFFERING" + RESET + ":")
        print('    -------------------------------------------------------')
        if int(userStronghold.food) > 0:
            print('    {1}:' + STR_FOOD)
        if int(userStronghold.wood) > 0:
            print('    {2}:' + STR_WOOD)
        if int(userStronghold.stone) > 0:
            print('    {3}:' + STR_STONE)
        if int(userStronghold.ore) > 0:
            print('    {4}:' + STR_ORE)
        print('    {5}: Cancel')
        print('    -------------------------------------------------------')
        print('')
        picking = True
        while picking:
            command = input("    Select a good or cancel listing: ")
            if int(userStronghold.food) > 0:
                if command == "1":
                    goodType = str(STR_FOOD)
                    gt = "Food"
                    picking = False
            if int(userStronghold.wood) > 0:
                if command == "2":
                    goodType = str(STR_WOOD)
                    gt = "Wood"
                    picking = False
            if int(userStronghold.stone) > 0:
                if command == "3":
                    goodType = str(STR_STONE)
                    gt = "Stone"
                    picking = False
            if int(userStronghold.ore) > 0:
                if command == "4":
                    goodType = str(STR_ORE)
                    gt = "Ore"
                    picking = False
            if command == "5":
                return "market"
            
        picking = True
        while picking:
            command = input("    How much" + goodType + "are you offering?: ")
            if IsPositiveInteger(command):
                if CheckResourceByType(userStronghold, gt, command):
                    goodAmount = str(WARNING + " " + str(command) + " " + RESET)
                    ga = str(command)
                    picking = False
                else:
                    print("    You don't have enough of that resource!")
            elif command == "cancel":
                return "market"
            else:
                print("    Positive integers only (or type cancel to exit): ")

        os.system("clear")
        header(userStronghold.name)
        listing = str("\n        " + seller + transaction + goodAmount + goodType + " [For] " + costAmount + costType)
        print("\n    Your Listing:")
        print(listing)
            
        picking = True
        while picking:
            command = input("\n\n    How much" + costType + "are you wanting?: ")
            if IsPositiveInteger(command):
                costAmount = str(WARNING + " " + command + " " + RESET)
                ca = str(command)
                picking = False
            elif command == "cancel":
                return "market"
            else:
                print("    Positive integers only (or type cancel to exit): ")

        os.system("clear")
        header(userStronghold.name)
        listing = str("\n        " + seller + transaction + goodAmount + goodType + " [For] " + costAmount + costType)
        print("\n    Your Listing:")
        print(listing)

        print('')
        print("    Please select how" + WARNING + " LONG" + RESET + " you want your listing to be up for:")
        print('    -------------------------------------------------------')
        print('    {1}: One Hour') 
        print('    {2}: Three Hours')
        print('    {3}: One Day')
        print('    {4}: Two Days')
        print('    {5}: Three Days')
        print('    {6}: Cancel')
        print('    -------------------------------------------------------')
        print('')
        picking = True
        while picking:
            command = input("    Input a time or cancel listing: ")
            if command == "1":
                shelfLife = "One Hour"
                sl = 3600
                picking = False
            elif command == "2":
                shelfLife = "Three Hours"
                sl = int(3600 * 3)
                picking = False
            elif command == "3":
                shelfLife = "One Day"
                sl = int(3600 * 24)
                picking = False
            elif command == "4":
                shelfLife = "Two Days"
                sl = int(3600 * 48)
                picking = False
            elif command == "5":
                shelfLife = "Three Days"
                sl = int(3600 * 72)
                picking = False
            elif command == "6":
                return "market"

        os.system("clear")
        header(userStronghold.name)
        listing = str("\n        " + seller + transaction + goodAmount + goodType + " [For] " + costAmount + costType)
        print("\n    Your Listing:")
        print(listing)

        time.sleep(0.5)
        print("\n    Your" + goodAmount + goodType + "will be returned after " + CYAN + shelfLife + RESET + " if no one accepts the offer.\n")
        time.sleep(0.5)
        if AnswerYes("    Finalize listing?"):
            serverMarket.AddGood(userStronghold.name, sl, gt, ga, ct, ca)
            serverMarket.write()
            DeductResourceByType(userStronghold, gt, ga)
            time.sleep(0.5)
            print("\n    Listing successful!")
            time.sleep(0.5)
            nothing = input("\n    Press enter to continue.")

        return "market"
    #--------------------------------------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------------------------------
    #                                                      TRADE
    #--------------------------------------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------------------------------
    else:
        os.system("clear")
        header(userStronghold.name)
        listing = str("\n        " + seller + transaction + goodAmount + goodType + " [For] " + costAmount + costType)
        print("\n    Your Listing:")
        print(listing)

        print('')
        print("    Please select the good you're" + WARNING + " WANTING" + RESET + ":")
        print('    -------------------------------------------------------')
        print('    {1}:' + STR_FOOD)
        print('    {2}:' + STR_WOOD)
        print('    {3}:' + STR_STONE)
        print('    {4}:' + STR_ORE)
        print('    {5}: Cancel')
        print('    -------------------------------------------------------')
        print('')
        picking = True
        while picking:
            command = input("    Select a good or cancel listing: ")
            if command == "1":
                costType = str(STR_FOOD)
                ct = "Food"
                picking = False
            elif command == "2":
                costType = str(STR_WOOD)
                ct = "Wood"
                picking = False
            elif command == "3":
                costType = str(STR_STONE)
                ct = "Stone"
                picking = False
            elif command == "4":
                costType = str(STR_ORE)
                ct = "Ore"
                picking = False
            elif command == "5":
                return "market"

        picking = True
        while picking:
            command = input("    How much" + costType + "are you wanting?: ")
            if IsPositiveInteger(command):    
                costAmount = str(WARNING + " " + str(command) + " " + RESET)
                ca = str(command)
                picking = False
            elif command == "cancel":
                return "market"
            else:
                print("    Positive integers only (or type cancel to exit): ")

        os.system("clear")
        header(userStronghold.name)
        listing = str("\n        " + seller + transaction + goodAmount + goodType + " [For] " + costAmount + costType)
        print("\n    Your Listing:")
        print(listing)

        print('')
        print("    Please select the good you're" + WARNING + " OFFERING" + RESET + ":")
        print('    -------------------------------------------------------')
        if int(userStronghold.food) > 0:
            print('    {1}:' + STR_FOOD)
        if int(userStronghold.wood) > 0:
            print('    {2}:' + STR_WOOD)
        if int(userStronghold.stone) > 0:
            print('    {3}:' + STR_STONE)
        if int(userStronghold.ore) > 0:
            print('    {4}:' + STR_ORE)
        print('    {5}: Cancel')
        print('    -------------------------------------------------------')
        print('')
        picking = True
        while picking:
            command = input("    Select a good or cancel listing: ")
            if int(userStronghold.food) > 0:
                if command == "1":
                    goodType = str(STR_FOOD)
                    gt = "Food"
                    picking = False
            if int(userStronghold.wood) > 0:
                if command == "2":
                    goodType = str(STR_WOOD)
                    gt = "Wood"
                    picking = False
            if int(userStronghold.stone) > 0:
                if command == "3":
                    goodType = str(STR_STONE)
                    gt = "Stone"
                    picking = False
            if int(userStronghold.ore) > 0:
                if command == "4":
                    goodType = str(STR_ORE)
                    gt = "Ore"
                    picking = False
            if command == "5":
                return "market"
            
        picking = True
        while picking:
            command = input("    How much" + goodType + "are you offering?: ")
            if IsPositiveInteger(command):
                if CheckResourceByType(userStronghold, gt, command):
                    goodAmount = str(WARNING + " " + str(command) + " " + RESET)
                    ga = str(command)
                    picking = False
                else:
                    print("    You don't have enough of that resource!")
            elif command == "cancel":
                return "market"
            else:
                print("    Positive integers only (or type cancel to exit): ")

        os.system("clear")
        header(userStronghold.name)
        listing = str("\n        " + seller + transaction + goodAmount + goodType + " [For] " + costAmount + costType)
        print("\n    Your Listing:")
        print(listing)

        print('')
        print("    Please select how" + WARNING + " LONG" + RESET + " you want your listing to be up for:")
        print('    -------------------------------------------------------')
        print('    {1}: One Hour') 
        print('    {2}: Three Hours')
        print('    {3}: One Day')
        print('    {4}: Two Days')
        print('    {5}: Three Days')
        print('    {6}: Cancel')
        print('    -------------------------------------------------------')
        print('')
        picking = True
        while picking:
            command = input("    Input a time or cancel listing: ")
            if command == "1":
                shelfLife = "One Hour"
                sl = 3600
                picking = False
            elif command == "2":
                shelfLife = "Three Hours"
                sl = int(3600 * 3)
                picking = False
            elif command == "3":
                shelfLife = "One Day"
                sl = int(3600 * 24)
                picking = False
            elif command == "4":
                shelfLife = "Two Days"
                sl = int(3600 * 48)
                picking = False
            elif command == "5":
                shelfLife = "Three Days"
                sl = int(3600 * 72)
                picking = False
            elif command == "6":
                return "market"

        os.system("clear")
        header(userStronghold.name)
        listing = str("\n        " + seller + transaction + goodAmount + goodType + " [For] " + costAmount + costType)
        print("\n    Your Listing:")
        print(listing)

        time.sleep(0.5)
        print("\n    Your" + goodAmount + goodType + "will be returned after " + CYAN + shelfLife + RESET + " if no one accepts the offer.\n")
        time.sleep(0.5)
        if AnswerYes("    Finalize listing?"):
            serverMarket.AddGood(userStronghold.name, sl, gt, ga, ct, ca)
            serverMarket.write()
            DeductResourceByType(userStronghold, gt, ga)
            time.sleep(0.5)
            print("\n    Listing successful!")
            time.sleep(0.5)
            nothing = input("\n    Press enter to continue.")

        return "market"

#==================================================================================
#   [AddResources]
#   parameter: userStronghold, type, amount
#   Adds resources based on passed amount
#==================================================================================
def AddResources(userStronghold, type, amount):
    if str(type) == "Gold":
        userStronghold.gold = str(int(userStronghold.gold) + int(amount))
    if str(type) == "Food":
        userStronghold.food = str(int(userStronghold.food) + int(amount))
    elif str(type) == "Wood":
        userStronghold.wood = str(int(userStronghold.wood) + int(amount))
    elif str(type) == "Stone":
        userStronghold.stone = str(int(userStronghold.stone) + int(amount))
    elif str(type) == "Ore":
        userStronghold.ore = str(int(userStronghold.ore) + int(amount))

#==================================================================================
#   [PurchasedGood]
#   parameter: num
#   returns: True/False depending on how user answers questions
#==================================================================================
def PurchasedGood(userStronghold, num):
    os.system("clear")
    header(userStronghold.name)
    good = serverMarket.GetGood(num)
    print("")
    if good.seller == "The Wandering Merchant":
        pas_market_greetings()

    print("    Observing the following offer:\n")
    time.sleep(0.5)
    print("   " + str(good.ListDetails()))

    if good.costType == "Gold":
        transaction = "sell"
    elif good.goodType == "Gold":
        transaction = "buy"
    else:
        transaction = "trade"

    if good.costType == "Gold":
        cost = [str(good.costAmount), '0', '0', '0', '0']
    if good.costType == "Food":
        cost = ['0', str(good.costAmount), '0', '0', '0']
    if good.costType == "Wood":
        cost = ['0', '0', str(good.costAmount), '0', '0']
    if good.costType == "Stone":
        cost = ['0', '0', '0', str(good.costAmount), '0']
    if good.costType == "Ore":
        cost = ['0', '0', '0', '0', str(good.costAmount)]

    if transaction == "sell":
        time.sleep(0.5)
        if HaveEnoughResources(userStronghold, cost, 1):
            if AnswerYes("\n    Purchase " + WARNING + str(good.goodAmount) + " " + good.GetGoodColor() + str(good.goodType) + RESET + " for " + WARNING + str(good.costAmount) + good.GetCostColor() + " " + str(good.costType) + RESET + "?"):
                time.sleep(0.5)
                
                DeductResources(userStronghold, cost, 1)
                AddResources(userStronghold, str(good.goodType), int(good.goodAmount))

                userStronghold.write()
                userStronghold.read()
                
                if good.seller == "The Wandering Merchant":
                    #log it for buyer
                    logString = str(good.goodAmount) + ' ' + good.goodType + " bought from " + good.seller + ' for ' + str(good.costAmount) + ' gold.'
                    Log(logString, userStronghold.name)

                    pas_market_transactionComplete()
                else:
                    sellerStronghold = Stronghold()
                    sellerStronghold.name = str(good.seller)
                    sellerStronghold.read()
                    AddResourceByType(sellerStronghold, good.costType, good.costAmount)
                    sellerStronghold.write()
                    sellerStronghold.read()
                    print("\n    Transaction complete!\n")
                    
                    #log it
                    logString = str(good.goodAmount) + ' ' + good.goodType + " sold to " + userStronghold.name + ' for ' + str(good.costAmount) + ' gold.'
                    Log(logString, good.seller)
                    #log it for buyer
                    logString = str(good.goodAmount) + ' ' + good.goodType + " bought from " + good.seller + ' for ' + str(good.costAmount) + ' gold.'
                    Log(logString, userStronghold.name)

                time.sleep(0.5)
                nothing = input("\n    Press enter to continue.")
                return True

            else:
                print("\n    Cancelling request..\n")
                if good.seller == "The Wandering Merchant":
                    time.sleep(0.5)
                    pas_market_transactionCancelled()
                nothing = input("\n    Press enter to continue...")
                return False
        else:
            print("\n    Not enough resources!\n")
            if good.seller == "The Wandering Merchant":
                time.sleep(0.5)
                pas_market_notEnoughFunds()
            time.sleep(0.5)
            nothing = input("\n    Press enter to look elsewhere...")
            return False
    elif transaction == "buy":
        time.sleep(0.5)
        if HaveEnoughResources(userStronghold, cost, 1):
            if AnswerYes("\n    Sell " + WARNING + str(good.costAmount) + " " + good.GetCostColor() + str(good.costType) + RESET + " for " + WARNING + str(good.goodAmount) + good.GetGoodColor() + " " + str(good.goodType) + RESET + "?"):
                time.sleep(0.5)
                
                DeductResources(userStronghold, cost, 1)
                AddResources(userStronghold, str(good.goodType), int(good.goodAmount))

                userStronghold.write()
                userStronghold.read()
                
                if good.seller == "The Wandering Merchant":
                    pas_market_transactionComplete()
                    logString = str(good.costAmount) + ' ' + good.costType + " sold to " + good.seller + ' for ' + str(good.goodAmount) + ' gold.'
                    Log(logString, userStronghold.name)
                else:
                    sellerStronghold = Stronghold()
                    sellerStronghold.name = str(good.seller)
                    sellerStronghold.read()
                    AddResourceByType(sellerStronghold, good.costType, good.costAmount)
                    sellerStronghold.write()
                    sellerStronghold.read()

                    #log it for seller
                    logString = str(good.costAmount) + ' ' + good.costType + " sold to " + userStronghold.name + ' for ' + str(good.goodAmount) + ' gold.'
                    Log(logString, good.seller)
                    #log it for buyer
                    logString = str(good.costAmount) + ' ' + good.costType + " bought from " + good.seller + ' for ' + str(good.goodAmount) + ' gold.'
                    Log(logString, userStronghold.name)

                    print("\n    Transaction complete!\n")

                time.sleep(0.5)
                nothing = input("\n    Press enter to continue.")
                return True

            else:
                print("\n    Cancelling request..\n")
                if good.seller == "The Wandering Merchant":
                    time.sleep(0.5)
                    pas_market_transactionCancelled()
                nothing = input("\n    Press enter to continue...")
                return False
        else:
            print("\n    Not enough resources!\n")
            if good.seller == "The Wandering Merchant":
                time.sleep(0.5)
                pas_market_notEnoughFunds()
            time.sleep(0.5)
            nothing = input("\n    Press enter to look elsewhere...")
            return False
    else:
        time.sleep(0.5)
        if HaveEnoughResources(userStronghold, cost, 1):
            if AnswerYes("\n    Trade " + WARNING + str(good.costAmount) + " " + good.GetCostColor() + str(good.costType) + RESET + " for " + WARNING + str(good.goodAmount) + good.GetGoodColor() + " " + str(good.goodType) + RESET + "?"):
                time.sleep(0.5)
                
                DeductResources(userStronghold, cost, 1)
                AddResources(userStronghold, str(good.goodType), int(good.goodAmount))

                userStronghold.write()
                userStronghold.read()
                
                if good.seller == "The Wandering Merchant":

                    #log it for buyer
                    logString = str(good.costAmount) + ' ' + good.costType + " traded with " + good.seller + ' for ' + str(good.goodAmount) + ' ' + good.goodType
                    Log(logString, userStronghold.name)

                    pas_market_transactionComplete()
                else:
                    sellerStronghold = Stronghold()
                    sellerStronghold.name = str(good.seller)
                    sellerStronghold.read()
                    AddResourceByType(sellerStronghold, good.costType, good.costAmount)
                    sellerStronghold.write()
                    sellerStronghold.read()

                    #log it for buyer
                    logString = str(good.costAmount) + ' ' + good.costType + " traded with " + good.seller + ' for ' + str(good.goodAmount) + ' ' + good.goodType
                    Log(logString, userStronghold.name)

                    #log it for seller
                    logString = str(good.goodAmount) + ' ' + good.goodType + " traded with " + userStronghold.name + ' for ' + str(good.costAmount) + ' ' + good.costType
                    Log(logString, good.seller)

                    print("\n    Transaction complete!\n")

                time.sleep(0.5)
                nothing = input("\n    Press enter to continue.")
                return True

            else:
                print("\n    Cancelling request..\n")
                if good.seller == "The Wandering Merchant":
                    time.sleep(0.5)
                    pas_market_transactionCancelled()
                nothing = input("\n    Press enter to continue...")
                return False
        else:
            print("\n    Not enough resources!\n")
            if good.seller == "The Wandering Merchant":
                time.sleep(0.5)
                pas_market_notEnoughFunds()
            time.sleep(0.5)
            nothing = input("\n    Press enter to look elsewhere...")
            return False

#def Log(inputString, username):
# with open('logFile.log', 'a') as logFile:
#    from datetime import datetime
#    now = datetime.now()
#    current_time = now.strftime("%H:%M")
#    logFile.write('\n' + username + ' |--| Time: ' + current_time + ' |--| Event: ' + inputString)









#========================================================================================================
#   [IsPositiveIntEqualOrGreaterThan]
#   parameters: integer, amount
#   returns: True/False
#       Checks if passed integer is both positive and an integer and then if it is more than "amount"
#========================================================================================================
def IsPositiveIntEqualOrGreaterThan(integer, amount):
    if IsPositiveInteger(integer) == False:
        return False
    elif int(integer) < int(amount):
        return False
    else:
        return True




#========================================================================================================
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#========================================================================================================
#                                          Battalions
#========================================================================================================
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#========================================================================================================

#==================================================================================
#   [GetAnswer]
#   parameters: question, qType, comparable, cap
#       When passed a question, checks the type and compares it to the comparable
#       before eventually returning a proper result.
#==================================================================================
def GetAnswer(question, qType, comparable, cap):
    looping = True
    foundChar = False
    while looping:
        if qType == '>':
            response = input(question)
            if IsPositiveIntEqualOrGreaterThan(response, comparable):
                if cap != None:
                    if int(response) > int(cap):
                        print("    Error, can't be over " + str(cap) + "!")
                    else:
                        return response
                else:
                    return response
            else:
                print("    Input a positive integer equal to or greater than: " + str(comparable))
        elif qType == '<':
            response = input(question)
            if IsPositiveIntEqualOrLessThan(response, comparable):
                return response
            else:
                print("    Input a positive integer equal to or less than: " + str(comparable))
        elif qType == 'in':
            response = input(question)
            if response in comparable:
                return response
            else:
                print("    Choose a proper option from: " + str(*comparable))

        elif qType == 'legalString':
            response = input(question)
            if int(len(response)) <= int(cap):
                for i in range(len(ILLEGAL_USERNAMES)):
                    if str(ILLEGAL_USERNAMES[i]) == str(response):
                        print("    Error, not a legal input!")
                        return ""
                for i in range(len(ILLEGAL_CHARACTERS)):
                    for j in range(len(response)):
                        if response[j] == ILLEGAL_CHARACTERS[i]:
                            foundChar = True
                            badChar = response[j]
                            break
                    else:
                        continue
                    break
                if foundChar:
                    print("    Error, can't use " + str(badChar) + " in input!\n")
                else:
                    return response
            else:
                print("    Error, input can't be longer than " + str(cap) + " characters!\n")
        else:
            return ""

        

#==================================================================================
#   [CreateNewBattalion]
#   parameter: station
#       Makes a new battalion at the passed station
#==================================================================================
def CreateNewBattalion(station):
    if isinstance(station, Stronghold):
        os.system("clear")
        header(station.name)
        if int(station.defenders) < BATTALION_MIN:
            print("\n    You don't have enough warriors at this location to make a battalion!\n")
            nothing = input("    Press enter to continue : ")
            return "battalions"
        else:
            name = "Default Battalion"
            commander = str(station.ruler)
            numTroops = BATTALION_MIN
            attLevel = station.attLevel
            speed = 1
            stamina = 1
            rations = 0
            xPos = str(station.xCoordinate)
            yPos = str(station.yCoordinate)

            os.system("clear")
            header(station.name)
            print("\n    Creating New Battalion: \n")

            name = GetAnswer("    Name your Battalion: ", "legalString", None, BATTALION_NAME_CAP)
            if str(name) == "":
                return "battalions"
            if serverArmies.ExistingName(name):
                print("\n    Battalion name already taken!")
                nothing = input("    Press enter to continue : ")
                return "battalions"
            print("")
            numTroops = GetAnswer(str("    How many troops will you assign to " + WARNING + str(name) + RESET + "? [min " + str(BATTALION_MIN) + "]: "), ">", BATTALION_MIN, BATTALION_MAX)
            if int(numTroops) > int(station.defenders):
                print("    You don't have enough troops for this battalion!\n")
                nothing = input("    Press enter to continue : ")
                return "battalions"
            print("")

            serverArmies.AddBattalion(str(name), str(commander), str(numTroops), str(attLevel), str(speed), str(stamina), str(rations), str(xPos), str(yPos), 0, 0, 0, 0, 0)
            serverArmies.write()

            station.defenders = int(station.defenders) - int(numTroops)
            station.write()

            nothing = input("    Press enter to continue : ")
            return "battalions"

    else:
        os.system("clear")
        headerFief(station)
        if int(station.defenders) < BATTALION_MIN:
            print("\n    You don't have enough warriors at this location to make a battalion!\n")
            nothing = input("    Press enter to continue : ")
            return "battalions"
            
    return "battalions"


#==================================================================================
#   [CheckBiome]
#   parameter: surroundings, direction, haveRaft
#==================================================================================
def CheckBiome(biome, direction, haveRaft):
    #If the way is blocked by water:
    # if biome == WATER:
    #     print("    A body of " + IC_WATER + "water" + RESET + " blocks your path to the " + direction)
    #     return ""
    # if biome == RIVER[0]:
    #     print("    A Southwest-bound " + IC_RIVER + "river" + RESET + " blocks your path to the " + direction)
    #     return ""
    # if biome == RIVER[1]:
    #     print("    A South-bound " + IC_RIVER + "river" + RESET + " blocks your path to the " + direction)
    #     return ""
    # if biome == RIVER[2]:
    #     print("    A Southeast-bound " + IC_RIVER + "river" + RESET + " blocks your path to the " + direction)
    #     return ""

    #For testing purposes, add a "raft" attribute:
    if str(biome) == WATER:
        print("    Your troops raft through the " + IC_WATER + "water" + RESET + " to the " + str(direction))
        return ""
    if str(biome) == RIVER[0]:
        print("    Your troops raft over the Southwest-bound " + IC_RIVER + "river" + RESET + " to the " + str(direction))
        return ""
    if str(biome) == RIVER[1]:
        print("    Your troops raft over the South-bound " + IC_RIVER + "river" + RESET + " to the " + str(direction))
        return ""
    if str(biome) == RIVER[2]:
        print("    Your troops raft over the Southeast-bound " + IC_RIVER + "river" + RESET + " to the " + str(direction))
        return ""
    if str(biome) == MOUNTAIN:
        print("    Your troops travel over the " + IC_MOUNTAIN + "mountain" + RESET + " to the " + str(direction))
        return ""
    if str(biome) == FOREST:
        print("    Your troops travel through the " + IC_FOREST + "forest" + RESET + " to the " + str(direction))
        return ""
    if str(biome) == PLAINS:
        print("    Your troops travel through the " + IC_PLAINS + "plains" + RESET + " to the " + str(direction))
        return ""
    if str(biome) == FIEF:
        print("    Your troops travel to the " + IC_FIEF + "fief" + RESET + " to the " + str(direction))
    if str(biome) == STRONGHOLD:
        print("    Your troops travel to the " + IC_STRONGHOLD + "stronghold" + RESET + " to the " + str(direction))
        return ""
    
#==================================================================================
#   [MoveBattalion]
#   parameter: station, battalion
#       Moves the battalion based on direction
#==================================================================================
def MoveBattalion(station, battalion, direction):
    os.system("clear")
    headerBattalion(battalion, station, serverMap)
    raft = True #Change this later
    surroundings = ScanSurroundings(serverMap.worldMap, int(battalion.xPos), int(battalion.yPos))
    #[dN, dNE, dE, dSE, dS, dSW, dW, dNW]
    # print(*surroundings)
    if direction == 'n':
        check = CheckBiome(surroundings[0], 'north', raft)
    if direction == 'ne':
        check = CheckBiome(surroundings[1], 'northeast', raft)
    if direction == 'e':
        check = CheckBiome(surroundings[2], 'east', raft)
    if direction == 'se':
        check = CheckBiome(surroundings[3], 'southeast', raft)
    if direction == 's':
        check = CheckBiome(surroundings[4], 'south', raft)
    if direction == 'sw':
        check = CheckBiome(surroundings[5], 'southwest', raft)
    if direction == 'w':
        check = CheckBiome(surroundings[6], 'west', raft)
    if direction == 'nw':
        check = CheckBiome(surroundings[7], 'northwest', raft)

    Wait()
    
    #Later use 'check' here to make sure a raft exists or something
    serverArmies.SetBattalionCoords(battalion, direction)


#==================================================================================
#   [AvailableDirections]
#   parameter: battalion
#   returns: list of directions based on map constraints
#==================================================================================
def AvailableDirections(currentBattalion):
    if int(currentBattalion.xPos) > 0 and int(currentBattalion.xPos) < MAP_WIDTH and int(currentBattalion.yPos) > 0 and int(currentBattalion.yPos) < MAP_HEIGHT:
        directions = ['n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw']
        print('    {NW} {N} {NE}')
        print('    {W}       {E}')
        print('    {SW} {S} {SE}')
    elif int(currentBattalion.xPos) == 0 and int(currentBattalion.yPos) > 0 and int(currentBattalion.yPos) < MAP_HEIGHT:
        directions = ['n', 'ne', 'e', 'se', 's']
        print('    {X} {N} {NE}')
        print('    {X}      {E}')
        print('    {X} {S} {SE}')
    elif int(currentBattalion.xPos) == MAP_WIDTH and int(currentBattalion.yPos) > 0 and int(currentBattalion.yPos) < MAP_HEIGHT:
        directions = ['n', 's', 'sw', 'w', 'nw']
        print('    {NW} {N} {X}')
        print('    {W}      {X}')
        print('    {SW} {S} {X}')
    elif int(currentBattalion.xPos) > 0 and int(currentBattalion.xPos) < MAP_WIDTH and int(currentBattalion.yPos) == 0:
        directions = ['e', 'se', 's', 'sw', 'w']
        print('    {X}  {X}  {X}')
        print('    {W}       {E}')
        print('    {SW} {S} {SE}')
    elif int(currentBattalion.xPos) > 0 and int(currentBattalion.xPos) < MAP_WIDTH and int(currentBattalion.yPos) == MAP_HEIGHT:
        directions = ['n', 'ne', 'e', 'w', 'nw']
        print('    {NW} {N} {NE}')
        print('    {W}       {E}')
        print('    {X}  {X}  {X}')
    elif int(currentBattalion.xPos) == MAP_WIDTH and int(currentBattalion.yPos) == MAP_HEIGHT:
        directions = ['n', 'w', 'nw']
        print('    {NW} {N}  {X}')
        print('    {W}       {X}')
        print('    {X}  {X}  {X}')
    elif int(currentBattalion.xPos) == 0 and int(currentBattalion.yPos) == 0:
        directions = ['e', 'se', 's']
        print('    {X} {X}  {X}')
        print('    {X}      {E}')
        print('    {X} {S} {SE}')
    elif int(currentBattalion.xPos) == MAP_WIDTH and int(currentBattalion.yPos) == 0:
        directions = ['s', 'sw', 'w']
        print('    {X}  {X} {X}')
        print('    {W}      {X}')
        print('    {SW} {S} {X}')
    elif int(currentBattalion.xPos) == 0 and int(currentBattalion.yPos) == MAP_HEIGHT:
        directions = ['n', 'ne', 'e']
        print('    {X} {N} {NE}')
        print('    {X}      {E}')
        print('    {X} {X}  {X}')
    
    return directions

