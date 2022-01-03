import os
import time
import random
from worldmap import *

#header() should be called on every page
def header():
    print('''
-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=--=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-
                                             UNNAMED FIEFDOM GAME
-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=--=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-'''
    + textColor.WARNING + '\n            Announcement: The Pre-Release has concluded! Congrats Steelwing! || Season 1 begins on 1/3/2021!'
    + textColor.RESET)

#this is the d20 roll function
def roll(mod):
    d20 = random.randint(1, 20)
    return d20 + mod

#define some text colors
class textColor:
    RED = '\033[91m'
    GREEN = '\033[92m'
    RESET = '\033[0m'
    DIM = '\033[2m'
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    WARNING = '\033[93m'
    YELLOW = '\033[33m'
    DARK_GRAY = '\033[90m'
    LIGHT_GRAY = '\033[37m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#define some artwork functions
def art1():
    print('''
  ,''-,.,----_                                 _,
,'         ..|                             ,,-'
| , --   ..._ \                           /
`'   ,       \/                          ,'_,,   _
| )  `..-    |                          ,,:   ,-'
. :-    _> _,-                         /  \   |
".-. /'' ,'                           |    |  |
   {  |''      ,.............,        |   /  /
   {{ ||    __/ \         ___ \ ...-'' \  ,-',.___
  _.{ '|---' / / \  ''         \oo  ,.__`.      \.
`' {  |'    /.'   \    -     )  \ooO    ,'\`-.._ `
  ,' | '\ ^/ .__.. \.____=___=''.\OOO  | .\    `:-
  ___            `'^'   ';  '' ' ^    .._ -
 /,' `\.                       __   o..| |'|O
 |||-- '|  \.        /'       [__] o.`--. [O\o  _,
 ```-''|+ ,                   /--\   `[] o..O  / `
  `'   '  '``-....--`-------.-.........,-----'' \.
    ''')


def art2():
    print('''
                             ^
         v                             ^
   /\                                      /` /`
  //`\                 ____               //`//`
  //`\               ,'/||\`.             /`\//`
 ///`\  ___   __    ///||||\`\    __   __//`// `|
 ///`\ /`\`\_/`\`. /////||`\`\` ,///`_////`|///``|
 //\`\//`\`\/`|`|'\|O________O|//////`////`\///``|
////`\O____O____[]O|O[]|--|[]O|O[]____O____O  ||'`
|  ||_O[]__O_| |__O|O__|''|__O|O__| | O__[]O,'   |
XX--. _  '  '  '   `  `0  0  ' '   ''   '  _ ,--X'
  X_ \/`-._______  __========__  ____,,-\/' \/ X
 `  -/\   | \/|||\/==||||||||==\/||||\/ /\_|/\=  `
    =---=_|_/\|||/\__||||||||__/\||||/\_==     ``
  `    `      `     o========o`     `    `  `  `
    `      `      `O/`     ` \O  `    `    `  `
    `  `          O/ ' `  '   \O     `     `    `
    ''')

def art3():
    print('''
    \,/

                    |>>>>    |>>>>           ^
                    |   __   |
             |>>>> [=|=|[]|=|=]     |>>>>
          ___|___  []    .   []  ___|___
         |||_|_||   [ (). () ]   ||_|_|||
          \||   /__[  ||  ||  ]__\   ||/
          [+| .|  _ .   _.   . _  |. |+]
          [+|. | ['] . /||\ . ['] | .|+]
          [+|  | ===  ||--||  === |  |+]
_..__.,-''[+| .|  . . |====| . .  |. |+]---,- ..
    |` | |______|_____|____|_____|______| | `|  `-
    |` |______________|.  .|_____________ | `|
    \  `|''||'|'|''|'||:  :||'|'||'||''|'|`  /
     \=-=-==-==-===-=-o.  .o-=-=-=-===-==-=-/
 '       '            '  '  '   '       '
    ''')

def art4():
    print('''
                                        v
                       _/\_               ^
        v          /\ /____\ /`
                  /__\ |<>| /__`
              _/\_|++| |<>| |++|_/`_
             /____\[]| |<>| |[]/____`
              |[]||++| |<>| |++||[]|
              |[]||++|_|<>|_|++||[]|
 ___________  |__||_=-=-=-=-=-_||__|  ___________
/_ _____    \_|^^^^^<={~00~}=>^^^^^|_/    _____ _`
  |_____|_____ ' '` <= {__} =>` '`' _____|_____|
 /_____,'  _  |` '`<_=_/||\_=_> ``'|  _  `._____`
O _______,'_\ |`' <|_=_|..|_=_|>`'`| /_`._______ O
 /________/   ``--.._=_|--|_=_,,--''   \________`
     '         '    'o/`` `\o  '    ' '       '
   '     '   ' '    o/ '  ' \o   '       '    '  '
     '             O/ ' '  ' \O      '     '    '
    ''')
    
    
