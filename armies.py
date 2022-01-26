from colors import *
from classes import *
import random

#======================================================================================
#   ::Idea Board::
#       Armies and Battalions have a similar setup to Markets and Goods.
#       The Armies class contains a list of all the Battalions in the game, so
#       they can be modified uniformly.
#       
#   Battalions:
#       These (possibly player-named) classes contain groups of warriors that can
#       traverse the world map. Battalions have a number of variables that lend to
#       a lot of strategy and gameplay mechanics, detailed below:
#
#               name :      Whatever the player decides to call the battalion (subject 
#                           to change) Can't contain some characters.
#
#               commander : Name of the player that owns it
#
#               numTroops : Number of units in the battalion
#
#               attLevel :  This will either be set up to mimic the Stronghold's 
#                           attack, or it will hold a value for each individual 
#                           battalions strength.
#
#               speed :     This determines how long it takes battalions to move
#                           along the world map.
#
#               stamina :   This determines how many moves a battalion has in a 
#                           yet to be specified time period.             
#         
#               rations :   This determines how long a battalion can be sustained
#                           for, and is replinished by using food resources.
#
#               xPos :      horizontal position on world map
#
#               yPos :      vertical position on world map
#       
#       When a battalion is created, the user must spend at least 100 units. If a 
#       battalion ever falls below 100 units, that's fine. At any point, a user may
#       disband a battalion when they're at an owned Fief or Stronghold to add those
#       troops to that locations defenses. A user cannot have more than 3 battalions
#       at any given time (subject to extension via possible stronghold upgrade).
#       Additionally, battalions have a cap of 1000 (currently) units.
#           
#   Things that need to be made:
#       - A page where the user can see and manage their battalions.
#       - A page with a map overlay (accessible from world maps) that shows where
#         active battalions are at.
#       - A function that allows users to transport troops in a battalion from one
#         coordinate on the map to another. Will require its own page too. Travel
#         system will be necessary.
#         
#======================================================================================
BATTALION_MIN = 100 #This is the min required to -create- a battalion.
BATTALION_MAX = 1000 #This is the maximum number of troops to a single battalion. Very much subject to change.

