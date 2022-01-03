import os
import time
import random
from classes import *

#--------------------------------------------------------------------------------------------------------------
#
#   This is a very early development build for a world map feature.
#
#--------------------------------------------------------------------------------------------------------------

#Color definitions. Had to pull these out of classes to make stuff work! Temp fix!
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
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

#Global variables
MAP_WIDTH = 30
MAP_HEIGHT = 30
DEFAULT_WEIGHT = 10     #A common weight total
WEIGHT_INTENSITY = 5    #Higher the number, the more focused the map will be
RANDOM_INTENSITY = 20   #Higher the number, the more chaotic the map will be
INSTANTLY_GENERATE = False
AUTOMATED = False
FIRST_PRINT = True
LOADING_INCREMENT = 0

#Map Icons
WATER = '~'
RIVER = '|'
MOUNTAIN = 'M'
PLAINS = '#'
FOREST = '^'
FIEF = 'X'
STRONGHOLD = 'H'
EMPTY = ' '
UNEXPLORED = '0'
RANDOM = '*'

#Map Icon Color
IC_WATER = BLUE
IC_RIVER = BLUE
IC_MOUNTAIN = DARK_GRAY
IC_PLAINS = YELLOW
IC_FOREST = GREEN
IC_FIEF = RED
IC_STRONGHOLD = BOLD
IC_UNEXPLORED = WARNING

#--------------------------------------------------------------------------------------------------------------
#   [GenerateWorldMap]
#   Parameters: seed
#
#   This is the primary function for generating a world map
#   Utilizes a passed 'seed' value that alters how the map is generated
#   The algorithm for generating the map should do the following:
#      1. Begin at a coordinate within a 2D-list
#      2. Write a character on the map
#      3. Move to new location based on current location
#      4. Determine a character to write based on adjacent locations
#      5. Loop through steps 2-4 until map is filled (unique cases aside)
#
#   To make the starting location not matter, the algorithm should scan
#   all adjacent areas to the current coordinate before deciding on a char
#   to write. If no char can be found, the algo should IDEALLY pick a random location
#   and try again. If it comes down to it, a manual scan from coordinate [0,0] onward
#   should be performed so no spaces are left unmarked. Additionally, this adjacency 
#   check should also check diagonal coordinates so that corners are not bottle-necked
#   and ignored. That should increase speed and efficiency.
#   
#   Fief locations will be determined later, but I'd like to have something that detects
#   the name of the fief and picks a location if it, say, has "Forest" in the name. More
#   on that later.
#
#   Algorithm is improvable. Has time-complexity over O(n^2)!
#--------------------------------------------------------------------------------------------------------------
def GenerateWorldMap(seed):
    os.system('clear')

    #Pull globals into this function and reset them:
    global AUTOMATED
    global INSTANTLY_GENERATE
    global FIRST_PRINT
    INSTANTLY_GENERATE = False
    AUTOMATED = False
    FIRST_PRINT = True

    #Define world map and set variables based on seed value:
    worldMap = [['0' for x in range(MAP_WIDTH)] for y in range(MAP_HEIGHT)]
    sPosX = int(seed[0])    #ToDo: Make this coordinate matter
    sPosY = int(seed[1])    #ToDo: Make this coordinate matter
    freqMountain = int(seed[2])
    freqPlains = int(seed[3])
    freqForest = int(seed[4])
    
    loop = True
    firstLoop = True

    #Print title, blank map, etc.
    print('World Map Devtool')
    print('worldMap before inserting anything: \n')
    print(worldMap)
    print('\n')
    print('Inserting stuff into worldMap: \n')

    while (loop):                                   #This should keep going until the map is filled (currently loops once)
        if firstLoop:                               #Check if this is the first loop (for coordinate stuff later)
            for y in range(MAP_HEIGHT):             #Iterate through each row of the map
                for x in range(MAP_WIDTH):          #Iterate through each symbol in the row
                    #Set the symbol at this location based on surroundings:
                    worldMap[y][x] = DefineSurroundings(worldMap, x, y, freqMountain, freqPlains, freqForest)

            firstLoop = False                       #First loop is done

        loop = False                                #Map should be complete, stop looping.

    print('\nFinished!')

    return worldMap

