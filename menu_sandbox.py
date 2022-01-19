from globals import *
from tests.sandbox import *

#This document contains screens for:
#   sandboxMenu
#   sbTestMap
#   sbCreateFief
#   sbPlotTestFiefs
#   sbViewMap

def SandboxMenu(screen):
#This is the about page for the game. Keep it updated
#------------------------------------------------------------------------------
    if screen == "sandboxMenu":
        os.system("clear")
        headerStripped()

        print('\n\n')
        print('     Welcome to the Sandbox Menu!')
        print('     Here, you can generate a test map to see how it works.')
        art_globe()

        print('\n\n\n\n\n')
        print("    Avalible Commands:")
        print('    -------------------------------------')
        print('    {1}: Return to Stronghold')
        print('    {2}: Generate a Test Map')
        # print('    {3}: Create Custom Fiefs')
        # print('    {3}: Add Test Fiefs to Map')   #Bug that adds these to main fiefs folder. Not sure why yet.
        print('    {3}: View Map (Generate First)')
        print('    -------------------------------------')
        print('')
        command = input("    Enter your command: ")

        if command == "1":
            return "stronghold"
        if command == "2":
            return "sbTestMap"
        # if command == "3":
        #     return "sbCreateFief"
        # if command == "3":
            # return "sbPlotTestFiefs"
        if command == "3":
            return "sbViewMap"

#This is a page where users can generate maps of their own
#------------------------------------------------------------------------------
    if screen == "sbTestMap":
        os.system("clear")
        headerStripped()

        TestResetFiefCoordinates()

        testMap.name = 'testMap'
        testMap.seed = GenerateSeed()
        testMap.height = MAP_HEIGHT
        testMap.width = MAP_WIDTH
        testMap.worldMap = GenerateWorldMap(testMap.seed)
        SetBiomeCounts(testMap)
        testMap.write()
        
        print('    World Map:')

        PrintColorMap(testMap.worldMap)

        print('\n    Getting ready to generate rivers...')
        time.sleep(3)
        GenerateRivers(testMap)

        time.sleep(1)
        nothing = input('\n    Continue:')

        return 'sandboxMenu'

#This is a page where users can view the maps they generate
#------------------------------------------------------------------------------
    if screen == "sbCreateFief":
        os.system("clear")
        headerStripped()

        print('    Welcome to the fief creation tool!')
        print('    Please be aware that other users may be able to see the fiefs you create!')
        newFief = input('\n    Enter the name of your new fief: ')
        testFief = TestFiefdom()
        testFief.name = newFief
        testFief.defenders = random.randint(10, 100)
        testFief.gold = random.randint(500, 3100)
        testFief.write()

        print('    ' + str(testFief.name) + ' has been created!')
        time.sleep(1)
        nothing = input('\nContinue:')

        return 'sandboxMenu'

#This is a page where users can add fiefs to their test map
#------------------------------------------------------------------------------
    if screen == "sbPlotTestFiefs":
        os.system("clear")
        headerStripped()

        testMap.name = 'testMap'
        testMap.read()
        
        TestPlotAllFiefs(testMap)

        time.sleep(1)
        nothing = input('\n    Continue:')

        return 'sandboxMenu'

#This is a page where users can view the maps they generate
#------------------------------------------------------------------------------
    if screen == "sbViewMap":
        os.system("clear")
        headerStripped()
        
        testMap.name = 'testMap'
        testMap.read()
        
        print('    Current Test Map:')

        PrintColorMap(testMap.worldMap)

        time.sleep(1)
        nothing = input('\n    Continue:')

        return 'sandboxMenu'

    return screen

#eof