def art5():
    print('''

                ^        />>>>
                        /`
                       /[]\                    ^
              |>>>    <{==}>       |>>>
      V      /^\       |--|       /^`
             /=\       |[]|       /=`
             |=|_=_=_=_|/\|_=_=_=_|=|
             |# +0 _+_ 0''0 _+_ 0+ #|
--=--- -=-=--|#   -  o (__) o  -   #|---=-=  ----=
  _____-  __ |# +_ -o(_|[]|_)o- _+ #| __-  __- __
    -  =--  [|#+_ +_  |[[]]|  _+ _+#|]  __
       -    [{[{[_____|[[]]|_____]}]}]  =- __
  _<]_   __  =--'-|==|=-=-=-|==|-_--=  __       -
 _\__/  ____     _|==|_    -|==|[_]   ____=--   -
  '-    -    --=  |==|      |==|\_/      -
     =-     =--     -   -- --          -=      =-
     ''')
    
    
def art6():
    print('''
            ,+.         /`
          --''-:.      /__\          ^
         /     V \   <`\--//>
        ,       ,'`.  \(\/)/                     ,
      _,`. /\,''    bO+|()|+Oo                  /
     .   '`'       o+-(\/\/)-+o               _/,'
    ,              (_('-00-')_)         v    ,'
   /     v      <\_ -\=[~~]=/- _/>          /
  ,              <|\ \|=--=|/ /|>          /
 /                |%\/:'__':\/%|         ,'
/     _^_ /\ _/\_  \/# /==\ #\/  _/\_ /\`_^_
--^=-/___\  /____\=\( |=/\=| )/=/____\  /___\---^-
      ____ O ====__\( ||00|| )/__==== O ____
_[]_./ == \ /\_,'=-|( ||''|| )/-=`._/\ / == \:;:;:
--=-=``--..\ \__/  |( |-==-| )|  \__/ /,,--''\----
[[[[[[[[[[[[[[[[[[/\__/=--=\__/\]]]]]]]]]]]]]]]]]]
      '       '       ''''''    '         ' '
    ''')
    
def art7():
    print('''
       ,-....    _/=-=-=--=-=-=\_    v
  ^   |  _,,'._ /|<.__.>~~<.__.>|`
     /-''     '  \=|--|-__-|--|=/   _,-'`'--._
   .'   /\________|===_/--\_===|___i____/\ `  `.
   '   /__====_==_==_/[____]\_==_==_====__\ `-._`
  /    /|_| _/'|/'\/[[| /\ |]]\/'\|'\_ |_|\     `.
 /     |/''|/.// \[[  //||`\  ]]/ `\.\|''\|      `
|      /___/^^\-/_\==//}=={`\==/_\-\^^\___\  ^
       |---]/\|-___-- {|--|} --___-|/\[---|
      /|_/\_/\_/___\_/0\__/0\_/___\_/\_/\_|`
  /\_/-==|| || |-=-| |'oUUo'| |-=-| || ||==-\_/`
  |  `'  || ||  =-=  |oUUUUo|  =-=  || ||  +'  |
 `\< `'_|__|  +  |_|/  '__'  \|_|   + |__|_ ' >//
\`\< '+'U  U   + U O  _[||]_  U U  +  O  U''+ >///
 `\_  ` |  | '   | |<|_||||_|>| |     |  |    _//
\`\`\______________|_0_[--]_0_________|______/////
      ' ~' ~ '  '~ ~ =-==-=-= ~ ~ '   ~  ~  '   '
    ''')

def art_farm1():
    print('''  ,'  ,'   ,  ,-  ,           ,'   /           ,'
 ,'  /    /  /   /   ,' ,'   /   ,'  ,'  ,'   /  ,
,'  /    /  /   /   /  ,'  ,'   /   /   /   .'  /
    ''')
def art_farm2():
    print(''' / / / / / / / / / / / / / / / / / / / / / / / / /
 / / / / / / / / / / / / / / / / / / / / / / / / /
 / / / / / / / / / / / / / / / / / / / / / / / / /
    ''')
def art_farm3():
    print('''[^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^
[^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^
[^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^
    ''')
def art_farm4():
    print('''[`~`][`~`][`~`][`~`][`~`][`~`][`~`][`~`][`~`][`~`]
[`~`][`~`][`~`][`~`][`~`][`~`][`~`][`~`][`~`][`~`]
[`~`][`~`][`~`][`~`][`~`][`~`][`~`][`~`][`~`][`~`]
    ''')
