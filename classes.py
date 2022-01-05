import os
import time
import random

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

#define biome globals:
MOUNTAIN = 'M'
FOREST = '^'
PLAINS = '#'

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

def biomeColor(biome):
    if biome == MOUNTAIN:
        return textColor.LIGHT_GRAY
    elif biome == FOREST:
        return textColor.GREEN
    elif biome == PLAINS:
        return textColor.YELLOW

#Define Art:

# '''+C+'''
# '''+R+'''

#==================================================
#   Fief Art: Campsite
#==================================================
#  ,''-,.,----_                                 _,
#,'         ..|                             ,,-'
#| , --   ..._ \                           /
#`'   ,       \/                          ,'_,,   _
#| )  `..-    |                          ,,:   ,-'
#. :-    _> _,-                         /  \   |
#".-. /'' ,'                           |    |  |
#   {  |''      ,.............,        |   /  /
#   {{ ||    __/ \         ___ \ ...-'' \  ,-',.___
#  _.{ '|---' / / \  ''         \oo  ,.__`.      \.
#`' {  |'    /.'   \    -     )  \ooO    ,'\`-.._ `
#  ,' | '\ ^/ .__.. \.____=___=''.\OOO  | .\    `:-
#  ___            `'^'   ';  '' ' ^    .._ -
# /,' `\.                       __   o..| |'|O
# |||-- '|  \.        /'       [__] o.`--. [O\o  _,
# ```-''|+ ,                   /--\   `[] o..O  / `
#  `'   '  '``-....--`-------.-.........,-----'' \.
#==================================================
def art_fief0(biome):
    C = biomeColor(biome)
    R = textColor.RESET
    print('''
  ,''-,.,----_                                 _,
,'         ..|                             ,,-'
| , --   ..._ \                           /
`'   ,       \/                          ,'_,,   _
| )  `..-    |                          ,,:   ,-'
. :-    _> _,-                         /  \   |
".-. /'' ,'                           |    |  |
   {  |''      ,.............,        |   /  /
   {{ ||    '''+C+'''__'''+R+'''/ \         ___ \ '''+C+'''...-'`'''+R+''' \  ,'''+C+'''-'''+R+'''','''+C+'''.___'''+R+'''
'''+C+'''  _'''+R+'''.{ '|'''+C+'''---`'''+R+''' / / \  ''         \oo  '''+C+''',.__'''+R+'''`.      '''+C+'''\.'''+R+'''
'''+C+'''``'''+R+''' {  |'    /.'   \    -     )  \ooO    ,'\`'''+C+'''-.._ `'''+R+'''
  ,' | '\ '''+C+'''^'''+R+'''/ .__.. \.____'''+C+'''='''+R+'''___'''+C+'''=''.'''+R+'''\OOO  | .\    '''+C+'''`:-'''+R+'''
  ___            '''+C+'''`'^'   ';  '' ' ^'''+R+'''    .._ -
 /,' `\.                       __   o..| |'|O
 '''+C+'''|||'''+R+'''-- '|  '''+C+'''\.        /' '''+R+'''      [__] o.`--. [O\o  '''+C+'''_,'''+R+'''
 '''+C+'''```-''|+ ,'''+R+'''                   /--\   `[] o..O  '''+C+'''/ `'''+R+'''
'''+C+'''  `'   '  '``-....--`-------.-.........,-----'' \.'''+R+'''
    ''')

#==================================================
#   Fief Art: Wooden Fences
#==================================================
#                             ^
#         v                             ^
#   /\                                      /` /`
#  //`\                 ____               //`//`
#  //`\               ,'/||\`.             /`\//`
# ///`\  ___   __    ///||||\`\    __   __//`// `|
# ///`\ /`\`\_/`\`. /////||`\`\` ,///`_////`|///``|
# //\`\//`\`\/`|`|'\|O________O|//////`////`\///``|
#////`\O____O____[]O|O[]|--|[]O|O[]____O____O  ||'`
#|  ||_O[]__O_| |__O|O__|''|__O|O__| | O__[]O,'   |
#XX--. _  '  '  '   `  `0  0  ' '   ''   '  _ ,--X'
#  X_ \/`-._______  __========__  ____,,-\/' \/ X
# `  -/\   | \/|||\/==||||||||==\/||||\/ /\_|/\=  `
#    =---=_|_/\|||/\__||||||||__/\||||/\_==     ``
#  `    `      `     o========o`     `    `  `  `
#    `      `      `O/`     ` \O  `    `    `  `
#    `  `          O/ ' `  '   \O     `     `    `
#==================================================
def art_fief1():
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

