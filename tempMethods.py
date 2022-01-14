import os
import worldmap
#from turtle import right
from globals import *

baselineTemp = 72
weatherSystemMod = -7

weatherStronghold = Stronghold()

#===================================================================
#    put in coords and get the temp modifier from the map
#===================================================================
def getTempMod(y, x):

    #get map symbol for current location

    tempMod = 0
    if serverMap.worldMap[int(y)][int(x)] == '^':
        tempMod = -5

    if serverMap.worldMap[int(y)][int(x)] == 'M':
        tempMod = -20

    if serverMap.worldMap[int(y)][int(x)] == '~':
        tempMod = 0

    if serverMap.worldMap[int(y)][int(x)] == '/':
        tempMod = 3

    if serverMap.worldMap[int(y)][int(x)] == '|':
        tempMod = 3

    if serverMap.worldMap[int(y)][int(x)] == '\\':
        tempMod = -1

    return tempMod

#======================================================================
#      eats up coords, a temp constant, and weather modifier, and
#      gives back the actual temp of a location
#======================================================================
def getLocalTemp(y, x, baselineTemp, weatherSystemMod, baselineMod):

    tempMod = getTempMod(y, x)
    realTempMod = 0

    if (y - 1) > -1 and (y + 1) < MAP_HEIGHT:
        realTempMod = (getTempMod(y-1, x) + getTempMod(y,x) + getTempMod(y+1,x)) // 3

    if (y - 1) == -1:
        realTempMod = (getTempMod(y,x) + getTempMod(y+1,x)) // 2

    if (y + 1) == MAP_HEIGHT:
        realTempMod = (getTempMod(y,x) + getTempMod(y-1,x)) // 2

    realTemp = realTempMod + baselineTemp + weatherSystemMod + baselineMod

    return realTemp

#==============================================================================
#    This method takes a temperature value in and outputs that value in color,
#    with the correct spacing so that the map remains square
#==============================================================================

def printWeatherMapChar(realTemp):
    #print actual temps in color
    if realTemp > 70 and realTemp < 90:
        print(textColor.RED, end = '')
        print(str(realTemp), end = '')
        print(textColor.RESET, end = '   ')

    if realTemp > 60 and realTemp <= 70:
        print(textColor.ORANGE, end = '')
        print(str(realTemp), end = '')
        print(textColor.RESET, end = '   ')

    if realTemp > 50 and realTemp <= 60:
        print(textColor.YELLOW, end = '')
        print(str(realTemp), end = '')
        print(textColor.RESET, end = '   ')

    if realTemp > 40 and realTemp <= 50:
        print(textColor.GREEN, end = '')
        print(str(realTemp), end = '')
        print(textColor.RESET, end = '   ')

    if realTemp > 30 and realTemp <= 40:
        print(textColor.BLUE, end = '')
        print(str(realTemp), end = '')    
        print(textColor.RESET, end = '   ')

#====================================================================================
#     Call this method to print out a temperature baseline map
#====================================================================================


def printTempMap(baselineMod):
    for i in range(MAP_HEIGHT):
            for j in range(MAP_WIDTH):
                symbol = serverMap.worldMap[i][j]
                if j == 0:
                    print('    ')
                    printWeatherMapChar(getLocalTemp(i, j, baselineTemp, weatherSystemMod, baselineMod))

                else:
                    printWeatherMapChar(getLocalTemp(i,j, baselineTemp, weatherSystemMod, baselineMod))
                
            print('')

#==============================================================================
#    This method takes a temperature value in and outputs that value in color,
#    with the correct spacing so that the map remains square (dot version)
#==============================================================================

def printWeatherMapDot(realTemp):
    #print actual temps in color
    if realTemp > 70 and realTemp < 90:
        print(textColor.RED, end = '')
        print("*", end = '')
        print(textColor.RESET, end = ' ')

    if realTemp > 60 and realTemp <= 70:
        print(textColor.ORANGE, end = '')
        print('*', end = '')
        print(textColor.RESET, end = ' ')

    if realTemp > 50 and realTemp <= 60:
        print(textColor.YELLOW, end = '')
        print('*', end = '')
        print(textColor.RESET, end = ' ')

    if realTemp > 40 and realTemp <= 50:
        print(textColor.GREEN, end = '')
        print('*', end = '')
        print(textColor.RESET, end = ' ')

    if realTemp > 30 and realTemp <= 40:
        print(textColor.BLUE, end = '')
        print('*', end = '')    
        print(textColor.RESET, end = ' ')

#====================================================================================
#     Call this method to print out a temperature baseline map of dots
#====================================================================================


def printTempMapDot(baselineMod):
    for i in range(MAP_HEIGHT):
            for j in range(MAP_WIDTH):
                symbol = serverMap.worldMap[i][j]
                if j == 0:
                    print('\n    ', end = ' ')
                    printWeatherMapDot(getLocalTemp(i, j, baselineTemp, weatherSystemMod, baselineMod))

                else:
                    printWeatherMapDot(getLocalTemp(i,j, baselineTemp, weatherSystemMod, baselineMod))
                
 #           print('')