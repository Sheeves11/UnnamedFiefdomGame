import os
import time
import random
from classes import *

#--------------------------------------------------------------------------------------------------------------
#
#   Making a map:
#       1. Always generate a map before doing any other map commands. ('wm' at stronghold)
#       2. Sprinkle on the fiefs. ('paf' at stronghold)
#       3. Add in strongholds. ('ts' at stronghold)
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
INTENSE_CYAN = "\033[0;96m"
INTENSE_PURPLE = "\033[0;95m"
MAGENTA_BACKGROUND = "\u001b[45m"
INTENSE_BLACK = "\033[1;90m"
WHITE_BACKGROUND = "\033[47m"
CYAN_BACKGROUND = "\033[0;106m" 

#Global variables
MAP_WIDTH = 20
MAP_HEIGHT = 20
DEFAULT_WEIGHT = 10         #A common weight total
WEIGHT_INTENSITY = 5        #Determines how focused the map will be
RANDOM_INTENSITY = 20       #Determines how chaotic the map will be

#River Variables
RIVER_MAP_SCANS = 1         #Determines how many times the map is ran through when placing rivers
RIVER_FREQUENCY = 3         #Determines how often rivers will appear
RIVER_FORK_FREQUENCY = 1    #Determines how often rivers will fork
RIVER_LENGTH_INTENSITY = 6  #Determines how long rivers can get
RIVER_AVERAGE_WEIGHT = 0.0
RIVER_RATIO = 60

SCAN_LEVEL = 3              #Don't change this. Determines how deeply the river generator should search for mountains.
RIVER_COUNT = 0             #Keeps track of how many rivers there have been recorded so far. (For efficiency)
RIVER_CAP = 2               #Maximum number of rivers to be chosen from the coordinates below.
RIVER_COORDS_0 = []         #Hold 3-tuples of river-coordinates. This holds the tuples for scan level 0
RIVER_COORDS_1 = []         #Hold 3-tuples of river-coordinates. This holds the tuples for scan level 1
RIVER_COORDS_2 = []         #Hold 3-tuples of river-coordinates. This holds the tuples for scan level 2

#Other Variables
INSTANTLY_GENERATE = False
AUTOMATED = False
FIRST_PRINT = True
LOADING_INCREMENT = 0

#Map Icons
WATER = '~'
RIVER = ['/','|','\\']
MOUNTAIN = 'M'
PLAINS = '#'
FOREST = '^'
FIEF = 'X'
STRONGHOLD = 'H'
EMPTY = ' '
UNEXPLORED = '0'
LOCATION = '@'
RANDOM = '*'

#Map Icon Color
IC_WATER = BLUE
IC_RIVER = BLUE
IC_MOUNTAIN = DARK_GRAY
IC_PLAINS = YELLOW
IC_FOREST = GREEN
IC_FIEF = RED
IC_STRONGHOLD = INTENSE_PURPLE
IC_UNEXPLORED = WARNING
IC_LOCATION = INTENSE_PURPLE+CYAN_BACKGROUND+BOLD

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
#
#   Issues: While using a 40x40 map, the print is too large and it is not very comfortable to generate the map 
#   this way. Need to cut it down some.
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
        # try:
        #     dN = wMap[posY - 1][posX]
        #     print('There is a ' + dN + ' to the north!')
        # except:
        #     dN = ' '
        #     print('North is off the map!')
        # try:
        #     dNE = wMap[posY - 1][posX + 1]
        #     print('There is a ' + dNE + ' to the northeast!')
        # except:
        #     dNE = ' '
        #     print('Northeast is off the map!')
        # try:
        #     dE = wMap[posY][posX + 1]
        #     print('There is a ' + dE + ' to the east!')
        # except:
        #     dE = ' '
        #     print('East is off the map!')
        # try:
        #     dSE = wMap[posY + 1][posX + 1]
        #     print('There is a ' + dSE + ' to the southeast!')
        # except:
        #     dSE = ' '
        #     print('Southeast is off the map!')
        # try:
        #     dS = wMap[posY + 1][posX]
        #     print('There is a ' + dS + ' to the south!')
        # except:
        #     dS = ' '
        #     print('South is off the map!')
        # try:
        #     dSW = wMap[posY + 1][posX - 1]
        #     print('There is a ' + dSW + ' to the southwest!')
        # except:
        #     dSW = ' '
        #     print('Southwest is off the map!')
        # try:
        #     dW = wMap[posY][posX - 1]
        #     print('There is a ' + dW + ' to the west!')
        # except:
        #     dW = ' '
        #     print('West is off the map!')
        # try:
        #     dNW = wMap[posY - 1][posX - 1]
        #     print('There is a ' + dNW + ' to the northwest!')
        # except:
        #     dNW = ' '
        #     print('North is off the map!')
    
        # #Define a list using the surrounding symbols:
        # surroundings = [dN, dNE, dE, dSE, dS, dSW, dW, dNW]

        surroundings = ScanSurroundings(wMap, posX, posY)
        dN = surroundings[0]
        dNE = surroundings[1]
        dE = surroundings[2]
        dSE = surroundings[3]
        dS = surroundings[4]
        dSW = surroundings[5]
        dW = surroundings[6]
        dNW = surroundings[7]

        #Print surrounding symbols in a relevant box formation
        print('\nSurroundings: ') 
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
        print('\nWeights: ') 
        print(*weights)

        #Define a combined list of symbols and weights:
        symbolTable = [(dN,weights[0]),(dNE,weights[1]),(dE,weights[2]),(dSE,weights[3]),(dS,weights[4]),(dSW,weights[5]),(dW,weights[6]),(dNW,weights[7]), (RANDOM,RANDOM_INTENSITY)]

        #Print new combined list:
        print('\nSymbol Table: ') 
        print(*symbolTable)

        #Define an expanded list of the combined list:
        pointTable = []
        for item, weight in symbolTable:
            pointTable.extend([item]*weight)
        
        #Choose a random item in the list:
        newPoint = random.choice(pointTable)

        #Print the randomly selected symbol:
        print('\nNew Point: ') 
        print(*newPoint)
        print('')
    #If the option to instantly generate the map is selected, no print statements are made:
    else:
        if FIRST_PRINT:
            os.system("clear")
            print('Generating Map...')
            FIRST_PRINT = False
        # try:
        #     dN = wMap[posY - 1][posX]
        # except:
        #     dN = ' '
        # try:
        #     dNE = wMap[posY - 1][posX + 1]
        # except:
        #     dNE = ' '
        # try:
        #     dE = wMap[posY][posX + 1]
        # except:
        #     dE = ' '
        # try:
        #     dSE = wMap[posY + 1][posX + 1]
        # except:
        #     dSE = ' '
        # try:
        #     dS = wMap[posY + 1][posX]
        # except:
        #     dS = ' '
        # try:
        #     dSW = wMap[posY + 1][posX - 1]
        # except:
        #     dSW = ' '
        # try:
        #     dW = wMap[posY][posX - 1]
        # except:
        #     dW = ' '
        # try:
        #     dNW = wMap[posY - 1][posX - 1]
        # except:
        #     dNW = ' '
        # #Define a list using the surrounding symbols:
        # surroundings = [dN, dNE, dE, dSE, dS, dSW, dW, dNW]

        surroundings = ScanSurroundings(wMap, posX, posY)
        dN = surroundings[0]
        dNE = surroundings[1]
        dE = surroundings[2]
        dSE = surroundings[3]
        dS = surroundings[4]
        dSW = surroundings[5]
        dW = surroundings[6]
        dNW = surroundings[7]

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
#   I didn't end up using this, so I converted it into an artificial loading function to go before something
#   and slow it down for no reason besides having a transition.
#--------------------------------------------------------------------------------------------------------------
def LoadingAnimation(thingLoading):
    os.system("clear")
    frame = LoadingAnimationIncrementor(4)
    if frame == 0:
        print(thingLoading)
    elif frame == 1:
        print(thingLoading + '.')
    elif frame == 2:
        print(thingLoading + '..')
    else:
        print(thingLoading + '...')
    time.sleep(0.1)