#--------------------------------------------------------------------------------------------------------------
#   [DefineSurroundings]
#   Parameters: wMap, posX, posY, freqM, freqP, freqF
#
#   Iterates through the map given the map itself and a set of 
#   values to determine what to write in the next position.
#   ToDo I don't think symb is actually necessary, as it is just the last
#   thing drawn... which should be in the surrounding area.
#   This function could likely benefit from reaching two spaces out instead of just 1, but
#   that would make it far more complex. 
#--------------------------------------------------------------------------------------------------------------
def DefineSurroundings(wMap, posX, posY, freqM, freqP, freqF):
    global AUTOMATED
    global INSTANTLY_GENERATE
    global FIRST_PRINT
    
    #Create points that are surrounding our current position
    #Prints each position at the top of the page:
    if not INSTANTLY_GENERATE:
        os.system("clear")
        print('posX: ' + str(posX) + ' posY: ' + str(posY))
        try:
            dN = wMap[posY - 1][posX]
            print('There is a ' + dN + ' to the north!')
        except:
            dN = ' '
            print('North is off the map!')
        try:
            dNE = wMap[posY - 1][posX + 1]
            print('There is a ' + dNE + ' to the northeast!')
        except:
            dNE = ' '
            print('Northeast is off the map!')
        try:
            dE = wMap[posY][posX + 1]
            print('There is a ' + dE + ' to the east!')
        except:
            dE = ' '
            print('East is off the map!')
        try:
            dSE = wMap[posY + 1][posX + 1]
            print('There is a ' + dSE + ' to the southeast!')
        except:
            dSE = ' '
            print('Southeast is off the map!')
        try:
            dS = wMap[posY + 1][posX]
            print('There is a ' + dS + ' to the south!')
        except:
            dS = ' '
            print('South is off the map!')
        try:
            dSW = wMap[posY + 1][posX - 1]
            print('There is a ' + dSW + ' to the southwest!')
        except:
            dSW = ' '
            print('Southwest is off the map!')
        try:
            dW = wMap[posY][posX - 1]
            print('There is a ' + dW + ' to the west!')
        except:
            dW = ' '
            print('West is off the map!')
        try:
            dNW = wMap[posY - 1][posX - 1]
            print('There is a ' + dNW + ' to the northwest!')
        except:
            dNW = ' '
            print('North is off the map!')
    
        #Define a list using the surrounding symbols:
        surroundings = [dN, dNE, dE, dSE, dS, dSW, dW, dNW]
        #Print surrounding symbols in a relevant box formation
        print('Surroundings: ') 
        print('- - - - -')
        print('- ' + dNW + ' ' + dN + ' ' + dNE + ' -')
        print('- ' + dW + '   ' + dE + ' -')
        print('- ' + dSW + ' ' + dS + ' ' + dSE + ' -')
        print('- - - - -')

        #Define a list of weight totals for each:
        weights = [0, 0, 0, 0, 0, 0, 0, 0]
        #Define a value to iterate through weights with:
        index = 0

        #Calculate the weight totals:
        for i in surroundings:
            if i == UNEXPLORED:
                weights[index] = 0
            elif i == EMPTY:
                weights[index] = 0
            elif i == WATER:
                weights[index] = 10
            elif i == RIVER:
                weights[index] = 10
            elif i == FOREST:
                weights[index] = freqF * WEIGHT_INTENSITY
            elif i == PLAINS:
                weights[index] = freqP * WEIGHT_INTENSITY
            elif i == MOUNTAIN:
                weights[index] =  freqM * WEIGHT_INTENSITY
            elif i == FIEF:
                weights[index] = 0
            elif i == STRONGHOLD:
                weights[index] = 0
            index = index + 1

        #Print weights:
        print('Weights: ') 
        print(*weights)

        #Define a combined list of symbols and weights:
        symbolTable = [(dN,weights[0]),(dNE,weights[1]),(dE,weights[2]),(dSE,weights[3]),(dS,weights[4]),(dSW,weights[5]),(dW,weights[6]),(dNW,weights[7]), (RANDOM,RANDOM_INTENSITY)]

        #Print new combined list:
        print('Symbol Table: ') 
        print(*symbolTable)

        #Define an expanded list of the combined list:
        pointTable = []
        for item, weight in symbolTable:
            pointTable.extend([item]*weight)
        
        #Choose a random item in the list:
        newPoint = random.choice(pointTable)

        #Print the randomly selected symbol:
        print('New Point: ') 
        print(*newPoint)

    #If the option to instantly generate the map is selected, no print statements are made:
    else:
        if FIRST_PRINT:
            os.system("clear")
            print('Generating Map...')
            FIRST_PRINT = False
        try:
            dN = wMap[posY - 1][posX]
        except:
            dN = ' '
        try:
            dNE = wMap[posY - 1][posX + 1]
        except:
            dNE = ' '
        try:
            dE = wMap[posY][posX + 1]
        except:
            dE = ' '
        try:
            dSE = wMap[posY + 1][posX + 1]
        except:
            dSE = ' '
        try:
            dS = wMap[posY + 1][posX]
        except:
            dS = ' '
        try:
            dSW = wMap[posY + 1][posX - 1]
        except:
            dSW = ' '
        try:
            dW = wMap[posY][posX - 1]
        except:
            dW = ' '
        try:
            dNW = wMap[posY - 1][posX - 1]
        except:
            dNW = ' '
        #Define a list using the surrounding symbols:
        surroundings = [dN, dNE, dE, dSE, dS, dSW, dW, dNW]
        #Define a list of weight totals for each:
        weights = [0, 0, 0, 0, 0, 0, 0, 0]
        #Define a value to iterate through weights with:
        index = 0
        #Calculate the weight totals:
        for i in surroundings:
            if i == UNEXPLORED:
                weights[index] = 0
            elif i == EMPTY:
                weights[index] = 0
            elif i == WATER:
                weights[index] = 10
            elif i == RIVER:
                weights[index] = 10
            elif i == FOREST:
                weights[index] = freqF * WEIGHT_INTENSITY
            elif i == PLAINS:
                weights[index] = freqP * WEIGHT_INTENSITY
            elif i == MOUNTAIN:
                weights[index] =  freqM * WEIGHT_INTENSITY
            elif i == FIEF:
                weights[index] = 0
            elif i == STRONGHOLD:
                weights[index] = 0
            index = index + 1
        #Define a combined list of symbols and weights:
        symbolTable = [(dN,weights[0]),(dNE,weights[1]),(dE,weights[2]),(dSE,weights[3]),(dS,weights[4]),(dSW,weights[5]),(dW,weights[6]),(dNW,weights[7]), (RANDOM,RANDOM_INTENSITY)]
        #Define an expanded list of the combined list:
        pointTable = []
        for item, weight in symbolTable:
            pointTable.extend([item]*weight)
        #Choose a random item in the list:
        newPoint = random.choice(pointTable)

    #If the RANDOM symbol was picked, get a random symbol:
    if newPoint == RANDOM:
        newPoint = GetRandomPoint()

    #If the user doesn't wish for the map to be instantly generated, go through the map generation slowly:
    if not INSTANTLY_GENERATE:
        SequentiallyPrintMap(wMap, posX, posY)
    
    #While the map making process isn't automated:
    if not AUTOMATED:
        #Offer the user the option to make each symbol at a time, or automate the process.
        userInput=input('\nContinue with manual input? press (enter) or type (auto): ')

        if userInput == 'auto':
            AUTOMATED = True
            #Additionally, if the user decides to automate the process, ask if they want it 
            #to be generated instantly:
            if not INSTANTLY_GENERATE:
                userInput=input('Would you like to instantly generate this map? (y/n): ')
                if userInput == 'y':
                    INSTANTLY_GENERATE = True

    #Return the symbol
    return newPoint

