from classes import *
from worldmap import *

#global variables
loop = True
currentUsername = 'default'
# tempName = {}
STRONGHOLD = True           #Used to differentiate strongholds/fiefs
USER_STRONGHOLD = True      #Used to differentiate attack/user strongholds

#fiefdom page variables
LINES_PER_PAGE = 15         #The number of fiefs/strongholds that appear in the list
currentPage = 1             #Used to keep track of the page the user should be on
userFiefCount = 0           #Used to keep track of how many fiefs the user controls.

#hourly production values
#these should be changed to match the values in fiefdombackend.py
goldOutput = 100
defenderOutput = 3

#create some default objects that we'll write over later
attackFief = Fiefdom()
userStronghold = Stronghold()
attackStronghold = Stronghold()
serverMap = Map()
testMap = TestMap() #This is for users to have fun messing with the map generator
firstMapRead = True
newUserAccount = False