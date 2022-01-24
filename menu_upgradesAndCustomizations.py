from globals import *

#This document contains screens for:
#   upgradeStronghold
#   upgradeFiefMenu
#   upgradeAttack
#   upgradeFarm
#   upgradeDefense
#   changeStrongholdColor
#   setStrongholdMessage

def UpgradesAndCustomizations(screen, userStronghold):
    global currentPage
#This is the screen for upgrading and customizing your stronghold
#----------------------------------------------------------------------------------
    if screen == "upgradeStronghold":
        os.system("clear")

        header(userStronghold.name)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print("     Avalible Commands:")
        print('     -------------------------------------------------------')
        print('     {1}: Return to Stronghold')
        print('     {2}: Upgrade Attack')
        print('     {3}: Change Stronghold Color')
        print('     {4}: Set Stronghold Message')

        print('     --------------------------------------------------------')
        print('')
        command = input("     Enter your command: ")

        if command == '1':
            screen = 'stronghold'

        if command == '2':
            screen = 'upgradeAttack'

        if command == '3':
            screen = 'changeStrongholdColor'

        if command == '4':
            screen = 'setStrongholdMessage'

#This is a menu for additional features
#----------------------------------------------------------------------------------
    if screen == "upgradeFiefMenu":
        os.system("clear")
        
        header(userStronghold.name)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print("    Avalible Commands:")
        print('    -------------------------------------------------------')
        print('    {1}: Go Back')
        print('    {2}: Upgrade Defenses')
        # print('    {3}: Upgrade Farms')
        # print('    {4}: Upgrade Training')
        print('    --------------------------------------------------------')
        print('')
        command = input("    Enter your command: ")

        if command == '1':
            screen = 'ownedFiefDetails'

        if command == '2':
            screen = 'upgradeDefense'

        # if command == '3':
        #     screen = 'upgradeFarm'

        # if command == '4':
        #     screen = 'upgradeFiefMenu'

    
    #This is the screen for updating a user's attack power.
#----------------------------------------------------------------------------------
    if screen == "upgradeAttack":
        os.system("clear")
        header(userStronghold.name)

        attTypeNext = 'undefined'
        attUpgradeCost = 0

        if userStronghold.attLevel == str('0'):
            attTypeNext = NAME_ATTACK_T1
            attUpgradeCost = UPGRADE_ATTACK_T1

        if userStronghold.attLevel == str('1'):
            attTypeNext = NAME_ATTACK_T2
            attUpgradeCost = UPGRADE_ATTACK_T2

        if userStronghold.attLevel == str('2'):
            attTypeNext = NAME_ATTACK_T3
            attUpgradeCost = UPGRADE_ATTACK_T3

        if userStronghold.attLevel == str('3'):
            attTypeNext = NAME_ATTACK_T4
            attUpgradeCost = UPGRADE_ATTACK_T4

        if userStronghold.attLevel == str('4'):
            attTypeNext = NAME_ATTACK_T5
            attUpgradeCost = UPGRADE_ATTACK_T5

        if userStronghold.attLevel == str('5'):
            attTypeNext = NAME_ATTACK_T6
            attUpgradeCost = UPGRADE_ATTACK_T6

        if userStronghold.attLevel == str('6'):
            attTypeNext = NAME_ATTACK_T7
            attUpgradeCost = UPGRADE_ATTACK_T7

        if userStronghold.attLevel == str('7'):
            print('\n\n')
            print('    Your current army is made of ' + userStronghold.attType)
            print('    This is currently the highest attack level!')
            print('\n\n\n\n\n\n\n\n\n\n')
            command = input("    Press Enter to Continue")

        else:
            print('\n\n')
            print('    Your current army is made of ' + userStronghold.attType)
            print('    Would you like to upgrade to ' + attTypeNext + ' for ' + GetResourceCost(attUpgradeCost, 1) + '?')

            upgradeInput = input('\n\n     Confirm Upgrade (y/n?): ')

            if upgradeInput == 'y' and HaveEnoughResources(userStronghold, attUpgradeCost, 1):
                print("    Upgrade Complete!")
                userStronghold.attType = attTypeNext
                userStronghold.attLevel = str(int(userStronghold.attLevel) + 1)
                DeductResources(userStronghold, attUpgradeCost, 1)
                userStronghold.write()
                userStronghold.read()

            elif upgradeInput == 'y' and HaveEnoughResources(userStronghold, attUpgradeCost, 1) == False:
                print('\n')
                print("    You need more resources first!\n\n\n\n")

            elif upgradeInput == 'n':
                print('\n')
                print("    No changes made.")

            print('\n\n\n\n\n\n\n\n\n\n')
            command = input("    Press Enter to Continue")

        screen = "stronghold"



