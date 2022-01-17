#=================================================
#=================================================
#                    Colors
#=================================================
#=================================================

#define some text colors
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
RED = '\033[91m'
DARK_RED = "\033[31m"
GREEN = '\033[92m'
DARK_GREEN = "\033[32m"
RESET = '\033[0m'
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
BRIGHT_YELLOW = WARNING
DARK_YELLOW = YELLOW
DIM = '\033[2m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
BOLD_DARK_GREEN = "\033[32m \033[1m" 
INTENSE_CYAN = "\033[0;96m"
INTENSE_PURPLE = "\033[0;95m"
INTENSE_BLACK = "\033[1;90m"
MAGENTA_BACKGROUND = "\u001b[45m"
WHITE_BACKGROUND = "\033[47m"
CYAN_BACKGROUND = "\033[0;106m" 
TEST_COLOR = "\033[41m"

#=====================
#    Unit Colors
#=====================
COLOR_THIEF = MAGENTA
COLOR_WARRIOR = LIGHT_GRAY
COLOR_FARMER = WARNING
COLOR_VENDOR = DARK_YELLOW
COLOR_FISHER = CYAN
COLOR_SCAVENGER = TEAL
COLOR_LUMBERJACK = GREEN
COLOR_HUNTER = DARK_GREEN
COLOR_MINER = RED
COLOR_PROSPECTOR = DARK_RED

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