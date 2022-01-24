#=================================================
#=================================================
#                    Colors
#=================================================
#=================================================

#define some text colors
#I want to start weeding out the use of this. 
#Initially I liked the idea of having a class for colors,
#and it may still not be a bad idea, but I think it's easier
#to just type the color and makes for less text in those long
#strings that tend to happen. 
class textColor:
    RED = '\033[91m'
    DARK_RED = "\033[31m"
    GREEN = '\033[92m'
    DARK_GREEN = "\033[32m"
    RESET = '\033[0m'
    DIM = '\033[2m'
    MAGENTA = '\033[95m'
    DARK_MAGENTA = "\033[35m"
    BLUE = '\033[94m'
    DARK_BLUE = "\033[34m"
    CYAN = '\033[96m'
    TEAL = "\033[36m"
    WARNING = '\033[93m'
    YELLOW = '\033[33m'
    DARK_GRAY = '\033[90m'
    LIGHT_GRAY = '\033[37m'
    PURPLE = "\033[0;95m"
    ORANGE = "\u001b[38;5;208m"
    BROWN = "\u001b[38;5;216m"
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#More, lazier color definitions.
#Some of the original colors were changed in this last update.
#I've commented them out instead of removing them entirely -SW
RED = '\033[91m'
ORANGE = "\u001b[38;5;208m"
PINK = "\033[38;5;213m"
LAVENDER = "\033[38;5;140m"
INDIGO = "\033[38;5;19m"    #Too Dark
PURPLE = "\033[38;5;57m"
SCARLET = "\033[38;5;196m"
BRIGHT_YELLOW = "\033[38;5;229m"
BLUE_GRAY = "\033[38;5;104m"
RED_GRAY = "\033[38;5;131m"
SALMON = "\033[38;5;203m"
MINT = "\033[38;5;157m"
LIME = "\033[38;5;76m"
SAGE = "\033[38;5;108m"
BROWN = "\u001b[38;5;94m"
# DARK_RED = "\033[31m"
DARK_RED = "\033[38;5;88m"
GREEN = '\033[92m'
# DARK_GREEN = "\033[32m"
DARK_GREEN = "\033[38;5;22m"
RESET = '\033[0m'
# MAGENTA = '\033[95m'
MAGENTA = "\033[35m"
DARK_MAGENTA = "\033[38;5;90m"
# BLUE = '\033[94m'
BLUE = "\033[38;5;27m"
NAVY = "\033[38;5;17m"  #Too Dark
# CYAN = '\033[96m'
CYAN = "\033[38;5;51m"
TEAL = "\033[36m"
WARNING = '\033[93m'
YELLOW = '\033[33m'
DARK_GRAY = '\033[90m'
LIGHT_GRAY = '\033[37m'
DARK_YELLOW = YELLOW
DIM = '\033[2m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
INTENSE_PURPLE = "\033[0;95m"
CYAN_BACKGROUND = "\033[0;106m" 

#=====================
#  Stronghold Colors
#=====================
# I was thinking we could randomize the stronghold color on creation, but haven't decided. 
colors = ['red', 'green', 'magenta', 'blue', 'yellow', 'cyan', 'gray', 'purple', 'orange', 'teal', 'pink', 'brown', 'mint', 'salmon', 'lavender']

#=====================
#    Unit Colors
#=====================
COLOR_THIEF = LAVENDER
COLOR_WARRIOR = BLUE_GRAY
COLOR_FARMER = YELLOW
COLOR_VENDOR = BRIGHT_YELLOW
COLOR_FISHER = CYAN
COLOR_SCAVENGER = TEAL
COLOR_LUMBERJACK = GREEN
COLOR_HUNTER = DARK_GREEN
COLOR_MINER = RED
COLOR_PROSPECTOR = SCARLET

#=====================
#   Outpost Colors
#=====================
OP_COLOR_FARMLAND = DARK_YELLOW
OP_COLOR_FISHERY = BLUE
OP_COLOR_LUMBERMILL = DARK_GREEN
OP_COLOR_MINE = DARK_GRAY

#=====================
#   Resource Colors
#=====================
C_GOLD = DARK_YELLOW
C_FOOD = DARK_RED
C_WOOD = DARK_GREEN
C_STONE = DARK_GRAY
C_ORE = DARK_MAGENTA

#=====================#=====================#=====================
#   [StrongholdColor]
#   parameter: color
#   returns: a color code based on the passed color variable
#=====================#=====================#=====================
def StrongholdColor(color):
    if color == 'red':
        return RED
    if color == 'green':
        return GREEN
    if color == 'magenta':
        return MAGENTA
    if color == 'white':
        return BOLD
    if color == 'blue':
        return BLUE
    if color == 'yellow':
        return YELLOW
    if color == 'cyan':
        return CYAN
    if color == 'gray':
        return DARK_GRAY
    if color == 'purple':
        return PURPLE
    if color == 'orange':
        return ORANGE
    if color == 'teal':
        return TEAL
    if color == 'pink':
        return PINK
    if color == 'brown':
        return BROWN
    if color == 'mint':
        return MINT
    if color == 'salmon':
        return SALMON
    if color == 'lavender':
        return LAVENDER



#define biome globals:
WATER = '~'
RIVER = ['/','|','\\']
MOUNTAIN = 'M'
PLAINS = '#'
FOREST = '^'
BACKSLASH_SUB = 'L'     #This needed to be added so the program could properly read/write '\'

def BiomeColor(biome):
    if biome == MOUNTAIN:
        return textColor.DARK_GRAY
    elif biome == FOREST:
        return textColor.GREEN
    elif biome == PLAINS:
        return textColor.YELLOW