#This is the screen for updating a fief's defenses. Note: there are two screens
#like this. One for fiefs and one for player strongholds.
#----------------------------------------------------------------------------------
    if screen == "upgradeDefense":
        os.system("clear")
        headerFief(attackFief)

        defTypeNext = 'undefined'
        defUpgradeCost = 0

        if attackFief.defLevel == str('0'):
            defTypeNext = NAME_DEFENSE_T1
            defUpgradeCost = UPGRADE_DEFENSE_T1

        if attackFief.defLevel == str('1'):
            defTypeNext = NAME_DEFENSE_T2
            defUpgradeCost = UPGRADE_DEFENSE_T2

        if attackFief.defLevel == str('2'):
            defTypeNext = NAME_DEFENSE_T3
            defUpgradeCost = UPGRADE_DEFENSE_T3

        if attackFief.defLevel == str('3'):
            defTypeNext = NAME_DEFENSE_T4
            defUpgradeCost = UPGRADE_DEFENSE_T4

        if attackFief.defLevel == str('4'):
            defTypeNext = NAME_DEFENSE_T5
            defUpgradeCost = UPGRADE_DEFENSE_T5

        if attackFief.defLevel == str('5'):
            defTypeNext = NAME_DEFENSE_T6
            defUpgradeCost = UPGRADE_DEFENSE_T6

        if attackFief.defLevel == str('6'):
            print('    Your current defense style is: ' + attackFief.defType)
            print('    This is currently the best defense style!')
            print('\n\n\n\n\n\n\n\n\n\n')
            command = input("    Press Enter to Continue")
        else:
            print('    Your current defense style is: ' + attackFief.defType)
            print('    Would you like to upgrade to ' + defTypeNext + ' for ' + GetResourceCost(defUpgradeCost, 1) + '?')

            upgradeInput = input('    (y/n): ')

            if upgradeInput == 'y' and HaveEnoughResources(attackFief, defUpgradeCost, 1):
                print("    Upgrade Complete!")
                attackFief.defType = defTypeNext
                attackFief.defLevel = str(int(attackFief.defLevel) + 1)
                DeductResources(attackFief, defUpgradeCost, 1)
                attackFief.write()
                attackFief.read()
                userStronghold.write()
                userStronghold.read()

            elif upgradeInput == 'y' and HaveEnoughResources(attackFief, defUpgradeCost, 1) == False:
                print("    You need more resources first!")

            elif upgradeInput == 'n':
                print("    No changes made.")

            print('\n\n\n\n\n\n\n\n\n\n')
            command = input("    Press Enter to Continue")

        currentPage = 1
        screen = "ownedFiefDetails"

    #This page prints a menu for choosing your stronghold's color:
    if screen == "changeStrongholdColor":
        os.system("clear")
        header(userStronghold.name)

        print('\n\n\n\n\n')
        print("     Choose a Stronghold Color:")
        print('    -------------------------------------')
        print('''    {1}: Red       '''+RED+'''#'''+RESET+'''   {10}: Purple     '''+PURPLE+'''#'''+RESET+''' ''')
        print('''    {2}: Green     '''+GREEN+'''#'''+RESET+'''   {11}: Orange     '''+ORANGE+'''#'''+RESET+''' ''')
        print('''    {3}: Blue      '''+BLUE+'''#'''+RESET+'''   {12}: Teal       '''+TEAL+'''#'''+RESET+''' ''')
        print('''    {4}: Yellow    '''+YELLOW+'''#'''+RESET+'''   {13}: Pink       '''+PINK+'''#'''+RESET+''' ''')
        print('''    {5}: Magenta   '''+MAGENTA+'''#'''+RESET+'''   {14}: Brown      '''+BROWN+'''#'''+RESET+''' ''')
        print('''    {6}: Cyan      '''+CYAN+'''#'''+RESET+'''   {15}: Mint       '''+MINT+'''#'''+RESET+''' ''')
        print('''    {7}: White     '''+BOLD+'''#'''+RESET+'''   {16}: Salmon     '''+SALMON+'''#'''+RESET+''' ''')
        print('''    {8}: Gray      '''+DARK_GRAY+'''#'''+RESET+'''   {17}: Lavender   '''+LAVENDER+'''#'''+RESET+''' ''')
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
        if command == "10":
            userStronghold.color = 'purple'
        if command == "11":
            userStronghold.color = 'orange'
        if command == "12":
            userStronghold.color = 'teal'
        if command == "13":
            userStronghold.color = 'pink'
        if command == "14":
            userStronghold.color = 'brown'
        if command == "15":
            userStronghold.color = 'mint'
        if command == "16":
            userStronghold.color = 'salmon'
        if command == "17":
            userStronghold.color = 'lavender'
        
        userStronghold.write()
        screen = "stronghold"

#This is the screen for setting your stronghold message
#----------------------------------------------------------------------------------
    if screen == "setStrongholdMessage":
        os.system("clear")
        header(userStronghold.name)
        print('\n\n')
        strongHoldMessage = '    Your current message is: ' + userStronghold.strongholdMessage
        print(strongHoldMessage.center(110, ' '), end = ' ')
        print('\n\n\n')

        art_signpost()
        print('\n\n\n')

        #get input for the stronghold message and only write it if less than 80 characters
        userStronghold.strongholdMessage = input('    Enter your new message: ')
        if len(userStronghold.strongholdMessage) > 80:
            print('\n    Error! Only 80 characters allowed!')

        if len(userStronghold.strongholdMessage) <= 80:
            print('\n    Message Accepted')
            userStronghold.write()

        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        tempInput = input('    Press Enter to Continue')
        screen = 'stronghold'
        
    return screen