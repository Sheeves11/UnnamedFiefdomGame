from globals import *

#This document contains screens for:
#   upgradeStronghold
#   upgradeAttack
#   upgradeFarm
#   upgradeDefense
#   changeStrongholdColor

def UpgradesAndCustomizations(screen):
    global currentPage
#This is the screen for upgrading and customizing your stronghold
#----------------------------------------------------------------------------------
    if screen == "upgradeStronghold":
        os.system("clear")

        header()
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print("     Avalible Commands:")
        print('     -------------------------------------------------------')
        print('     {1}: Return to Stronghold')
        print('     {2}: Upgrade Attack')
        print('     {3}: Change Stronghold Color')
        print('     --------------------------------------------------------')
        print('')
        command = input("     Enter your command: ")

        if command == '1':
            screen = 'stronghold'

        if command == '2':
            screen = 'upgradeAttack'

        if command == '3':
            screen = 'changeStrongholdColor'
    
    #This is the screen for updating a user's attack power.
#----------------------------------------------------------------------------------
    if screen == "upgradeAttack":
        os.system("clear")
        header()

        attTypeNext = 'undefined'
        attUpgradeCost = 0

        if userStronghold.attLevel == str('0'):
            attTypeNext = 'Angry Villagers with Sharpened Pitchforks'
            attUpgradeCost = 500

        if userStronghold.attLevel == str('1'):
            attTypeNext = 'Semi-trained Longbow Archers'
            attUpgradeCost = 3500

        if userStronghold.attLevel == str('2'):
            attTypeNext = 'Military Recruits'
            attUpgradeCost = 10000

        if userStronghold.attLevel == str('3'):
            attTypeNext = 'Fairly Well-trained Archers with Flaming Arrows'
            attUpgradeCost = 45000

        if userStronghold.attLevel == str('4'):
            attTypeNext = 'Drunks with Trebuchets'
            attUpgradeCost = 75000

        if userStronghold.attLevel == str('5'):
            attTypeNext = 'Scientists who are Experiementing with Biological Warfare'
            attUpgradeCost = 200000

        if userStronghold.attLevel == str('6'):
            attTypeNext = 'Peasents with Guns'
            attUpgradeCost = 400000

        if userStronghold.attLevel == str('7'):
            print('\n\n')
            print('    Your current army is made of ' + userStronghold.attType)
            print('    This is currently the highest attack level!')
            print('\n\n\n\n\n\n\n\n\n\n')
            command = input("    Press Enter to Continue")

        else:
            print('\n\n')
            print('    Your current army is made of ' + userStronghold.attType)
            print('    Would you like to upgrade to ' + attTypeNext + ' for ' + str(attUpgradeCost) + ' gold?')

            upgradeInput = input('\n\n     Confirm Upgrade (y/n?): ')

            if upgradeInput == 'y' and int(userStronghold.gold) >= attUpgradeCost:
                print("    Upgrade Complete!")
                userStronghold.attType = attTypeNext
                userStronghold.attLevel = str(int(userStronghold.attLevel) + 1)
                userStronghold.gold = str(int(userStronghold.gold) - attUpgradeCost)
                userStronghold.write()
                userStronghold.read()

            elif upgradeInput == 'y' and int(userStronghold.gold) < attUpgradeCost:

                print('\n')
                print("    You need more gold first!\n\n\n\n")

            elif upgradeInput == 'n':
                print('\n')
                print("    No changes made.")

            print('\n\n\n\n\n\n\n\n\n\n')
            command = input("    Press Enter to Continue")

        screen = "stronghold"

#This is the screen for updating a fief's farm/gold production.
#----------------------------------------------------------------------------------
    if screen == "upgradeFarm":
        #these variables define the next upgrade level and the cost of that level
        farmTypeNext = 'undefined'
        farmUpgradeCost = 0
        os.system("clear")
        header()

        if attackFief.goldMod == str('1'):
            farmTypeNext = 'Watering Cans'
            farmUpgradeCost = 500

        if attackFief.goldMod == str('2'):
            farmTypeNext = 'Wheelbarrows'
            farmUpgradeCost = 2000

        if attackFief.goldMod == str('3'):
            farmTypeNext = 'Fertilizer'
            farmUpgradeCost = 5000

        if attackFief.goldMod == str('4'):
            farmTypeNext = 'Horse Plows'
            farmUpgradeCost = 10000

        if attackFief.goldMod == str('5'):
            farmTypeNext = 'Crop Rotation'
            farmUpgradeCost = 20000

        if attackFief.goldMod == str('6'):
            farmTypeNext = 'Artificial Selection'
            farmUpgradeCost = 40000

        if attackFief.goldMod == str('7'):
            print('\n    Your fiefdom\'s gold output is currently: ' + str((int(attackFief.goldMod) * goldOutput)) + ' per hour.')
            print('    This is currently the highest gold output!')

            print('\n\n\n\n\n\n\n\n\n\n')
            command = input("    Press Enter to Continue")

        else:
            print('\n    Your fiefdom\'s gold output is currently: ' + str((int(attackFief.goldMod) * goldOutput)) + ' per hour.')
            print('    Would you like to upgrade to ' + farmTypeNext + ' for ' + str(farmUpgradeCost) + ' gold?')

            upgradeInput = input('\n    y/n: ')

            if upgradeInput == 'y' and int(userStronghold.gold) >= farmUpgradeCost:
                print("\n    Upgrade Complete!")
                attackFief.farmType = farmTypeNext
                attackFief.goldMod = str(int(attackFief.goldMod) + 1)
                userStronghold.gold = str(int(userStronghold.gold) - farmUpgradeCost)
                attackFief.write()
                attackFief.read()
                userStronghold.write()
                userStronghold.read()
                currentPage = 1
                screen = "fiefdoms"

            elif upgradeInput == 'y' and int(userStronghold.gold) < farmUpgradeCost:
                print("\n    You need more gold first!")

            elif upgradeInput == 'n':
                print("\n    No changes made.")

            print('\n\n\n\n\n\n\n\n\n\n')
            command = input("    Press Enter to Continue")

        currentPage = 1
        screen = "homeDetails"