class Armies:
    battalions = []
    #==================================================================================
    #   [AddBattalion]
    #   parameters: self, name, commander, numTroops, attLevel, speed, stamina, rations, 
    #               xPos, yPos
    #       Adds a new battalion to the Armies battalions list
    #==================================================================================
    def AddBattalion(self, name, commander, numTroops, attLevel, speed, stamina, rations, xPos, yPos, invGold, invFood, invWood, invStone, invOre):
        newBattalion = Battalion(name, commander, numTroops, attLevel, speed, stamina, rations, xPos, yPos, invGold, invFood, invWood, invStone, invOre)
        self.battalions.append(newBattalion)

    #==================================================================================
    #   [ExistingName]
    #   parameters: self, name
    #   returns: True/False
    #       Compares passed name to other battalion names in battalions
    #==================================================================================
    def ExistingName(self, name):
        # self.read()
        for i in range(len(self.battalions)):
            if str(self.battalions[i].name) == str(name):
                return True
        else:
            return False
    
    #==================================================================================
    #   [GetBattalions]
    #   parameters: self
    #       Gets a list of battalions
    #==================================================================================
    def GetBattalions(self):
        batts = []
        for i in range(len(self.battalions)):
            batts.append(self.battalions[i].ListDetails())
        return batts

    #==================================================================================
    #   [GetBattalionData]
    #   parameters: self
    #       Gets a list of battalion coordinates
    #==================================================================================
    def GetBattalionData(self):
        coords = []
        for i in range(len(self.battalions)):
            coords.append((self.battalions[i].yPos, self.battalions[i].xPos, self.battalions[i].commander, self.battalions[i].name))
        return coords

    #==================================================================================
    #   [GetCommanderByLocation]
    #   parameters: self
    #       Gets a list of battalions
    #==================================================================================
    def GetCommanderByLocation(self, y, x):
        for i in range(len(self.battalions)):
            if int(self.battalions[i].yPos) == int(y) and int(self.battalions[i].xPos) == int(x):
                return self.battalions[i].commander

    #==================================================================================
    #   [GetBattalionObjects]
    #   parameters: self
    #       Gets a list of battalions
    #==================================================================================
    def GetBattalionObjects(self):
        batts = []
        for i in range(len(self.battalions)):
            batts.append(self.battalions[i])
        return batts

    #==================================================================================
    #   [GetBattalion]
    #   parameters: self, index
    #       Returns a Battalion object at passed index
    #==================================================================================
    def GetBattalion(self, index):
        return self.battalions[index]

    #==================================================================================
    #   [GetBattalionByName]
    #   parameters: self, name
    #       Returns a Battalion object at passed index
    #==================================================================================
    def GetBattalion(self, name):
        for i in range(len(self.battalions)):
            if self.battalions[i].name == name:
                return self.battalions[i]

    #==================================================================================
    #   [RemoveBattalion]
    #   parameters: self, index
    #       Removes Battalion at index from the battalions list.
    #==================================================================================
    def RemoveBattalion(self, bat):
        for i in range(len(self.battalions)):
            if bat == self.battalions[i]:
                self.battalions.pop(i)
        self.write()

    #==================================================================================
    #   [RemoveBattalion]
    #   parameters: self, index
    #       Removes Battalion at index from the battalions list.
    #==================================================================================
    def SetBattalionCoords(self, bat, direction):
        for i in range(len(self.battalions)):
            if bat == self.battalions[i]:
                if direction == 'n':
                    self.battalions[i].yPos = str(int(self.battalions[i].yPos) - 1)
                elif direction == 'ne':
                    self.battalions[i].yPos = str(int(self.battalions[i].yPos) - 1)
                    self.battalions[i].xPos = str(int(self.battalions[i].xPos) + 1)
                elif direction == 'e':
                    self.battalions[i].xPos = str(int(self.battalions[i].xPos) + 1)
                elif direction == 'se':
                    self.battalions[i].yPos = str(int(self.battalions[i].yPos) + 1)
                    self.battalions[i].xPos = str(int(self.battalions[i].xPos) + 1)
                elif direction == 's':
                    self.battalions[i].yPos = str(int(self.battalions[i].yPos) + 1)
                elif direction == 'sw':
                    self.battalions[i].yPos = str(int(self.battalions[i].yPos) + 1)
                    self.battalions[i].xPos = str(int(self.battalions[i].xPos) - 1)
                elif direction == 'w':
                    self.battalions[i].xPos = str(int(self.battalions[i].xPos) - 1)
                elif direction == 'nw':
                    self.battalions[i].yPos = str(int(self.battalions[i].yPos) - 1)
                    self.battalions[i].xPos = str(int(self.battalions[i].xPos) - 1)

        self.write()

    #==================================================================================
    #   [write]
    #==================================================================================
    def write(self):
        armiesFile = 'armies/serverArmies.txt'
        try:
            with open(armiesFile, 'w') as f:
                f.write(str("["))
                for i in range(len(self.battalions)):
                    f.write(str("["))
                    f.write("('" + str(self.battalions[i].name) + "'), ")
                    f.write("('" + str(self.battalions[i].commander) + "'), ")
                    f.write("('" + str(self.battalions[i].numTroops) + "'), ")
                    f.write("('" + str(self.battalions[i].attLevel) + "'), ")
                    f.write("('" + str(self.battalions[i].speed) + "'), ")
                    f.write("('" + str(self.battalions[i].stamina) + "'), ")
                    f.write("('" + str(self.battalions[i].rations) + "'), ")
                    f.write("('" + str(self.battalions[i].xPos) + "'), ")
                    f.write("('" + str(self.battalions[i].yPos) + "'),")
                    f.write("('" + str(self.battalions[i].invGold) + "'),")
                    f.write("('" + str(self.battalions[i].invFood) + "'),")
                    f.write("('" + str(self.battalions[i].invWood) + "'),")
                    f.write("('" + str(self.battalions[i].invStone) + "'),")
                    f.write("('" + str(self.battalions[i].invOre) + "')")
                    if i < len(self.battalions) - 1:
                        f.write(str("], "))
                    else:
                        f.write(str("]"))
                f.write(str("]"))
        except:
            print('Could not write armies file!')
            pass

    #==================================================================================
    #   [read]
    #==================================================================================
    def read(self):
        armiesFile = 'armies/serverArmies.txt'
        self.battalions = []
        try:
            readArmiesFile = open(armiesFile, 'r')
            rL = eval(readArmiesFile.read())
            readArmiesFile.close()

            for i in range(len(rL)):
                self.AddBattalion(str(rL[i][0]), str(rL[i][1]), str(rL[i][2]), str(rL[i][3]), str(rL[i][4]), str(rL[i][5]), str(rL[i][6]), str(rL[i][7]), str(rL[i][8]), str(rL[i][9]), str(rL[i][10]), str(rL[i][11]), str(rL[i][12]), str(rL[i][13]))

        except:
            # print('Could not read armies file!')
            pass