#--------------------------------------------------------------------------------------------------------------
#   [SilentlyGenerateWorldMap]
#   Parameters: seed
#
#   Does the same thing as GenerateWordlMap but with no prints or user interaction
#--------------------------------------------------------------------------------------------------------------
def SilentlyGenerateWorldMap(seed):
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
                    worldMap[y][x] = SilentlyDefineSurroundings(worldMap, x, y, freqMountain, freqPlains, freqForest)

            firstLoop = False
        loop = False
    return worldMap

#--------------------------------------------------------------------------------------------------------------
#   [SilentlyDefineSurroundings]
#   Parameters: wMap, posX, posY, freqM, freqP, freqF
#
#   Does the same thing as PrintSurroundings but with no prints or user interaction
#--------------------------------------------------------------------------------------------------------------
def SilentlyDefineSurroundings(wMap, posX, posY, freqM, freqP, freqF):
    # try:
    #     dN = wMap[posY - 1][posX]
    # except:
    #     dN = ' '
    # try:
    #     dNE = wMap[posY - 1][posX + 1]
    # except:
    #     dNE = ' '
    # try:
    #     dE = wMap[posY][posX + 1]
    # except:
    #     dE = ' '
    # try:
    #     dSE = wMap[posY + 1][posX + 1]
    # except:
    #     dSE = ' '
    # try:
    #     dS = wMap[posY + 1][posX]
    # except:
    #     dS = ' '
    # try:
    #     dSW = wMap[posY + 1][posX - 1]
    # except:
    #     dSW = ' '
    # try:
    #     dW = wMap[posY][posX - 1]
    # except:
    #     dW = ' '
    # try:
    #     dNW = wMap[posY - 1][posX - 1]
    # except:
    #     dNW = ' '

    # #Define a list using the surrounding symbols:
    # surroundings = [dN, dNE, dE, dSE, dS, dSW, dW, dNW]
    
    surroundings = ScanSurroundings(wMap, posX, posY)
    dN = surroundings[0]
    dNE = surroundings[1]
    dE = surroundings[2]
    dSE = surroundings[3]
    dS = surroundings[4]
    dSW = surroundings[5]
    dW = surroundings[6]
    dNW = surroundings[7]

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
#   Returns: A random biome symbol
#--------------------------------------------------------------------------------------------------------------
def GetRandomPoint():
    symbolTable = [(WATER, DEFAULT_WEIGHT),(FOREST, DEFAULT_WEIGHT), (PLAINS, DEFAULT_WEIGHT), (MOUNTAIN, DEFAULT_WEIGHT)]
    pointTable = []
    for item, weight in symbolTable:
        pointTable.extend([item]*weight)
    return random.choice(pointTable)

#--------------------------------------------------------------------------------------------------------------
#   [GetRandomLandPoint]
#   Returns: a random solid land biome symbol
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
            elif symbol == RIVER[0] or symbol == RIVER[1] or symbol == RIVER[2]:
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
            elif symbol == LOCATION:
                print(IC_LOCATION + symbol + RESET, end=" ")
        print('')

#--------------------------------------------------------------------------------------------------------------
#   [PrintLegend]
#   Prints a legend for the map
#--------------------------------------------------------------------------------------------------------------
def PrintLegend():
    print('- Legend -----------')
    print('- ' + IC_WATER + WATER + RESET + ' : Water        -')
    #print('- ' + IC_RIVER + RIVER + RESET + ' : River        -')
    print('- ' + IC_FOREST + FOREST + RESET + ' : Forest       -')
    print('- ' + IC_PLAINS + PLAINS + RESET + ' : Plains       -')
    print('- ' + IC_MOUNTAIN + MOUNTAIN + RESET + ' : Mountain     -')
    print('- ' + IC_FIEF + FIEF + RESET + ' : Fief         -')
    print('- ' + IC_STRONGHOLD + STRONGHOLD + RESET + ' : Stronghold   -')
    print('- ' + IC_LOCATION + LOCATION + RESET + ' : You are Here -')

#--------------------------------------------------------------------------------------------------------------
#   [DefineFiefBiome]
#   Parameters: fiefClass
#
#   Sets a fief's biome based on the fief's name. If no match is found, the fief is assigned a random biome 
#   instead.
#--------------------------------------------------------------------------------------------------------------
def DefineFiefBiome(fiefClass):
    forestBiomeNames = ['forest', 'wood', 'root', 'grove', 'thicket', 'glade', 'pine', 'timber', 'covert', 'canopy']
    plainsBiomeNames = ['plain', 'field', 'prairie', 'flat', 'expanse', 'grass', 'meadow', 'steppe', 'plateau', 'heath', 'moor', 'hollow']
    mountainBiomeNames = ['mount', 'alp', 'bluff', 'cliff', 'crag', 'mesa', 'peak', 'range', 'ridge', 'pike', 'hill', 'butte', 'height']

    print('Fief name: ' + str(fiefClass.name))
    #Check if the name sounds like a forest
    for i in range(len(forestBiomeNames)):
        if forestBiomeNames[i] in str(fiefClass.name).lower():
            print('Name contains ' + str(forestBiomeNames[i]) + ", so it's a forest!")
            fiefClass.biome = FOREST
    #Check if the name sounds like a mountain
    for i in range(len(mountainBiomeNames)):
        if mountainBiomeNames[i] in str(fiefClass.name).lower():
            print('Name contains ' + str(mountainBiomeNames[i]) + ", so it's a mountain!")
            fiefClass.biome = MOUNTAIN
    #Check if the name sounds like a plains
    for i in range(len(plainsBiomeNames)):
        if plainsBiomeNames[i] in str(fiefClass.name).lower():
            print('Name contains ' + str(plainsBiomeNames[i]) + ", so it's a plains!")
            fiefClass.biome = PLAINS
    #Select randomly if the name doesn't sound like any of the previous biomes
    if fiefClass.biome == '0':
        print('Fief name does not contain a specific biome type, setting a random biome.')
        fiefClass.biome = GetRandomLandPoint()

    #Update the fiefClass file
    fiefClass.write()

#--------------------------------------------------------------------------------------------------------------
#   [SilentlyDefineFiefBiome]
#   Parameters: fiefClass
#
#   Sets a fief's biome based on the fief's name. If no match is found, the fief is assigned a random biome 
#   instead. Does this without printing anything
#--------------------------------------------------------------------------------------------------------------
def SilentlyDefineFiefBiome(fiefClass):
    forestBiomeNames = ['forest', 'wood', 'root', 'grove', 'thicket', 'glade', 'pine', 'timber', 'covert', 'canopy']
    plainsBiomeNames = ['plain', 'field', 'prairie', 'flat', 'expanse', 'grass', 'meadow', 'steppe', 'plateau', 'heath', 'moor', 'hollow']
    mountainBiomeNames = ['mount', 'alp', 'bluff', 'cliff', 'crag', 'mesa', 'peak', 'range', 'ridge', 'pike', 'hill', 'butte', 'height']
    #Check if the name sounds like a forest
    for i in range(len(forestBiomeNames)):
        if forestBiomeNames[i] in str(fiefClass.name).lower():
            fiefClass.biome = FOREST
    #Check if the name sounds like a mountain
    for i in range(len(mountainBiomeNames)):
        if mountainBiomeNames[i] in str(fiefClass.name).lower():
            fiefClass.biome = MOUNTAIN
    #Check if the name sounds like a plains
    for i in range(len(plainsBiomeNames)):
        if plainsBiomeNames[i] in str(fiefClass.name).lower():
            fiefClass.biome = PLAINS
    #Select randomly if the name doesn't sound like any of the previous biomes
    if fiefClass.biome == '0':
        fiefClass.biome = GetRandomLandPoint()
    #Update the fiefClass file
    fiefClass.write()

#--------------------------------------------------------------------------------------------------------------
#   [PlotAllFiefs]
#   Parameters: mapClass
#   Plots all fief files on the world map
#--------------------------------------------------------------------------------------------------------------
def PlotAllFiefs(mapClass):
    for filename in os.listdir('fiefs'):
        with open(os.path.join('fiefs', filename), 'r') as f:
            time.sleep(0.3)
            os.system("clear")
            fiefClass = filename[:-4]
            fiefClass = Fiefdom()
            fiefClass.name = filename[:-4]
            fiefClass.read()
            QuietlyPlaceFiefInWorldMap(fiefClass, mapClass)

