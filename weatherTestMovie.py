import os
import worldmap
#from turtle import right
from globals import *
from tempMethods import *

serverMap.name = "serverMap"
serverMap.read()


for i in [1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,17,15,11,7,4,2,-2,-3,-5,-6,-10]:
    os.system('clear')
    print('\n\n    Map Print Here:\n\n    ')
    printTempMapDot(i)
#    tempInput = input('\n\n    Press Enter to Continue')
    time.sleep(1)

os.system('clear')