#==================================================
#   Fief Art: Really Deep Trenches
#==================================================
#    \,/
#
#                    |>>>>    |>>>>           ^
#                    |   __   |
#             |>>>> [=|=|[]|=|=]     |>>>>
#          ___|___  []    .   []  ___|___
#         |||_|_||   [ (). () ]   ||_|_|||
#          \||   /__[  ||  ||  ]__\   ||/
#          [+| .|  _ .   _.   . _  |. |+]
#          [+|. | ['] . /||\ . ['] | .|+]
#          [+|  | ===  ||--||  === |  |+]
#_..__.,-''[+| .|  . . |====| . .  |. |+]---,- ..
#    |` | |______|_____|____|_____|______| | `|  `-
#    |` |______________|.  .|_____________ | `|
#    \  `|''||'|'|''|'||:  :||'|'||'||''|'|`  /
#     \=-=-==-==-===-=-o.  .o-=-=-=-===-==-=-/
# '       '            '  '  '   '       '
#==================================================
def art_fief2():
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

#==================================================
#   Fief Art: Tall Towers
#==================================================
#                                        v
#                       _/\_               ^
#        v          /\ /____\ /`
#                  /__\ |<>| /__`
#              _/\_|++| |<>| |++|_/`_
#             /____\[]| |<>| |[]/____`
#              |[]||++| |<>| |++||[]|
#              |[]||++|_|<>|_|++||[]|
# ___________  |__||_=-=-=-=-=-_||__|  ___________
#/_ _____    \_|^^^^^<={~00~}=>^^^^^|_/    _____ _`
#  |_____|_____ ' '` <= {__} =>` '`' _____|_____|
# /_____,'  _  |` '`<_=_/||\_=_> ``'|  _  `._____`
#O _______,'_\ |`' <|_=_|..|_=_|>`'`| /_`._______ O
# /________/   ``--.._=_|--|_=_,,--''   \________`
#     '         '    'o/`` `\o  '    ' '       '
#   '     '   ' '    o/ '  ' \o   '       '    '  '
#     '             O/ ' '  ' \O      '     '    '
#==================================================
def art_fief3():
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
    
