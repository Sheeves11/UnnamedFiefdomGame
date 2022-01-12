from globals import *

#This document contains screens for:
#   hireAndRecruit
#   thieves
#   mercs

def HireMenu(screen, userStronghold):
    global currentPage
#This is a menu for hiring and recruiting troops
#----------------------------------------------------------------------------------
    if screen == "hireAndRecruit":
        os.system("clear")

        header(currentUsername)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print("     Avalible Commands:")
        print('     -------------------------------------------------------')
        print('     {1}: Return to Stronghold')
        print('     {2}: Hire Mercenaries')
        print('     {3}: Hire Thieves')
        print('     --------------------------------------------------------')
        print('')
        command = input("     Enter your command: ")

        if command == '1':
            screen = 'stronghold'

        if command == '2':
            screen = 'mercs'

        if command == '3':
            screen = 'thieves'


#This is the screen for purchacing soldiers
#----------------------------------------------------------------------------------
    if screen == "thieves":
        #define the cost of a soldier here
        thiefCost = 1000

        os.system("clear")
        header(currentUsername)

        print('''
            
            
            
        As in all cities, your stronghold is home to a number of seedy characters who frequent the criminal underbelly
        of society. For a price, they will be loyal to you.
        
        Thieves do not contribute to your gold production, but they can infilitrate other player strongholds
        and return with stolen gold.
        ''')

        print('\n\n\n        You currently have ' + str(userStronghold.thieves) + ' thieves and ' +  str(userStronghold.gold) + ' gold.')

        print('        You can hire thieves for ' + str(thiefCost) + ' gold each')

        upgradeInput = input('\n        Enter the number of thieves you would like to hire: ')

        try:
            int(upgradeInput)
        except:
            upgradeInput = '0'

        if int(upgradeInput) == 0:
            print("        No changes were made!")

        elif int(upgradeInput) < 0:
            print("        You can't hire a negative number of thieves")

        elif (int(upgradeInput) * thiefCost) <=  int(userStronghold.gold):
            print("    Hiring " + str(upgradeInput) + " thieves...")
            time.sleep(0.5)
            userStronghold.thieves = str(int(userStronghold.thieves) + int(upgradeInput))
            print("    Success! You now have " + str(userStronghold.thieves) + " thieves at your disposal.")
            userStronghold.gold = str(int(userStronghold.gold) - (thiefCost * int(upgradeInput)))
            userStronghold.write()
            userStronghold.read()

        else:
            print("        You need more gold first!")

        print("\n\n\n\n\n\n\n\n\n")

        print("        Avalible Commands:")
        print('        -------------------------------------')
        print('        {1}: Return to Stronghold')
        print('        {2}: View Fiefdoms')
        print('        {3}: View Player Strongholds')
        print('        -------------------------------------')
        print('')
        command = input("        Enter your command: ")

        if command == "1":
            screen = "stronghold"
        if command == "2":
            currentPage = 1
            screen = "fiefdoms"
        if command == "3":
            currentPage = 1
            screen = "playerStrongholds"


#This is the screen for purchacing soldiers
#----------------------------------------------------------------------------------
    if screen == "mercs":
        #define the cost of a soldier here
        mercCost = 10

        os.system("clear")
        header(currentUsername)

        print('\n\n\n')
        print('    You currently have ' + str(userStronghold.defenders) + ' soldiers and ' +  str(userStronghold.gold) + ' gold.')

        print('    You can hire mercinaries for ' + str(mercCost) + ' gold each?')

        upgradeInput = input('\n    How many mercinaries would you like to hire? : ')

        try:
            int(upgradeInput)
        except:
            upgradeInput = '0'

        if int(upgradeInput) == 0:
            print("    No changes were made!")

        elif int(upgradeInput) < 0:
            print("    You can't hire a negative number of soldiers")

        elif (int(upgradeInput) * mercCost) <=  int(userStronghold.gold):
            print("    Hiring " + str(upgradeInput) + " soldiers...")
            time.sleep(0.5)
            userStronghold.defenders = str(int(userStronghold.defenders) + int(upgradeInput))
            print("    Success! You now have " + str(userStronghold.defenders) + " soldiers at your disposal.")
            userStronghold.gold = str(int(userStronghold.gold) - (mercCost * int(upgradeInput)))
            userStronghold.write()
            userStronghold.read()

        else:
            print("    You need more gold first!")

        print("\n\n\n\n\n\n\n\n\n")
        print("    Avalible Commands:")
        print('    -------------------------------------')
        print('    {1}: Return to Stronghold')
        print('    {2}: View Fiefdoms')
        print('    -------------------------------------')
        print('')
        command = input("    Enter your command: ")

        if command == "1":
            screen = "stronghold"
        if command == "2":
            currentPage = 1
            screen = "fiefdoms"
    return screen