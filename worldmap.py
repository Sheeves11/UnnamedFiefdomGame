import os
import time
import random
from array import *

#This is a very early development build for a world map feature.
#Not yet implemented!

#Global variables
MAP_WIDTH = 10
MAP_HEIGHT = 10
DEFAULT_WEIGHT = 1

#Map Icons
WATER = '~'
RIVER = '|'
MOUNTAIN = 'M'
PLAINS = '#'
FOREST = '^'
FIEF = 'X'
STRONGHOLD = 'H'

#Manually inserted map-grid for visualizing. It is 20x8
def ManualWorldMapSizeTest():
    print('''
        ~~~~~~~~~~~~~~~~~~~~
        ~~~##############~~~
        ~~####^##X#M##H###~~
        ~####^X^##MMM######~
        ~##^^^^^###|####X##~
        ~~###^^##X##|#####~~
        ~~~##########|###~~~
        ~~~~~~~~~~~~~~~~~~~~
    ''')

#This is the primary function for generating a world map
#Utilizes a passed 'seed' value that alters how the map is generated
#The algorithm for generating the map should do the following:
#   1. Begin at a coordinate within a 2D-array
#   2. Write a character on the map
#   3. Move to new location based on current location
#   4. Determine a character to write based on adjacent locations
#   5. Loop through steps 2-4 until map is filled (unique cases aside)
#To make the starting location not matter, the algorithm should scan
#all adjacent areas to the current coordinate before deciding on a char
#to write. If no char can be found, the algo should IDEALLY pick a random location
#and try again. If it comes down to it, a manual scan from coordinate [0,0] onward
#should be performed so no spaces are left unmarked. Additionally, this adjacency 
#check should also check diagonal coordinates so that corners are not bottle-necked
#and ignored. That should increase speed and efficiency.
#
#Fief locations will be determined later, but I'd like to have something that detects
#the name of the fief and picks a location if it, say, has "Forest" in the name. More
#on that later.
def WorldMap(seed):
    os.system('clear')

    worldMap = [['0'] * MAP_WIDTH] * MAP_HEIGHT    #Change this later if we want to do small/medium/large map presets

    seed = '00555' #ToDo: Make seed generator work
    sPosX = seed[0]
    sPosY = seed[1]
    freqMountain = seed[2]
    freqPlains = seed[3]
    freqForest = seed[4]

    symbol = FIEF
    
    loop = True
    firstLoop = True
    print('This is a test for the world map feature!')
    print('worldMap before inserting anything: \n')
    print(worldMap)
    print('\n')
    print('Inserting stuff into worldMap: \n')
    #This algorithm may be improvable. Has time-complexity O(n^2)!
    while (loop):                                   #This should keep going until the map is filled
        if firstLoop:                               #First check if this is the first loop
#            for y in range(len(worldMap[sPosY:])):          #This iterates through the height of the map from sPosY [I think]
#                for x in range(len(worldMap[y[sPosX:]])):   #This iterates through the width of the map from sPosX [I think]
#                    worldMap[x][y] = 'X'
#            for y in range(len(worldMap)):
#                for x in range(len(worldMap[y])):
#                    worldMap[x][y] = 'X'
            for y in range(MAP_HEIGHT):
                print('Pos y: ' + str(y))
                for x in range(MAP_WIDTH):
                    #print('Pos x: ' + str(x))

                    temp = plotPoint(worldMap, symbol, x, y, freqMountain, freqPlains, freqForest)
                    symbol = temp

                    worldMap[0][x] = symbol
            firstLoop = False
        loop = False

    print('Attempting to print world map below! \n')
#    for y in range(len(worldMap)):
#        for x in range(len(worldMap[y])):
#            print(worldMap[y][x])
#        print('\n')

#Prints out the map in a nicely spaced grid
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            print(worldMap[0][x], end=" ")
        #print('')
    print('\nFinished!\n')
                    
        

def plotPoint(wMap, symb, posX, posY, freqM, freqP, freqF):
    #Create points that are surrounding our current pos
    try:
        print('Current symbol: ' + symb)
    except:
        print('Current symbol: None')
    try:
        dN = wMap[posY - 1][posX]
        print('There is a ' + dN + ' to the north!')
    except:
        dN = ' '
        print('North is off the map!')
    print('Current symbol: ' + symb)
    try:
        dE = wMap[posY][posX + 1]
        print('There is a ' + dN + ' to the east!')
    except:
        dE = ' '
        print('East is off the map!')
    try:
        dW = wMap[posY][posX - 1]
        print('There is a ' + dN + ' to the west!')
    except:
        dW = ' '
        print('West is off the map!')
    try:
        dS = wMap[posY + 1][posX]
        print('There is a ' + dN + ' to the south!')
    except:
        dS = ' '
        print('South is off the map!')

    newPoint = FIEF #temporary
    return newPoint



#To Do: Write this function
def GenerateRandomSeed():
    print('\nThis does nothing!\n')

#eof