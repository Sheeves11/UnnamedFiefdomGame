from globals import *



#======================================================================================
#   [Idea Board]
#
#       Expanding on combat features:
#           Elements of Engagement:
#               - Reaction-Time elements:
#                       Some story dialogue that sets up a sequence for the user to
#                       press a particular key.
#                       Time could be measured between the start of the event and the
#                       end of the event (when key is pressed).
#                       Depending on the value, the event could be lost, or the user
#                       could help bend the odds in their favor. 
#                       Key could be random. Time could be shortened based on number
#                       disadvantages. Etc.
#
#               - RPG elements:
#                       Deciding between retreating or attacking. 
#                       Giving an order to focus attacks on a certain area or group.
#                       Changing combat formations.
#                       These things could be further fleshed out with behind-
#                       the-scenes rolls that have weights depending on other elements
#                       (like number of warriors on each side, stamina values, etc.)
#
#               - Puzzles and Problems:
#                       This could potentially be cheesy or may not sit right with
#                       some users, but could implement puzzles or logic based 
#                       questions into the combat sequences. If done in a creative and
#                       relevant way, it could be a nice addition. 
#
#======================================================================================

#This document contains screens for:
#   thiefPage
#   battle

def CombatAndThieveryMenu(screen, userStronghold, attackStronghold):
#This is the theif attack page, which you will see when trying
#to steal gold from another player
#
#------------------------------------------------------------------------------
    if screen == "thiefPage":
        os.system("clear")
        header(userStronghold.name)

        #this is where the battle logic happens!
        print('    \n\n')
        print('    ' + attackStronghold.name + '\'s Stronghold has ' + attackStronghold.defenders + ' soldiers keeping a watchful eye. You have ' + str(userStronghold.thieves) + ' who are ready for a heist.')
        print('    Rumor has it that their coffers hold ' + str(attackStronghold.gold) + ' gold pieces.')
        print('    Your thieves work best in groups of 3 per 100 soldiers. Too few and they lack manpower. Too many and they draw unwanted attention.')
        print('    ')
        print('        ...\n')
        time.sleep(1)
        
        desiredAttackers = 0
        attackers = 0

        if int(userStronghold.thieves) > 0:
            try:
                desiredAttackers = int(input('    Enter the number of thieves you would like to send on this mission: '))
            except:
                print('\n\n    That is not a valid option, sorry!')
                Attackers = 0

            if int(desiredAttackers) <= int(userStronghold.thieves)  and int(desiredAttackers) > 0:
    #            print('desieredAttackers = ' + str(desiredAttackers))
                attackers = int(desiredAttackers)
            else:
                print('    invalid number')
                attackers = 0
        

            goldToSteal = attackStronghold.gold

    #        print('Thieves Attacking: ' + str(attackers))
    #        print('Defending Stronghold: ' + attackStronghold.name)
    #        print('Attacking Stronghold: ' + str(userStronghold.name))
    #        print('Potential Gold To Be Stolen: ' + str(attackStronghold.gold))
    #        print('Defenders: ' + str(attackStronghold.defenders))
    #        print('\n\nThief Logic Time: ')
            
            thiefs = float(attackers)
            defs = float(attackStronghold.defenders)
            potentialGold = float(attackStronghold.gold)
            maxCarriedGold = 0
            
            ratio = float(thiefs / defs)

            chance = float(4.4 + (ratio * 4180) + (-61607 * (ratio * ratio)))

            maxCarriedGold = thiefs * (potentialGold // 10)
            maxCarriedGold = maxCarriedGold * (1 + thiefs // 2)

            
    #        print('Percent Chance of Success: ' + str(chance))
    #        print('Max Stolen Gold = ' + str(maxCarriedGold))
            
            if int(maxCarriedGold) > int(attackStronghold.gold):
                maxCarriedGold = int(attackStronghold.gold)
            
            randomNum = roll(0) * 5
    #        print('\nRandom Roll is: ' + str(randomNum))

            if int(randomNum) > int(chance) and int(attackers) > 0:
                
                print('    Despite their valient efforts, your thieves have been captured.\n    This mission is a failure.')

                #log this event
                #for enemy
                logString = userStronghold.name + ' sent a gang of ' + str(int(thiefs)) + ' thieves to steal from you. They have been dealt with.'
                Log(logString, attackStronghold.ruler)

                #for current player
                logString = 'You sent thieves to ' + attackStronghold.ruler + '\'s Stronghold. They didn\'t come back.'
                Log(logString, userStronghold.ruler)
                
                userStronghold.thieves = int(userStronghold.thieves) - int(attackers)
                userStronghold.write()
                userStronghold.read()

                print('    You have ' + str(userStronghold.thieves) + ' thieves remaining.')

            elif int(randomNum) <= int(chance) and int(attackers) > 0:
                print('    Success! Your thieves return with pocketsfull of gold!\n    Your thieves managed to secure ' + str(int(maxCarriedGold)) + ' gold for the stronghold!')

                #log this event
                #for enemy
                logString = userStronghold.name + ' is rumored to have sent a gang of thieves to your stronghold.'
                Log(logString, attackStronghold.ruler)

                #for current player
                logString = 'You sent thieves to ' + attackStronghold.ruler + '\'s Stronghold. They secured ' + str(int(maxCarriedGold)) + ' gold.'
                Log(logString, userStronghold.ruler)
                
                userStronghold.gold = int(maxCarriedGold) + int(userStronghold.gold)
                userStronghold.write()
                userStronghold.read()

                attackStronghold.gold = int(attackStronghold.gold) - int(maxCarriedGold)
                attackStronghold.write()
                attackStronghold.read()

                print('    You now have ' + str(userStronghold.gold) + ' gold.')

            else:
                print('    Nothing Happened')
        
        else:
            print("    You don't have any thieves hired!")

        tempInput = input('    Press Enter To Continue ')
        return "enemyStrongholdDetails"


#The "battle" page simulates a battle between two Fiefdoms. This is currently the most
#complicated page and could use some cleaning up.
#
#To Do
# - add a better system for determining winners and casualties. The current system
#   is almost entirely random, which is bad.
# - make it prettier
#
#------------------------------------------------------------------------------
    if screen == "battle":
        os.system("clear")
        header(userStronghold.name)
        #headerFief(attackFief)

        #Idea: We're going to do a DnD style battle using D20s and modifiers.
        #roll(mod) is going to give the result of a roll plus modifiers and is
        #defined at the start of the file.

        #This if statement prevents players from attacking a player's home stronghold
        #Eventually this will be replaced with a formula that allows you to attack
        #for gold
        if attackFief.home == 'True':
            os.system('clear')
            print('    You are unable to claim a player\'s home stronghold')
            time.sleep(3)
            return 'stronghold'

        #this is where the battle logic happens!
        if attackFief.home == 'False':
            print('            \n')
            print('                    ------------------------------------------------------------------------------')
            print('                    ------------------------------------------------------------------------------')
            print('                    ------------------------------------------------------------------------------')

            print('''    
                    Your forces gather their strength, write their goodbyes in letters back home,
                    and eat what could be their very last meal.

                    At dawn, with the sun to your backs, you charge towards glory!'''
    )
            print('\n                    This battle is between ' + attackFief.name + ' and ' + userStronghold.name)
            print('\n                    Simulating Battle...')
            time.sleep(1.5)

            attackers = int(userStronghold.defenders)
            defenders = int(attackFief.defenders)

            defenseLosses = 0
            attackLosses = 0
            attackMod = int(userStronghold.attLevel)
            defenseMod = int(attackFief.defLevel)

            for i in range(3):

                for i in range(int(4)):
                    maxDeaths = attackers // 4

                    while (defenders > 1 and attackers > 1) and maxDeaths > 0 :
                        defense = roll(defenseMod)
                        attack = roll(attackMod)
                        maxDeaths = maxDeaths - 1
                        if attack > defense:
                            defenders = defenders - 1
                            defenseLosses = defenseLosses + 1
                        if attack <= defense:
                            attackers = attackers - 1
                            attackLosses = attackLosses + 1

            print('    \n')
            print('                    ------------------------------------------------------------------------------')
            print('                    -----------------------------Battle Results-----------------------------------')
            print('                    ------------------------------------------------------------------------------')
            print('    \n')
            print('                    ' + userStronghold.ruler + ' lost ' + str(attackLosses) + ' soldiers')
            print('                    ' + attackFief.ruler + ' lost ' + str(defenseLosses) + ' soldiers')
            print('    \n')
            print('                    ------------------------------------------------------------------------------')
            print('                    ------------------------------------------------------------------------------')
            print('    \n\n')

            #if the current player wins
            if attackers > defenders:
                #log this event
                #for enemy
                logString = userStronghold.name + ' attacked you at ' + attackFief.name + '. They won.'
                Log(logString, attackFief.ruler)

                #for current player
                logString = 'You attacked ' + attackFief.ruler + ' at ' + attackFief.name + '. You won.'
                Log(logString, userStronghold.ruler)




                pas_battle_won()
                print(textColor.WARNING + '                    You are the new ruler of ' + attackFief.name + '\n' + textColor.RESET)

                attackFief.defenders = defenders
                attackFief.ruler = userStronghold.ruler
                attackFief.write()

                userStronghold.defenders = attackers
                userStronghold.write()

                # userStronghold.gold = str(int(userStronghold.gold) + int(attackFief.gold))
                # print('    You now have a total of ' + str(userStronghold.gold) + ' gold!')
                # attackFief.gold = str('0')

                userStronghold.write()
                attackFief.write()
                nothing = input('\n                    Press Enter to Continue ')
                currentPage = 1
                return "ownedFiefDetails"

            #if the other player wins
            if attackers <= defenders:
                #log this event
                #for enemy
                logString = userStronghold.name + ' attacked you. They lost valiantly.'
                Log(logString, attackFief.ruler)

                #for current player
                logString = 'You attacked ' + attackFief.ruler + ' at ' + attackFief.name + '. They routed your army.'
                Log(logString, userStronghold.ruler)


                pas_battle_lost()
                print('                    Your forces, now many fewer in number, begin the long march home.\n')

                attackFief.defenders = defenders
                attackFief.write()

                userStronghold.defenders = attackers
                userStronghold.write()
                nothing = input('\n                    Press Enter to Continue ')
                currentPage = 1

                return "stronghold"
            

    return screen