#--------------------------------------------------------------------------------------------------------------
#   [LoadingAnimationIncrementor]
#   Parameter: cap
#
#   Uses a global variable to cycle through a loading animation and returns a number based on the cap passed
#--------------------------------------------------------------------------------------------------------------
def LoadingAnimationIncrementor(cap):
    global LOADING_INCREMENT

    if LOADING_INCREMENT > cap:
        LOADING_INCREMENT = 0
    else:
        LOADING_INCREMENT += 1

    return LOADING_INCREMENT

#--------------------------------------------------------------------------------------------------------------
#   [LoadingAnimation]
#   Parameter: thingLoading
#
#   Prints a passed string with an animation after it that changes each time the screen is refreshed.
#   Function should be used in loops where the system is being cleared several times.
#--------------------------------------------------------------------------------------------------------------
def LoadingAnimation(thingLoading):
    frame = LoadingAnimationIncrementor(4)
    if frame == 0:
        print(thingLoading)
    elif frame == 1:
        print(thingLoading + '.')
    elif frame == 2:
        print(thingLoading + '..')
    else:
        print(thingLoading + '...')

#--------------------------------------------------------------------------------------------------------------
#   [QuietlyGenerateWorldMap]
#   Parameters: seed
#
#   Does the same thing as GenerateWordlMap but with no prints or user interaction
#--------------------------------------------------------------------------------------------------------------
def QuietlyGenerateWorldMap(seed):
    worldMap = [['0' for x in range(MAP_WIDTH)] for y in range(MAP_HEIGHT)]
    sPosX = int(seed[0])
    sPosY = int(seed[1])
    freqMountain = int(seed[2])
    freqPlains = int(seed[3])
    freqForest = int(seed[4])
    
    loop = True
    firstLoop = True
    while (loop):
        if firstLoop:
            for y in range(MAP_HEIGHT):
                for x in range(MAP_WIDTH):
                    worldMap[y][x] = QuietlyDefineSurroundings(worldMap, x, y, freqMountain, freqPlains, freqForest)

            firstLoop = False
        loop = False
    return worldMap