#--------------------------------------------------------------------------------------------------------------
#   [SilentlyPlotAllFiefs]
#   Parameters: mapClass
#   Plots all fief files on the world map
#--------------------------------------------------------------------------------------------------------------
def SilentlyPlotAllFiefs(mapClass):
    for filename in os.listdir('fiefs'):
        with open(os.path.join('fiefs', filename), 'r') as f:
            fiefClass = filename[:-4]
            fiefClass = Fiefdom()
            fiefClass.name = filename[:-4]
            fiefClass.read()
            SilentlyPlaceFiefInWorldMap(fiefClass, mapClass)

#--------------------------------------------------------------------------------------------------------------
#   [PlaceFiefInWorldMap]
#   Parameters: fiefClass, mapClass
#
#   Sets a fief's biome based on the fief's name. If no match is found, the fief is assigned a random biome 
#   instead.
#--------------------------------------------------------------------------------------------------------------
def PlaceFiefInWorldMap(fiefClass, mapClass):
    if (fiefClass.biome == '0') and (fiefClass.name != 'Default Fiefdom'):
        DefineFiefBiome(fiefClass)
        print('Defined Biome as: ' + str(fiefClass.biome))
        remaining = 0
        cycle = 0
        pickingPoint = 0

        #Check if there are still biome slots open for a particular biome.
        #If none are available, then change the fief's biome and try again.
        #If there aren't any open spots at all, then stop the loop.
        while remaining == 0 and cycle < 4:
            remaining = CheckRemainingBiomes(fiefClass.biome, mapClass)
            if remaining == 0:
                fiefClass.biome = CycleBiome(fiefClass.biome)
                cycle += 1
        if cycle > 3:
            print('Error, no more room for fiefs left on this map!')
        else:
            while pickingPoint < 10:    #Tries to get a point. Fails if it manages to select an occupied point 10 times.
            #Select one of the available biomes at random
                print('Picking a random ' + str(fiefClass.biome) + ' biome out of the ones available:')
                point = GetRandomPointByBiome(fiefClass.biome, mapClass)
                print('Picked point: ' + str(point))

                #If a biome was found:
                if point > 0:
                    coordinates = GetPointCoordinates(fiefClass.biome, point, mapClass.worldMap)

                    if CrossCheckFiefCoordinates(coordinates):
                        print('Successfully selected coordinates!:')
                        print(*coordinates)
                        fiefClass.setCoordinates(coordinates)
                        print('Successfully set coordinates!: ')
                        print('xCoordinate: ' + str(fiefClass.xCoordinate) + ' yCoordinate: ' + str(fiefClass.yCoordinate))
                        print('Updating used biomes in mapClass, biome is ' + str(fiefClass.biome) + ': ')
                        UpdateUsedBiomes(fiefClass.biome, mapClass)
                        print('Used Forests: ' + str(mapClass.usedForests))
                        print('Used Plains: ' + str(mapClass.usedPlains))
                        print('Used Mountains: ' + str(mapClass.usedMountains))
                        print('Inserting Fief into map:')
                        InsertFiefAtLocation(fiefClass.yCoordinate, fiefClass.xCoordinate, mapClass)
                        
                        PrintColorMap(mapClass.worldMap)

                        fiefClass.write()
                        pickingPoint = 10

                    else:
                        pickingPoint += 1
    else:
        if fiefClass.name == 'Default Fiefdom':
            print("That fiefdom doesn't exist!")
        else:
            print('That fief is already on the map!')


#--------------------------------------------------------------------------------------------------------------
#   [QuietlyPlaceFiefInWorldMap]
#   Parameters: fiefClass, mapClass
#
#   Sets a fief's biome based on the fief's name. If no match is found, the fief is assigned a random biome 
#   instead. This version doesn't print as much diagnostic stuff.
#--------------------------------------------------------------------------------------------------------------
def QuietlyPlaceFiefInWorldMap(fiefClass, mapClass):
    if (fiefClass.biome == '0') and (fiefClass.name != 'Default Fiefdom'):
        DefineFiefBiome(fiefClass)
        remaining = 0
        cycle = 0
        pickingPoint = 0
        spotFound = False

        #Check if there are still biome slots open for a particular biome.
        #If none are available, then change the fief's biome and try again.
        #If there aren't any open spots at all, then stop the loop.
        while remaining == 0 and cycle < 4:
            remaining = CheckRemainingBiomes(fiefClass.biome, mapClass)
            if remaining == 0:
                fiefClass.biome = CycleBiome(fiefClass.biome)
                cycle += 1
        if cycle > 3:
            print('Error, no more room for fiefs left on this map!')
        else:
            while pickingPoint < 10:    #Tries to get a point. Fails if it manages to select an occupied point 10 times.
                #Select one of the available biomes at random
                point = GetRandomPointByBiome(fiefClass.biome, mapClass)
                #If a biome was found:
                if point > 0:
                    coordinates = GetPointCoordinates(fiefClass.biome, point, mapClass.worldMap)

                    if CrossCheckFiefCoordinates(coordinates):
                        print(*coordinates)
                        fiefClass.setCoordinates(coordinates)
                        UpdateUsedBiomes(fiefClass.biome, mapClass)
                        InsertFiefAtLocation(fiefClass.yCoordinate, fiefClass.xCoordinate, mapClass)
                        
                        PrintColorMap(mapClass.worldMap)

                        fiefClass.write()
                        pickingPoint = 10
                        spotFound = True
                    else:
                        pickingPoint += 1
            if spotFound == False:
                print("Error, couldn't find an empty spot!")
    else:
        if fiefClass.name == 'Default Fiefdom':
            print("That fiefdom doesn't exist!")
        else:
            print(str(fiefClass.name) + ' is already on the map!')

#--------------------------------------------------------------------------------------------------------------
#   [SilentlyPlaceFiefInWorldMap]
#   Parameters: fiefClass, mapClass
#
#   Sets a fief's biome based on the fief's name. If no match is found, the fief is assigned a random biome 
#   instead. This version doesn't print anything unless an error occurs.
#--------------------------------------------------------------------------------------------------------------
def SilentlyPlaceFiefInWorldMap(fiefClass, mapClass):
    if (fiefClass.biome == '0') and (fiefClass.name != 'Default Fiefdom'):
        SilentlyDefineFiefBiome(fiefClass)
        remaining = 0
        cycle = 0
        pickingPoint = 0
        spotFound = False

        #Check if there are still biome slots open for a particular biome.
        #If none are available, then change the fief's biome and try again.
        #If there aren't any open spots at all, then stop the loop.
        while remaining == 0 and cycle < 4:
            remaining = CheckRemainingBiomes(fiefClass.biome, mapClass)
            if remaining == 0:
                fiefClass.biome = CycleBiome(fiefClass.biome)
                cycle += 1
        if cycle > 3:
            print('Error, no more room for fiefs left on this map!')
        else:
            while pickingPoint < 10:    #Tries to get a point. Fails if it manages to select an occupied point 10 times.
                #Select one of the available biomes at random
                point = GetRandomPointByBiome(fiefClass.biome, mapClass)
                #If a biome was found:
                if point > 0:
                    coordinates = GetPointCoordinates(fiefClass.biome, point, mapClass.worldMap)

                    if CrossCheckFiefCoordinates(coordinates):
                        if CrossCheckStrongholdCoordinates(coordinates):
                            fiefClass.setCoordinates(coordinates)
                            UpdateUsedBiomes(fiefClass.biome, mapClass)
                            InsertFiefAtLocation(fiefClass.yCoordinate, fiefClass.xCoordinate, mapClass)
                            fiefClass.write()
                            pickingPoint = 10
                            spotFound = True
                        else:
                            pickingPoint += 1
                    else:
                        pickingPoint += 1
            if spotFound == False:
                print("Error, couldn't find an empty spot!")
    else:
        if fiefClass.name == 'Default Fiefdom':
            print("That fiefdom doesn't exist!")
        else:
            print(str(fiefClass.name) + ' is already on the map!')