#==================================================
#   Fief Art: In a Lake
#==================================================
#                                      v
#                 ^        />>>>
#                         /`
#                        /[]\                    ^
#               |>>>    <{==}>       |>>>
#       V      /^\       |--|       /^`
#              /=\       |[]|       /=`
#              |=|_=_=_=_|/\|_=_=_=_|=|
#              |# +0 _+_ 0''0 _+_ 0+ #|
#/--=--- -=-=--|#   -  o (__) o  -   #|---=-=  ----=
#   _____-  __ |# +_ -o(_|[]|_)o- _+ #| __-  __- __
#     -  =--  [|#+_ +_  |[[]]|  _+ _+#|]  __
#O       -    [{[{[_____|[[]]|_____]}]}]  =- __
#   _<]_   __  =--'-|==|=-=-=-|==|-_--=  __       -
#  _\__/  ____     _|==|_    -|==|[_]   ____=--   -
#   '-    -    --=  |==|      |==|\_/      -
#      =-     =--     -   -- --          -=      =-
#==================================================
def art_fief4():
    print('''
                                      v
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
    
#==================================================
#   Fief Art: On a Mountain
#==================================================
#            ,+.         /`
#          --''-:.      /__\          ^
#         /     V \   <`\--//>
#        ,       ,'`.  \(\/)/                     ,
#      _,`. /\,''    bO+|()|+Oo                  /
#     .   '`'       o+-(\/\/)-+o               _/,'
#    ,              (_('-00-')_)         v    ,'
#   /     v      <\_ -\=[~~]=/- _/>          /
#  ,              <|\ \|=--=|/ /|>          /
# /                |%\/:'__':\/%|         ,'
#/     _^_ /\ _/\_  \/# /==\ #\/  _/\_ /\`_^_
#--^=-/___\  /____\=\( |=/\=| )/=/____\  /___\---^-
#      ____ O ====__\( ||00|| )/__==== O ____
#_[]_./ == \ /\_,'=-|( ||''|| )/-=`._/\ / == \:;:;:
#--=-=``--..\ \__/  |( |-==-| )|  \__/ /,,--''\----
#[[[[[[[[[[[[[[[[[[/\__/=--=\__/\]]]]]]]]]]]]]]]]]]
#      '       '       ''''''    '         ' '
#==================================================
def art_fief5():
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

#==================================================
#   Fief Art: Boiling Oil
#==================================================
#       ,-.._     _/=-=-=--=-=-=\_    v
#  ^   |  _,,'._ /|<.__.>~~<.__.>|`
#     /-''     '  \=|--|-__-|--|=/   _,-'`'--._
#   .'   /\________|===_/--\_===|___i____/\ `  `.
#   '   /__====_==_==_/[____]\_==_==_====__\ `-._`
#  /    /|_| _/'|/'\/[[| /\ |]]\/'\|'\_ |_|\     `.
# /     |/''|/.// \[[  //||`\  ]]/ `\.\|''\|      `
#|      /___/^^\-/_\==//}=={`\==/_\-\^^\___\  ^
#       |---]/\|-___-- {|--|} --___-|/\[---|
#      /|_/\_/\_/___\_/0\__/0\_/___\_/\_/\_|`
#  /\_/-==|| || |-=-| |'oUUo'| |-=-| || ||==-\_/`
#  |  `'  || ||  =-=  |oUUUUo|  =-=  || ||  +'  |
# `\< `'_|__|  +  |_|/  '__'  \|_|   + |__|_ ' >//
#\`\< '+'U  U   + U O  _[||]_  U U  +  O  U''+ >///
# `\_  ` |  | '   | |<|_||||_|>| |     |  |    _//
#\`\`\______________|_0_[--]_0_________|______/////
#      ' ~' ~ '  '~ ~ =-==-=-= ~ ~ '   ~  ~  '   '
#==================================================
def art_fief6():
    print('''
       ,-.._     _/=-=-=--=-=-=\_    v
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

#==================================================
#   Farm Art: Rank 0
#==================================================
#  ,'  ,'   ,  ,-  ,           ,'   /           ,'
# ,'  /    /  /   /   ,' ,'   /   ,'  ,'  ,'   /  ,
#,'  /    /  /   /   /  ,'  ,'   /   /   /   .'  /
#==================================================
def art_farm0():
    print('''  ,'  ,'   ,  ,-  ,           ,'   /           ,'
 ,'  /    /  /   /   ,' ,'   /   ,'  ,'  ,'   /  ,
,'  /    /  /   /   /  ,'  ,'   /   /   /   .'  /
    ''')

#==================================================
#   Farm Art: Rank 1
#==================================================
# / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / /
#==================================================
def art_farm1():
    print(''' / / / / / / / / / / / / / / / / / / / / / / / / /
 / / / / / / / / / / / / / / / / / / / / / / / / /
 / / / / / / / / / / / / / / / / / / / / / / / / /
    ''')

#==================================================
#   Farm Art: Rank 2
#==================================================
#[^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^
#[^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^
#[^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^
#==================================================
def art_farm2():
    print('''[^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^
[^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^
[^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^
    ''')

#==================================================
#   Farm Art: Rank 3
#==================================================
#[`~`][`~`][`~`][`~`][`~`][`~`][`~`][`~`][`~`][`~`]
#[`~`][`~`][`~`][`~`][`~`][`~`][`~`][`~`][`~`][`~`]
#[`~`][`~`][`~`][`~`][`~`][`~`][`~`][`~`][`~`][`~`]
#==================================================
def art_farm3():
    print('''[`~`][`~`][`~`][`~`][`~`][`~`][`~`][`~`][`~`][`~`]
[`~`][`~`][`~`][`~`][`~`][`~`][`~`][`~`][`~`][`~`]
[`~`][`~`][`~`][`~`][`~`][`~`][`~`][`~`][`~`][`~`]
    ''')

#==================================================
#   Farm Art: Rank 4
#==================================================
#[*&*][*&*][*&*][*&*][*&*][*&*][*&*][*&*][*&*][*&*]
#[*&*][*&*][*&*][*&*][*&*][*&*][*&*][*&*][*&*][*&*]
#[*&*][*&*][*&*][*&*][*&*][*&*][*&*][*&*][*&*][*&*]
#==================================================
def art_farm4():
    print('''[*&*][*&*][*&*][*&*][*&*][*&*][*&*][*&*][*&*][*&*]
[*&*][*&*][*&*][*&*][*&*][*&*][*&*][*&*][*&*][*&*]
[*&*][*&*][*&*][*&*][*&*][*&*][*&*][*&*][*&*][*&*]
    ''')

#==================================================
#   Farm Art: Rank 5
#==================================================
#<(*)><(*)><(*)><(*)><(*)><(*)><(*)><(*)><(*)><(*)>
#<(*)><(*)><(*)><(*)><(*)><(*)><(*)><(*)><(*)><(*)>
#<(*)><(*)><(*)><(*)><(*)><(*)><(*)><(*)><(*)><(*)>
#==================================================
def art_farm5():
    print('''<(*)><(*)><(*)><(*)><(*)><(*)><(*)><(*)><(*)><(*)>
<(*)><(*)><(*)><(*)><(*)><(*)><(*)><(*)><(*)><(*)>
<(*)><(*)><(*)><(*)><(*)><(*)><(*)><(*)><(*)><(*)>
    ''')

#==================================================
#   Farm Art: Rank 6
#==================================================
#|~@~||~@~||~@~||~@~||~@~||~@~||~@~||~@~||~@~||~@~|
#|~@~||~@~||~@~||~@~||~@~||~@~||~@~||~@~||~@~||~@~|
#|~@~||~@~||~@~||~@~||~@~||~@~||~@~||~@~||~@~||~@~|
#==================================================
def art_farm6():
    print('''|~@~||~@~||~@~||~@~||~@~||~@~||~@~||~@~||~@~||~@~|
|~@~||~@~||~@~||~@~||~@~||~@~||~@~||~@~||~@~||~@~|
|~@~||~@~||~@~||~@~||~@~||~@~||~@~||~@~||~@~||~@~|
    ''')

def art_mountain():
    print(textColor.DARK_GRAY + '''M M M M M M M M M M M M M M M M M M M M M M M M M ''' + textColor.RESET)
def art_forest():
    print(textColor.GREEN + '''^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ''' + textColor.RESET)
def art_plains():
    print(textColor.YELLOW + '''# # # # # # # # # # # # # # # # # # # # # # # # # ''' + textColor.RESET)

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
                self.biome = f.readline().strip()
                self.xCoordinate = f.readline().strip()
                self.yCoordinate = f.readline().strip()
        except:
            self.write()   
    def setCoordinates(self, coordinates):
        self.yCoordinate = coordinates[0]
        self.xCoordinate = coordinates[1]
            
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
        strongholdFile = 'strongholds/' + self.name + '.txt'
        
        #this part creates a file if it isn't made yet        
        try:
            with open(strongholdFile, 'x') as f:
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
            with open(strongholdFile, 'w') as f:
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
        strongholdFile = 'strongholds/' + self.name + '.txt'
        try:
            with open(strongholdFile, 'r') as f:
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

    def setCoordinates(self, coordinates):
        self.yCoordinate = coordinates[0]
        self.xCoordinate = coordinates[1]

class Map:
    seed = '00555'
    name = 'default'
    width = 5
    height = 5
    
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

    success = False #Temporary bool
    #--------------------------------------------------------------------------------------------------------------
    #   Writes a map file as a 2-d list like so:
    #   [['seed'], ['width'], ['height'], ['numWater'], ['numRivers'], ['numPlains'], ['numForests'], 
    #   ['numMountains'], ['usedPlains'], ['usedForests'], ['usedMountains'], ['worldMap ROW 1'], [worldMap ROW 2], 
    #   [worldMap ROW 3], [...], [worldMap ROW height]
    #--------------------------------------------------------------------------------------------------------------
    def write(self):
        mapFile = 'map/' + self.name + '.txt'
        
        #this part creates a file if it isn't made yet. SW: This has not been tested.
        try:
            with open(mapFile, 'x') as f:
                f.write(str("["))
                f.write("['" + str(self.seed) + "'],")
                f.write("['" + str(self.width) + "'],")
                f.write("['" + str(self.height) + "'],")
                f.write("['" + str(self.numWater) + "'],")
                f.write("['" + str(self.numRivers) + "'],")
                f.write("['" + str(self.numPlains) + "'],")
                f.write("['" + str(self.numForests) + "'],")
                f.write("['" + str(self.numMountains) + "'],")
                f.write("['" + str(self.usedPlains) + "'],")
                f.write("['" + str(self.usedForests) + "'],")
                f.write("['" + str(self.usedMountains) + "'],")
                for i in range(int(self.height)):
                    f.write(str("["))
                    for j in range(int(self.width)):
                        if j < int(self.width) - 1:
                            f.write("'" + str(self.worldMap[i][j]) + "',")
                        else:
                            f.write("'" + str(self.worldMap[i][j]) + "'")
                    if i < int(self.height) - 1:
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
                f.write("['" + str(self.width) + "'],")
                f.write("['" + str(self.height) + "'],")
                f.write("['" + str(self.numWater) + "'],")
                f.write("['" + str(self.numRivers) + "'],")
                f.write("['" + str(self.numPlains) + "'],")
                f.write("['" + str(self.numForests) + "'],")
                f.write("['" + str(self.numMountains) + "'],")
                f.write("['" + str(self.usedPlains) + "'],")
                f.write("['" + str(self.usedForests) + "'],")
                f.write("['" + str(self.usedMountains) + "'],")
                for i in range(int(self.height)):
                    f.write(str("["))
                    for j in range(int(self.width)):
                        if j < int(self.width) - 1:
                            f.write("'" + str(self.worldMap[i][j]) + "',")
                        else:
                            f.write("'" + str(self.worldMap[i][j]) + "'")
                    if i < int(self.height) - 1:
                        f.write(str("],"))
                    else:
                        f.write(str("]"))
                f.write(str("]"))
        except:
            pass

    #--------------------------------------------------------------------------------------------------------------
    #   Opens the map file and reads the whole thing into the variable "readList" before closing it.
    #   The first 11 variables are stored in a "values" array for sorting into appropriate variables.
    #   Then, each row of the map is loaded into the worldMap 2d-list.
    #--------------------------------------------------------------------------------------------------------------
    def read(self):
        mapFile = 'map/' + self.name + '.txt'
        try:
            readMapFile = open(mapFile, 'r')
            readList = eval(readMapFile.read())
            readMapFile.close()
            self.worldMap = []  #Needs to clear the world map if anything happened to be in there before reading.
            for count in range(len(readList)):
                if count <= 10:
                    self.values.append(readList[count])
                    
                if count > 10:
                    self.worldMap.append(readList[count])

            self.success = True

        except:
            print('Could not read file!')
            pass

        if self.success == True:
            self.seed = str(self.values[0]).lstrip("['").rstrip("']")
            self.width = str(self.values[1]).lstrip("['").rstrip("']")
            self.height = str(self.values[2]).lstrip("['").rstrip("']")
            self.numWater = str(self.values[3]).lstrip("['").rstrip("']")
            self.numRivers = str(self.values[4]).lstrip("['").rstrip("']")
            self.numPlains = str(self.values[5]).lstrip("['").rstrip("']")
            self.numForests = str(self.values[6]).lstrip("['").rstrip("']")
            self.numMountains = str(self.values[7]).lstrip("['").rstrip("']")
            self.usedPlains = str(self.values[8]).lstrip("['").rstrip("']")
            self.usedForests = str(self.values[9]).lstrip("['").rstrip("']")
            self.usedMountains = str(self.values[10]).lstrip("['").rstrip("']")
            # print('seed: ' + str(self.seed))
            # print('width: ' + str(self.width))
            # print('height: ' + str(self.height))
            # print('numWater: ' + str(self.numWater))
            # print('numPlains: ' + str(self.numPlains))
            # print('numForests: ' + str(self.numForests))
            # print('numMountains: ' + str(self.numMountains))
            # print('usedPlains: ' + str(self.usedPlains))
            # print('usedForests: ' + str(self.usedForests))
            # print('usedMountains: ' + str(self.usedMountains))

    def selfDiagnostic(self):
        print('Running diagnostic on map class...')
        print('Current attributes are: ')
        print('name: ' + str(self.name))
        print('seed: ' + str(self.seed))
        print('width: ' + str(self.width))
        print('height: ' + str(self.height))
        print('numWater: ' + str(self.numWater))
        print('numPlains: ' + str(self.numPlains))
        print('numForests: ' + str(self.numForests))
        print('numMountains: ' + str(self.numMountains))
        print('usedPlains: ' + str(self.usedPlains))
        print('usedForests: ' + str(self.usedForests))
        print('usedMountains: ' + str(self.usedMountains))
        # print('worldMap:')
        # print(*self.worldMap)

#eof
