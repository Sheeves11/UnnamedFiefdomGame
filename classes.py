# from _typeshed import ReadableBuffer
import os
import time
import random
from colors import *

#============================
#  UNIT RESOURCE MODIFIERS
#============================
HUNTER_FOOD_MOD = 2     #Use this to balance hunter food generation

# For VENDOR_GOLD_PER_HOUR:
# Max vendors is currently 5 per farm
# This amount of gold is doubled at max rank
# With 8 fully upgraded farms, you can get 40 vendors. 
# With 40 vendors, you can fetch 4k gold/hr if the value below is 50
VENDOR_GOLD_PER_HOUR = 50

#============================


#this is the d20 roll function
def roll(mod):
    d20 = random.randint(1, 20)
    return d20 + mod

#define biome globals:
WATER = '~'
RIVER = ['/','|','\\']
MOUNTAIN = 'M'
PLAINS = '#'
FOREST = '^'
BACKSLASH_SUB = 'L'     #This needed to be added so the program could properly read/write '\'

def biomeColor(biome):
    if biome == MOUNTAIN:
        return textColor.DARK_GRAY
    elif biome == FOREST:
        return textColor.GREEN
    elif biome == PLAINS:
        return textColor.YELLOW
    
#the fiefdom class holds variables that define a player's stats
class Fiefdom:
    name = 'Default Fiefdom'
    ruler = 'Unclaimed'
    home = False
    defenders = 100
    gold = 500
    wood = 0
    stone = 0
    food = 0
    ore = 0
    defLevel = 0
    defType = "Open Camp"
    attLevel = 0
    attType = "Angry Mob"
    goldMod = '1'
    defenderMod = '1'
    farmType = "Dirt Patch"
    thieves = 0
    biome = '0'
    xCoordinate = 0
    yCoordinate = 0
    adjacentWater = 0
    adjacentRivers = 0
    adjacentMountains = 0
    adjacentForests = 0
    adjacentPlains = 0
    strongholdMessage = 'Message Not Set'

    op_farmlandTier = 0
    op_farmlandPrimaryPer = 0
    op_farmlandSecondaryPer = 0
    op_farmlandPrimaryUnits = 0
    op_farmlandSecondaryUnits = 0
    op_farmlandNumBuilt = 0
    op_fisheryTier = 0
    op_fisheryPrimaryPer = 0
    op_fisherySecondaryPer = 0
    op_fisheryPrimaryUnits = 0
    op_fisherySecondaryUnits = 0
    op_fisheryNumBuilt = 0
    op_lumberMillTier = 0
    op_lumberMillPrimaryPer = 0
    op_lumberMillSecondaryPer = 0
    op_lumberMillPrimaryUnits = 0
    op_lumberMillSecondaryUnits = 0
    op_lumberMillNumBuilt = 0
    op_mineTier = 0
    op_minePrimaryPer = 0
    op_mineSecondaryPer = 0
    op_minePrimaryUnits = 0
    op_mineSecondaryUnits = 0
    op_mineNumBuilt = 0

    

    #take the current fiefdom and write it to the /fiefs directory
    def write(self):
        fiefFile = 'fiefs/' + self.name + '.txt'
        
        #this part creates a file if it isn't made yet        
        try:
            with open(fiefFile, 'x') as f:
                f.write(self.name + '\n')
                f.write(self.ruler + '\n')
                f.write(str(self.home) + '\n')
                f.write(str(self.defenders) + '\n')
                f.write(str(self.gold) + '\n')
                f.write(str(self.wood) + '\n')
                f.write(str(self.stone) + '\n')
                f.write(str(self.food) + '\n')
                f.write(str(self.ore) + '\n')
                f.write(str(self.defLevel) + '\n')
                f.write(str(self.defType) + '\n')
                f.write(str(self.attLevel) + '\n')
                f.write(str(self.attType) + '\n')
                f.write(str(self.goldMod) + '\n')
                f.write(str(self.defenderMod) + '\n')
                f.write(str(self.farmType) + '\n')
                f.write(str(self.thieves) + '\n')
                f.write(str(self.biome) + '\n')
                f.write(str(self.xCoordinate) + '\n')
                f.write(str(self.yCoordinate) + '\n')
                f.write(str(self.adjacentWater) + '\n')
                f.write(str(self.adjacentRivers) + '\n')
                f.write(str(self.adjacentMountains) + '\n')
                f.write(str(self.adjacentForests) + '\n')
                f.write(str(self.adjacentPlains) + '\n')
                f.write(str(self.strongholdMessage) + '\n')
                f.write(str(self.op_farmlandTier) + '\n')
                f.write(str(self.op_farmlandPrimaryPer) + '\n')
                f.write(str(self.op_farmlandSecondaryPer) + '\n')
                f.write(str(self.op_farmlandPrimaryUnits) + '\n')
                f.write(str(self.op_farmlandSecondaryUnits) + '\n')
                f.write(str(self.op_farmlandNumBuilt) + '\n')
                f.write(str(self.op_fisheryTier) + '\n')
                f.write(str(self.op_fisheryPrimaryPer) + '\n')
                f.write(str(self.op_fisherySecondaryPer) + '\n')
                f.write(str(self.op_fisheryPrimaryUnits) + '\n')
                f.write(str(self.op_fisherySecondaryUnits) + '\n')
                f.write(str(self.op_fisheryNumBuilt) + '\n')
                f.write(str(self.op_lumberMillTier) + '\n')
                f.write(str(self.op_lumberMillPrimaryPer) + '\n')
                f.write(str(self.op_lumberMillSecondaryPer) + '\n')
                f.write(str(self.op_lumberMillPrimaryUnits) + '\n')
                f.write(str(self.op_lumberMillSecondaryUnits) + '\n')
                f.write(str(self.op_lumberMillNumBuilt) + '\n')
                f.write(str(self.op_mineTier) + '\n')
                f.write(str(self.op_minePrimaryPer) + '\n')
                f.write(str(self.op_mineSecondaryPer) + '\n')
                f.write(str(self.op_minePrimaryUnits) + '\n')
                f.write(str(self.op_mineSecondaryUnits) + '\n')
                f.write(str(self.op_mineNumBuilt) + '\n')

        except:
            pass

        #write the class variables down line by line in the text file
        try:
            with open(fiefFile, 'w') as f:
                f.write(self.name + '\n')
                f.write(self.ruler + '\n')
                f.write(str(self.home) + '\n')
                f.write(str(self.defenders) + '\n')
                f.write(str(self.gold) + '\n')
                f.write(str(self.wood) + '\n')
                f.write(str(self.stone) + '\n')
                f.write(str(self.food) + '\n')
                f.write(str(self.ore) + '\n')
                f.write(str(self.defLevel) + '\n')
                f.write(str(self.defType) + '\n')
                f.write(str(self.attLevel) + '\n')
                f.write(str(self.attType) + '\n')
                f.write(str(self.goldMod) + '\n')
                f.write(str(self.defenderMod) + '\n')
                f.write(str(self.farmType) + '\n')
                f.write(str(self.thieves) + '\n')
                f.write(str(self.biome) + '\n')
                f.write(str(self.xCoordinate) + '\n')
                f.write(str(self.yCoordinate) + '\n')
                f.write(str(self.adjacentWater) + '\n')
                f.write(str(self.adjacentRivers) + '\n')
                f.write(str(self.adjacentMountains) + '\n')
                f.write(str(self.adjacentForests) + '\n')
                f.write(str(self.adjacentPlains) + '\n')
                f.write(str(self.strongholdMessage) + '\n')
                f.write(str(self.op_farmlandTier) + '\n')
                f.write(str(self.op_farmlandPrimaryPer) + '\n')
                f.write(str(self.op_farmlandSecondaryPer) + '\n')
                f.write(str(self.op_farmlandPrimaryUnits) + '\n')
                f.write(str(self.op_farmlandSecondaryUnits) + '\n')
                f.write(str(self.op_farmlandNumBuilt) + '\n')
                f.write(str(self.op_fisheryTier) + '\n')
                f.write(str(self.op_fisheryPrimaryPer) + '\n')
                f.write(str(self.op_fisherySecondaryPer) + '\n')
                f.write(str(self.op_fisheryPrimaryUnits) + '\n')
                f.write(str(self.op_fisherySecondaryUnits) + '\n')
                f.write(str(self.op_fisheryNumBuilt) + '\n')
                f.write(str(self.op_lumberMillTier) + '\n')
                f.write(str(self.op_lumberMillPrimaryPer) + '\n')
                f.write(str(self.op_lumberMillSecondaryPer) + '\n')
                f.write(str(self.op_lumberMillPrimaryUnits) + '\n')
                f.write(str(self.op_lumberMillSecondaryUnits) + '\n')
                f.write(str(self.op_lumberMillNumBuilt) + '\n')
                f.write(str(self.op_mineTier) + '\n')
                f.write(str(self.op_minePrimaryPer) + '\n')
                f.write(str(self.op_mineSecondaryPer) + '\n')
                f.write(str(self.op_minePrimaryUnits) + '\n')
                f.write(str(self.op_mineSecondaryUnits) + '\n')
                f.write(str(self.op_mineNumBuilt) + '\n')
        except:
            pass

    #read class variables line by line
    def read(self):
        fiefFile = 'fiefs/' + self.name + '.txt'
        try:
            with open(fiefFile, 'r') as f:
                self.name = f.readline().strip()
                self.ruler = f.readline().strip()
                self.home = f.readline().strip()
                self.defenders = f.readline().strip()
                self.gold = f.readline().strip()
                self.wood = f.readline().strip()
                self.stone = f.readline().strip()
                self.food = f.readline().strip()
                self.ore = f.readline().strip()
                self.defLevel = f.readline().strip()
                self.defType = f.readline().strip()
                self.attLevel = f.readline().strip()
                self.attType = f.readline().strip()
                self.goldMod = f.readline().strip()
                self.defenderMod = f.readline().strip()
                self.farmType = f.readline().strip()
                self.thieves = f.readline().strip()
                self.biome = f.readline().strip()
                self.xCoordinate = f.readline().strip()
                self.yCoordinate = f.readline().strip()
                self.adjacentWater = f.readline().strip()
                self.adjacentRivers = f.readline().strip()
                self.adjacentMountains = f.readline().strip()
                self.adjacentForests = f.readline().strip()
                self.adjacentPlains = f.readline().strip()
                self.strongholdMessage = f.readline().strip()
                self.op_farmlandTier = f.readline().strip()
                self.op_farmlandPrimaryPer = f.readline().strip()
                self.op_farmlandSecondaryPer = f.readline().strip()
                self.op_farmlandPrimaryUnits = f.readline().strip()
                self.op_farmlandSecondaryUnits = f.readline().strip()
                self.op_farmlandNumBuilt = f.readline().strip()
                self.op_fisheryTier = f.readline().strip()
                self.op_fisheryPrimaryPer = f.readline().strip()
                self.op_fisherySecondaryPer = f.readline().strip()
                self.op_fisheryPrimaryUnits = f.readline().strip()
                self.op_fisherySecondaryUnits = f.readline().strip()
                self.op_fisheryNumBuilt = f.readline().strip()
                self.op_lumberMillTier = f.readline().strip()
                self.op_lumberMillPrimaryPer = f.readline().strip()
                self.op_lumberMillSecondaryPer = f.readline().strip()
                self.op_lumberMillPrimaryUnits = f.readline().strip()
                self.op_lumberMillSecondaryUnits = f.readline().strip()
                self.op_lumberMillNumBuilt = f.readline().strip()
                self.op_mineTier = f.readline().strip()
                self.op_minePrimaryPer = f.readline().strip()
                self.op_mineSecondaryPer = f.readline().strip()
                self.op_minePrimaryUnits = f.readline().strip()
                self.op_mineSecondaryUnits = f.readline().strip()
                self.op_mineNumBuilt = f.readline().strip()

        except:
            self.write()   

    def setCoordinates(self, coordinates):
        self.yCoordinate = coordinates[0]
        self.xCoordinate = coordinates[1]

    def setSurroundings(self, surroundings):
        for i in range(len(surroundings)):
            if surroundings[i] == WATER:
                self.adjacentWater = str(int(self.adjacentWater) + 1)
            elif surroundings[i] == RIVER[0] or surroundings[i] == RIVER[1] or surroundings[i] == RIVER[2]:
                self.adjacentRivers = str(int(self.adjacentRivers) + 1)
            elif surroundings[i] == PLAINS:
                self.adjacentPlains = str(int(self.adjacentPlains) + 1)
            elif surroundings[i] == MOUNTAIN:
                self.adjacentMountains = str(int(self.adjacentMountains) + 1)
            elif surroundings[i] == FOREST:
                self.adjacentForests = str(int(self.adjacentForests) + 1)

    def GetPrimaryPer(self, outpost):
        if outpost == "farmland":
            return int(self.op_farmlandPrimaryUnits) * (int(self.op_farmlandTier) + 1)
        if outpost == "fishery":
            return int(self.op_fisheryPrimaryUnits) * (int(self.op_fisheryTier) + 1)
        if outpost == "lumberMill":
            return int(self.op_lumberMillPrimaryUnits) * (int(self.op_lumberMillTier) + 1)
        if outpost == "mine":
            return int(self.op_minePrimaryUnits) * (int(self.op_mineTier) + 1)

    def GetSecondaryPer(self, outpost):
        if outpost == "farmland":
            return int(self.op_farmlandSecondaryUnits) * int(self.op_farmlandTier) * VENDOR_GOLD_PER_HOUR
        if outpost == "lumberMill":
            return int(self.op_lumberMillSecondaryUnits) * int(self.op_lumberMillTier) * HUNTER_FOOD_MOD
        if outpost == "mine":
            return int(self.op_mineSecondaryUnits) * int(self.op_mineTier)
        
            