#--------------------------------------------------------------------------------------------------------------
#   [InsertFiefAtLocation]
#   Parameters: yPos, xPos, mapClass
#   Finds the x and y position in the world map and writes an X
#--------------------------------------------------------------------------------------------------------------
def InsertFiefAtLocation(yPos, xPos, mapClass):
    for i in range(len(mapClass.worldMap)):
        for j in range(len(mapClass.worldMap[i])):
            if i == yPos and j == xPos:
                mapClass.worldMap[i][j] = FIEF
    mapClass.write()

#--------------------------------------------------------------------------------------------------------------
#   [GetPointCoordinates]
#   Parameters: biome, point, mapClass
#   Returns: a set of coordinates based on the point parameter.
#--------------------------------------------------------------------------------------------------------------
def GetPointCoordinates(biome, point, wMap):
    coordinates = [0, 0]
    counter = 0
    if biome == FOREST:
        for i in range(len(wMap)):
            for j in range(len(wMap[i])):
                if wMap[i][j] == FOREST:
                    counter += 1
                    if counter == point:
                        coordinates[0] = i
                        coordinates[1] = j
    elif biome == PLAINS:
        for i in range(len(wMap)):
            for j in range(len(wMap[i])):
                if wMap[i][j] == PLAINS:
                    counter += 1
                    if counter == point:
                        coordinates[0] = i
                        coordinates[1] = j
    elif biome == MOUNTAIN:
        for i in range(len(wMap)):
            for j in range(len(wMap[i])):
                if wMap[i][j] == MOUNTAIN:
                    counter += 1
                    if counter == point:
                        coordinates[0] = i
                        coordinates[1] = j

    return coordinates

#--------------------------------------------------------------------------------------------------------------
#   [CrossCheckFiefCoordinates]
#   Parameters: coordinates
#   Returns: True if no other fiefs have the same coordinates
#
#   Issues: This is a bit tedious, having to check each file this way. Another way to make this work could be
#   to have an list stored in the Map object that contains tuples of coordinates that are occupied by fiefs.
#   This way, strongholds could benefit from that as well. For now, I'm not so sure I want to mess with the 
#   currently functional map class though after all the read/write woes. 
#--------------------------------------------------------------------------------------------------------------
def CrossCheckFiefCoordinates(coordinates):
    
    for filename in os.listdir('fiefs'):
            with open(os.path.join('fiefs', filename), 'r') as f:
                tempName = filename[:-4]
                tempName = Fiefdom()
                tempName.name = filename[:-4]
                tempName.read()
                # print('Cross checking with: ' + str(tempName.name))
                if tempName.yCoordinate == coordinates[0] and tempName.xCoordinate == coordinates[1]:
                    print('Error, same coordinates as ' + str(tempName.name) + '!')
                    return False
    return True

#--------------------------------------------------------------------------------------------------------------
#   [CrossCheckStrongholdCoordinates]
#   Parameters: coordinates
#   Returns: True if no strongholds have the same coordinates
#--------------------------------------------------------------------------------------------------------------
def CrossCheckStrongholdCoordinates(coordinates):
    
    for filename in os.listdir('strongholds'):
            with open(os.path.join('strongholds', filename), 'r') as f:
                tempName = filename[:-4]
                tempName = Stronghold()
                tempName.name = filename[:-4]
                tempName.read()
                # print('Cross checking with: ' + str(tempName.name))
                if tempName.yCoordinate == coordinates[0] and tempName.xCoordinate == coordinates[1]:
                    print('Error, same coordinates as ' + str(tempName.name) + '!')
                    return False
    return True

#--------------------------------------------------------------------------------------------------------------
#   [CheckRemainingBiomes]
#   Parameters: biome, mapClass
#   Returns: number of remaining biomes of the passed type in the passed mapClass
#--------------------------------------------------------------------------------------------------------------
def CheckRemainingBiomes(biome, mapClass):
    if biome == FOREST:
        return int(mapClass.numForests) - int(mapClass.usedForests)
    elif biome == MOUNTAIN:
        return int(mapClass.numMountains) - int(mapClass.usedMountains)
    elif biome == PLAINS:
        return int(mapClass.numPlains) - int(mapClass.usedPlains)
    else:
        return 0

#--------------------------------------------------------------------------------------------------------------
#   [GetRandomPointByBiome]
#   Parameters: biome, mapClass
#   Returns: an random int based on the number of matching biomes in the passed mapClass
#--------------------------------------------------------------------------------------------------------------
def GetRandomPointByBiome(biome, mapClass):
    if biome == FOREST:
        return random.randint(1, int(mapClass.numForests))
    if biome == MOUNTAIN:
        return random.randint(1, int(mapClass.numMountains))
    if biome == PLAINS:
        return random.randint(1, int(mapClass.numPlains))

#--------------------------------------------------------------------------------------------------------------
#   [CycleBiome]
#   Parameters: biome
#   Returns: a different biome based on the biome passed
#--------------------------------------------------------------------------------------------------------------
def CycleBiome(biome):
    if biome == FOREST:
        print('No forests left, changing biome to a mountain:')
        return MOUNTAIN
    elif biome == MOUNTAIN:
        print('No mountains left, changing biome to a plains:')
        return PLAINS
    elif biome == PLAINS:
        print('No plains left, changing biome to a forest:')
        return FOREST

#--------------------------------------------------------------------------------------------------------------
#   [UpdateUsedBiomes]
#   Parameters: biome, mapClass
#   Returns: an random int based on the number of matching biomes in the passed mapClass
#--------------------------------------------------------------------------------------------------------------
def UpdateUsedBiomes(biome, mapClass):
    count = 0
    if biome == FOREST:
        count = int(mapClass.usedForests) + 1
        mapClass.usedForests = str(count)
    elif biome == MOUNTAIN:
        count = int(mapClass.usedMountains) + 1
        mapClass.usedMountains = str(count)
    elif biome == PLAINS:
        count = int(mapClass.usedPlains) + 1
        mapClass.usedPlains = str(count)

    mapClass.write()

#--------------------------------------------------------------------------------------------------------------
#   [GetBiomeCounts]
#   Parameters: wMap
#
#   Gets a list containing the number of biomes found in the passed map object.
#   List layout is:
#       [numWater, numRivers, numForest, numMountain, numPlains]
#--------------------------------------------------------------------------------------------------------------
def GetBiomeCounts(wMap):
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
#   [SetBiomeCounts]
#   Parameters: mapClass
#
#   Sets the number of biomes in the map class
#--------------------------------------------------------------------------------------------------------------
def SetBiomeCounts(mapClass):
    biomeCounts = GetBiomeCounts(mapClass.worldMap)
    mapClass.numWater = biomeCounts[0]
    mapClass.numRivers = biomeCounts[1]
    mapClass.numForests = biomeCounts[2]
    mapClass.numMountains = biomeCounts[3]
    mapClass.numPlains = biomeCounts[4]

#--------------------------------------------------------------------------------------------------------------
#   [DefineStrongholdBiome]
#   Parameters: strongholdClass
#   Sets a stronghold's biome randomly.
#--------------------------------------------------------------------------------------------------------------
def DefineStrongholdBiome(strongholdClass):
    strongholdClass.biome = GetRandomLandPoint()
    strongholdClass.write()


#--------------------------------------------------------------------------------------------------------------
#   [PlotAllStrongholds]
#   Parameters: mapClass
#   Plots all stronghold files on the world map (this won't be used too often, since strongholds will
#   typically be added one at a time as new users are made)
#--------------------------------------------------------------------------------------------------------------
def PlotAllStrongholds(mapClass):
    for filename in os.listdir('strongholds'):
        with open(os.path.join('strongholds', filename), 'r') as f:
            time.sleep(0.3)
            os.system("clear")
            strongholdClass = filename[:-4]
            strongholdClass = Stronghold()
            strongholdClass.name = filename[:-4]
            strongholdClass.read()
            QuietlyPlaceStrongholdInWorldMap(strongholdClass, mapClass)

#--------------------------------------------------------------------------------------------------------------
#   [SilentlyPlotAllStrongholds]
#   Parameters: mapClass
#   Plots all stronghold files on the world map (this won't be used too often, since strongholds will
#   typically be added one at a time as new users are made). This version has no prints.
#--------------------------------------------------------------------------------------------------------------
def SilentlyPlotAllStrongholds(mapClass):
    for filename in os.listdir('strongholds'):
        with open(os.path.join('strongholds', filename), 'r') as f:
            strongholdClass = filename[:-4]
            strongholdClass = Stronghold()
            strongholdClass.name = filename[:-4]
            strongholdClass.read()
            SilentlyPlaceStrongholdInWorldMap(strongholdClass, mapClass)