#--------------------------------------------------------------------------------------------------------------
#   [QuietlyDefineSurroundings]
#   Parameters: wMap, posX, posY, freqM, freqP, freqF
#
#   Does the same thing as PrintSurroundings but with no prints or user interaction
#--------------------------------------------------------------------------------------------------------------
def QuietlyDefineSurroundings(wMap, posX, posY, freqM, freqP, freqF):
    try:
        dN = wMap[posY - 1][posX]
    except:
        dN = ' '
    try:
        dNE = wMap[posY - 1][posX + 1]
    except:
        dNE = ' '
    try:
        dE = wMap[posY][posX + 1]
    except:
        dE = ' '
    try:
        dSE = wMap[posY + 1][posX + 1]
    except:
        dSE = ' '
    try:
        dS = wMap[posY + 1][posX]
    except:
        dS = ' '
    try:
        dSW = wMap[posY + 1][posX - 1]
    except:
        dSW = ' '
    try:
        dW = wMap[posY][posX - 1]
    except:
        dW = ' '
    try:
        dNW = wMap[posY - 1][posX - 1]
    except:
        dNW = ' '

    #Define a list using the surrounding symbols:
    surroundings = [dN, dNE, dE, dSE, dS, dSW, dW, dNW]
    
    #Define a list of weight totals for each:
    weights = [0, 0, 0, 0, 0, 0, 0, 0]
    index = 0

    #Calculate the weight totals:
    for i in surroundings:
        if i == UNEXPLORED:
            weights[index] = 0
        elif i == EMPTY:
            weights[index] = 0
        elif i == WATER:
            weights[index] = 10
        elif i == RIVER:
            weights[index] = 10
        elif i == FOREST:
            weights[index] = freqF * WEIGHT_INTENSITY
        elif i == PLAINS:
            weights[index] = freqP * WEIGHT_INTENSITY
        elif i == MOUNTAIN:
            weights[index] =  freqM * WEIGHT_INTENSITY
        elif i == FIEF:
            weights[index] = 0
        elif i == STRONGHOLD:
            weights[index] = 0
        index = index + 1

    #Define a combined list of symbols and weights, including the RANDOM option.
    symbolTable = [(dN,weights[0]),(dNE,weights[1]),(dE,weights[2]),(dSE,weights[3]),(dS,weights[4]),(dSW,weights[5]),(dW,weights[6]),(dNW,weights[7]), (RANDOM,RANDOM_INTENSITY)]

    #Define a table to extend values based on weights and pull a random choice from it
    pointTable = []
    for item, weight in symbolTable:
        pointTable.extend([item]*weight)
    newPoint = random.choice(pointTable)

    #IF the random choice is selected, get a random point.
    if newPoint == RANDOM:
        newPoint = GetRandomPoint()

    #Return the symbol
    return newPoint

