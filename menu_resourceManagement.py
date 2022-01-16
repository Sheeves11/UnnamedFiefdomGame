from globals import *

def ResourceManagementMenu(screen, userStronghold):
    if screen == "sendResourcesFromStronghold":
        os.system("clear")
        header(userStronghold.name)

        SendResources(userStronghold, userStronghold)   #Redundant...but necessary for now

        return "stronghold"
    if screen == "sendResourcesFromFief":
        os.system("clear")
        headerFief(attackFief)

        SendResources(attackFief, userStronghold)

        return "ownedFiefDetails"

    return screen