#--------------------------------------------------------------------------------------------------------------
#   [QuietlyPlaceStrongholdInWorldMap]
#   Parameters: strongholdClass, mapClass
#
#   Sets a fief's biome based on the fief's name. If no match is found, the fief is assigned a random biome 
#   instead. This version doesn't print as much diagnostic stuff.
#--------------------------------------------------------------------------------------------------------------
def QuietlyPlaceStrongholdInWorldMap(strongholdClass, mapClass):
    if (strongholdClass.biome == '0') and (strongholdClass.name != 'Default Stronghold'):
        DefineStrongholdBiome(strongholdClass)
        remaining = 0
        cycle = 0
        pickingPoint = 0
        spotFound = False

        #Check if there are still biome slots open for a particular biome.
        #If none are available, then change the stronghold's biome and try again.
        #If there aren't any open spots at all, then stop the loop.
        while remaining == 0 and cycle < 4:
            remaining = CheckRemainingBiomes(strongholdClass.biome, mapClass)
            if remaining == 0:
                strongholdClass.biome = CycleBiome(strongholdClass.biome)
                cycle += 1
        if cycle > 3:
            print('Error, no more room left on this map!')
        else:
            while pickingPoint < 10:    #Tries to get a point. Fails if it manages to select an occupied point 10 times.
                #Select one of the available biomes at random
                point = GetRandomPointByBiome(strongholdClass.biome, mapClass)
                #If a biome was found:
                if point > 0:
                    #Grab some coordinates:
                    coordinates = GetPointCoordinates(strongholdClass.biome, point, mapClass.worldMap)  
                    #If coordinates aren't the same as some fief:
                    if CrossCheckFiefCoordinates(coordinates):  
                        #If the coordinates aren't the same as some other stronghold:                                        
                        if CrossCheckStrongholdCoordinates(coordinates):   
                            #Update map and stronghold:  
                            print('Adding ' + str(strongholdClass.name) + "'s stronghold to the map!")                           
                            print(*coordinates)
                            strongholdClass.setCoordinates(coordinates)
                            UpdateUsedBiomes(strongholdClass.biome, mapClass)
                            InsertStrongholdAtLocation(strongholdClass.yCoordinate, strongholdClass.xCoordinate, mapClass)
                            
                            PrintColorMap(mapClass.worldMap)

                            strongholdClass.write()
                            pickingPoint = 10
                            spotFound = True
                        else:
                            pickingPoint += 1
                    else:
                        pickingPoint += 1
            if spotFound == False:
                print("Error, couldn't find an empty spot!")
    else:
        if strongholdClass.name == 'Default Stronghold':
            print("That stronghold doesn't exist!")
        else:
            print(str(strongholdClass.name) + "'s stronghold is already on the map!")

#--------------------------------------------------------------------------------------------------------------
#   [SilentlyPlaceStrongholdInWorldMap]
#   Parameters: strongholdClass, mapClass
#
#   These are getting redundant, I know. 
#   Sets a fief's biome based on the fief's name. If no match is found, the fief is assigned a random biome 
#   instead. This version doesn't print a single thing unless an error happens.
#--------------------------------------------------------------------------------------------------------------
def SilentlyPlaceStrongholdInWorldMap(strongholdClass, mapClass):
    if (strongholdClass.biome == '0') and (strongholdClass.name != 'Default Stronghold'):
        DefineStrongholdBiome(strongholdClass)
        remaining = 0
        cycle = 0
        pickingPoint = 0
        spotFound = False

        #Check if there are still biome slots open for a particular biome.
        #If none are available, then change the stronghold's biome and try again.
        #If there aren't any open spots at all, then stop the loop.
        while remaining == 0 and cycle < 4:
            remaining = CheckRemainingBiomes(strongholdClass.biome, mapClass)
            if remaining == 0:
                strongholdClass.biome = CycleBiome(strongholdClass.biome)
                cycle += 1
        if cycle > 3:
            print('Error, no more room left on this map!')
        else:
            while pickingPoint < 10:    #Tries to get a point. Fails if it manages to select an occupied point 10 times.
                #Select one of the available biomes at random
                point = GetRandomPointByBiome(strongholdClass.biome, mapClass)
                #If a biome was found:
                if point > 0:
                    #Grab some coordinates:
                    coordinates = GetPointCoordinates(strongholdClass.biome, point, mapClass.worldMap)  
                    #If coordinates aren't the same as some fief:
                    if CrossCheckFiefCoordinates(coordinates):  
                        #If the coordinates aren't the same as some other stronghold:                                        
                        if CrossCheckStrongholdCoordinates(coordinates):   
                            #Update map and stronghold:  
                            strongholdClass.setCoordinates(coordinates)
                            UpdateUsedBiomes(strongholdClass.biome, mapClass)
                            InsertStrongholdAtLocation(strongholdClass.yCoordinate, strongholdClass.xCoordinate, mapClass)

                            strongholdClass.write()
                            pickingPoint = 10
                            spotFound = True
                        else:
                            pickingPoint += 1
                    else:
                        pickingPoint += 1
            if spotFound == False:
                print("Error, couldn't find an empty spot!")
    else:
        if strongholdClass.name == 'Default Stronghold':
            print("That stronghold doesn't exist!")
        else:
            print(str(strongholdClass.name) + "'s stronghold is already on the map!")
#--------------------------------------------------------------------------------------------------------------
#   [InsertStrongholdAtLocation]
#   Parameters: yPos, xPos, mapClass
#   Finds the x and y position in the world map and writes an H
#--------------------------------------------------------------------------------------------------------------
def InsertStrongholdAtLocation(yPos, xPos, mapClass):
    for i in range(len(mapClass.worldMap)):
        for j in range(len(mapClass.worldMap[i])):
            if i == yPos and j == xPos:
                mapClass.worldMap[i][j] = STRONGHOLD
    mapClass.write()


#--------------------------------------------------------------------------------------------------------------
#   [ScanSurroundings]
#   Parameters: wMap, posX, posY
#   Returns: an array of map symbols in the form: [dN, dNE, dE, dSE, dS, dSW, dW, dNW]
#   where each symbol represents an icon.
#--------------------------------------------------------------------------------------------------------------
def ScanSurroundings(wMap, posX, posY):
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

    return [dN, dNE, dE, dSE, dS, dSW, dW, dNW]



#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#
#   While the river function below works, I don't particularly like what it looks like. Going to try an
#   entirely new method and see how it goes!
#
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
# #--------------------------------------------------------------------------------------------------------------
# #   [InsertRivers]
# #   Parameters: mapClass, posX, posY
# #
# #   Checks surroundings to see if a river should be placed or not.
# #   Below are cases to check. 
# #   If any cases are tabbed over, then they are dependant on the cases above them.
# #       1) Mountain @ N  : + 3 chance to draw '|'
# #       2) Mountain @ NW : + 3 chance to draw '\'
# #       3) Mountain @ NE : + 3 chance to draw '/'
# #           4) Water @ S     : + 2 chance to draw '|'
# #           5) Water @ SW    : + 2 chance to draw '/'
# #           6) Water @ SE    : + 2 chance to draw '\'
# #           7) Water @ S     : + 2 chance to draw '|'
# #           8) Water @ SW    : + 2 chance to draw '/'
# #           9) Water @ SE    : + 2 chance to draw '\'
# #       10) River @ N     : + 5 chance to draw '|'
# #       11) River @ NW    : + 5 chance to draw '\'
# #       12) River @ NE    : + 5 chance to draw '/'
# #           13) Water @ S     : 0 chance to draw a river #Let rivers flow into bodies of water!
# #           14) Water @ SW    : 0 chance to draw a river
# #           15) Water @ SE    : 0 chance to draw a river
# #       16) River @ E    : 0 chance to draw a river
# #       17) River @ W    : 0 chance to draw a river


