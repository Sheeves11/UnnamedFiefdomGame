import os
import time
import random
from array import *

#Global variables
MAP_WIDTH = 20
MAP_HEIGHT = 8
DEFAULT_WEIGHT = 1

#Map Icons
WATER = '~'
RIVER = '|'
MOUNTAIN = 'M'
PLAINS = '#'
FOREST = '^'
FIEF = 'X'
STRONGHOLD = 'H'

#Manually inserted map-grid for visualizing the size above
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

    worldMap = [[None] * MAP_WIDTH] * MAP_HEIGHT    #Change this later if we want to do small/medium/large map presets
    seed = '00555' #ToDo: Make seed generator work
    sPosX = seed[0]
    sPosY = seed[1]
    freqMountain = seed[2]
    freqPlains = seed[3]
    freqForest = seed[4]
    
    loop = True
    firstLoop = True
    
    print('This is a test for the world map feature!')
    #This algorithm may be improvable. Has time-complexity O(n^2)!
    while (loop):                                   #This should keep going until the map is filled
        if firstLoop:                               #First check if this is the first loop
            for y in range(len(worldMap[sPosY:])):          #This iterates through the height of the map from sPosY [I think]
                for x in range(len(worldMap[y[sPosX:]])):   #This iterates through the width of the map from sPosX [I think]
                    worldMap[x][y] = 'X'
        loop = false

    print('Attempting to print world map below! \n')
    for y in range(len(worldMap)):
        for x in range(len(worldMap[y])):
            print(worldMap[x][y])
        print('\n')

    print('\nFinished!\n')
                    
        



#To Do: Write this function
def GenerateRandomSeed():