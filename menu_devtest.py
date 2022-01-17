from globals import *
from market import *

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
        print('    {8}: Add Resources Tool (for testing!)')
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
            return 'devTestAddResources'

        if command == '9':
            return 'devTestWorldMapDiagnostics'

        if command == '10':
            return 'devTestRiverTool'
        
        if command == 't':
            screen = 'testScreen1'
        if command == 't2':
            screen = 'testScreen2'


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
    if screen == "devTestAddResources":
        os.system("clear")
        header(currentUsername)

        print('    Adding Resources!...')

        userStronghold.gold = str(int(userStronghold.gold) + 1000000)
        userStronghold.food = str(int(userStronghold.food) + 10000)
        userStronghold.wood = str(int(userStronghold.wood) + 10000)
        userStronghold.stone = str(int(userStronghold.stone) + 10000)
        userStronghold.ore = str(int(userStronghold.ore) + 1000)
        userStronghold.write()

        time.sleep(0.5)
        print('    ...Resources Added!')
        time.sleep(0.5)
        return 'stronghold'

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
    if screen == "testScreen1":
        os.system("clear")
        header(userStronghold.name)
        
        serverArmies.AddBattalion("Crimson Somethings", "y", "200", "1", "1", "1", "200", "5", "5")
        serverArmies.AddBattalion("Cool Dudes", "y", "105", "1", "1", "1", "120", "6", "6")
        serverArmies.AddBattalion("Neato Banditos", "y", "160", "1", "1", "1", "120", "7", "7")

        serverArmies.write()

        serverArmies.read()

        nothing = input('    Continue:')
        return 'devTest'

    if screen == "testScreen2":
        os.system("clear")

        print("Attempting to read!")
        serverMarket.read()

        serverMarket.ListGoods()

        nothing = input('    Continue:')
        return 'devTest'

    return screen

#eof