#This is the screen for updating a fief's defenses. Note: there are two screens
#like this. One for fiefs and one for player strongholds.
#----------------------------------------------------------------------------------
    if screen == "upgradeDefense":
        os.system("clear")

        header()

        defTypeNext = 'undefined'
        defUpgradeCost = 0

        if attackFief.defLevel == str('0'):
            defTypeNext = 'Wooden Fences'
            defUpgradeCost = 500

        if attackFief.defLevel == str('1'):
            defTypeNext = 'Really Deep Ditches'
            defUpgradeCost = 2500

        if attackFief.defLevel == str('2'):
            defTypeNext = 'Tall Towers'
            defUpgradeCost = 5000

        if attackFief.defLevel == str('3'):
            defTypeNext = 'In a Lake'
            defUpgradeCost = 10000

        if attackFief.defLevel == str('4'):
            defTypeNext = 'On Top of a Mountain'
            defUpgradeCost = 20000

        if attackFief.defLevel == str('5'):
            defTypeNext = 'Boiling Oil'
            defUpgradeCost = 50000

        if attackFief.defLevel == str('6'):
            print('    Your current defense style is: ' + attackFief.defType)
            print('    This is currently the best defense style!')
            print('\n\n\n\n\n\n\n\n\n\n')
            command = input("    Press Enter to Continue")
        else:
            print('    Your current defense style is: ' + attackFief.defType)
            print('    Would you like to upgrade to ' + defTypeNext + ' for ' + str(defUpgradeCost) + ' gold?')

            upgradeInput = input('    (y/n): ')

            if upgradeInput == 'y' and int(userStronghold.gold) >= defUpgradeCost:
                print("    Upgrade Complete!")
                attackFief.defType = defTypeNext
                attackFief.defLevel = str(int(attackFief.defLevel) + 1)
                userStronghold.gold = str(int(userStronghold.gold) - defUpgradeCost)
                attackFief.write()
                attackFief.read()
                userStronghold.write()
                userStronghold.read()

            elif upgradeInput == 'y' and int(userStronghold.gold) < defUpgradeCost:

                print("    You need more gold first!")

            elif upgradeInput == 'n':
                print("    No changes made.")

            print('\n\n\n\n\n\n\n\n\n\n')
            command = input("    Press Enter to Continue")

        currentPage = 1
        screen = "homeDetails"

    #This page prints a menu for choosing your stronghold's color:
    if screen == "changeStrongholdColor":
        os.system("clear")
        header()

        print('\n\n\n\n\n')
        print("     Choose a Stronghold Color:")
        print('    -------------------------------------')
        print('''    {1}: Red       '''+textColor.RED+'''#'''+textColor.RESET+''' ''')
        print('''    {2}: Green     '''+textColor.GREEN+'''#'''+textColor.RESET+''' ''')
        print('''    {3}: Blue      '''+textColor.BLUE+'''#'''+textColor.RESET+''' ''')
        print('''    {4}: Yellow    '''+textColor.YELLOW+'''#'''+textColor.RESET+''' ''')
        print('''    {5}: Magenta   '''+textColor.MAGENTA+'''#'''+textColor.RESET+''' ''')
        print('''    {6}: Cyan      '''+textColor.CYAN+'''#'''+textColor.RESET+''' ''')
        print('''    {7}: White     '''+textColor.BOLD+'''#'''+textColor.RESET+''' ''')
        print('''    {8}: Gray      '''+textColor.DARK_GRAY+'''#'''+textColor.RESET+''' ''')
        print('    {9}: Leave color as is')
        print('    -------------------------------------')
        print('')
        command = input("    Enter your command: ")

        if command == "1":
            userStronghold.color = 'red'
        if command == "2":
            userStronghold.color = 'green'
        if command == "3":
            userStronghold.color = 'blue'
        if command == "4":
            userStronghold.color = 'yellow'
        if command == "5":
            userStronghold.color = 'magenta'
        if command == "6":
            userStronghold.color = 'cyan'
        if command == "7":
            userStronghold.color = 'white'
        if command == "8":
            userStronghold.color = 'gray'
        
        userStronghold.write()
        screen = "stronghold"

        
    return screen