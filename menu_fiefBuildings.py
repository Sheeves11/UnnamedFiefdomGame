from globals import *

#This document contains screens for:
#   outposts
#   fisheries
#   lumberMills
#   farmlands
#   mines

def FiefBuildingsMenu(screen, userStronghold):
    if screen == "outposts":
        unitType = "unit"
        unitsOwned = 0
        unitCap = 10
        unitBaseCost = 1000
        outpostType = ""
        prev = "outposts"

        os.system("clear")
        header(userStronghold.name)

        # #Show different expansions available only if land exists for them:
        # if int(attackFief.adjacentWater) > 0 or int(attackFief.adjacentRivers) > 0:
        #     print("    You have room to construct " + str(int(attackFief.adjacentWater) + int(attackFief.adjacentRivers)) + " Fisheries.")
        # if int(attackFief.adjacentForests) > 0:
        #     print("    You have room to construct " + str(attackFief.adjacentForests) + " Lumber Mills.")
        # if int(attackFief.adjacentPlains) > 0:
        #     print("    You have room to construct " + str(attackFief.adjacentPlains) + " Farmlands.")
        # if int(attackFief.adjacentMountains) > 0:
        #     print("    You have room to construct " + str(attackFief.adjacentMountains) + " Mines.")
        
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
        if int(attackFief.adjacentWater) > 0 or int(attackFief.adjacentRivers) > 0:
            if str(command) == '2':
                screen = "fisheries"
        if int(attackFief.adjacentForests) > 0:
            if str(command) == '3':
                screen = "lumberMills"
        if int(attackFief.adjacentPlains) > 0:
            if str(command) == '4':
                screen = "farmlands"
        if int(attackFief.adjacentMountains) > 0:
            if str(command) == '5':
                screen = "mines"

    if screen == "fisheries":
        os.system("clear")
        header(userStronghold.name)

        outpostType = "fishery"

        print("\n    Avalible Commands:")
        print('    -------------------------------------')
        print('    {1}: Go Back')
        print('    {2}: Hire Fishers')
        print('    {3}: Hire Scavengers')
        print('    {4}: Upgrade Fisheries')
        print('    {5}: Construct New Fishery')
        print('    -------------------------------------')
        print('')
        command = input("    Enter your command: ")
        
        if str(command) == '1':
            return "outposts"
        if str(command) == '2':
            unitType = "Fisher"
            screen = "hireOutpostUnits"
        if str(command) == '3':
            unitType = "Scavenger"
            screen = "hireOutpostUnits"
        if str(command) == '4':
            return "outposts"
        if str(command) == '5':
            return "outposts"

    if screen == "lumberMills":
        os.system("clear")
        header(userStronghold.name)

        outpostType = "lumberMill"

        print("\n    Avalible Commands:")
        print('    -------------------------------------')
        print('    {1}: Go Back')
        print('    {2}: Hire Lumberjacks')
        print('    {3}: Hire Hunters')
        print('    {4}: Upgrade Lumber Mills')
        print('    {5}: Construct New Lumber Mill')
        print('    -------------------------------------')
        print('')
        command = input("    Enter your command: ")
        
        if str(command) == '1':
            return "outposts"
        if str(command) == '2':
            unitType = "Lumberjack"
            screen = "hireOutpostUnits"
        if str(command) == '3':
            unitType = "Hunter"
            screen = "hireOutpostUnits"
        if str(command) == '4':
            return "outposts"
        if str(command) == '5':
            return "outposts"
    
    if screen == "farmlands":
        os.system("clear")
        header(userStronghold.name)

        outpostType = "farmland"

        print("\n    Avalible Commands:")
        print('    -------------------------------------')
        print('    {1}: Go Back')
        print('    {2}: Hire Farmers')
        print('    {3}: Hire Vendors')
        print('    {4}: Upgrade Lumber Mills')
        print('    {5}: Construct New Lumber Mill')
        print('    -------------------------------------')
        print('')
        command = input("    Enter your command: ")
        
        if str(command) == '1':
            return "outposts"
        if str(command) == '2':
            unitType = "Farmer"
            screen = "hireOutpostUnits"
        if str(command) == '3':
            unitType = "Vendor"
            screen = "hireOutpostUnits"
        if str(command) == '4':
            return "outposts"
        if str(command) == '5':
            return "outposts"

        return "ownedFiefDetails"

    if screen == "mines":
        os.system("clear")
        header(userStronghold.name)

        outpostType = "mine"

        print("\n    Avalible Commands:")
        print('    -------------------------------------')
        print('    {1}: Go Back')
        print('    {2}: Hire Miners')
        print('    {3}: Hire Prospectors')
        print('    {4}: Upgrade Mines')
        print('    {5}: Construct New Mine')
        print('    -------------------------------------')
        print('')
        command = input("    Enter your command: ")
        
        if str(command) == '1':
            return "outposts"
        if str(command) == '2':
            unitType = "Miner"
            screen = "hireOutpostUnits"
        if str(command) == '3':
            unitType = "Prospector"
            screen = "hireOutpostUnits"
        if str(command) == '4':
            return "outposts"
        if str(command) == '5':
            return "outposts"
            
        return "ownedFiefDetails"

    if screen == "hireOutpostUnits":
        if outpostType == "farmland":
            if unitType == "Farmer"
        elif outpostType == "fishery":
            pass
        elif outpostType == "lumberMill":
            pass
        elif outpostType == "mine":
            pass

        os.system("clear")
        header(userStronghold.name)
        spotsAvailable = unitCap - unitsOwned
        print("    You currently have " + str(unitsOwned) + " " + unitType + " hired.")
        time.sleep(0.5)
        print("    You have room for " + str(spotsAvailable) + " more of these units.")
        time.sleep(0.5)
        unitInput = input("    How many " + unitType + " would you like to hire? : ")

        try:
            int(unitInput)
        except:
            unitInput = '0'

        if int(unitInput) == 0:
            print("    No changes were made!")

        elif int(unitInput) < 0:
            print("    You can't hire a negative number of " + unitType + "!")

        elif (int(unitInput) * unitBaseCost) <=  int(userStronghold.gold):
            print("    Hiring " + str(unitInput) + unitType + " units...")
            time.sleep(0.5)
            print("    Success! You now have " + str(unitsOwned) + " " + unitType + " units!")
            # print("    Success! You now have " + str(userStronghold.defenders) + " soldiers at your disposal.")
            # userStronghold.gold = str(int(userStronghold.gold) - (mercCost * int(unitInput)))
            userStronghold.write()
            userStronghold.read()

        else:
            print("    You need more gold first!")
        return "outposts"

    

    return screen