from globals import *

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
                
                userStronghold.thieves = int(userStronghold.thieves) - int(attackers)
                userStronghold.write()
                userStronghold.read()

                print('    You have ' + str(userStronghold.thieves) + ' thieves remaining.')

            elif int(randomNum) <= int(chance) and int(attackers) > 0:
                print('    Success! Your thieves return with pocketsfull of gold!\n    Your thieves managed to secure ' + str(maxCarriedGold) + ' gold for the stronghold!')
                
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

        tempInput = input('    Press Enter To Continue')
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
        # header(userStronghold.name)
        headerFief(attackFief)

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
            print('\n\n    This battle is between ' + attackFief.name + ' and ' + userStronghold.name)
            print('\n\n    Simulating Battle...')
            time.sleep(1)
            print('\n        ...\n')
            time.sleep(1)

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
            print('    ------------------------------------------------------------------------------')
            print('    -----------------------------Battle Results-----------------------------------')
            print('    ------------------------------------------------------------------------------')
            print('    \n')
            print('    ' + userStronghold.ruler + ' lost ' + str(attackLosses) + ' soldiers')
            print('    ' + attackFief.ruler + ' lost ' + str(defenseLosses) + ' soldiers')
            print('    \n')
            print('    ------------------------------------------------------------------------------')
            print('    ------------------------------------------------------------------------------')
            print('    \n\n')

            #if the current player wins
            if attackers > defenders:
                print('    After a hard fought battle, your weary forces remain standing')
                print('    You are the new ruler of ' + attackFief.name)

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

            #if the other player wins
            if attackers <= defenders:
                print('    Although your soldiers fought valiantly, they were unable to overcome ' + attackFief.ruler + '\'s forces')
                print('    Your forces, now many fewer in number, begin the long march home.')

                attackFief.defenders = defenders
                attackFief.write()

                userStronghold.defenders = attackers
                userStronghold.write()


            time.sleep(1)
            nothing = input('    Press Enter to Continue')
            currentPage = 1
            return "fiefdoms"

    return screen