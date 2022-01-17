from colors import *

#==================================================================================
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
#               name : Whatever the player decides to call the battalion (subject 
#                      to change)
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
#==================================================================================
BATTALION_MIN = 10

class Armies:
    battalions = []
    #==================================================================================
    #   [AddBattalion]
    #   parameters: self, name, commander, numTroops, attLevel, speed, stamina, rations, 
    #               xPos, yPos
    #       Adds a new battalion to the Armies battalions list
    #==================================================================================
    def AddBattalion(self, name, commander, numTroops, attLevel, speed, stamina, rations, xPos, yPos):
        newBattalion = Battalion(name, commander, numTroops, attLevel, speed, stamina, rations, xPos, yPos)
        self.battalions.append(newBattalion)
    
    #==================================================================================
    #   [GetBattalions] NOTE - [WIP]
    #   parameters: self
    #       Gets a list of battalions   
    #==================================================================================
    def GetBattalions(self):
        battalions = []
        # for i in range(len(self.battalions)):
            # battalions.append(self.battalions[i].ListDetails())
        return battalions

    #==================================================================================
    #   [GetBattalion]
    #   parameters: self, index
    #       Returns a Battalion object at passed index
    #==================================================================================
    def GetBattalion(self, index):
        return self.battalions[index]

    #==================================================================================
    #   [RemoveBattalion]
    #   parameters: self, index
    #       Removes Battalion at index from the battalions list.
    #==================================================================================
    def RemoveBattalion(self, index):
        self.battalions.pop(index)
        self.write()

    #==================================================================================
    #   [write]
    #==================================================================================
    def write(self):
        armiesFile = 'armies/serverArmies.txt'
        #If no file has been made yet:
        try:
            with open(armiesFile, 'x') as f:
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
                    f.write("('" + str(self.battalions[i].yPos) + "')")
                    if i < len(self.battalions) - 1:
                        f.write(str("], "))
                    else:
                        f.write(str("]"))
                f.write(str("]"))
        except:
            pass
        #If file has already been made:
        try:
            with open(armiesFile, 'x') as f:
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
                    f.write("('" + str(self.battalions[i].yPos) + "')")
                    if i < len(self.battalions) - 1:
                        f.write(str("], "))
                    else:
                        f.write(str("]"))
                f.write(str("]"))
        except:
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
                self.AddBattalion(str(rL[i][0]), str(rL[i][1]), str(rL[i][2]), str(rL[i][3]), str(rL[i][4]), str(rL[i][5]), str(rL[i][6]), str(rL[i][7]), str(rL[i][8]))

        except:
            print('Could not read armies file!')
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

    def __init__(self, name, commander, numTroops, attLevel, speed, stamina, rations, xPos, yPos):
        self.name = name
        self.commander = commander
        self.numTroops = numTroops
        self.attLevel = attLevel
        self.speed = speed
        self.stamina = stamina
        self.rations = rations
        self.xPos = xPos
        self.yPos = yPos

