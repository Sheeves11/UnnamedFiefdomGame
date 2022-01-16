from globals import *

#This document contains screens for:
#   devTest
#   devTestCreateDefaults
#   devTestWorldMap
#   devTestFiefPlacement
#   devTestPlotAllFiefs
#   devTestPlotAllStrongholds
#   devTestGenerateWorld
#   devTestAddGold
#   devTestWorldMapDiagnostics
#   devTestRiverTool

def DevTestMenu(screen, userStronghold):
#This is the new devtest menu with all the devtest commands sorted out and neat
#------------------------------------------------------------------------------
    if screen == "devTest":
        os.system("clear")
        header(currentUsername)
        print("\n")

        print('    Welcome to the dev test menu. This should only be used for testing purposes.')
        print('\n')
        
        art_devBricks()

        print("    Avalible Commands:")
        print('    -------------------------------------------------------')
        print('    {1}: Return to Stronghold')
        print('    {2}: Create Default Fiefs')
        print('    {3}: Generate World Map (Must do this before 4-6)')
        print('    {4}: Add Fief Tool')
        print('    {5}: Add all Fiefs Tool')
        print('    {6}: Add all Strongholds Tool')
        print('    {7}: Quick Generate World (DO NOT USE if 3-6 were used!)')
        print('    {8}: Add Gold Tool (for testing!)')
        print('    {9}: World Map Diagnostic (Only run after step 3 or 7)')
        print('    {10}: World Map River Tool')
        print('    --------------------------------------------------------')
        print('    Note: To quick generate a world, just hit 7. To go step ')
        print('          by step, start at 3 and proceed without using 7!  ')
        print('')
        command = input("    Enter your command: ")

        if command == '1':
            currentPage = 1
            return "stronghold"

        if command == '2':
            return 'devTestCreateDefaults'

        if command == '3':
            return 'devTestWorldMap'

        if command == '4':
            return 'devTestFiefPlacement'

        if command == '5':
            return 'devTestPlotAllFiefs'

        if command == '6':
            return 'devTestPlotAllStrongholds'

        if command == '7':
            return 'devTestGenerateWorld'

        if command == '8':
            return 'devTestAddGold'

        if command == '9':
            return 'devTestWorldMapDiagnostics'

        if command == '10':
            return 'devTestRiverTool'
        
        if command == 't':
            screen = 'testScreen'


#This is a "secret" page that you can use to create default Fiefdoms
#to seed your installation with land that can be taken.
#
#It should be taken out if you ever open this game up to many players
#----------------------------------------------------------------------------------
    if screen == "devTestCreateDefaults":
        os.system("clear")
        header(currentUsername)

        print('    Seeding the world with default fiefdoms')

        names = ['Razor Hills', 'Stormgrove',
                'Dreadwall', 'Bellhollow', 'Howling Plains',
                'Knoblands', 'Kestrel Keep', 'Direbrook',
                'Greystone', 'Midgar']
        for x in names:
            currentFief = Fiefdom()
            currentFief.name = x
            currentFief.defenders = random.randint(10, 100)
            currentFief.gold = random.randint(500, 3100)
            currentFief.write()

        time.sleep(2)
        print('    Seeding Complete')
        currentPage = 1
        return "fiefdoms"

#This is another "secret" page that can be used to add funds for testing purposes
#
#It should be taken out if you ever open this game up to many players
#----------------------------------------------------------------------------------
    if screen == "devTestAddGold":
        os.system("clear")
        header(currentUsername)

        print('    Adding Funds!...')

        userStronghold.gold = str(int(userStronghold.gold) + 1000000)
        userStronghold.write()

        time.sleep(0.5)
        print('    ...Funds Added!')
        time.sleep(0.5)
        return 'devTest'

#This is a devtool for making the world map for a server
#
#It eventually needs to be accessed in another way
#----------------------------------------------------------------------------------
    if screen == "devTestWorldMap":
        os.system("clear")
        header(currentUsername)

        serverMap.name = 'serverMap'
        serverMap.seed = GenerateSeed()
        serverMap.height = MAP_HEIGHT
        serverMap.width = MAP_WIDTH
        serverMap.worldMap = GenerateWorldMap(serverMap.seed)
        SetBiomeCounts(serverMap)
        serverMap.write()

        print('\n')
        PrintColorMap(serverMap.worldMap)

        nothing = input('\n    Continue:')

        return 'devTest'

#This is currently just a test page to see if fief placement in the world map works as intended
#----------------------------------------------------------------------------------
    if screen == "devTestFiefPlacement":
        os.system("clear")
        header(currentUsername)

        fief = Fiefdom()
        command = input('    Enter a fief name to input: ')

        fileFief = 'fiefs/' + command + '.txt'
        try:
            with open(fileFief, 'r') as f:
                fief.name = f.readline().strip()
                fief.read()
        except:
            print ('    No file found')

        PlaceFiefInWorldMap(fief, serverMap)

        nothing = input('    Continue:')

        return 'devTest'