# #       All cases are on a North to South basis.
# #       Mountain to:
# #           Water: +5
# #           Plains: +3
# #           Forest: +2
# #           Mountain: +1
# #        River to:
# #           Water: NONE
# #           Plains: +5
# #           Forest: +3
# #--------------------------------------------------------------------------------------------------------------
# def InsertRivers(mapClass, posX, posY):
#     riverOdds = [0, 0, 0]
#     riverOdds[0] = RIVER_FREQUENCY #odds for a '/' river
#     riverOdds[1] = RIVER_FREQUENCY #odds for a '|' river
#     riverOdds[2] = RIVER_FREQUENCY #odds for a '\' river
    
#     forkChance = RIVER_FORK_FREQUENCY
#     skip = False

#     #Define a list using the surrounding symbols:
#     surroundings = ScanSurroundings(mapClass.worldMap, posX, posY)
#     P = mapClass.worldMap[posY][posX]    #Current Position
#     dN = surroundings[0]
#     dNE = surroundings[1]
#     dE = surroundings[2]
#     dSE = surroundings[3]
#     dS = surroundings[4]
#     dSW = surroundings[5]
#     dW = surroundings[6]
#     dNW = surroundings[7]

#     #Increase chance of river forking in plains:
#     if P == PLAINS:
#         forkChance += 3
    
#     #If current position is a river or water, ignore it (I may have this function scan the map more than once when placing rivers)
#     if P == WATER or P == RIVER[0] or P == RIVER[1] or P == RIVER[2] or P == MOUNTAIN:
#         skip = True
#     #If there aren't any mountains or water bodies to the north, then skip.
#     elif dN != MOUNTAIN and dN != WATER and dNW != MOUNTAIN and dNW != WATER and dNE != MOUNTAIN and dNE != WATER:
#         if dN != RIVER[1] and dNW != RIVER[0] and dNW != RIVER[1] and dNE != RIVER[2] and dNE != RIVER[1]:
#             skip = True
#     if skip != True:
#         #Series of if statements checks several cases and creates a weight based on conditions:
                
#         if dNE == MOUNTAIN:
#             if dSE == WATER:
#                 riverOdds[0] += 3
#             else:
#                 riverOdds[0] += 1
#             if P == PLAINS:
#                 riverOdds[0] += 2
#             elif P == FOREST:
#                 riverOdds[0] += 1
            
#         elif dNE == WATER:
#             # if dS == WATER:
#             #     riverOdds[1] += 2
#             # else:
#             riverOdds[0] += 1
#             # if dSW == WATER:
#             #     riverOdds[0] += 5
#             # else:
#             #     riverOdds[0] += 3
#             # if dSE == WATER:
#             #     riverOdds[2] += 0
#             # else:
#             #     riverOdds[2] += 0
#             if P == PLAINS:
#                 riverOdds[0] += 2
#             elif P == FOREST:
#                 riverOdds[0] += 1
            
#             # #Water likes to flow into plains:
#             # if dW == PLAINS:
#             #     riverOdds[0] += 2
#             #     riverOdds[1] += 2
#             #     riverOdds[2] += 2
#             # if dE == PLAINS:
#             #     riverOdds[0] += 2
#             #     riverOdds[1] += 2
#             #     riverOdds[2] += 2

#         elif dNE == RIVER[0]:
#             riverOdds[0] += 5
#             riverOdds[1] += 2
#             riverOdds[2] = 0
#         elif dNE == RIVER[1]:
#             riverOdds[0] += 3
#             riverOdds[1] = 0
#             riverOdds[2] = 0
#         elif dNE == RIVER[2]:
#             riverOdds[0] = 0
#             riverOdds[1] = 0
#             riverOdds[2] = 0

#         if dNW == MOUNTAIN:
#             if dSE == WATER:
#                 riverOdds[2] += 3
#             else:
#                 riverOdds[2] += 1
#             if P == PLAINS:
#                 riverOdds[2] += 2
#             elif P == FOREST:
#                 riverOdds[2] += 1
            
#         elif dNW == WATER:
#             # if dS == WATER:
#             #     riverOdds[1] += 2
#             # else:
#             riverOdds[2] += 1
#             # if dSW == WATER:
#             #     riverOdds[0] += 0
#             # else:
#             #     riverOdds[0] += 0
#             # if dSE == WATER:
#             #     riverOdds[2] += 5
#             # else:
#             #     riverOdds[2] += 3
#             if P == PLAINS:
#                 riverOdds[2] += 2
#             elif P == FOREST:
#                 riverOdds[2] += 1

#             # #Water likes to flow into plains:
#             # if dW == PLAINS:
#             #     riverOdds[0] += 2
#             #     riverOdds[1] += 2
#             #     riverOdds[2] += 2
#             # if dE == PLAINS:
#             #     riverOdds[0] += 2
#             #     riverOdds[1] += 2
#             #     riverOdds[2] += 2

#         elif dNW == RIVER[0]:
#             riverOdds[0] = 0
#             riverOdds[1] = 0
#             riverOdds[2] = 0
#         elif dNW == RIVER[1]:
#             riverOdds[0] = 0
#             riverOdds[1] = 0
#             riverOdds[2] += 2
#         elif dNW == RIVER[2]:
#             riverOdds[0] = 0
#             riverOdds[1] += 0
#             riverOdds[2] += 5

#         if dN == WATER:
#             # if dS == WATER:
#             #     riverOdds[1] += 5
#             # else:
#             riverOdds[1] += 1
#             # if dSW == WATER:
#             #     riverOdds[0] += 5
#             # else:
#             #     riverOdds[0] += 1
#             # if dSE == WATER:
#             #     riverOdds[2] += 5
#             # else:
#             #     riverOdds[2] += 1
#             if P == PLAINS:
#                 riverOdds[1] += 2
#             elif P == FOREST:
#                 riverOdds[1] += 1
            
#         elif dN == MOUNTAIN:
#             if dS == WATER:
#                 riverOdds[1] += 3
#             else:
#                 riverOdds[1] += 1
#             # if dSW == WATER:
#             #     riverOdds[0] += 3
#             # else:
#             #     riverOdds[0] += 1
#             # if dSE == WATER:
#             #     riverOdds[2] += 3
#             # else:
#             #     riverOdds[2] += 1
#             if P == PLAINS:
#                 riverOdds[1] += 2
#             elif P == FOREST:
#                 riverOdds[1] += 1

#         elif dN == RIVER[0]:
#             riverOdds[0] = 0
#             riverOdds[1] = 0
#             riverOdds[2] += 2
#         elif dN == RIVER[1]:
#             riverOdds[0] = 0
#             riverOdds[1] += 5
#             riverOdds[2] = 0
#         elif dN == RIVER[2]:
#             riverOdds[0] += 2
#             riverOdds[1] = 0
#             riverOdds[2] = 0
        
        
#             # #Water likes to flow into plains:
#             # if dW == PLAINS:
#             #     riverOdds[0] += 2
#             #     riverOdds[1] += 2
#             #     riverOdds[2] += 2
#             # if dE == PLAINS:
#             #     riverOdds[0] += 2
#             #     riverOdds[1] += 2
#             #     riverOdds[2] += 2

#         # elif dN == RIVER[0] or dN == RIVER[1] or dN == RIVER[2]:
#         #     if P == WATER:
#         #         riverOdds[0] == 0
#         #         riverOdds[1] == 0
#         #         riverOdds[2] == 0
#         #     else:
#         #         riverOdds[0] += 3
#         #         riverOdds[1] += 5
#         #         riverOdds[2] += 3

#         #If the current position is a mountain and there are no other mountains to flow from, don't draw a river.
#         # if P == MOUNTAIN:
#         #     if dN != MOUNTAIN:
#         #         riverOdds[1] = 0
#         #         if dNE != MOUNTAIN:
#         #             riverOdds[0] = 0
#         #         if dNW != MOUNTAIN:
#         #             riverOdds[2] = 0
        
