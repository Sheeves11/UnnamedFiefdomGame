from globals import *

#This document contains screens for:
#   outposts
#   fisheries
#   lumberMills
#   farmlands
#   mines

def FiefBuildingsMenu(screen, userStronghold):
    if screen == "outposts":
        os.system("clear")
        header(userStronghold.name)

        #Show different expansions available only if land exists for them:
        if int(attackFief.adjacentWater) > 0 or int(attackFief.adjacentRivers) > 0:
            print("    You have room to construct " + str(int(attackFief.adjacentWater) + int(attackFief.adjacentRivers)) + " Fisheries.")
        if int(attackFief.adjacentForests) > 0:
            print("    You have room to construct " + str(attackFief.adjacentForests) + " Lumber Mills.")
        if int(attackFief.adjacentPlains) > 0:
            print("    You have room to construct " + str(attackFief.adjacentPlains) + " Farmlands.")
        if int(attackFief.adjacentMountains) > 0:
            print("    You have room to construct " + str(attackFief.adjacentMountains) + " Mines.")
        
        print("\n    Avalible Commands:")
        print('    -------------------------------------')
        print('    {1}: Go Back')
        #Show different expansions available only if land exists for them:
        if int(attackFief.adjacentWater) > 0 or int(attackFief.adjacentRivers) > 0:
            print("    {2}: Manage Fisheries [" + str(int(attackFief.adjacentWater) + int(attackFief.adjacentRivers)) + "]")
        if int(attackFief.adjacentForests) > 0:
            print("    {3}: Manage Lumber Mills [" + str(attackFief.adjacentForests) + "]")
        if int(attackFief.adjacentPlains) > 0:
            print("    {4}: Manage Farmlands [" + str(attackFief.adjacentPlains) + "]")
        if int(attackFief.adjacentMountains) > 0:
            print("    {5}: Manage Mines [" + str(attackFief.adjacentMountains) + "]")
        print('    -------------------------------------')
        print('')
        command = input("    Enter your command: ")
        
        if str(command) == '1':
            return "ownedFiefDetails"
        if str(command) == '2':
            return "fisheries"
        if str(command) == '3':
            return "lumberMills"
        if str(command) == '4':
            return "farmlands"
        if str(command) == '5':
            return "mines"

    if screen == "fisheries":
        os.system("clear")
        header(userStronghold.name)

        return "ownedFiefDetails"

    if screen == "outposts":
        os.system("clear")
        header(userStronghold.name)

        return "ownedFiefDetails"

    if screen == "lumberMills":
        os.system("clear")
        header(userStronghold.name)

        return "ownedFiefDetails"

    if screen == "farmlands":
        os.system("clear")
        header(userStronghold.name)

        return "ownedFiefDetails"

    if screen == "mines":
        os.system("clear")
        header(userStronghold.name)

        return "ownedFiefDetails"

    

    return screen