#This plots all fiefs on the server at once
#----------------------------------------------------------------------------------
    if screen == "devTestPlotAllFiefs":
        os.system("clear")
        header(currentUsername)

        PlotAllFiefs(serverMap)

        nothing = input('    Continue:')

        return 'devTest'
        
#This plots all strongholds on the server at once
#----------------------------------------------------------------------------------
    if screen == "devTestPlotAllStrongholds":
        os.system("clear")
        header(currentUsername)

        PlotAllStrongholds(serverMap)

        nothing = input('    Continue:')

        return 'devTest'


#This impelments all the map related functions in one go
#----------------------------------------------------------------------------------
    if screen == "devTestGenerateWorld":
        os.system("clear")
        header(currentUsername)

        serverMap.name = 'serverMap'
        serverMap.seed = GenerateSeed()
        serverMap.height = MAP_HEIGHT
        serverMap.width = MAP_WIDTH
        serverMap.worldMap = SilentlyGenerateWorldMap(serverMap.seed)
        SetBiomeCounts(serverMap)
        serverMap.write()

        os.system("clear")
        PlotAllFiefs(serverMap)

        os.system("clear")
        PlotAllStrongholds(serverMap)

        os.system("clear")
        print('    World Generation Complete!')
        print('')
        PrintColorMap(serverMap.worldMap)

        nothing = input('    Continue:')

        return 'devTest'

#This impelments all the map related functions in one go
#----------------------------------------------------------------------------------
    if screen == "devTestWorldMapDiagnostics":
        os.system("clear")
        header(currentUsername)

        serverMap.selfDiagnostic()
        # print('\n')
        # PrintLegend()
        print('\n')
        PrintColorMap(serverMap.worldMap)

        nothing = input('    Continue:')

        return 'devTest'

#This allows you to add rivers to a map
#-----------------------------------------------------------------------------------
    if screen == "devTestRiverTool":
        os.system("clear")

        serverMap.read()
        GenerateRivers(serverMap)

        nothing = input('    Continue:')
        
        return 'devTest'

#This is a test screen for quickly testing out formatting and the like.
#-----------------------------------------------------------------------------------
    if screen == "testScreen":
        os.system("clear")

        print("    Testing out resource printing functions:\n\n")

        PrintResourceCost("    Upgrading this thing to tier 1 costs", RESOURCE_TEST_VALUES_1, ".")
        if HaveEnoughResources(userStronghold, RESOURCE_TEST_VALUES_1):
            print("    Your stronghold can afford this!")
        try:
            if HaveEnoughResources(attackFief, RESOURCE_TEST_VALUES_1):
                print("    " + str(attackFief.name) + " can afford this!")
        except:
            print("    No current attackFief available.")

        PrintResourceCost("    Upgrading this thing to tier 2 costs", RESOURCE_TEST_VALUES_2, ".")
        if HaveEnoughResources(userStronghold, RESOURCE_TEST_VALUES_2):
            print("    Your stronghold can afford this!")
        try:
            if HaveEnoughResources(attackFief, RESOURCE_TEST_VALUES_2):
                print("    " + str(attackFief.name) + " can afford this!")
        except:
            print("    No current attackFief available.")
        PrintResourceCost("    Upgrading this thing to tier 3 costs", RESOURCE_TEST_VALUES_3, ".")
        if HaveEnoughResources(userStronghold, RESOURCE_TEST_VALUES_3):
            print("    Your stronghold can afford this!")
        try:
            if HaveEnoughResources(attackFief, RESOURCE_TEST_VALUES_3):
                print("    " + str(attackFief.name) + " can afford this!")
        except:
            print("    No current attackFief available.")
        PrintResourceCost("    Upgrading this thing to tier 4 costs", RESOURCE_TEST_VALUES_4, ".")
        if HaveEnoughResources(userStronghold, RESOURCE_TEST_VALUES_4):
            print("    Your stronghold can afford this!")
        try:
            if HaveEnoughResources(attackFief, RESOURCE_TEST_VALUES_4):
                print("    " + str(attackFief.name) + " can afford this!")
        except:
            print("    No current attackFief available.")


        unitType = "Farmer"
        flavorText = "    "
        costModifier = 0
        unitCap = UCAP_FARMER * int(attackFief.op_farmlandNumBuilt)

        HireUnit(attackFief, unitType, UCOST_FARMER, costModifier, unitCap, attackFief.op_farmlandPrimaryUnits, COLOR_FARMER, flavorText)

        nothing = input('    Continue:')
        return 'devTest'

    return screen

#eof