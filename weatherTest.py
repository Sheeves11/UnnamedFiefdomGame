import os
from globals import *

baselineTemp = 72
weatherSystemMod = -7

weatherStronghold = Stronghold()

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


def getLocalTemp(y, x, baselineTemp, weatherSystemMod):

    #get map symbol for current location
#    symbol = serverMap.worldMap[y][x]
    symbol = 'W'

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

    realTemp = tempMod + baselineTemp + weatherSystemMod

    #assign colors based on temp
    if realTemp > 70 and realTemp < 90:
        print(textColor.RED, end = '')
        print(str(symbol), end = '')
        print(textColor.RESET, end = '  ')

    if realTemp > 60 and realTemp <= 70:
        print(textColor.ORANGE, end = '')
        print(str(symbol), end = '')
        print(textColor.RESET, end = '  ')

    if realTemp > 50 and realTemp <= 60:
        print(textColor.YELLOW, end = '')
        print(str(symbol), end = '')
        print(textColor.RESET, end = '  ')

    if realTemp > 40 and realTemp <= 50:
        print(textColor.GREEN, end = '')
        print(str(symbol), end = '')
        print(textColor.RESET, end = '  ')

    if realTemp > 30 and realTemp <= 40:
        print(textColor.BLUE, end = '')
        print(str(symbol), end = '')    
        print(textColor.RESET, end = '  ')

    
#    print(str(realTemp), end = ' ')    



print('------------------------------Weather Calculations-------------------------------------------')
print('Baseline (Global) Temp: ' + str(baselineTemp))
print('Temp Biome Modifier: ' + str(tempMod))
print('Weather System Modifier: ' + str(weatherSystemMod))
print('Actual Temp: ' + str(localTemp))
print('---------------------------------------------------------------------------------------------')
print('\n\n')

print('------------------------------Attemping a Temp Map Print--------------------------------------')
print('\n')

#for i in serverMap.worldMap[i][5]:
#    print(str(serverMap.worldMap[i][5]))
#    print(' ')

for i in range(MAP_HEIGHT):
        for j in range(MAP_WIDTH):
            symbol = serverMap.worldMap[i][j]
            if j == 0:
                print('    ')
                getLocalTemp(i, j, baselineTemp, weatherSystemMod)

            else:
                getLocalTemp(i,j, baselineTemp, weatherSystemMod)
               
        print('')








#for i in range(MAP_HEIGHT):             #Iterate through each row of the map
#    for j in range(MAP_WIDTH):          #Iterate through each symbol in the row
#        if j == 0 and i != 0:
#            print(str(serverMap.worldMap[i][j]))
#        else:
#            print(str(serverMap.worldMap[i][j]), end = " ")
#print('')

print('\n\n')
print('---------------------------------------------------------------------------------------------')
print('\n\n')

#coords = serverMap.worldMap[-7][-34]
#print('\nTrying to read the coords at 7,34: ' + str(coords))



tempText = input('\n\n\n\n\nPress Enter To Continue: ')