def art_farm5():
    print('''[*&*][*&*][*&*][*&*][*&*][*&*][*&*][*&*][*&*][*&*]
[*&*][*&*][*&*][*&*][*&*][*&*][*&*][*&*][*&*][*&*]
[*&*][*&*][*&*][*&*][*&*][*&*][*&*][*&*][*&*][*&*]
    ''')
def art_farm6():
    print('''<(*)><(*)><(*)><(*)><(*)><(*)><(*)><(*)><(*)><(*)>
<(*)><(*)><(*)><(*)><(*)><(*)><(*)><(*)><(*)><(*)>
<(*)><(*)><(*)><(*)><(*)><(*)><(*)><(*)><(*)><(*)>
    ''')
def art_farm7():
    print('''|~@~||~@~||~@~||~@~||~@~||~@~||~@~||~@~||~@~||~@~|
|~@~||~@~||~@~||~@~||~@~||~@~||~@~||~@~||~@~||~@~|
|~@~||~@~||~@~||~@~||~@~||~@~||~@~||~@~||~@~||~@~|
    ''')
#the fiefdom class holds variables that define a player's stats
class Fiefdom:
    name = 'Default Fiefdom'
    ruler = 'Unclaimed'
    home = False
    defenders = 100
    gold = 500
    defLevel = 0
    defType = "Open Camp"
    attLevel = 0
    attType = "Angry Mob"
    goldMod = '1'
    defenderMod = '1'
    farmType = "Dirt Patch"
    thieves = 0
    biome = '0'
    xCoordinate = 0
    yCoordinate = 0

    #take the current fiefdom and write it to the /fiefs directory
    def write(self):
        fiefFile = 'fiefs/' + self.name + '.txt'
        
        #this part creates a file if it isn't made yet        
        try:
            with open(fiefFile, 'x') as f:

                f.write(self.name + '\n')
                f.write(self.ruler + '\n')
                f.write(str(self.home) + '\n')
                f.write(str(self.defenders) + '\n')
                f.write(str(self.gold) + '\n')
                f.write(str(self.defLevel) + '\n')
                f.write(str(self.defType) + '\n')
                f.write(str(self.attLevel) + '\n')
                f.write(str(self.attType) + '\n')
                f.write(str(self.goldMod) + '\n')
                f.write(str(self.defenderMod) + '\n')
                f.write(str(self.farmType) + '\n')
                f.write(str(self.thieves) + '\n')
        except:
            pass

        #write the class variables down line by line in the text file
        try:
            with open(fiefFile, 'w') as f:
                f.write(self.name + '\n')
                f.write(self.ruler + '\n')
                f.write(str(self.home) + '\n')
                f.write(str(self.defenders) + '\n')
                f.write(str(self.gold) + '\n')
                f.write(str(self.defLevel) + '\n')
                f.write(str(self.defType) + '\n')
                f.write(str(self.attLevel) + '\n')
                f.write(str(self.attType) + '\n')
                f.write(str(self.goldMod) + '\n')
                f.write(str(self.defenderMod) + '\n')
                f.write(str(self.farmType) + '\n')
                f.write(str(self.thieves) + '\n')
        except:
            pass

    #read class variables line by line
    def read(self):
        fiefFile = 'fiefs/' + self.name + '.txt'
        try:
            with open(fiefFile, 'r') as f:
                self.name = f.readline().strip()
                self.ruler = f.readline().strip()
                self.home = f.readline().strip()
                self.defenders = f.readline().strip()
                self.gold = f.readline().strip()
                self.defLevel = f.readline().strip()
                self.defType = f.readline().strip()
                self.attLevel = f.readline().strip()
                self.attType = f.readline().strip()
                self.goldMod = f.readline().strip()
                self.defenderMod = f.readline().strip()
                self.farmType = f.readline().strip()
                self.thieves = f.readline().strip()
        except:
            self.write()   
            
