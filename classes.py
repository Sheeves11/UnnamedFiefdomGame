import os
import time
import random

#header() should be called on every page
def header():
    print('''
-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=--=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-
                                             UNNAMED FIEFDOM GAME
-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=--=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-'''
    + textColor.WARNING + '\n                          Announcement: Season 1 will begin on December 20th, 2021!'
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
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#define some artwork functions
def art1():
    print('''
                        ______
                       /     /\ 
                      /     /  \ 
                     /_____/----\_    (  
                    "     "          ).  
                   _ ___          o (:') o   
                  (@))_))        o ~/~~\~ o   
                                  o  o  o
    ''')


def art2():
    print('''
                                )
                              _(
                          ___|_|_________
                         /___|_|_________\ 
                    ()  /_________________\ 
                `'.()))/___________________\ '-.'`'.
               .,'(())()   ____     ____  |,.'     '-.
                  )(()))  |)~~(|   |)~~(| |. '-. ()`'.
                 ()()(()) ||__||   ||__|| | `'.,(())
                ())()(()))________________|___ ()))()
                ()((())()))| | | | | | | | | | (()()))
               ()))(()()())|_|_|_|_|_|_|_|_|_|)(()(()
               (()((())(()-------------------|(())(())
               ~^~ ^" ^"  ^~^   ^"   ~^~    ^~^~(()(()
               ^"     ^~^   ~^~   ^"    ^~^   ~~^~""^
    ''')

def art3():
    print('''
                 ^       /\             /\   ~!~
                    ^   (())           (())
             ^         /(())\         /(())\      ~!~
                      (((())))       (((())))
                      |^|^^|^|_______|^|^^|^|
                  /\   |^^^^|-_-_-_-_-|^^^^|   /\ 
                 (())  | "" |+_+_+_+_+| "" |  (())
                ((())) |    |[X]_+_[X]|    | ((()))
               (((())))|    |+_+_+_+_+|    |(((())))
               |^|^^|^||____|-_-_-_-_-|____||^|^^|^|
                |^^^^|_-_-_-_-_-_-_-_-_-_-_-_|^^^^|
            ~^~~| "" |_-_-_-_-_-_-_-_-_-_-_-_| "" |~~
            ~~  |    |_+_+_+_+_+_+_+_+_+_+_+_|    | ~^~
             ~^^|    |_+[X]+_[X]_+_[X]_+[X]+_|    |~~^
                |    |_+_+_+_+_+/l\+_+_+_+_+_|    |
                |    |_-_-_-_-_|:::|_-_-_-_-_|    |
                |____|_+_+_+_+_|:::|_+_+_+_+_|____|
            @@@@@@@@@@@@@@@@@@@@"""@@@@@@@@@@@@@@@@@@@@
    ''')

def art4():
    print('''
                                  |>>>
                                  |
                    |>>>      _  _|_  _         |>>>
                    |        |;| |;| |;|        |
                _  _|_  _    \ .    .  /    _  _|_  _
               |;|_|;|_|;|    \ :. ,  /    |;|_|;|_|;|
               \ ..      /    ||;   . |    \ .    .  /
                \ .  ,  /     ||:  .  |     \ :  .  /
                 ||:   |_   _ ||_ . _ | _   _||:   |
                 ||:  .|||_|;|_|;|_|;|_|;|_|;||:.  |
                 ||:   ||.    .     .      . ||:  .|
                 ||: . || .     . .   .  ,   ||:   |       \,/
                 ||:   ||:  ,  _______   .   ||: , |            /`\ 
                 ||:   || .   /+++++++\    . ||:   |
                 ||:   ||.    |+++++++| .    ||: . |
              __ ||: . ||: ,  |+++++++|.  . _||_   |
     ____--`~    '--~~__|.    |+++++__|----~    ~`---,              ___
-~--~                   ~---__|,--~'                  ~~----_____-~'   `~----~~
    ''')
    
    
def art5():
    print('''
                                 |--__
                                 |
                                 X
                        |-___   / \       |--__
                        |      =====      |
                        X      | .:|      X
                       / \     | O |     / \ 
                      =====   |:  . |   =====
                      |.: |__| .   : |__| :.|
                      |  :|. :  ...   : |.  |
              __   __W| .    .  ||| .      :|W__  --
            -- __  W  WWWW______"""______WWWW   W -----  --
        -  -     ___  ---    ____     ____----       --__  -
            --__    --    --__     -___        __-   _
     ''')
    
    
def art6():
    print('''
                  ^                 
                 / \                                                      
            ^   _|.|_   ^          
          _|I|  |I .|  |.|_        
          \II||~~| |~~||  /        
           ~\~|~~~~~~~|~/~        
             \|II I ..|/           
        /\    |II.    |    /\      
       /  \  _|III .  |_  /  \     
       |-~| /(|I.I I  |)\ |~-|     
     _/(I | +-----------+ |. )\_  
     \~-----/____-~-____\-----~/   
      |I.III|  /(===)\  |  .. |   
      /~~~-----_________---~~~\   
     `##########!\-#####%!!!!!| |\  
    _/###########!!\~~-_##%!!!\_/|
    \##############!!!!!/~~-_%!!!!\ 
  ~)######################!!!!!/~~--\_\       
    ''')
    
def art7():
    print('''
    ''')

#the fifedom class holds variables that define a player's stats
class Fifedom:
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

    #take the current fifedom and write it to the /fifes directory
    def write(self):
        fifeFile = 'fifes/' + self.name + '.txt'
        
        #this part creates a file if it isn't made yet        
        try:
            with open(fifeFile, 'x') as f:

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
        except:
            pass

        #write the class variables down line by line in the text file
        try:
            with open(fifeFile, 'w') as f:
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
        except:
            pass

    #read class variables line by line
    def read(self):
        fifeFile = 'fifes/' + self.name + '.txt'
        try:
            with open(fifeFile, 'r') as f:
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
        except:
            self.write()          
            
#eof
