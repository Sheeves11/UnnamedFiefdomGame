import os
import worldmap
from globals import *
from tempMethods import *

os.system('clear')
loop = True
currentFief = Fiefdom()

gameTime = int(readGametime())
base = int(readBaseline())

writeWeather(str(base), gameTime)
print('\n    Reading the baseline from a file: ' + str(readBaseline()) + " degrees Fahrenheit")


while (loop):
    os.system('clear')

    
    print('\n===========================Weather Incrementor v0.0.0.0.1====================================\n')
#    print('    The current baseline temperature is: ' + readBaseline() + " degrees Fahrenheit")
#    print('\n    Getting current game time...')
#    print('    Current game time is: ' + str(gameTime))
#    print('\n        ------------------------------------------------------------------------------------        ')
    print('\n    Incrementing the current game time...')
    gameTime = readRealUnconvertedGametimeHour()
    incrementGametime( gameTime, base)
    print('    Current in-game time: ' + str(readRealGametimeHour()) + ':' + str(readRealGametimeMin()) + ' ' + str(readRealGametimeAmpm()))
    print('    Server time is now: ' + str(readRealUnconvertedGametimeHour()))
    print('\n    Incrementing the dang weather...')
    print('    The temperature is now: ' + readBaseline() + " degrees Fahrenheit")

    base = int(readBaseline())

    if readGametime() == 1:
        base = 34
        writeWeather(str(base), gameTime)

    if readGametime() == 2:
        base = 34
        writeWeather(str(base), gameTime)

    if readGametime() == 3:
        base = 33
        writeWeather(str(base), gameTime)


    if readGametime() == 4:
        base = 32
        writeWeather(str(base), gameTime)

    if readGametime() == 5:
        base = 32
        writeWeather(str(base), gameTime)

    if readGametime() == 6:
        base = 32
        writeWeather(str(base), gameTime)

    if readGametime() == 7:
        base = 31
        writeWeather(str(base), gameTime)

    if readGametime() == 8:
        base = 44
        writeWeather(str(base), gameTime)

    if readGametime() == 9:
        base = 50
        writeWeather(str(base), gameTime)

    if readGametime() == 10:
        base = 55
        writeWeather(str(base), gameTime)

    if readGametime() == 11:
        base = 56
        writeWeather(str(base), gameTime)

    if readGametime() == 12:
        base = 57
        writeWeather(str(base), gameTime)

    if readGametime() == 13:
        base = 58
        writeWeather(str(base), gameTime)

    if readGametime() == 14:
        base = 59
        writeWeather(str(base), gameTime)

    if readGametime() == 15:
        base = 59
        writeWeather(str(base), gameTime)

    if readGametime() == 16:
        base = 60
        writeWeather(str(base), gameTime)

    if readGametime() == 17:
        base = 61
        writeWeather(str(base), gameTime)

    if readGametime() == 18:
        base = 59
        writeWeather(str(base), gameTime)

    if readGametime() == 19:
        base = 51
        writeWeather(str(base), gameTime)

    if readGametime() == 20:
        base = 46
        writeWeather(str(base), gameTime)

    if readGametime() == 21:
        base = 44
        writeWeather(str(base), gameTime)

    if readGametime() == 22:
        base = 43
        writeWeather(str(base), gameTime)

    if readGametime() == 23:
        base = 39
        writeWeather(str(base), gameTime)

    if readGametime() == 24:
        base = 36
        writeWeather(str(base), gameTime)

    

    time.sleep(WEATHER_INTERVAL)