#         # #Handle river forking:
#         # if dW == RIVER[0]:
#         #     riverOdds[0] = 0                            # / / No parallel rivers.
#         #     riverOdds[1] = RIVER_FORK_FREQUENCY         # / |
#         #     riverOdds[2] = RIVER_FORK_FREQUENCY         # / \
#         # elif dW == RIVER[1]:
#         #     if dNW == MOUNTAIN and dN == MOUNTAIN:
#         #         riverOdds[0] = RIVER_FORK_FREQUENCY
#         #     else:
#         #         riverOdds[0] = 0                        # | / This sort of formation is very specific.
#         #     riverOdds[1] = 0                            # | | No parallel rivers. 
#         #     riverOdds[2] = RIVER_FORK_FREQUENCY         # | \
#         # elif dW == RIVER[2]:
#         #     if dNW == MOUNTAIN and dN == MOUNTAIN:
#         #         riverOdds[0] = RIVER_FORK_FREQUENCY
#         #     else:
#         #         riverOdds[0] = 0                        # \ / This sort of formation is very specific.
#         #     if dNW == MOUNTAIN and dN == MOUNTAIN:
#         #         riverOdds[1] = RIVER_FORK_FREQUENCY
#         #     else:
#         #         riverOdds[1] = 0                        # \ | This sort of formation is very specific.
#         #     riverOdds[2] = 0                            # \ \ No parallel rivers.
        
#         # #This only comes into play after subsequent runs through this function.
#         # if dE == RIVER[0]:
#         #     riverOdds[0] = 0                            # / /
#         #     if dNW == MOUNTAIN and dN == MOUNTAIN:
#         #         riverOdds[1] = RIVER_FORK_FREQUENCY
#         #     else:
#         #         riverOdds[1] = 0                        # | /
#         #     if dNE == MOUNTAIN and dN == MOUNTAIN:
#         #         riverOdds[2] = RIVER_FORK_FREQUENCY
#         #     else:
#         #         riverOdds[2] = 0                        # \ /
#         # elif dE == RIVER[1]:
#         #     riverOdds[0] = RIVER_FORK_FREQUENCY         # / |
#         #     riverOdds[1] = 0                            # | |
#         #     if dNE == MOUNTAIN and dN == MOUNTAIN:
#         #         riverOdds[2] = RIVER_FORK_FREQUENCY
#         #     else:
#         #         riverOdds[2] = 0                        # \ |
#         # elif dE == RIVER[2]:
#         #     riverOdds[0] = RIVER_FORK_FREQUENCY         # / \
#         #     riverOdds[1] = RIVER_FORK_FREQUENCY         # | \
#         #     riverOdds[2] = 0                            # \ \

#     # print('Odds of / are: [' + str(riverOdds[0]) + '] Odds of | are: [' + str(riverOdds[1]) + '] Odds of \\ are: [' + str(riverOdds[2]) + ']')

#     if dN != MOUNTAIN and dN != WATER and dNW != MOUNTAIN and dNW != WATER and dNE == MOUNTAIN:
#         riverOdds[1] = 0
#         riverOdds[2] = 0
#     elif dN != MOUNTAIN and dN != WATER and dNW != MOUNTAIN and dNW != WATER and dNE == WATER:
#         riverOdds[1] = 0
#         riverOdds[2] = 0
#     elif dN != MOUNTAIN and dN != WATER and dNE != MOUNTAIN and dNE != WATER and dNW == MOUNTAIN:
#         riverOdds[1] = 0
#         riverOdds[0] = 0
#     elif dN != MOUNTAIN and dN != WATER and dNE != MOUNTAIN and dNE != WATER and dNW == WATER:
#         riverOdds[1] = 0
#         riverOdds[0] = 0

#     RiverAverageWeight(riverOdds)

#     if skip == False:
#         symbolTable = [(RIVER[0], riverOdds[0]), (RIVER[1], riverOdds[1]), (RIVER[2], riverOdds[2]), (P, RIVER_RATIO)]

#         #Define a combined list of symbols and weights, including the RANDOM option.
#         #symbolTable = [(dN,weights[0]),(dNE,weights[1]),(dE,weights[2]),(dSE,weights[3]),(dS,weights[4]),(dSW,weights[5]),(dW,weights[6]),(dNW,weights[7]), (RANDOM,RANDOM_INTENSITY)]

#         #Define a table to extend values based on weights and pull a random choice from it
#         pointTable = []
#         for item, weight in symbolTable:
#             pointTable.extend([item]*weight)
#         newPoint = random.choice(pointTable)

#         #Add river if new point isn't P:
#         if newPoint != P:
#             mapClass.worldMap[posY][posX] = newPoint

#     #Return the symbol
#     # return newPoint


# #--------------------------------------------------------------------------------------------------------------
# #   [RiverAverageWeightCalculator]
# #   Parameters: weights
# #   Adds to river average weight total global variable
# #--------------------------------------------------------------------------------------------------------------
# def RiverAverageWeight(weights):
#     global RIVER_AVERAGE_WEIGHT
#     totalWeight = weights[0] + weights[1] + weights[2]
#     averageWeight = totalWeight * 0.33
#     RIVER_AVERAGE_WEIGHT += averageWeight

