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
def getLocalTemp(y, x, baselineTemp, weatherSystemMod):

    tempMod = getTempMod(y, x)
    realTempMod = 0

    if (y - 1) > -1 and (y + 1) < MAP_HEIGHT:
        realTempMod = (getTempMod(y-1, x) + getTempMod(y,x) + getTempMod(y+1,x)) // 3

    if (y - 1) == -1:
        realTempMod = (getTempMod(y,x) + getTempMod(y+1,x)) // 2

    if (y + 1) == MAP_HEIGHT:
        realTempMod = (getTempMod(y,x) + getTempMod(y-1,x)) // 2

    realTemp = realTempMod + baselineTemp + weatherSystemMod

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


def printTempMap():
    for i in range(MAP_HEIGHT):
            for j in range(MAP_WIDTH):
                symbol = serverMap.worldMap[i][j]
                if j == 0:
                    print('    ')
                    printWeatherMapChar(getLocalTemp(i, j, baselineTemp, weatherSystemMod))

                else:
                    printWeatherMapChar(getLocalTemp(i,j, baselineTemp, weatherSystemMod))
                
            print('')



#===================================================================================
#       These are some printouts for testing the weather methods above
#===================================================================================

os.system("clear")

print('\n\n')
print('THIS IS A TEST OF THE UNNAMED FIEFDOM GAME EMERGENCY WEATHER BROADCAST SYSTEM')
print('---------------------------------------------------------------------------------------------')
print('\n\n')

#---------------fetch the current weather-------------

username = input('Enter the Stronghold where you would like to check the weather: ')

weatherStronghold.name = username
weatherStronghold.read()

print('\n\n')
print('------------------------------------Coord Checks--------------------------------------------')
print('Stronghold to check the weather at: ' + str(weatherStronghold.name))
print('Stronghold Biome: ' + str(weatherStronghold.biome))
print('Stronghold X Coord: ' + str(weatherStronghold.xCoordinate))
print('Stronghold Y Coord: ' + str(weatherStronghold.yCoordinate))
print('---------------------------------------------------------------------------------------------')
print('\n\n')

serverMap.name = "serverMap"
serverMap.read()

if serverMap.worldMap[int(weatherStronghold.yCoordinate)][int(weatherStronghold.xCoordinate)] == '^':
    tempMod = -5

if serverMap.worldMap[int(weatherStronghold.yCoordinate)][int(weatherStronghold.xCoordinate)] == 'M':
    tempMod = -20

if serverMap.worldMap[int(weatherStronghold.yCoordinate)][int(weatherStronghold.xCoordinate)] == '~':
    tempMod = 0

if serverMap.worldMap[int(weatherStronghold.yCoordinate)][int(weatherStronghold.xCoordinate)] == '/':
    tempMod = 3

if serverMap.worldMap[int(weatherStronghold.yCoordinate)][int(weatherStronghold.xCoordinate)] == '|':
    tempMod = 3

if serverMap.worldMap[int(weatherStronghold.yCoordinate)][int(weatherStronghold.xCoordinate)] == '\\':
    tempMod = -1


localTemp = tempMod + baselineTemp + weatherSystemMod


print('------------------------------Weather Calculations-------------------------------------------')
print('Baseline (Global) Temp: ' + str(baselineTemp))
print('Temp Biome Modifier: ' + str(tempMod))
print('Weather System Modifier: ' + str(weatherSystemMod))
print('Actual Temp: ' + str(localTemp))
print('---------------------------------------------------------------------------------------------')
print('\n\n')

print('------------------------------Attemping a Weather Map Print--------------------------------------')
print('\n')

printTempMap()

print('\n\n')
print('---------------------------------------------------------------------------------------------')
print('\n\n')

tempText = input('\n\n\n\n\nPress Enter To Continue: ')
