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
MAP_WIDTH = 40
MAP_HEIGHT = 40
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