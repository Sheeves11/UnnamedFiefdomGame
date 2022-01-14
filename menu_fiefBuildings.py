from globals import *

#This document contains screens for:
#   outposts
#   fisheries
#   lumberMills
#   farmlands
#   mines
#   outpostConstruction
#   upgradeOutposts
#   hireOutpostUnits

def FiefBuildingsMenu(screen, userStronghold):
    #==================================================================================================================================
    # outposts - Main menu for fief outposts
    #==================================================================================================================================
    if screen == "outposts":
        unitType = "unit"
        outpostType = ""

        os.system("clear")
        header(userStronghold.name)
        
        print("\n    Avalible Commands:")
        print('    -------------------------------------')
        print('    {1}: Go Back')
        #Show different expansions available only if land exists for them:
        if int(attackFief.adjacentPlains) > 0:
            print("    {2}: Manage Farmlands [" + str(attackFief.adjacentPlains) + "]")
        if int(attackFief.adjacentWater) > 0 or int(attackFief.adjacentRivers) > 0:
            print("    {3}: Manage Fisheries [" + str(int(attackFief.adjacentWater) + int(attackFief.adjacentRivers)) + "]")
        if int(attackFief.adjacentForests) > 0:
            print("    {4}: Manage Lumber Mills [" + str(attackFief.adjacentForests) + "]")
        if int(attackFief.adjacentMountains) > 0:
            print("    {5}: Manage Mines [" + str(attackFief.adjacentMountains) + "]")
        print('    -------------------------------------')
        print('')
        command = input("    Enter your command: ")
        
        if str(command) == '1':
            return "ownedFiefDetails"
        if int(attackFief.adjacentPlains) > 0:
            if str(command) == '2':
                screen = "farmlands"
        if int(attackFief.adjacentWater) > 0 or int(attackFief.adjacentRivers) > 0:
            if str(command) == '3':
                screen = "fisheries"
        if int(attackFief.adjacentForests) > 0:
            if str(command) == '4':
                screen = "lumberMills"
        if int(attackFief.adjacentMountains) > 0:
            if str(command) == '5':
                screen = "mines"

    #==================================================================================================================================
    # farmlands - Menu for constructing farmland related units and buildings
    #==================================================================================================================================
    if screen == "farmlands":
        os.system("clear")
        header(userStronghold.name)

        outpostType = "Farmland"

        if int(attackFief.op_farmlandNumBuilt) > 0:
            print("    You currently have " + str(attackFief.op_farmlandNumBuilt) + " Farmlands built.\n")
            
            if int(attackFief.op_farmlandPrimaryUnits) > 0:
                print("    You have " + str(attackFief.op_farmlandPrimaryUnits) + " Farmers growing food at a")
                print("    rate of " + str(attackFief.op_farmlandPrimaryPer) + " per hour.\n")
            else:
                print("    You have not hired any Farmers yet.\n")

            if int(attackFief.op_farmlandTier) > 0:
                if int(attackFief.op_farmlandSecondaryUnits) > 0:
                    print("    You have " + str(attackFief.op_farmlandSecondaryUnits) + " Vendors doing whatever they do")
                    print("    at a rate of " + str(attackFief.op_farmlandSecondaryPer) + " per hour.\n")
                else:
                    print("    You have not hired any Vendors yet.\n")

        else:
            print("    You haven't constructed any Farmlands yet.\n")

        print("\n    Avalible Commands:")
        print('    -------------------------------------')
        print('    {1}: Go Back')
        if int(attackFief.op_farmlandPrimaryUnits) < (int(UCAP_FARMER) * int(attackFief.op_farmlandNumBuilt)):
            print('    {2}: Hire Farmers')
        if (int(attackFief.op_farmlandSecondaryUnits) < (int(UCAP_VENDOR) * int(attackFief.op_farmlandNumBuilt)) and int(attackFief.op_farmlandTier) > 0):
            print('    {3}: Hire Vendors')
        if int(attackFief.op_farmlandNumBuilt) > 0 and int(attackFief.op_farmlandTier) < 2:
            print('    {4}: Upgrade Farmlands')
        if int(attackFief.op_farmlandNumBuilt) < int(attackFief.adjacentPlains):
            print('    {5}: Construct New Farmland')
        print('    -------------------------------------')
        print('')
        command = input("    Enter your command: ")
        
        if str(command) == '1':
            return "outposts"
        if int(attackFief.op_farmlandPrimaryUnits) < (int(UCAP_FARMER) * int(attackFief.op_farmlandNumBuilt)):
            if str(command) == '2':
                unitType = "Farmer"
                screen = "hireOutpostUnits"
        if (int(attackFief.op_farmlandSecondaryUnits) < (int(UCAP_VENDOR) * int(attackFief.op_farmlandNumBuilt)) and int(attackFief.op_farmlandTier) > 0):
            if str(command) == '3':
                unitType = "Vendor"
                screen = "hireOutpostUnits"
        if int(attackFief.op_farmlandNumBuilt) > 0 and int(attackFief.op_farmlandTier) < 2:
            if str(command) == '4':
                screen = "upgradeOutposts"
        if int(attackFief.op_farmlandNumBuilt) < int(attackFief.adjacentPlains):
            if str(command) == '5':
                screen = "outpostConstruction"

    #==================================================================================================================================
    # fisheries - Menu for constructing fishery related units and buildings
    #==================================================================================================================================
    if screen == "fisheries":
        os.system("clear")
        header(userStronghold.name)

        outpostType = "Fishery"

        #TODO - Print a descriptive message here that details the productiveness of all the fisheries around this fief!

        if int(attackFief.op_fisheryNumBuilt) > 0:
            print("    You currently have " + str(attackFief.op_fisheryNumBuilt) + " Fisheries built.\n")
            
            if int(attackFief.op_fisheryPrimaryUnits) > 0:
                print("    You have " + str(attackFief.op_fisheryPrimaryUnits) + " Fishers catching food at a")
                print("    rate of " + str(attackFief.op_fisheryPrimaryPer) + " per hour.\n")
            else:
                print("    You have not hired any Fishers yet.\n")

            if int(attackFief.op_fisheryTier) > 0:
                if int(attackFief.op_fisherySecondaryUnits) > 0:
                    print("    You have " + str(attackFief.op_fisherySecondaryUnits) + " Scavengers gathering random materials")
                    print("    at a rate of " + str(attackFief.op_fisherySecondaryPer) + " per hour.\n")
                else:
                    print("    You have not hired any Scavengers yet.\n")

        else:
            print("    You haven't constructed any Fisheries yet.\n")
    
        print("\n    Avalible Commands:")
        print('    -------------------------------------')
        print('    {1}: Go Back')
        if int(attackFief.op_fisheryPrimaryUnits) < (int(UCAP_FISHER) * int(attackFief.op_fisheryNumBuilt)):
            print('    {2}: Hire Fishers')
        if (int(attackFief.op_fisherySecondaryUnits) < (int(UCAP_SCAVENGER) * int(attackFief.op_fisheryNumBuilt)) and int(attackFief.op_fisheryTier) > 0):
            print('    {3}: Hire Scavengers')
        if int(attackFief.op_fisheryNumBuilt) > 0 and int(attackFief.op_fisheryTier) < 2:
            print('    {4}: Upgrade Fisheries')
        if int(attackFief.op_fisheryNumBuilt) < int(attackFief.adjacentWater) + int(attackFief.adjacentRivers):
            print('    {5}: Construct New Fishery')
        print('    -------------------------------------')
        print('')
        command = input("    Enter your command: ")
        
        if str(command) == '1':
            return "outposts"
        if int(attackFief.op_fisheryPrimaryUnits) < (int(UCAP_FISHER) * int(attackFief.op_fisheryNumBuilt)):
            if str(command) == '2':
                unitType = "Fisher"
                screen = "hireOutpostUnits"
        if (int(attackFief.op_fisherySecondaryUnits) < (int(UCAP_SCAVENGER) * int(attackFief.op_fisheryNumBuilt)) and int(attackFief.op_fisheryTier) > 0):
            if str(command) == '3':
                unitType = "Scavenger"
                screen = "hireOutpostUnits"
        if int(attackFief.op_fisheryNumBuilt) > 0 and int(attackFief.op_fisheryTier) < 2:
            if str(command) == '4':
                screen = "upgradeOutposts"
        if int(attackFief.op_fisheryNumBuilt) < int(attackFief.adjacentWater) + int(attackFief.adjacentRivers):
            if str(command) == '5':
                screen = "outpostConstruction"
                
    #==================================================================================================================================
    # lumberMills - Menu for constructing lumber mill related units and buildings
    #==================================================================================================================================
    if screen == "lumberMills":
        os.system("clear")
        header(userStronghold.name)

        outpostType = "Lumber Mill"

        #TODO - Print a descriptive message here that details the productiveness of all the fisheries around this fief!
        if int(attackFief.op_lumberMillNumBuilt) > 0:
            print("    You currently have " + str(attackFief.op_lumberMillNumBuilt) + " Lumber Mills built.\n")
            if int(attackFief.op_lumberMillPrimaryUnits) > 0:
                    print("    You have " + str(attackFief.op_lumberMillPrimaryUnits) + " Lumberjacks gathering wood at a")
                    print("    rate of " + str(attackFief.op_lumberMillPrimaryPer) + " per hour.\n")
            else:
                print("    You have not hired any Lumberjacks yet.\n")

            if int(attackFief.op_lumberMillTier) > 0:
                if int(attackFief.op_lumberMillSecondaryUnits) > 0:
                    print("    You have " + str(attackFief.op_lumberMillSecondaryUnits) + " Hunters hunting for food")
                    print("    at a rate of " + str(attackFief.op_lumberMillSecondaryPer) + " per hour.\n")
                else:
                    print("    You have not hired any Hunters yet.\n")

        else:
            print("    You haven't constructed any Lumber Mills yet.\n")

        

        print("\n    Avalible Commands:")
        print('    -------------------------------------')
        print('    {1}: Go Back')
        if int(attackFief.op_lumberMillPrimaryUnits) < (int(UCAP_LUMBERJACK) * int(attackFief.op_lumberMillNumBuilt)):
            print('    {2}: Hire Lumberjacks')
        if (int(attackFief.op_lumberMillSecondaryUnits) < (int(UCAP_HUNTER) * int(attackFief.op_lumberMillNumBuilt)) and int(attackFief.op_lumberMillTier) > 0):
            print('    {3}: Hire Hunters')
        if int(attackFief.op_lumberMillNumBuilt) > 0 and int(attackFief.op_lumberMillTier) < 2:
            print('    {4}: Upgrade Lumber Mills')
        if int(attackFief.op_lumberMillNumBuilt) < int(attackFief.adjacentForests):
            print('    {5}: Construct New Lumber Mill')
        print('    -------------------------------------')
        print('')
        command = input("    Enter your command: ")
        
        if str(command) == '1':
            return "outposts"
        if int(attackFief.op_lumberMillPrimaryUnits) < (int(UCAP_LUMBERJACK) * int(attackFief.op_lumberMillNumBuilt)):
            if str(command) == '2':
                unitType = "Lumberjack"
                screen = "hireOutpostUnits"
        if (int(attackFief.op_lumberMillSecondaryUnits) < (int(UCAP_HUNTER) * int(attackFief.op_lumberMillNumBuilt)) and int(attackFief.op_lumberMillTier) > 0):
            if str(command) == '3':
                unitType = "Hunter"
                screen = "hireOutpostUnits"
        if int(attackFief.op_lumberMillNumBuilt) > 0 and int(attackFief.op_lumberMillTier) < 2:
            if str(command) == '4':
                screen = "upgradeOutposts"
        if int(attackFief.op_lumberMillNumBuilt) < int(attackFief.adjacentForests):
            if str(command) == '5':
                screen = "outpostConstruction"

    #==================================================================================================================================
    # mines - Menu for constructing mine related units and buildings
    #==================================================================================================================================
    if screen == "mines":
        os.system("clear")
        header(userStronghold.name)

        outpostType = "Mine"

        if int(attackFief.op_mineNumBuilt) > 0:
            print("    You currently have " + str(attackFief.op_mineNumBuilt) + " Mines built.\n")
            if int(attackFief.op_minePrimaryUnits) > 0:
                print("    You have " + str(attackFief.op_minePrimaryUnits) + " Miners gathering stone at a")
                print("    rate of " + str(attackFief.op_minePrimaryPer) + " per hour.\n")
            else:
                
                print("    You have not hired any Miners yet.\n")

            if int(attackFief.op_mineTier) > 0:
                if int(attackFief.op_mineSecondaryUnits) > 0:
                    print("    You have " + str(attackFief.op_mineSecondaryUnits) + " Prospectors gathering iron")
                    print("    at a rate of " + str(attackFief.op_mineSecondaryPer) + " per hour.\n")
                else:
                    print("    You have not hired any Prospectors yet.\n")
        else:
            print("    You haven't constructed any Mines yet.\n")

        print("\n    Avalible Commands:")
        print('    -------------------------------------')
        print('    {1}: Go Back')
        if int(attackFief.op_minePrimaryUnits) < (int(UCAP_MINER) * int(attackFief.op_mineNumBuilt)):
            print('    {2}: Hire Miners')
        if (int(attackFief.op_mineSecondaryUnits) < (int(UCAP_PROSPECTOR) * int(attackFief.op_mineNumBuilt)) and int(attackFief.op_mineTier) > 0):
            print('    {3}: Hire Prospectors')
        if int(attackFief.op_mineNumBuilt) > 0 and int(attackFief.op_mineTier) < 2:
            print('    {4}: Upgrade Mines')
        if int(attackFief.op_mineNumBuilt) < int(attackFief.adjacentMountains):
            print('    {5}: Construct New Mine')
        print('    -------------------------------------')
        print('')
        command = input("    Enter your command: ")
        
        if str(command) == '1':
            return "outposts"
        if int(attackFief.op_minePrimaryUnits) < (int(UCAP_MINER) * int(attackFief.op_mineNumBuilt)):
            if str(command) == '2':
                unitType = "Miner"
                screen = "hireOutpostUnits"
        if (int(attackFief.op_mineSecondaryUnits) < (int(UCAP_PROSPECTOR) * int(attackFief.op_mineNumBuilt)) and int(attackFief.op_mineTier) > 0):
            if str(command) == '3':
                unitType = "Prospector"
                screen = "hireOutpostUnits"
        if int(attackFief.op_mineNumBuilt) > 0 and int(attackFief.op_mineTier) < 2:
            if str(command) == '4':
                screen = "upgradeOutposts"
        if int(attackFief.op_mineNumBuilt) < int(attackFief.adjacentMountains):
            if str(command) == '5':
                screen = "outpostConstruction"

    #==================================================================================================================================
    # outpostConstruction - menu for constructing new outposts
    #==================================================================================================================================
    if screen == "outpostConstruction":
        # ConstructOutpost(userStronghold, outpostType, tier, numberBuilt, spotsAvailable, cost, flavorText)
        if outpostType == "Farmland":
            spotsAvailable = int(attackFief.adjacentPlains) - int(attackFief.op_farmlandNumBuilt)
            tier = int(attackFief.op_farmlandTier)
            if int(tier) == 0:
                cost = OP_COST_T1_FARMLAND
            elif int(tier) == 1:
                cost = OP_COST_T1_FARMLAND + OP_COST_T2_FARMLAND
            elif int(tier) == 2:
                cost = OP_COST_T1_FARMLAND + OP_COST_T2_FARMLAND + OP_COST_T3_FARMLAND

            #TODO - Add some descriptive text here
            flavorText = ""

            ConstructOutpost(userStronghold, outpostType, tier, attackFief.op_farmlandNumBuilt, spotsAvailable, cost, flavorText)
            return "farmlands"

        elif outpostType == "Fishery":
            spotsAvailable = int(attackFief.adjacentWater) + int(attackFief.adjacentRivers) - int(attackFief.op_fisheryNumBuilt)
            tier = int(attackFief.op_fisheryTier)
            if int(tier) == 0:
                cost = OP_COST_T1_FISHERY
            elif int(tier) == 1:
                cost = OP_COST_T1_FISHERY + OP_COST_T2_FISHERY
            elif int(tier) == 2:
                cost = OP_COST_T1_FISHERY + OP_COST_T2_FISHERY + OP_COST_T3_FISHERY

            #TODO - Add some descriptive text here
            flavorText = ""

            ConstructOutpost(userStronghold, outpostType, tier, attackFief.op_fisheryNumBuilt, spotsAvailable, cost, flavorText)
            return "fisheries"

        elif outpostType == "Lumber Mill":
            spotsAvailable = int(attackFief.adjacentForests) - int(attackFief.op_lumberMillNumBuilt)
            tier = int(attackFief.op_lumberMillTier)
            if int(tier) == 0:
                cost = OP_COST_T1_LUMBERMILL
            elif int(tier) == 1:
                cost = OP_COST_T1_LUMBERMILL + OP_COST_T2_LUMBERMILL
            elif int(tier) == 2:
                cost = OP_COST_T1_LUMBERMILL + OP_COST_T2_LUMBERMILL + OP_COST_T3_LUMBERMILL

            #TODO - Add some descriptive text here
            flavorText = ""

            ConstructOutpost(userStronghold, outpostType, tier, attackFief.op_lumberMillNumBuilt, spotsAvailable, cost, flavorText)
            return "lumberMills"

        elif outpostType == "Mine":
            spotsAvailable = int(attackFief.adjacentMountains) - int(attackFief.op_mineNumBuilt)
            tier = int(attackFief.op_mineTier)
            if int(tier) == 0:
                cost = OP_COST_T1_MINE
            elif int(tier) == 1:
                cost = OP_COST_T1_MINE + OP_COST_T2_MINE
            elif int(tier) == 2:
                cost = OP_COST_T1_MINE + OP_COST_T2_MINE + OP_COST_T3_MINE

            #TODO - Add some descriptive text here
            flavorText = ""

            ConstructOutpost(userStronghold, outpostType, tier, attackFief.op_mineNumBuilt, spotsAvailable, cost, flavorText)
            return "mines"

        return "outposts"

    #==================================================================================================================================
    # upgradeOutposts - menu for upgrading existing outposts
    #==================================================================================================================================
    if screen == "upgradeOutposts":
        # UpgradeOutpost(userStronghold, outpostType, tier, numberBuilt, cost, flavorText):
        if outpostType == "Farmland":
            tier = int(attackFief.op_farmlandTier)
            if int(tier) == 0:
                cost = OP_COST_T1_FARMLAND * int(attackFief.op_farmlandNumBuilt)
            elif int(tier) == 1:
                cost = OP_COST_T2_FARMLAND * int(attackFief.op_farmlandNumBuilt)
            elif int(tier) == 2:
                cost = OP_COST_T3_FARMLAND * int(attackFief.op_farmlandNumBuilt)

            #TODO - Add some descriptive text here
            flavorText = ""

            UpgradeOutpost(userStronghold, outpostType, tier, attackFief.op_farmlandNumBuilt, cost, flavorText)
            return "farmlands"

        elif outpostType == "Fishery":
            tier = int(attackFief.op_fisheryTier)
            if int(tier) == 0:
                cost = OP_COST_T1_FISHERY * int(attackFief.op_fisheryNumBuilt)
            elif int(tier) == 1:
                cost = OP_COST_T2_FISHERY * int(attackFief.op_fisheryNumBuilt)
            elif int(tier) == 2:
                cost = OP_COST_T3_FISHERY * int(attackFief.op_fisheryNumBuilt)

            #TODO - Add some descriptive text here
            flavorText = ""

            UpgradeOutpost(userStronghold, outpostType, tier, attackFief.op_fisheryNumBuilt, cost, flavorText)
            return "fisheries"

        elif outpostType == "Lumber Mill":
            tier = int(attackFief.op_lumberMillTier)
            if int(tier) == 0:
                cost = OP_COST_T1_LUMBERMILL * int(attackFief.op_lumberMillNumBuilt)
            elif int(tier) == 1:
                cost = OP_COST_T2_LUMBERMILL * int(attackFief.op_lumberMillNumBuilt)
            elif int(tier) == 2:
                cost = OP_COST_T3_LUMBERMILL * int(attackFief.op_lumberMillNumBuilt)

            #TODO - Add some descriptive text here
            flavorText = ""

            UpgradeOutpost(userStronghold, outpostType, tier, attackFief.op_lumberMillNumBuilt, cost, flavorText)
            return "lumberMills"

        elif outpostType == "Mine":
            tier = int(attackFief.op_mineTier)
            if int(tier) == 0:
                cost = OP_COST_T1_MINE * int(attackFief.op_mineNumBuilt)
            elif int(tier) == 1:
                cost = OP_COST_T2_MINE * int(attackFief.op_mineNumBuilt)
            elif int(tier) == 2:
                cost = OP_COST_T3_MINE * int(attackFief.op_mineNumBuilt)

            #TODO - Add some descriptive text here
            flavorText = ""

            UpgradeOutpost(userStronghold, outpostType, tier, attackFief.op_mineNumBuilt, cost, flavorText)
            return "mines"

        return "outposts"

    #==================================================================================================================================
    # hireOutpostUnits - menu for hiring outpost units
    #==================================================================================================================================
    if screen == "hireOutpostUnits":
        # HireUnit(userStronghold, unitType, unitBaseCost, unitCostModifier, unitCap, unitsOwned, flavorText)
        if unitType == "Farmer":
            flavorText = "    "
            costModifier = 0
            unitCap = UCAP_FARMER * int(attackFief.op_farmlandNumBuilt)
            HireUnit(userStronghold, unitType, UCOST_FARMER, costModifier, unitCap, attackFief.op_farmlandPrimaryUnits, flavorText)
            return "farmlands"

        if unitType == "Vendor":
            flavorText = "    "
            costModifier = 0
            unitCap = UCAP_VENDOR * int(attackFief.op_farmlandNumBuilt)
            HireUnit(userStronghold, unitType, UCOST_VENDOR, costModifier, unitCap, attackFief.op_farmlandSecondaryUnits, flavorText)
            return "farmlands"

        if unitType == "Fisher":
            flavorText = "    "
            costModifier = 0
            unitCap = UCAP_FISHER * int(attackFief.op_fisheryNumBuilt)
            HireUnit(userStronghold, unitType, UCOST_FISHER, costModifier, unitCap, attackFief.op_fisheryPrimaryUnits, flavorText)
            return "fisheries"

        if unitType == "Scavenger":
            flavorText = "    "
            costModifier = 0
            unitCap = UCAP_SCAVENGER * int(attackFief.op_fisheryNumBuilt)
            HireUnit(userStronghold, unitType, UCOST_SCAVENGER, costModifier, unitCap, attackFief.op_fisherySecondaryUnits, flavorText)
            return "fisheries"

        if unitType == "Lumberjack":
            flavorText = "    "
            costModifier = 0
            unitCap = UCAP_LUMBERJACK * int(attackFief.op_lumberMillNumBuilt)
            HireUnit(userStronghold, unitType, UCOST_LUMBERJACK, costModifier, unitCap, attackFief.op_lumberMillPrimaryUnits, flavorText)
            return "lumberMills"

        if unitType == "Hunter":
            flavorText = "    "
            costModifier = 0
            unitCap = UCAP_HUNTER * int(attackFief.op_lumberMillNumBuilt)
            HireUnit(userStronghold, unitType, UCOST_HUNTER, costModifier, unitCap, attackFief.op_lumberMillSecondaryUnits, flavorText)
            return "lumberMills"

        if unitType == "Miner":
            flavorText = "    "
            costModifier = 0
            unitCap = UCAP_MINER * int(attackFief.op_mineNumBuilt)
            HireUnit(userStronghold, unitType, UCOST_MINER, costModifier, unitCap, attackFief.op_minePrimaryUnits, flavorText)
            return "mines"

        if unitType == "Prospector":
            flavorText = "    "
            costModifier = 0
            unitCap = UCAP_PROSPECTOR * int(attackFief.op_mineNumBuilt)
            HireUnit(userStronghold, unitType, UCOST_PROSPECTOR, costModifier, unitCap, attackFief.op_mineSecondaryUnits, flavorText)
            return "mines"

        return "outposts"

    return screen