#--------------------------------------------------------------------------------------------------------------
#   [GetRandomPoint]
#
#   Grabs a random biome symbol
#--------------------------------------------------------------------------------------------------------------
def GetRandomPoint():
    symbolTable = [(WATER, DEFAULT_WEIGHT),(FOREST, DEFAULT_WEIGHT), (PLAINS, DEFAULT_WEIGHT), (MOUNTAIN, DEFAULT_WEIGHT)]
    pointTable = []
    for item, weight in symbolTable:
        pointTable.extend([item]*weight)
    return random.choice(pointTable)

#--------------------------------------------------------------------------------------------------------------
#   [GetRandomLandPoint]
#
#   Grabs a random solid land biome symbol
#--------------------------------------------------------------------------------------------------------------
def GetRandomLandPoint():
    symbolTable = [(FOREST, DEFAULT_WEIGHT), (PLAINS, DEFAULT_WEIGHT), (MOUNTAIN, DEFAULT_WEIGHT)]
    pointTable = []
    for item, weight in symbolTable:
        pointTable.extend([item]*weight)
    return random.choice(pointTable)

#--------------------------------------------------------------------------------------------------------------
#   [SequentiallyPrintMap]
#   Parameters: wMap, posX, posY
#
#   A visual char-by-char generation of the map
#--------------------------------------------------------------------------------------------------------------
def SequentiallyPrintMap(wMap, posX, posY):
    for i in range(MAP_HEIGHT):
        for j in range(MAP_WIDTH):
            if i == posY and j == posX:
                print(CYAN + wMap[i][j] + RESET, end=" ")
            else:
                print(wMap[i][j], end=" ")
        print('')
    time.sleep(0.1)

#--------------------------------------------------------------------------------------------------------------
#   [PrintColorMap]
#   Parameters: wMap
#
#   Iterates through a WorldMap and prints a color version.
#--------------------------------------------------------------------------------------------------------------
def PrintColorMap(wMap):
    for i in range(MAP_HEIGHT):
        for j in range(MAP_WIDTH):
            symbol = wMap[i][j]
            if symbol == UNEXPLORED:
                print(IC_UNEXPLORED + symbol + RESET, end=" ")
            elif symbol == EMPTY:
                print(symbol, end=" ")
            elif symbol == WATER:
                print(IC_WATER + symbol + RESET, end=" ")
            elif symbol == RIVER:
                print(IC_RIVER + symbol + RESET, end=" ")
            elif symbol == FOREST:
                print(IC_FOREST + symbol + RESET, end=" ")
            elif symbol == PLAINS:
                print(IC_PLAINS + symbol + RESET, end=" ")
            elif symbol == MOUNTAIN:
                print(IC_MOUNTAIN + symbol + RESET, end=" ")
            elif symbol == FIEF:
                print(IC_FIEF + symbol + RESET, end=" ")
            elif symbol == STRONGHOLD:
                print(IC_STRONGHOLD + symbol + RESET, end=" ")
        print('')