#SW: I am splitting this to safely determine if it is necessary to keep the above stuff or not
class Stronghold:
    name = 'Default Stronghold'
    ruler = 'Unclaimed'
    home = False
    defenders = 100
    gold = 500
    wood = 0
    stone = 0
    food = 0
    ore = 0
    defLevel = 0
    defType = "Open Camp"
    attLevel = 0
    attType = "Angry Mob"
    goldMod = '1'
    defenderMod = '1'
    farmType = "Dirt Patch"
    thieves = 0
    biome = '0'
    xCoordinate = 0
    yCoordinate = 0
    color = 'red'
    strongholdMessage = 'message not set'

    #take the current stronghold and write it to the /strongholds directory
    def write(self):
        strongholdFile = 'strongholds/' + self.name + '.txt'
        
        #this part creates a file if it isn't made yet        
        try:
            with open(strongholdFile, 'x') as f:
                f.write(self.name + '\n')
                f.write(self.ruler + '\n')
                f.write(str(self.home) + '\n')
                f.write(str(self.defenders) + '\n')
                f.write(str(self.gold) + '\n')
                f.write(str(self.wood) + '\n')
                f.write(str(self.stone) + '\n')
                f.write(str(self.food) + '\n')
                f.write(str(self.ore) + '\n')
                f.write(str(self.defLevel) + '\n')
                f.write(str(self.defType) + '\n')
                f.write(str(self.attLevel) + '\n')
                f.write(str(self.attType) + '\n')
                f.write(str(self.goldMod) + '\n')
                f.write(str(self.defenderMod) + '\n')
                f.write(str(self.farmType) + '\n')
                f.write(str(self.thieves) + '\n')
                f.write(str(self.biome) + '\n')
                f.write(str(self.xCoordinate) + '\n')
                f.write(str(self.yCoordinate) + '\n')
                f.write(str(self.color) + '\n')
                f.write(str(self.strongholdMessage) + '\n')
        except:
            pass

        #write the class variables down line by line in the text file
        try:
            with open(strongholdFile, 'w') as f:
                f.write(self.name + '\n')
                f.write(self.ruler + '\n')
                f.write(str(self.home) + '\n')
                f.write(str(self.defenders) + '\n')
                f.write(str(self.gold) + '\n')
                f.write(str(self.wood) + '\n')
                f.write(str(self.stone) + '\n')
                f.write(str(self.food) + '\n')
                f.write(str(self.ore) + '\n')
                f.write(str(self.defLevel) + '\n')
                f.write(str(self.defType) + '\n')
                f.write(str(self.attLevel) + '\n')
                f.write(str(self.attType) + '\n')
                f.write(str(self.goldMod) + '\n')
                f.write(str(self.defenderMod) + '\n')
                f.write(str(self.farmType) + '\n')
                f.write(str(self.thieves) + '\n')
                f.write(str(self.biome) + '\n')
                f.write(str(self.xCoordinate) + '\n')
                f.write(str(self.yCoordinate) + '\n')
                f.write(str(self.color) + '\n')
                f.write(str(self.strongholdMessage) + '\n')
        except:
            pass

    #read class variables line by line
    def read(self):
        strongholdFile = 'strongholds/' + self.name + '.txt'
        try:
            with open(strongholdFile, 'r') as f:
                self.name = f.readline().strip()
                self.ruler = f.readline().strip()
                self.home = f.readline().strip()
                self.defenders = f.readline().strip()
                self.gold = f.readline().strip()
                self.wood = f.readline().strip()
                self.stone = f.readline().strip()
                self.food = f.readline().strip()
                self.ore = f.readline().strip()
                self.defLevel = f.readline().strip()
                self.defType = f.readline().strip()
                self.attLevel = f.readline().strip()
                self.attType = f.readline().strip()
                self.goldMod = f.readline().strip()
                self.defenderMod = f.readline().strip()
                self.farmType = f.readline().strip()
                self.thieves = f.readline().strip()
                self.biome = f.readline().strip()
                self.xCoordinate = f.readline().strip()
                self.yCoordinate = f.readline().strip()
                self.color = f.readline().strip()
                self.strongholdMessage = f.readline().strip()
        except:
            self.write()     

    def setCoordinates(self, coordinates):
        self.yCoordinate = coordinates[0]
        self.xCoordinate = coordinates[1]


