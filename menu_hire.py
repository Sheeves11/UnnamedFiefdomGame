from globals import *

#This document contains screens for:
#   hireAndRecruit
#   hireThieves
#   hireWarriors

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
        print('     {2}: Hire Warriors')
        print('     {3}: Hire Thieves')
        print('     --------------------------------------------------------')
        print('')
        command = input("     Enter your command: ")

        if command == '1':
            screen = 'stronghold'

        if command == '2':
            screen = 'hireWarriors'

        if command == '3':
            screen = 'hireThieves'


#This is the screen for purchacing thieves
#----------------------------------------------------------------------------------
    if screen == "hireThieves":
        os.system("clear")
        header(userStronghold.name)
        flavorText = '''
    As in all cities, your stronghold is home to a number of seedy characters who frequent the criminal underbelly
    of society. For a price, they will be loyal to you.

    Thieves do not contribute to your gold production, but they can infilitrate other player strongholds
    and return with stolen gold.
        '''
        costModifier = 0
        HireUnit(userStronghold, "Thief", UCOST_THIEF, costModifier, UCAP_THIEF, userStronghold.thieves, COLOR_THIEF, flavorText)
        return "stronghold"

#This is the screen for purchacing soldiers
#----------------------------------------------------------------------------------
    if screen == "hireWarriors":
        os.system("clear")
        header(userStronghold.name)
        flavorText = '''
    With these fighting machines and meat shields at your command, lay waste to your adversaries and defend
    what's yours.

    Warriors are your means to survive and conquer.
        '''
        costModifier = float(userStronghold.attLevel) * 0.5    #Scales with attack - 10/15/15/20/20/25/25/30....etc.
        #Note that the cost modifier currently does nothing, may need to add it back into the loop somehow.
        #Add a unitCap modifier later based on some kind of stronghold capacity upgrade?
        HireUnit(userStronghold, "Warrior", UCOST_WARRIOR, costModifier, UCAP_WARRIOR, userStronghold.defenders, COLOR_WARRIOR, flavorText)
        return "stronghold"

    return screen