#--------------------------------------------------------------------------------------------------------------
#   [DefineFiefBiome]
#   Parameters: fief
#
#   Sets a fief's biome based on the fief's name. If no match is found, the fief is assigned a random biome 
#   instead.
#--------------------------------------------------------------------------------------------------------------
def DefineFiefBiome(fief):
    forestBiomeNames = ['forest', 'wood', 'root', 'grove', 'thicket', 'glade', 'pine', 'timber', 'covert', 'canopy']
    plainsBiomeNames = ['plain', 'field', 'prairie', 'flat', 'expanse', 'grass', 'meadow', 'steppe', 'plateau', 'heath', 'moor', 'hollow']
    mountainBiomeNames = ['mount', 'alp', 'bluff', 'cliff', 'crag', 'mesa', 'peak', 'range', 'ridge', 'pike', 'hill', 'butte', 'height']

    #Check if the name sounds like a forest
    for i in range(len(forestBiomeNames)):
        if forestBiomeNames[i] in fief.name:
            fief.biome = FOREST
    #Check if the name sounds like a mountain
    for i in range(len(mountainBiomeNames)):
        if mountainBiomeNames[i] in fief.name:
            fief.biome = MOUNTAIN
    #Check if the name sounds like a plains
    for i in range(len(plainsBiomeNames)):
        if plainsBiomeNames[i] in fief.name:
            fief.biome = PLAINS
    #Select randomly if the name doesn't sound like any of the previous biomes
    if fief.biome == '0':
        fief.biome = GetRandomLandPoint()

    #Update the fief file
    fief.write()

#--------------------------------------------------------------------------------------------------------------
#   [getBiomeCounts]
#   Parameters: wMap
#
#   Gets a list containing the number of biomes found in the passed map object.
#   List layout is:
#       [numWater, numRivers, numForest, numMountain, numPlains]
#--------------------------------------------------------------------------------------------------------------
def getBiomeCounts(wMap):
    numWater = 0
    numRivers = 0
    numForests = 0
    numMountains = 0
    numPlains = 0

    for i in range(len(wMap)):
        for j in range(len(wMap[i])):
            if wMap[i][j] == WATER:
                numWater += 1
            if wMap[i][j] == RIVER:
                numRivers += 1
            if wMap[i][j] == FOREST:
                numForests += 1
            if wMap[i][j] == MOUNTAIN:
                numMountains += 1
            if wMap[i][j] == PLAINS:
                numPlains += 1

    biomeCounts = [numWater, numRivers, numForests, numMountains, numPlains]
    return biomeCounts

#--------------------------------------------------------------------------------------------------------------
#   [setBiomeCounts]
#   Parameters: wMap
#
#   Gets a list containing the number of biomes found in the passed map object.
#   List layout is:
#       [numWater, numRivers, numForest, numMountain, numPlains]
#--------------------------------------------------------------------------------------------------------------
def setBiomeCounts(WorldMap):
    biomeCounts = getBiomeCounts(WorldMap.worldMap)
    WorldMap.numWater = biomeCounts[0]
    WorldMap.numRivers = biomeCounts[1]
    WorldMap.numForests = biomeCounts[2]
    WorldMap.numMountains = biomeCounts[3]
    WorldMap.numPlains = biomeCounts[4]

#--------------------------------------------------------------------------------------------------------------
#   [GenerateSeed]
#
#   Generates a random "seed" value for the map to add further variation in map generation.
#   Currently not very intuitive, likely land-heavy. Needs fine-tuning!
#--------------------------------------------------------------------------------------------------------------
def GenerateSeed():
    seed = ''
    x = 0
    y = 0
    biomeMountain = random.randint(1, 9)
    biomePlains = random.randint(1, 9)
    biomeForest = random.randint(1, 9)
    
    seed += str(x)
    seed += str(y)
    seed += str(biomeMountain)
    seed += str(biomePlains)
    seed += str(biomeForest)

    return seed

#eof