# #--------------------------------------------------------------------------------------------------------------
# #   [SequentiallyAddRivers]
# #   Parameters: wMap, posX, posY
# #
# #   A visual char-by-char generation rivers
# #--------------------------------------------------------------------------------------------------------------
# def SequentiallyAddRivers(wMap, posX, posY):
#     for i in range(MAP_HEIGHT):
#         for j in range(MAP_WIDTH):
#             if i == posY and j == posX:
#                 print(CYAN + wMap[i][j] + RESET, end=" ")
#             else:
#                 print(wMap[i][j], end=" ")
#         print('')
#     time.sleep(0.1)

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#                                           New River Method
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#   [DefineRiverSource]
#   Parameters: mapClass, posX, posY, scanLevel
#
#   Scans the map in search of an ideal river source, drawing one consistent river when one is found.
#--------------------------------------------------------------------------------------------------------------
def DefineRiverSource(mapClass, posX, posY, scanLevel):
    # global RIVER_COUNT
    global RIVER_COORDS_0
    global RIVER_COORDS_1
    global RIVER_COORDS_2
    #Define a list using the surrounding symbols:
    surroundings = ScanSurroundings(mapClass.worldMap, posX, posY)
    P = mapClass.worldMap[posY][posX]    #Current Position
    dN = surroundings[0]
    dNE = surroundings[1]
    dE = surroundings[2]
    dSE = surroundings[3]
    dS = surroundings[4]
    dSW = surroundings[5]
    dW = surroundings[6]
    dNW = surroundings[7]

    #River source just needs to have a mountain to the north and something else (besides water) below it.
    #If an ideal source is found, then that should be picked over others. 
    #An ideal source looks like something below:
    
    #       M M -
    #       M - -
    #       - - -

    #Here, the river source could start at the corner of these mountains like below:

    #       M M -
    #       M \ -
    #       - - -

    #There are two ideal sources, and preferably they're closer to the top of the map. 
    #First, scan map for an ideal source.
    #If none are found, then move on.

    
    if NoAdjacentRivers(surroundings) and P!= MOUNTAIN and P!= WATER and dS != MOUNTAIN and dS != WATER:
        # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
        # scanLevel 0:
        # Checks the map for the following two formations:
        #       M M ?           ? M M
        #       M - -           - - M
        #       ? - -           - - ?
        # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
        # if scanLevel == 0 and RIVER_COUNT < RIVER_CAP:    #I may do away with the river cap and instead have this function pick coordinates and compile them into a list
        if scanLevel == 0:
            if dN == MOUNTAIN: # and dS != MOUNTAIN and dS != WATER:
                #   M M ?
                #   M \ -
                #   ? - -
                if dNW == MOUNTAIN and dW == MOUNTAIN and dSE != MOUNTAIN and dSE != WATER and dE != MOUNTAIN and dE != WATER:
                    print('Ideal southeast-bound source point found! ' + str(posY) + ' ' + str(posX))
                    # mapClass.worldMap[posY][posX] = '\\'
                    # RIVER_COUNT += 1
                    RIVER_COORDS_0.append(RIVER[2], int(posY), int(posX))

                #   ? M M
                #   - / M
                #   - - ?
                elif dNE == MOUNTAIN and dE == MOUNTAIN and dSW != MOUNTAIN and dSW != WATER and dW != MOUNTAIN and dW != WATER:
                    print('Ideal southwest-bound source point found! ' + str(posY) + ' ' + str(posX))
                    # mapClass.worldMap[posY][posX] = '/'
                    # RIVER_COUNT += 1
                    RIVER_COORDS_0.append(RIVER[0], int(posY), int(posX))
        # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
        # scanLevel 1:
        # Next, need to define what happens when the river source above was too specific. Once here, this is the phase that should be fairly sure to find a source.
        # Here, we'll be looking for any coupled mountains in the following formations:
        #       M M ?       ? M M       M ? ?       ? ? M
        #       ? \ -       - / ?       M \ -       - / M
        #       ? - -       - - ?       ? - -       - - ?
        # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
        # if scanLevel == 1 and RIVER_COUNT < RIVER_CAP:
        if scanLevel == 1:
            if dN == MOUNTAIN: # and dS != MOUNTAIN and dS != WATER:
                if dNW == MOUNTAIN:
                    #   M M ?       M M ?
                    #   ? \ -       ? | -
                    #   ? - -       ? - -
                    if dSE != MOUNTAIN and dSE != WATER and dE != MOUNTAIN and dE != WATER:
                        print('Second-best south-east bound source point found! ' + str(posY) + ' ' + str(posX))
                        RIVER_COORDS_1.append(RIVER[2], int(posY), int(posX))
                        #RIVER_COORDS_1.append(RIVER[1], int(posY), int(posX)) #Leave this uncommented if you want the alternate | river version thronw in the mix! --For now, I'll avoid this

                elif dNE == MOUNTAIN:
                    #   ? M M       ? M M
                    #   - / ?       - | ?
                    #   - - ?       - - ?
                    if dSW != MOUNTAIN and dSW != WATER and dW != MOUNTAIN and dW != WATER:
                        print('Second-best south-west bound source point found! ' + str(posY) + ' ' + str(posX))
                        RIVER_COORDS_1.append(RIVER[0], int(posY), int(posX))
                        #RIVER_COORDS_1.append(RIVER[1], int(posY), int(posX)) #Leave this uncommented if you want the alternate | river version thronw in the mix! --For now, I'll avoid this
            #   M ? ?
            #   M \ -
            #   ? - -
            elif dNW == MOUNTAIN and dW == MOUNTAIN and dSE != MOUNTAIN and dSE != WATER and dE != MOUNTAIN and dE != WATER:
                print('Second-best south-east bound source point found! ' + str(posY) + ' ' + str(posX))
                RIVER_COORDS_1.append(RIVER[2], int(posY), int(posX))

            #   ? ? M
            #   - / M
            #   - - ?
            elif dNE == MOUNTAIN and dE == MOUNTAIN and dSW != MOUNTAIN and dSW != WATER and dW != MOUNTAIN and dW != WATER:
                print('Second-best south-west bound source point found! ' + str(posY) + ' ' + str(posX))
                RIVER_COORDS_1.append(RIVER[0], int(posY), int(posX))
        # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
        # scanLevel 2:
        # At this point, we'll take whatever we can get. So long as a single mountain is in the north and we have a clear shot elsewhere, we will use that. 
        # This is likely only going to come into play when the map just has very few mountains.
        # 
        #       ? M ?      M ? ?      ? ? M 
        #       ? | ?      ? \ ?      ? / ? 
        #       - - -      ? - -      - - ? 
        # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
        if scanLevel == 2:
            #   ? M ? 
            #   ? | ? 
            #   - - - 
            if dN == MOUNTAIN and dSW != MOUNTAIN and dSW != WATER and dSE != MOUNTAIN and dSE != WATER:
                print('Third-best south bound source point found! ' + str(posY) + ' ' + str(posX))
                RIVER_COORDS_2.append(RIVER[1], int(posY), int(posX))

            #   M ? ? 
            #   ? \ ? 
            #   ? - - 
            elif dNW == MOUNTAIN and dSE != MOUNTAIN and dSE != WATER:
                RIVER_COORDS_2.append(RIVER[2], int(posY), int(posX))

            #   ? ? M 
            #   ? / ? 
            #   - - ? 
            elif dNW == MOUNTAIN and dSW != MOUNTAIN and dSW != WATER:
                RIVER_COORDS_2.append(RIVER[0], int(posY), int(posX))


        #As for scanLevel == 2, that is where the rivers will actually be drawn. 
        #Alternatively, this function can just try to find the river head, then stop after finding one. 
        #Then a new function could make recursive calls to itself and actually simulate a river-flow.

# #--------------------------------------------------------------------------------------------------------------
# #   [ScanForIdealSource]
# #   Parameters: mapClass
# #
# #   Scans for an ideal river source and returns the coordinates
# #--------------------------------------------------------------------------------------------------------------
# def ScanForIdealSource(mapClass):
#     for i in range(MAP_HEIGHT):
#         for j in range(MAP_WIDTH):
#             surroundings = ScanSurroundings(mapClass.worldMap, i, j)

#--------------------------------------------------------------------------------------------------------------
#   [NoAdjacentRivers]
#   Parameters: surroundings
#   Returns: True/False
#   Looks at surroundings and reports if there is a river nearby or not.
#--------------------------------------------------------------------------------------------------------------
def NoAdjacentRivers(surroundings):
    for i in range(len(surroundings)):
        if surroundings[i] == '/' or surroundings[i] == '|' or surroundings[i] == '\\':
            return False
    return True

#--------------------------------------------------------------------------------------------------------------
#   [GenerateRivers]
#   Parameters: seed
#
#   Does the same thing as GenerateWordlMap but with no prints or user interaction
#--------------------------------------------------------------------------------------------------------------
def GenerateRivers(mapClass):
    # global RIVER_MAP_SCANS
    # global RIVER_AVERAGE_WEIGHT
    # RIVER_AVERAGE_WEIGHT = 0.0
 
    # riverSourceCoordinates = ScanForIdealSource(mapClass.worldMap)
    for i in range (SCAN_LEVEL):
        print('Scan Level:' + str(i))
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                DefineRiverSource(mapClass, y, x, i)
                # print(mapClass.worldMap[y][x], end=" ")
            print('')
        print('\n')
        PrintColorMap(mapClass.worldMap)

    print('Total matches found at scan level 0: ' + str(len(RIVER_COORDS_0)))
    print('Total matches found at scan level 1: ' + str(len(RIVER_COORDS_1)))
    print('Total matches found at scan level 2: ' + str(len(RIVER_COORDS_2)))
    # print('Total Average River Weight Value: ' + str(RIVER_AVERAGE_WEIGHT))
    # calculatedWeight = (RIVER_AVERAGE_WEIGHT/(MAP_HEIGHT*MAP_WIDTH))/RIVER_MAP_SCANS
    # print('Total Calculated Average River Weight is: ' + str(calculatedWeight))
    # print('Value for 1:1 ratio is: ' + str(int(calculatedWeight) * 3))
    mapClass.write()



#--------------------------------------------------------------------------------------------------------------
#   [WorldMapLocation]
#   Parameters: yPos, xPos, mapClass
#   Replaces current x and y position in the world map with a new icon, prints the map, then reverts the map.
#--------------------------------------------------------------------------------------------------------------
def WorldMapLocation(yPos, xPos, mapClass):
    tempIcon = mapClass.worldMap[yPos][xPos]
    mapClass.worldMap[yPos][xPos] = LOCATION
    PrintColorMap(mapClass.worldMap)
    mapClass.worldMap[yPos][xPos] = tempIcon

#--------------------------------------------------------------------------------------------------------------
#   [SilentlyGenerateWorld]
#   Parameters: mapClass
#   This function combines the other functions to silently generate the world in the background.
#--------------------------------------------------------------------------------------------------------------
def SilentlyGenerateWorld(mapClass):
    mapClass.name = 'serverMap'
    mapClass.seed = GenerateSeed()
    mapClass.height = MAP_HEIGHT
    mapClass.width = MAP_WIDTH
    # LoadingAnimation('Generating World Map')
    mapClass.worldMap = SilentlyGenerateWorldMap(mapClass.seed)
    SetBiomeCounts(mapClass)
    mapClass.write()
    # LoadingAnimation('Placing Fiefs and Strongholds')
    SilentlyPlotAllFiefs(mapClass)
    SilentlyPlotAllStrongholds(mapClass)

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