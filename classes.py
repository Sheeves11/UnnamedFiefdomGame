# from _typeshed import ReadableBuffer
import os
import time
import random

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

#define some text colors
class textColor:
    RED = '\033[91m'
    GREEN = '\033[92m'
    RESET = '\033[0m'
    DIM = '\033[2m'
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    WARNING = '\033[93m'
    YELLOW = '\033[33m'
    DARK_GRAY = '\033[90m'
    LIGHT_GRAY = '\033[37m'
    PURPLE = "\033[0;95m"
    ORANGE = "\u001b[38;5;208m"
    BROWN = "\u001b[38;5;216m"
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def biomeColor(biome):
    if biome == MOUNTAIN:
        return textColor.DARK_GRAY
    elif biome == FOREST:
        return textColor.GREEN
    elif biome == PLAINS:
        return textColor.YELLOW

def strongholdColor(color):
    if color == 'red':
        return textColor.RED
    if color == 'green':
        return textColor.GREEN
    if color == 'magenta':
        return textColor.MAGENTA
    if color == 'white':
        return textColor.BOLD
    if color == 'blue':
        return textColor.BLUE
    if color == 'yellow':
        return textColor.YELLOW
    if color == 'cyan':
        return textColor.CYAN
    if color == 'gray':
        return textColor.DARK_GRAY

    


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

        except:
            self.write()   
    def setCoordinates(self, coordinates):
        self.yCoordinate = coordinates[0]
        self.xCoordinate = coordinates[1]

    def setSurroundings(self, surroundings):
        for i in range(len(surroundings)):
            if surroundings[i] == WATER:
                self.adjacentWater += 1
            elif surroundings[i] == RIVER[0] or surroundings[i] == RIVER[1] or surroundings[i] == RIVER[2]:
                self.adjacentRivers += 1
            elif surroundings[i] == PLAINS:
                self.adjacentPlains += 1
            elif surroundings[i] == MOUNTAIN:
                self.adjacentMountains += 1
            elif surroundings[i] == FOREST:
                self.adjacentForests += 1
            
#SW: I am splitting this to safely determine if it is necessary to keep the above stuff or not
class Stronghold:
    name = 'Default Stronghold'
    ruler = 'Unclaimed'
    home = False
    defenders = 100
    gold = 500
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
                            f.write("'" + str(self.worldMap[i][j]) + "',")
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
                            f.write("'" + str(self.worldMap[i][j]) + "',")
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
                    self.worldMap.append(readList[count])

            self.success = True

        except:
            print('Could not read file!')
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
            # print('seed: ' + str(self.seed))
            # print('width: ' + str(self.width))
            # print('height: ' + str(self.height))
            # print('numWater: ' + str(self.numWater))
            # print('numPlains: ' + str(self.numPlains))
            # print('numForests: ' + str(self.numForests))
            # print('numMountains: ' + str(self.numMountains))
            # print('usedPlains: ' + str(self.usedPlains))
            # print('usedForests: ' + str(self.usedForests))
            # print('usedMountains: ' + str(self.usedMountains))

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
        # print('worldMap:')
        # print(*self.worldMap)

#eof