class Map:
    seed = '00555'
    name = 'default'
    width = 5
    height = 5
    
    numWater = 0
    numRivers = 0
    numPlains = 0
    numForests = 0
    numMountains = 0
    
    usedPlains = 0
    usedForests = 0
    usedMountains = 0

    values = []
    worldMap = []

    success = False #Temporary bool
    #--------------------------------------------------------------------------------------------------------------
    #   Writes a map file as a 2-d list like so:
    #   [['seed'], ['width'], ['height'], ['numWater'], ['numRivers'], ['numPlains'], ['numForests'], 
    #   ['numMountains'], ['usedPlains'], ['usedForests'], ['usedMountains'], ['worldMap ROW 1'], [worldMap ROW 2], 
    #   [worldMap ROW 3], [...], [worldMap ROW height]
    #--------------------------------------------------------------------------------------------------------------
    def write(self):
        mapFile = 'map/' + self.name + '.txt'
        
        #this part creates a file if it isn't made yet. SW: This has not been tested.
        try:
            with open(mapFile, 'x') as f:
                f.write(str("["))
                f.write("['" + str(self.seed) + "'],")
                f.write("['" + str(self.width) + "'],")
                f.write("['" + str(self.height) + "'],")
                f.write("['" + str(self.numWater) + "'],")
                f.write("['" + str(self.numRivers) + "'],")
                f.write("['" + str(self.numPlains) + "'],")
                f.write("['" + str(self.numForests) + "'],")
                f.write("['" + str(self.numMountains) + "'],")
                f.write("['" + str(self.usedPlains) + "'],")
                f.write("['" + str(self.usedForests) + "'],")
                f.write("['" + str(self.usedMountains) + "'],")
                for i in range(int(self.height)):
                    f.write(str("["))
                    for j in range(int(self.width)):
                        if j < int(self.width) - 1:
                            if self.worldMap[i][j] == RIVER[2]:
                                f.write("'" + BACKSLASH_SUB + "',")
                            else:
                                f.write("'" + str(self.worldMap[i][j]) + "',")
                        else:
                            if self.worldMap[i][j] == RIVER[2]:
                                f.write("'" + BACKSLASH_SUB + "'")
                            else:
                                f.write("'" + str(self.worldMap[i][j]) + "'")
                    if i < int(self.height) - 1:
                        f.write(str("],"))
                    else:
                        f.write(str("]"))
                f.write(str("]"))
        except:
            pass

        #write the class variables down line by line in the text file
        try:
            with open(mapFile, 'w') as f:
                f.write(str("["))
                f.write("['" + str(self.seed) + "'],")
                f.write("['" + str(self.width) + "'],")
                f.write("['" + str(self.height) + "'],")
                f.write("['" + str(self.numWater) + "'],")
                f.write("['" + str(self.numRivers) + "'],")
                f.write("['" + str(self.numPlains) + "'],")
                f.write("['" + str(self.numForests) + "'],")
                f.write("['" + str(self.numMountains) + "'],")
                f.write("['" + str(self.usedPlains) + "'],")
                f.write("['" + str(self.usedForests) + "'],")
                f.write("['" + str(self.usedMountains) + "'],")
                for i in range(int(self.height)):
                    f.write(str("["))
                    for j in range(int(self.width)):
                        if j < int(self.width) - 1:
                            if self.worldMap[i][j] == RIVER[2]:
                                f.write("'" + BACKSLASH_SUB + "',")
                            else:
                                f.write("'" + str(self.worldMap[i][j]) + "',")
                        else:
                            if self.worldMap[i][j] == RIVER[2]:
                                f.write("'" + BACKSLASH_SUB + "'")
                            else:
                                f.write("'" + str(self.worldMap[i][j]) + "'")
                    if i < int(self.height) - 1:
                        f.write(str("],"))
                    else:
                        f.write(str("]"))
                f.write(str("]"))
        except:
            pass

    #--------------------------------------------------------------------------------------------------------------
    #   Opens the map file and reads the whole thing into the variable "readList" before closing it.
    #   The first 11 variables are stored in a "values" array for sorting into appropriate variables.
    #   Then, each row of the map is loaded into the worldMap 2d-list.
    #--------------------------------------------------------------------------------------------------------------
    def read(self):
        mapFile = 'map/' + self.name + '.txt'
        try:
            readMapFile = open(mapFile, 'r')
            readList = eval(readMapFile.read())
            readMapFile.close()
            self.worldMap = []  #Needs to clear the world map if anything happened to be in there before reading.
            for count in range(len(readList)):
                if count <= 10:
                    self.values.append(readList[count])
                    
                if count > 10:
                    for i in range(len(readList[count])):
                        if readList[count][i] == BACKSLASH_SUB:
                            readList[count][i] = RIVER[2]
                    self.worldMap.append(readList[count])

            self.success = True

        except:
            print('Could not read map file!')
            pass

        if self.success == True:
            self.seed = str(self.values[0]).lstrip("['").rstrip("']")
            self.width = str(self.values[1]).lstrip("['").rstrip("']")
            self.height = str(self.values[2]).lstrip("['").rstrip("']")
            self.numWater = str(self.values[3]).lstrip("['").rstrip("']")
            self.numRivers = str(self.values[4]).lstrip("['").rstrip("']")
            self.numPlains = str(self.values[5]).lstrip("['").rstrip("']")
            self.numForests = str(self.values[6]).lstrip("['").rstrip("']")
            self.numMountains = str(self.values[7]).lstrip("['").rstrip("']")
            self.usedPlains = str(self.values[8]).lstrip("['").rstrip("']")
            self.usedForests = str(self.values[9]).lstrip("['").rstrip("']")
            self.usedMountains = str(self.values[10]).lstrip("['").rstrip("']")

    def selfDiagnostic(self):
        print('Running diagnostic on map class...')
        print('Current attributes are: ')
        print('name: ' + str(self.name))
        print('seed: ' + str(self.seed))
        print('width: ' + str(self.width))
        print('height: ' + str(self.height))
        print('numWater: ' + str(self.numWater))
        print('numRivers: ' + str(self.numRivers))
        print('numPlains: ' + str(self.numPlains))
        print('numForests: ' + str(self.numForests))
        print('numMountains: ' + str(self.numMountains))
        print('usedPlains: ' + str(self.usedPlains))
        print('usedForests: ' + str(self.usedForests))
        print('usedMountains: ' + str(self.usedMountains))


#eof
