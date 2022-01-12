from os.path import exists
from classes import *
from worldmap import *
from passages import *
from art import *

#Most files should import this file.
#Doing so grants access to classes, art, and worldmap as well.

#Globals
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

serverMap = Map()
testMap = TestMap() #This is for users to have fun messing with the map generator
firstMapRead = True
newUserAccount = False


#------------------------------------------------------------------------------
#   The following functions don't really have a proper home.
#------------------------------------------------------------------------------
def FirstLaunch():
    try:
        with open('settings.txt', 'r+') as settingsFile:
            # print('Opened settings.txt')
            line = settingsFile.readline().strip()
            if line.endswith('no'):
                # print('Settings.txt ends with no.')
                settingsFile.seek(0)
                # print('Attempting to write over line')
                settingsFile.write('Map Initialized: yes')
                # print('Wrote over the line!')
                settingsFile.close()
                return True
            else:
                # print('Settings did not end in no!')
                settingsFile.close()
                return False
    except:
        print('Error, something wrong with settings.txt!')
        return False


def CheckLegalUsername(username):
    illegalUserNames = ['', ' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
    if username.strip() == "":
        return False
    for i in range(len(illegalUserNames)):
        if username == illegalUserNames[i]:
            return False
    return True

def printFiefArt(attackFief):
    if attackFief.biome == str('^'):
            art_forest()
        
    if attackFief.biome == str('M'):
        art_mountain()
    
    if attackFief.biome == str('#'):
        art_plains()

    if attackFief.defLevel == str(0):
        art_fief0(attackFief.biome)

    if attackFief.defLevel == str(1):
        art_fief1(attackFief.biome)

    if attackFief.defLevel == str(2):
        art_fief2(attackFief.biome)

    if attackFief.defLevel == str(3):
        art_fief3(attackFief.biome)

    if attackFief.defLevel == str(4):
        art_fief4(attackFief.biome)

    if attackFief.defLevel == str(5):
        art_fief5(attackFief.biome)

    if attackFief.defLevel == str(6):
        art_fief6(attackFief.biome)

    if attackFief.goldMod == str(1):
        art_farm0()

    if attackFief.goldMod == str(2):
        art_farm1()

    if attackFief.goldMod == str(3):
        art_farm2()

    if attackFief.goldMod == str(4):
        art_farm3()

    if attackFief.goldMod == str(5):
        art_farm4()

    if attackFief.goldMod == str(6):
        art_farm5()

    if attackFief.goldMod == str(7):
        art_farm6()