class Battalion:
    name = "Default Battalion"
    commander = "Default Commander"
    numTroops = "0"
    attLevel = "0"
    speed = "0"
    stamina = "0"
    rations = "0"
    xPos = "0"
    yPos = "0"
    invGold = "0"
    invFood = "0"
    invWood = "0"
    invStone = "0"
    invOre = "0"

    def __init__(self, name, commander, numTroops, attLevel, speed, stamina, rations, xPos, yPos, invGold, invFood, invWood, invStone, invOre):
        self.name = name
        self.commander = commander
        self.numTroops = numTroops
        self.attLevel = attLevel
        self.speed = speed
        self.stamina = stamina
        self.rations = rations
        self.xPos = xPos
        self.yPos = yPos
        self.invGold = invGold
        self.invFood = invFood
        self.invWood = invWood
        self.invStone = invStone
        self.invOre = invOre

    def ListDetails(self):
        name = str("    name: " + str(self.name))
        commander = str(" commander: " + str(self.commander))
        numTroops = str(" numTroops: " + str(self.numTroops))
        attLevel = str(" attLevel: " + str(self.attLevel))
        speed = str(" speed: " + str(self.speed))
        stamina = str(" stamina: " + str(self.stamina))
        rations = str(" rations: " + str(self.rations))
        xPos = str(" xPos: " + str(self.xPos))
        yPos = str(" yPos: " + str(self.yPos))
        invGold = str(" Gold: " + str(self.invGold))
        invFood = str(" Food: " + str(self.invFood))
        invWood = str(" Wood: " + str(self.invWood))
        invStone = str(" Stone: " + str(self.invStone))
        invOre = str(" Ore: " + str(self.invOre))

        return str(name + commander + numTroops + attLevel + speed + stamina + rations + xPos + yPos + invGold + invFood + invWood + invStone + invOre)

    def MenuBar(self, userStronghold):
        SHC = StrongholdColor(userStronghold.color)
        name = str("{ " + SHC + str(self.name) + RESET + " }")
        # commander = str(" commander: " + str(self.commander))
        numTroops = str(" | Warriors: " + COLOR_WARRIOR + str(self.numTroops) + RESET)
        attLevel = str(" | Attack: " + MAGENTA + str(self.attLevel) + RESET)
        speed = str(" | Speed: " + LIME + str(self.speed) + RESET)
        stamina = str(" | Stamina: " + YELLOW + str(self.stamina) + RESET)
        # rations = str(" | Rations: " + C_FOOD + str(self.rations) + RESET)
        xPos = str(" | X: " + RED_GRAY + str(self.xPos) + RESET)
        yPos = str(" | Y: " + RED_GRAY + str(self.yPos) + RESET)

        return str(name + numTroops + attLevel + speed + stamina + xPos + yPos)

    def MenuBarWithLocation(self, userStronghold, location):
        SHC = StrongholdColor(userStronghold.color)
        name = str("{ " + SHC + str(self.name) + RESET + " }")
        # commander = str(" commander: " + str(self.commander))
        numTroops = str(" | Warriors: " + COLOR_WARRIOR + str(self.numTroops) + RESET)
        attLevel = str(" | Attack: " + MAGENTA + str(self.attLevel) + RESET)
        speed = str(" | Speed: " + LIME + str(self.speed) + RESET)
        stamina = str(" | Stamina: " + YELLOW + str(self.stamina) + RESET)
        # rations = str(" | Rations: " + C_FOOD + str(self.rations) + RESET)
        # xPos = str(" | X: " + RED_GRAY + str(self.xPos) + RESET)
        # yPos = str(" | Y: " + RED_GRAY + str(self.yPos) + RESET)
        # loc = str(" | Location: " + RED_GRAY + location)
        loc = str(" | " + location)

        return str(name + numTroops + attLevel + speed + stamina + loc)

    def Inventory(self):
        invGold = str("| Gold: " + C_GOLD + str(self.invGold) + RESET)
        invFood = str(" | Food: " + C_FOOD + str(self.invFood) + RESET)
        invWood = str(" | Wood: " + C_WOOD + str(self.invWood) + RESET)
        invStone = str(" | Stone: " + C_STONE + str(self.invStone) + RESET)
        invOre = str(" | Ore: " + C_ORE + str(self.invOre) + RESET + " |")

        return str(invGold + invFood + invWood + invStone + invOre)

    def PrintGold(self):
        return str(C_GOLD + str(self.invGold) + RESET)
    def PrintFood(self):
        return str(C_FOOD + str(self.invFood) + RESET)
    def PrintWood(self):
        return str(C_WOOD + str(self.invWood) + RESET)
    def PrintStone(self):
        return str(C_STONE + str(self.invStone) + RESET)
    def PrintOre(self):
        return str(C_ORE + str(self.invOre) + RESET)


