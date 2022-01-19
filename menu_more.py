from globals import *
from tempMethods import *
import worldmap

#This document contains screens for:
#   moreCommands
#   messageBoard
#   pastWinners
#   about
#   tempMap
#   features


def MoreMenu(screen, userStronghold):

#This is a menu for additional features
#----------------------------------------------------------------------------------
    if screen == "moreCommands":
        os.system("clear")
        headerStripped()
        
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print("     Avalible Commands:")
        print('     -------------------------------------------------------')
        print('     {1}: Return to Stronghold')
        print('     {2}: Past Winners')
        print('     {3}: Upcoming Features')
        print('     {4}: About')
        print('     {5}: Sandbox Mode')
        print('     {6}: View Temp Map (this is still in development)')
        print('     --------------------------------------------------------')
        print('')
        command = input("     Enter your command: ")

        if command == '1':
            screen = 'stronghold'

        if command == '2':
            screen = 'pastWinners'

        if command == '3':
            screen = 'features'

        if command == '4':
            screen = 'about'

        if command == '5':
            screen = 'sandboxMenu'

        if command == '6':
            screen = 'tempMap'

#This is the screen for the message board.
#----------------------------------------------------------------------------------
    if screen == "messageBoard":
        os.system("clear")
        headerStripped()

        print('\n    Welcome to the message board! Keep it friendly :)')
        print('\n    --------------------------------------------------------------------------------------\n')

        #print off recent messages
        #dump the last 30 lines of chatlog.log to the screen
        with open('chatlog.log', "r") as logfile:
            lines = logfile.readlines()
            last_lines = lines[-30:]
            last_lines = [line[:-1] for line in last_lines]
            for i in last_lines:
                print ('    ' + i)

        print('\n    --------------------------------------------------------------------------------------\n\n')
        tempMessage = input("    Type your message here or type \"leave\" to visit your stronghold:\n\n    ")
        if tempMessage == 'leave':
            screen = 'stronghold'

        elif tempMessage == 'truncate chat':
            log = open("chatlog.log", "r+")
            log.truncate(0)
            log.close()
        else:
            #add tempMessage to the chat log
            with open('chatlog.log', 'a') as log:
                log.write(userStronghold.name + ': ' + str(tempMessage) + '\n')

            #refresh this page
            screen = 'messageBoard'

# This is the screen for displaying past winners. Update it whenever we have a new winner
#----------------------------------------------------------------------------------
    if screen == "pastWinners":
        os.system("clear")
        headerStripped()

        print('\n    These are your honorable past winners of Unnamed Fiefdom Game')
        print('\n    --------------------------------------------------------------------------------------\n')
        print('\n    Pre-Release (12/20/21): Steelwing\n')
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        tempInput = input('    Press Enter to Continue')
        screen = 'moreCommands'

#This is the about page for the game. Keep it updated
#------------------------------------------------------------------------------
    if screen == "about":
        os.system("clear")
        headerStripped()

        print('\n\n')

        print('''

      Intro:

      Unnamed Fiefdom Game is a python programming project by Mike Quain (mquain@uark.edu) of the University of Arkansas,
      and Joshua Davis, also of the University of Arkansas. The game draws inspiration from the BBS door games of the late
      80s and early 90s, as well as more modern text-based games like Kings of Chaos. We started building this game in late
      2021 and it is still very much a work in progress. We welcome any an all contributions of code or bug reports.
      
      Thanks for playing!

      Additional Info is avalible at github.com/Sheeves11/UntitledFiefdomGame

        ''')

        tempInput = input('    Press Enter to Continue')
        return 'moreCommands'

#This prints out a little temperature cycle movie 
#------------------------------------------------------------------------------
    if screen == "tempMap":
        os.system('clear')
        headerStripped()
        print('    --------------------------------------------------------------------------------------------------------------   ')
        print('                                             T E M P E R A T U R E   M A P                                        ')
        print('    --------------------------------------------------------------------------------------------------------------   ')
        gameTime = int(readGametime())
        base = int(readBaseline())
        writeWeather(str(base), gameTime)
        updateWeatherFile()
        tempPrintout = '    Current Average Temperature: ' + str(readBaseline())
        print(textColor.WARNING, end = '')
        print('                                Current time: ' + str(readRealGametimeHour()) + ':' + str(readRealGametimeMin()) + ' ' + str(readRealGametimeAmpm() + tempPrintout))
        print(textColor.RESET, end = '')

        serverMap.name = "serverMap"
        serverMap.read()


        printTempMapDot(0)


        tempInput = input('\n\n                   Press Enter to Continue')
        return 'stronghold'

#This is the features page for the game. Keep it updated
#------------------------------------------------------------------------------
    if screen == "features":
        os.system("clear")

        headerStripped()
        print('\n\n')

        print('''


      Current Status:

      The game is currently in the the pre-release stage of development and new features are being added on a
      daily basis! Make sure you check back often to see what's new!

      Upcoming Features:

      {Weather Events} - Weather events and patterns will affect your fiefdom's performance. Rain could cost you
                         your advantage in battle, or a drought could hurt your gold production! Something as
                         simple as waiting for a clear sunset could give you the advantage in an attack where
                         the sun is in your opponent's eyes.

      {Market Investments} - Invest your gold in the markets! Prices will rise and fall as the season moves along.
                             Ride the charts on your way to the top.

      Thanks for playing! Submit your suggestions github.com/Sheeves11/UntitledFiefdomGame

        ''')

        tempInput = input('    Press Enter to Continue')
        return 'moreCommands'

    return screen