#SW: I am splitting this to safely determine if it is necessary to keep the above stuff or not
class Stronghold:
    name = 'Default Stronghold'
    ruler = 'Unclaimed'
    home = False
    defenders = 100
    gold = 500
    defLevel = 0
    defType = "Open Camp"
    attLevel = 0
    attType = "Angry Mob"
    goldMod = '1'
    defenderMod = '1'
    farmType = "Dirt Patch"
    thieves = 0
    biome = '0'
    xCoordinate = 0
    yCoordinate = 0

    #take the current stronghold and write it to the /strongholds directory
    def write(self):
        fiefFile = 'strongholds/' + self.name + '.txt'
        
        #this part creates a file if it isn't made yet        
        try:
            with open(fiefFile, 'x') as f:
                f.write(self.name + '\n')
                f.write(self.ruler + '\n')
                f.write(str(self.home) + '\n')
                f.write(str(self.defenders) + '\n')
                f.write(str(self.gold) + '\n')
                f.write(str(self.defLevel) + '\n')
                f.write(str(self.defType) + '\n')
                f.write(str(self.attLevel) + '\n')
                f.write(str(self.attType) + '\n')
                f.write(str(self.goldMod) + '\n')
                f.write(str(self.defenderMod) + '\n')
                f.write(str(self.farmType) + '\n')
                f.write(str(self.thieves) + '\n')
                f.write(str(self.biome) + '\n')
                f.write(str(self.xCoordinate) + '\n')
                f.write(str(self.yCoordinate) + '\n')
        except:
            pass

        #write the class variables down line by line in the text file
        try:
            with open(fiefFile, 'w') as f:
                f.write(self.name + '\n')
                f.write(self.ruler + '\n')
                f.write(str(self.home) + '\n')
                f.write(str(self.defenders) + '\n')
                f.write(str(self.gold) + '\n')
                f.write(str(self.defLevel) + '\n')
                f.write(str(self.defType) + '\n')
                f.write(str(self.attLevel) + '\n')
                f.write(str(self.attType) + '\n')
                f.write(str(self.goldMod) + '\n')
                f.write(str(self.defenderMod) + '\n')
                f.write(str(self.farmType) + '\n')
                f.write(str(self.thieves) + '\n')
                f.write(str(self.biome) + '\n')
                f.write(str(self.xCoordinate) + '\n')
                f.write(str(self.yCoordinate) + '\n')
        except:
            pass

    #read class variables line by line
    def read(self):
        fiefFile = 'strongholds/' + self.name + '.txt'
        try:
            with open(fiefFile, 'r') as f:
                self.name = f.readline().strip()
                self.ruler = f.readline().strip()
                self.home = f.readline().strip()
                self.defenders = f.readline().strip()
                self.gold = f.readline().strip()
                self.defLevel = f.readline().strip()
                self.defType = f.readline().strip()
                self.attLevel = f.readline().strip()
                self.attType = f.readline().strip()
                self.goldMod = f.readline().strip()
                self.defenderMod = f.readline().strip()
                self.farmType = f.readline().strip()
                self.thieves = f.readline().strip()
                self.biome = f.readline().strip()
                self.xCoordinate = f.readline().strip()
                self.yCoordinate = f.readline().strip()
        except:
            self.write()     
            

class Map:
    seed = '00555'
    name = 'default'
    width = 40
    height = 40
    
    numWater = 0
    numRivers = 0
    numPlains = 0
    numForests = 0
    numMountains = 0
    
    usedPlains = 0
    usedForests = 0
    usedMountains = 0

    values = []
    worldMap = []

    #Testing map read/write updates (1)
    def write(self):
        mapFile = 'map/' + self.name + '.txt'
        
        #this part creates a file if it isn't made yet. SW: This has not been tested.
        try:
            with open(mapFile, 'x') as f:
                f.write(str("["))
                for i in range(self.height):
                    f.write(str("["))
                    for j in range(self.width):
                        if j < self.width - 1:
                            f.write("'" + str(self.worldMap[i][j]) + "',")
                        else:
                            f.write("'" + str(self.worldMap[i][j]) + "'")
                    if i < self.height - 1:
                        f.write(str("],"))
                    else:
                        f.write(str("]"))
                f.write(str("]"))
        except:
            pass

        #write the class variables down line by line in the text file
        try:
            with open(mapFile, 'w') as f:
                f.write(str("["))
                f.write("['" + str(self.seed) + "'],")
                for i in range(self.height):
                    f.write(str("["))
                    for j in range(self.width):
                        if j < self.width - 1:
                            f.write("'" + str(self.worldMap[i][j]) + "',")
                        else:
                            f.write("'" + str(self.worldMap[i][j]) + "'")
                    if i < self.height - 1:
                        f.write(str("],"))
                    else:
                        f.write(str("]"))
                f.write(str("]"))
        except:
            pass

    #read class variables line by line and save them into self.worldMap
    def read(self):
        mapFile = 'map/' + self.name + '.txt'
        try:
            readMapFile = open(mapFile, 'r')
            readList = eval(readMapFile.read())
            readMapFile.close()

            for count in range(len(readList)):
                if count == 0:
                    self.values.append(readList[count])
                if count > 1:
                    self.worldMap.append(readList[count])

        except:
            print('Could not read file!')
            pass
            
#eof
