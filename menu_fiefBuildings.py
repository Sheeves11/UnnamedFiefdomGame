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
    GrabGlobalColors()
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
            print("    {2}: Manage" + OP_COLOR_FARMLAND + " Farmlands " + RESET + "[" + WARNING + str(attackFief.adjacentPlains) + RESET + "]")
        if int(attackFief.adjacentWater) > 0 or int(attackFief.adjacentRivers) > 0:
            print("    {3}: Manage" + OP_COLOR_FISHERY + " Fisheries " + RESET + "[" + WARNING + str(int(attackFief.adjacentWater) + int(attackFief.adjacentRivers)) + RESET + "]")
        if int(attackFief.adjacentForests) > 0:
            print("    {4}: Manage" + OP_COLOR_LUMBERMILL + " Lumber Mills " + RESET + "[" + WARNING + str(attackFief.adjacentForests) + RESET + "]")
        if int(attackFief.adjacentMountains) > 0:
            print("    {5}: Manage" + OP_COLOR_MINE + " Mines " + RESET + "[" + WARNING + str(attackFief.adjacentMountains) + RESET + "]")
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
            print("    You currently have " + WARNING + str(attackFief.op_farmlandNumBuilt) + OP_COLOR_FARMLAND + " Farmlands" + RESET + " built.\n")
            
            if int(attackFief.op_farmlandPrimaryUnits) > 0:
                print("    You have " + WARNING + str(attackFief.op_farmlandPrimaryUnits) + COLOR_FARMER + " Farmers" + RESET + " growing food at a")
                print("    rate of " + CYAN + str(attackFief.op_farmlandPrimaryPer) + RESET + " per hour.\n")
            else:
                print("    You have not hired any" + COLOR_FARMER + " Farmers" + RESET + " yet.\n")

            if int(attackFief.op_farmlandTier) > 0:
                if int(attackFief.op_farmlandSecondaryUnits) > 0:
                    print("    You have " + WARNING + str(attackFief.op_farmlandSecondaryUnits) + COLOR_VENDOR + " Vendors" + RESET + " doing whatever they do")
                    print("    at a rate of " + CYAN + str(attackFief.op_farmlandSecondaryPer) + RESET + " per hour.\n")
                else:
                    print("    You have not hired any" + COLOR_VENDOR + " Vendors" + RESET + " yet.\n")

        else:
            print("    You haven't constructed any" + OP_COLOR_FARMLAND + " Farmlands" + RESET + " yet.\n")

        print("\n    Avalible Commands:")
        print('    -------------------------------------')
        print('    {1}: Go Back')
        if int(attackFief.op_farmlandPrimaryUnits) < (int(UCAP_FARMER) * int(attackFief.op_farmlandNumBuilt)):
            print('    {2}: Hire' + COLOR_FARMER + ' Farmers' + RESET)
        if (int(attackFief.op_farmlandSecondaryUnits) < (int(UCAP_VENDOR) * int(attackFief.op_farmlandNumBuilt)) and int(attackFief.op_farmlandTier) > 0):
            print('    {3}: Hire' + COLOR_VENDOR + ' Vendors' + RESET)
        if int(attackFief.op_farmlandNumBuilt) > 0 and int(attackFief.op_farmlandTier) < 2:
            print('    {4}: Upgrade' + OP_COLOR_FARMLAND + ' Farmlands' + RESET)
        if int(attackFief.op_farmlandNumBuilt) < int(attackFief.adjacentPlains):
            print('    {5}: Construct New' + OP_COLOR_FARMLAND + ' Farmland' + RESET)
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
            print("    You currently have " + WARNING + str(attackFief.op_fisheryNumBuilt) + OP_COLOR_FISHERY + " Fisheries" + RESET + " built.\n")
            
            if int(attackFief.op_fisheryPrimaryUnits) > 0:
                print("    You have " + WARNING + str(attackFief.op_fisheryPrimaryUnits) + COLOR_FISHER + " Fishers" + RESET + " catching food at a")
                print("    rate of " + CYAN + str(attackFief.op_fisheryPrimaryPer) + RESET + " per hour.\n")
            else:
                print("    You have not hired any" + COLOR_FISHER + " Fishers" + RESET + " yet.\n")

            if int(attackFief.op_fisheryTier) > 0:
                if int(attackFief.op_fisherySecondaryUnits) > 0:
                    print("    You have " + WARNING + str(attackFief.op_fisherySecondaryUnits) + COLOR_SCAVENGER + " Scavengers" + RESET + " gathering random materials")
                    print("    at a rate of " + CYAN + str(attackFief.op_fisherySecondaryPer) + RESET + " per hour.\n")
                else:
                    print("    You have not hired any" + COLOR_SCAVENGER + " Scavengers" + RESET + " yet.\n")

        else:
            print("    You haven't constructed any" + OP_COLOR_FISHERY + " Fisheries" + RESET + " yet.\n")
    
        print("\n    Avalible Commands:")
        print('    -------------------------------------')
        print('    {1}: Go Back')
        if int(attackFief.op_fisheryPrimaryUnits) < (int(UCAP_FISHER) * int(attackFief.op_fisheryNumBuilt)):
            print('    {2}: Hire' + COLOR_FISHER + ' Fishers' + RESET)
        if (int(attackFief.op_fisherySecondaryUnits) < (int(UCAP_SCAVENGER) * int(attackFief.op_fisheryNumBuilt)) and int(attackFief.op_fisheryTier) > 0):
            print('    {3}: Hire' + COLOR_SCAVENGER + ' Scavengers' + RESET)
        if int(attackFief.op_fisheryNumBuilt) > 0 and int(attackFief.op_fisheryTier) < 2:
            print('    {4}: Upgrade' + OP_COLOR_FISHERY + ' Fisheries' + RESET)
        if int(attackFief.op_fisheryNumBuilt) < int(attackFief.adjacentWater) + int(attackFief.adjacentRivers):
            print('    {5}: Construct New' + OP_COLOR_FISHERY + ' Fishery' + RESET)
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
            print("    You currently have " + WARNING + str(attackFief.op_lumberMillNumBuilt) + OP_COLOR_LUMBERMILL + " Lumber Mills" + RESET + " built.\n")
            if int(attackFief.op_lumberMillPrimaryUnits) > 0:
                    print("    You have " + WARNING + str(attackFief.op_lumberMillPrimaryUnits) + COLOR_LUMBERJACK + " Lumberjacks" + RESET + " gathering wood at a")
                    print("    rate of " + CYAN + str(attackFief.op_lumberMillPrimaryPer) + RESET + " per hour.\n")
            else:
                print("    You have not hired any" + COLOR_LUMBERJACK + " Lumberjacks" + RESET + " yet.\n")

            if int(attackFief.op_lumberMillTier) > 0:
                if int(attackFief.op_lumberMillSecondaryUnits) > 0:
                    print("    You have " + WARNING + str(attackFief.op_lumberMillSecondaryUnits) + COLOR_HUNTER + " Hunters" + RESET + " hunting for food")
                    print("    at a rate of " + CYAN + str(attackFief.op_lumberMillSecondaryPer) + RESET + " per hour.\n")
                else:
                    print("    You have not hired any" + COLOR_HUNTER + " Hunters" + RESET + " yet.\n")

        else:
            print("    You haven't constructed any" + OP_COLOR_LUMBERMILL + " Lumber Mills" + RESET + " yet.\n")

        

        print("\n    Avalible Commands:")
        print('    -------------------------------------')
        print('    {1}: Go Back')
        if int(attackFief.op_lumberMillPrimaryUnits) < (int(UCAP_LUMBERJACK) * int(attackFief.op_lumberMillNumBuilt)):
            print('    {2}: Hire' + COLOR_LUMBERJACK + ' Lumberjacks' + RESET)
        if (int(attackFief.op_lumberMillSecondaryUnits) < (int(UCAP_HUNTER) * int(attackFief.op_lumberMillNumBuilt)) and int(attackFief.op_lumberMillTier) > 0):
            print('    {3}: Hire' + COLOR_HUNTER + ' Hunters' + RESET)
        if int(attackFief.op_lumberMillNumBuilt) > 0 and int(attackFief.op_lumberMillTier) < 2:
            print('    {4}: Upgrade' + OP_COLOR_LUMBERMILL + ' Lumber Mills' + RESET)
        if int(attackFief.op_lumberMillNumBuilt) < int(attackFief.adjacentForests):
            print('    {5}: Construct New' + OP_COLOR_LUMBERMILL + ' Lumber Mill' + RESET)
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
            print("    You currently have " + WARNING + str(attackFief.op_mineNumBuilt) + OP_COLOR_MINE + " Mines" + RESET + " built.\n")
            if int(attackFief.op_minePrimaryUnits) > 0:
                print("    You have " + WARNING + str(attackFief.op_minePrimaryUnits) + COLOR_MINER + " Miners" + RESET + " gathering stone at a")
                print("    rate of " + CYAN + str(attackFief.op_minePrimaryPer) + RESET + " per hour.\n")
            else:
                
                print("    You have not hired any" + COLOR_MINER + " Miners" + RESET + " yet.\n")

            if int(attackFief.op_mineTier) > 0:
                if int(attackFief.op_mineSecondaryUnits) > 0:
                    print("    You have " + WARNING + str(attackFief.op_mineSecondaryUnits) + COLOR_PROSPECTOR + " Prospectors" + RESET + " gathering iron")
                    print("    at a rate of " + CYAN + str(attackFief.op_mineSecondaryPer) + RESET + " per hour.\n")
                else:
                    print("    You have not hired any" + COLOR_PROSPECTOR + " Prospectors" + RESET + " yet.\n")
        else:
            print("    You haven't constructed any" + OP_COLOR_MINE + " Mines" + RESET + " yet.\n")

        print("\n    Avalible Commands:")
        print('    -------------------------------------')
        print('    {1}: Go Back')
        if int(attackFief.op_minePrimaryUnits) < (int(UCAP_MINER) * int(attackFief.op_mineNumBuilt)):
            print('    {2}: Hire' + COLOR_MINER + ' Miners' + RESET)
        if (int(attackFief.op_mineSecondaryUnits) < (int(UCAP_PROSPECTOR) * int(attackFief.op_mineNumBuilt)) and int(attackFief.op_mineTier) > 0):
            print('    {3}: Hire' + COLOR_PROSPECTOR + ' Prospectors' + RESET)
        if int(attackFief.op_mineNumBuilt) > 0 and int(attackFief.op_mineTier) < 2:
            print('    {4}: Upgrade' + OP_COLOR_MINE + ' Mines' + RESET)
        if int(attackFief.op_mineNumBuilt) < int(attackFief.adjacentMountains):
            print('    {5}: Construct New' + OP_COLOR_MINE + ' Mine' + RESET)
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
        # ConstructOutpost(userStronghold, outpostType, tier, numberBuilt, spotsAvailable, cost, color, flavorText)
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

            ConstructOutpost(userStronghold, outpostType, tier, attackFief.op_farmlandNumBuilt, spotsAvailable, cost, OP_COLOR_FARMLAND, flavorText)
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

            ConstructOutpost(userStronghold, outpostType, tier, attackFief.op_fisheryNumBuilt, spotsAvailable, cost, OP_COLOR_FISHERY, flavorText)
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

            ConstructOutpost(userStronghold, outpostType, tier, attackFief.op_lumberMillNumBuilt, spotsAvailable, cost, OP_COLOR_LUMBERMILL, flavorText)
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

            ConstructOutpost(userStronghold, outpostType, tier, attackFief.op_mineNumBuilt, spotsAvailable, cost, OP_COLOR_MINE, flavorText)
            return "mines"

        return "outposts"

    #==================================================================================================================================
    # upgradeOutposts - menu for upgrading existing outposts
    #==================================================================================================================================
    if screen == "upgradeOutposts":
        # UpgradeOutpost(userStronghold, outpostType, tier, numberBuilt, cost, color, flavorText):
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

            UpgradeOutpost(userStronghold, outpostType, tier, attackFief.op_farmlandNumBuilt, cost, OP_COLOR_FARMLAND, flavorText)
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

            UpgradeOutpost(userStronghold, outpostType, tier, attackFief.op_fisheryNumBuilt, cost, OP_COLOR_FISHERY, flavorText)
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

            UpgradeOutpost(userStronghold, outpostType, tier, attackFief.op_lumberMillNumBuilt, cost, OP_COLOR_LUMBERMILL, flavorText)
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

            UpgradeOutpost(userStronghold, outpostType, tier, attackFief.op_mineNumBuilt, cost, OP_COLOR_MINE, flavorText)
            return "mines"

        return "outposts"

    #==================================================================================================================================
    # hireOutpostUnits - menu for hiring outpost units
    #==================================================================================================================================
    if screen == "hireOutpostUnits":
        # HireUnit(userStronghold, unitType, unitBaseCost, unitCostModifier, unitCap, unitsOwned, color, flavorText)
        if unitType == "Farmer":
            flavorText = "    "
            costModifier = 0
            unitCap = UCAP_FARMER * int(attackFief.op_farmlandNumBuilt)

            HireUnit(userStronghold, unitType, UCOST_FARMER, costModifier, unitCap, attackFief.op_farmlandPrimaryUnits, COLOR_FARMER, flavorText)
            return "farmlands"

        if unitType == "Vendor":
            flavorText = "    "
            costModifier = 0
            unitCap = UCAP_VENDOR * int(attackFief.op_farmlandNumBuilt)

            HireUnit(userStronghold, unitType, UCOST_VENDOR, costModifier, unitCap, attackFief.op_farmlandSecondaryUnits, COLOR_VENDOR, flavorText)
            return "farmlands"

        if unitType == "Fisher":
            flavorText = "    "
            costModifier = 0
            unitCap = UCAP_FISHER * int(attackFief.op_fisheryNumBuilt)

            HireUnit(userStronghold, unitType, UCOST_FISHER, costModifier, unitCap, attackFief.op_fisheryPrimaryUnits, COLOR_FISHER, flavorText)
            return "fisheries"

        if unitType == "Scavenger":
            flavorText = "    "
            costModifier = 0
            unitCap = UCAP_SCAVENGER * int(attackFief.op_fisheryNumBuilt)

            HireUnit(userStronghold, unitType, UCOST_SCAVENGER, costModifier, unitCap, attackFief.op_fisherySecondaryUnits, COLOR_SCAVENGER, flavorText)
            return "fisheries"

        if unitType == "Lumberjack":
            flavorText = "    "
            costModifier = 0
            unitCap = UCAP_LUMBERJACK * int(attackFief.op_lumberMillNumBuilt)

            HireUnit(userStronghold, unitType, UCOST_LUMBERJACK, costModifier, unitCap, attackFief.op_lumberMillPrimaryUnits, COLOR_LUMBERJACK, flavorText)
            return "lumberMills"

        if unitType == "Hunter":
            flavorText = "    "
            costModifier = 0
            unitCap = UCAP_HUNTER * int(attackFief.op_lumberMillNumBuilt)

            HireUnit(userStronghold, unitType, UCOST_HUNTER, costModifier, unitCap, attackFief.op_lumberMillSecondaryUnits, COLOR_HUNTER, flavorText)
            return "lumberMills"

        if unitType == "Miner":
            flavorText = "    "
            costModifier = 0
            unitCap = UCAP_MINER * int(attackFief.op_mineNumBuilt)

            HireUnit(userStronghold, unitType, UCOST_MINER, costModifier, unitCap, attackFief.op_minePrimaryUnits, COLOR_MINER, flavorText)
            return "mines"

        if unitType == "Prospector":
            flavorText = "    "
            costModifier = 0
            unitCap = UCAP_PROSPECTOR * int(attackFief.op_mineNumBuilt)

            HireUnit(userStronghold, unitType, UCOST_PROSPECTOR, costModifier, unitCap, attackFief.op_mineSecondaryUnits, COLOR_PROSPECTOR, flavorText)
            return "mines"

        return "outposts"

    return screen

