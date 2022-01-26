import random
import time
from colors import *
# This is a file containing print functions for the games writing!

def AnswerYes(question):
    listening = True
    while listening:
        reply = input(question + " (y/n):")
        reply = reply.lower()
        if reply == 'y':
            listening = False
            return True
        elif reply == 'n':
            listening = False
            return False
        else:
            pass

def GetRandomChar():
    chars = 'abcdefghijklmnopqrstuvwxyz'
    return random.choice(chars)

def GetSmallRandomFloat():
    return round(random.uniform(0.30, 1.00), 2)

def GetMediumRandomFloat():
    return round(random.uniform(0.50, 2.00), 2)

def GetLargeRandomFloat():
    return round(random.uniform(0.60, 3.00), 2)

def ReactionTimeEvent():
    spacer = "    "
    randomChar = GetRandomChar()
    ready = str(CYAN + spacer + spacer + "Ready!")
    nock = str(spacer + spacer + GREEN + "Nock!")
    draw = str(spacer + spacer + spacer + spacer + WARNING + "Draw!")
    loose = str(spacer + spacer + spacer + spacer + spacer + ORANGE + "   LOOSE! " + RED + "  |" + RESET + randomChar + RED + "|" + RESET)
    orders = [ready, ".", ".", ".\n\n", nock, ".", ".", ".\n\n", draw, ".", ".", ".\n\n", loose]
    waitTime = 0.1
    incorrectInput = True
    dots = 0
    for i in range(len(orders)):
        
        if str(orders[i]) == "." or str(orders[i]) == ".\n\n":
            dots = int(dots) + 1
        if int(dots) == 3 and str(orders[i]) != nock:
            waitTime = GetSmallRandomFloat()
        elif int(dots) == 6 and str(orders[i]) != draw:
            waitTime = GetMediumRandomFloat()
        elif int(dots) == 9 and str(orders[i]) != loose:
            waitTime = GetLargeRandomFloat()
        else:
            waitTime = 0.1

        print(str(str(orders[i])).ljust(10, " "), sep='', end=' ', flush=True); time.sleep(waitTime)
    
    s = time.time()
    while incorrectInput:
        check = input(RED + " = " + RESET)
        if str(check) == str(randomChar):
            f = time.time()
            incorrectInput = False
        else:
            print(str(spacer + spacer + loose), sep='', end=' ', flush=True)

    totalTime = float(f) - float(s)
    speedColor = DARK_GRAY

    if totalTime < 0.4:
        speedColor = MAGENTA
    elif totalTime < 0.5:
        speedColor = CYAN
    elif totalTime < 0.7:
        speedColor = GREEN
    elif totalTime < 1:
        speedColor = WARNING
    elif totalTime < 1.5:
        speedColor = ORANGE
    else:
        speedColor = RED
    
    formattedTime = "{:.4f}".format(totalTime)

    print(speedColor + "\n    Response Time: " + str(formattedTime) + " seconds" + RESET)


def LoadingAnimation(biome):
    waitTime = 0.1
    C = BiomeColor(biome)
    for i in range(10):
        print(str(C + "." + RESET).ljust(10, " "), sep='', end=' ', flush=True); time.sleep(waitTime)

def ReactionTimeEvent2():
    spacer = "    "
    randomChar = GetRandomChar()
    ready = str(CYAN + spacer + spacer + "Ready!")
    nock = str(spacer + spacer + GREEN + "Nock!")
    draw = str(spacer + spacer + spacer + spacer + WARNING + "Draw!")
    loose = str(spacer + spacer + spacer + spacer + spacer + ORANGE + "   LOOSE! " + RED + "  |" + RESET + randomChar + RED + "|" + RESET)
    orders = [ready, ".", ".", ".\n\n", nock, ".", ".", ".\n\n", draw, ".", ".", ".\n\n", loose]
    waitTime = 0.1
    incorrectInput = True
    dots = 0
    for i in range(len(orders)):
        
        if str(orders[i]) == "." or str(orders[i]) == ".\n\n":
            dots = int(dots) + 1
        if int(dots) == 3 and str(orders[i]) != nock:
            waitTime = GetSmallRandomFloat()
        elif int(dots) == 6 and str(orders[i]) != draw:
            waitTime = GetMediumRandomFloat()
        elif int(dots) == 9 and str(orders[i]) != loose:
            waitTime = GetLargeRandomFloat()
        else:
            waitTime = 0.1

        print(str(str(orders[i])).ljust(10, " "), sep='', end=' ', flush=True); time.sleep(waitTime)
    
    s = time.time()
    while incorrectInput:
        check = input(RED + " = " + RESET)
        if str(check) == str(randomChar):
            f = time.time()
            incorrectInput = False
        else:
            print(str(spacer + spacer + loose), sep='', end=' ', flush=True)
    
    print(RESET + "\n    Total time taken: " + str(float(f) - float(s)))



#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#                              Biome Passages
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#   These passages have three parts to them because they will be mix-and-
#   matched with each other to form "unique" descriptions of a location.
#   Keep that in mind somewhat when writing the primary, secondary, and 
#   tertiary descriptions so that they flow and don't get too redundant with
#   one another. These shouldn't have any logic, just straightforward 
#   descriptive passages. They should be broken into sentences that could
#   flow together rather than be large paragraphs. Make more than just 3
#   each, by all means.
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Forests
#------------------------------------------------------------------------------
# Primary Passages:
def pas_forest_p1():
    print("Lively pines greet you with their fresh and soothing scent lingering in the air.")
def pas_forest_p2():
    print("Your boots crunch on the umber brown forest floor. As you look up, you realize that you can no longer see they sky.")
def pas_forest_p3():
    print("The ground grows soft as you march between the towering oaks.")

# Secondary Passages:
def pas_forest_s1():
    print("Bushels of red berries decorate the skirts of the trees, beckoning the foolish and repelling the wise.")
def pas_forest_s2():
    print("Mushrooms dot the forest floor, growing undisturbed beneath the ancient trees.")
def pas_forest_s3():
    print("In the distance, a wildcat howls.")

# Tertiary Passages:
def pas_forest_t1():
    print("A pair of jays screeches from high above.")
def pas_forest_t2():
    print("The woven web of leaves falls away to reveal a beautiful glade.")
def pas_forest_t3():
    print("You hear the metallic tinkling of a forest stream.")

#------------------------------------------------------------------------------
# Mountains
#------------------------------------------------------------------------------
# Primary Passages:
def pas_mountain_p1():
    print("The fang-white mountain looms over you.")
def pas_mountain_p2():
    print("The grizzled path is dotted by unmovable boulders. They look to have fallen from high above.")
def pas_mountain_p3():
    print("Scraggly pines stand strong in the face of an ancient wind")

# Secondary Passages:
def pas_mountain_s1():
    print("From this angle, these peaks look to be the tallest thing you've ever seen.")
def pas_mountain_s2():
    print("An eagle soars high above the mountain pass.")
def pas_mountain_s3():
    print("The rocks that surround you seem to have a story to tell. You stare at a rock. The rock stares back.")

# Tertiary Passages:
def pas_mountain_t1():
    print("In the distance you spot a mountain goat casually walking up the craggy slope.")
def pas_mountain_t2():
    print("You hear a wild screech echo through the valley.")
def pas_mountain_t3():
    print("The thin air has you feeling a little light-headed.")

#------------------------------------------------------------------------------
# Plains
#------------------------------------------------------------------------------
# Primary Passages:
def pas_plains_p1():
    print("A vast stretch of land lies before you, its fertile soil protected by billions of tiny blades")
def pas_plains_p2():
    print("The sky really does look bigger out here.")
def pas_plains_p3():
    print("It is said that the plains are known to drive men mad. Luckily you are already mad.")

# Secondary Passages:
def pas_plains_s1():
    print("The wind thunders across an endless sea of grass in waves.")
def pas_plains_s2():
    print("You spot the ruins of an old homestead. \"Who in their right mind would live out here,\" you wonder?")
def pas_plains_s3():
    print("There sure are a lot of ticks out here.")

# Tertiary Passages:
def pas_plains_t1():
    print("In the distance, you think you hear rolling thunder.")
def pas_plains_t2():
    print("In the distance, you see a lone tree standing strong against the wind. How did it get there?")
def pas_plains_t3():
    print("You've read about places like this. To be fair the book was also pretty borning.")


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#                              Encounter Passages
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#   These passages are for specific events or stories that take place during
#   travel. This is just a placeholder for their naming schema.
#------------------------------------------------------------------------------

#   Encounter 1 - "Name it here"
def pas_e1_1():
    print("")

def pas_e1_2():
    print("")

#... etc. These encounters may have logic or y/n questions added too. Like below:

def pas_e1_3():
    print("You come across a big sword in a rock.")
    #You can ask a yes or no question in a passage by typing it like this:
    if AnswerYes("Pull the sword out of the rock?"): 
        print("You pulled the sword out of the rock.")      #If user answers yes.
    else:
        print("You decided to leave the sword alone.")      #If user answers no.


#   Encounter 2 - "Name it here"
def pas_e2_1():
    print("")









#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#                              Combat Passages
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#   These passages are specifically for combat related encounters and may need
#   finer tuning than regular encounters. They're staged like the biomes as
#   well. 
#------------------------------------------------------------------------------

#   Encounter 1 - "Name it here"
def pas_c1_1():
    print("\n\n    Enemy troops are advancing! Prepare yourself to react in time!")

def pas_c1_2():
    response = input("\n    Hit { " + WARNING + "Enter" + RESET + " } to start, or type { " + CYAN + "help" + RESET + " } for more information first : ")
    if response == "help":
        print("\n    [" + CYAN + "Reaction Time Event" + RESET + "]: Upon hitting enter, a random character (or sequence of them)")
        print("    will appear on the screen. Type it/them and hit enter as quickly as possible for the best outcome!\n")
        nothing = input("    Press enter to start the encounter : ")

    print("\n")
    ReactionTimeEvent()


#   Encounter 2 - "Name it here"
def pas_c2_1():
    print("")









#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#                              Market Passages
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def pas_market_notEnoughFunds():
    rando = random.randint(1,20)
    if rando == 1:
        print(TEAL + "    *The goods are snatched from your hands as the merchant notices your lack of payment*\n" + RESET)
    if rando == 2:
        print(TEAL + "    *The merchant notices your lack of offerings and turns to help another customer*\n" + RESET)
    if rando == 3:
        print(TEAL + "    *The merchant sighs*\n" + RESET)
    if rando == 4:
        print(TEAL + "    *The merchant is sad*\n" + RESET)
    if rando == 5:
        print(TEAL + "    *The merchant hobbles about, tossing the goods you wanted around like they don't matter*\n    *They all land perfectly where you found them*" + RESET)
    if rando == 6:
        print(TEAL + "    *The merchant produces a small goat figurine from their goat pocket and eats it while making eye contact with you*\n" + RESET) #the second goat was a typo, but it made it better
    if rando == 7:
        print(TEAL + "    *The merchant disappears in twinkling light, along with all their goods*" + RESET)
    if rando == 8:
        print(TEAL + "    *You briefly forget about the merchant*" + RESET)
    if rando == 9:
        print(TEAL + "    *The merchant sets up a table and eats a meal before motioning you to go away*" + RESET)
    if rando == 10:
        print(TEAL + "    *The merchant takes a long sip of their tea*" + RESET)
    if rando == 11:
        print(TEAL + "    *The merchant slaps you, then cartwheels out of sight*" + RESET)
    if rando == 12:
        print(TEAL + "    *The merchant magically makes your empty pockets talk like sock puppets*" + RESET)
    if rando == 13:
        print(TEAL + "    *The merchant really wishes you had more resources*" + RESET)
    if rando == 14:
        print(TEAL + "    *The merchant whistles sharply and a taxi appears*" + RESET)
    if rando == 15:
        print(TEAL + "    *The merchant is better than you*" + RESET)
    if rando == 16:
        print(TEAL + "    *The merchant lies on the ground and rolls away*" + RESET)
    if rando == 17:
        print(TEAL + "    *The merchant stares at you blankly*" + RESET)
    if rando == 18:
        print(TEAL + "    *The merchant rolls their eyes*" + RESET)
    if rando == 19:
        print(TEAL + "    *The merchant wonders if they should just build their own stronghold*" + RESET)
    if rando == 20:
        print(TEAL + "    *The merchant is pretty annoyed*" + RESET)

def pas_market_transactionComplete():
    rando = random.randint(1,20)
    if rando == 1:
        print(TEAL + "    *The merchant smiles and shakes your hand*\n" + RESET)
    if rando == 2:
        print(TEAL + "    *The merchant accepts the transaction and starts to mumble on incoherently*\n" + RESET)
    if rando == 3:
        print(TEAL + "    *The merchant claps twice and your goods are neatly transferred to precisely where you wanted them (probably)*\n" + RESET)
    if rando == 4:
        print(TEAL + "    *The merchant nods accordingly*\n" + RESET)
    if rando == 5:
        print(TEAL + "    *The merchant dances as your transaction is completed*\n" + RESET)
    if rando == 6:
        print(TEAL + "    *The merchant knows who you are*\n" + RESET)
    if rando == 7:
        print(TEAL + "    *The merchant likes small cakes, but you didn't have any to give them*\n" + RESET)
    if rando == 8:
        print(TEAL + "    *The merchant is happy*\n" + RESET)
    if rando == 9:
        print(TEAL + "    *The merchant jumps a few feet into the air and a bunch of resources fall out of their coat*\n" + RESET)
    if rando == 10:
        print(TEAL + "    *The merchant gives you a high-five*\n" + RESET)
    if rando == 11:
        print(TEAL + "    *The merchant wants to join you on your journeys, but decides to just be a merchant instead*\n" + RESET)
    if rando == 12:
        print(TEAL + "    *The merchant instantly teleports your goods to your stronghold*\n" + RESET)
    if rando == 13:
        print(TEAL + "    *The merchant offers you some tea*\n" + RESET)
    if rando == 14:
        print(TEAL + "    *The merchant grunts in a bragging fashion*\n" + RESET)
    if rando == 15:
        print(TEAL + "    *The merchant salutes you and makes you pancakes*\n" + RESET)
    if rando == 16:
        print(TEAL + "    *The merchant takes your offering and builds a little stronghold for it*\n" + RESET)
    if rando == 17:
        print(TEAL + "    *With arms in the air, the merchant coughs loudly in acceptance*\n" + RESET)
    if rando == 18:
        print(TEAL + "    *The merchant gives you a thumbs up*\n" + RESET)
    if rando == 19:
        print(TEAL + "    *The merchant removes their cloak, revealing another merchant*\n" + RESET)
    if rando == 20:
        print(TEAL + "    *The merchant starts to juggle some stones dangerously*\n" + RESET)

def pas_market_greetings():
    rando = random.randint(1,20)
    if rando == 1:
        print(TEAL + "    *The merchant appears to be draped in green, obscuring their identity while somehow retaining an inviting atmosphere*\n" + RESET)
    if rando == 2:
        print(TEAL + "    *The merchant nearly gives you a heart attack as they appear at the mere thought of a possible transaction*\n" + RESET)
    if rando == 3:
        print(TEAL + "    *The merchant waves at you with a few hands*\n" + RESET)
    if rando == 4:
        print(TEAL + "    *The merchant crawls out of the ground and shakes your foot*\n" + RESET)
    if rando == 5:
        print(TEAL + "    *The merchant is talking to the clouds about breakfast*\n" + RESET)
    if rando == 6:
        print(TEAL + "    *The merchant is pretty normal today*\n" + RESET)
    if rando == 7:
        print(TEAL + "    *The merchant likes seeing you*\n" + RESET)
    if rando == 8:
        print(TEAL + "    *The merchant welcomes you into their tent to discuss your possible transaction*\n" + RESET)
    if rando == 9:
        print(TEAL + "    *The merchant is flapping wildly*\n" + RESET)
    if rando == 10:
        print(TEAL + "    *The merchant appears from a nearby tree*\n" + RESET)
    if rando == 11:
        print(TEAL + "    *The merchant knocks something over on their way to greet you*\n" + RESET)
    if rando == 12:
        print(TEAL + "    *The merchant is looking pretty kind today*\n" + RESET)
    if rando == 13:
        print(TEAL + "    *The merchant jumps a few feet into the air and a bunch of resources fall out of their coat*\n" + RESET)
    if rando == 14:
        print(TEAL + "    *You hear the merchant grumbling nearby*\n" + RESET)
    if rando == 15:
        print(TEAL + "    *You feel like you've been here before*\n" + RESET)
    if rando == 16:
        print(TEAL + "    *You feel tired, but then the merchant appears*\n" + RESET)
    if rando == 17:
        print(TEAL + "    *A deal is afoot*\n" + RESET)
    if rando == 18:
        print(TEAL + "    *The merchant flags you down when they notice you perusing*\n" + RESET)
    if rando == 19:
        print(TEAL + "    *The merchant is standing around in a cool way*\n" + RESET)
    if rando == 20:
        print(TEAL + "    *You see the merchant cupping something in their hands*\n" + RESET)

def pas_market_transactionCancelled():
    rando = random.randint(1,20)
    if rando == 1:
        print(TEAL + "    *The merchant smells you and spits on the ground*\n" + RESET)
    if rando == 2:
        print(TEAL + "    *The merchant consumes an entire watermelon, rind and all*\n" + RESET)
    if rando == 3:
        print(TEAL + "    *The merchant stomps around*\n" + RESET)
    if rando == 4:
        print(TEAL + "    *The merchant disappears*\n" + RESET)
    if rando == 5:
        print(TEAL + "    *The merchant climbs a tree*\n" + RESET)
    if rando == 6:
        print(TEAL + "    *The merchant quickly forgets you*\n" + RESET)
    if rando == 7:
        print(TEAL + "    *The merchant nods and waves*\n" + RESET)
    if rando == 8:
        print(TEAL + "    *The merchant was an illusion*\n" + RESET)
    if rando == 9:
        print(TEAL + "    *The merchant bites at a piece of wood while ignoring you*\n" + RESET)
    if rando == 10:
        print(TEAL + "    *The merchant shrugs and leaves*\n" + RESET)
    if rando == 11:
        print(TEAL + "    *The merchant shakes a nearby tree until stuff falls on your head*\n" + RESET)
    if rando == 12:
        print(TEAL + "    *The merchant looks at thier watch*\n" + RESET)
    if rando == 13:
        print(TEAL + "    *The merchant starts flipping a coin*\n" + RESET)
    if rando == 14:
        print(TEAL + "    *The merchant doesn't care*\n" + RESET)
    if rando == 15:
        print(TEAL + "    *The merchant starts reading a book*\n" + RESET)
    if rando == 16:
        print(TEAL + "    *The merchant has a bit of a moment*\n" + RESET)
    if rando == 17:
        print(TEAL + "    *The merchant stares at you*\n" + RESET)
    if rando == 18:
        print(TEAL + "    *The merchant gets mad but doesn't do anything*\n" + RESET)
    if rando == 19:
        print(TEAL + "    *The merchant hops away*\n" + RESET)
    if rando == 20:
        print(TEAL + "    *The merchant wants to know why*\n" + RESET)

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#                             Battle Passages
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def pas_battle_lost():
    rando = random.randint(1,10)
    if rando == 1:
        print(RED + "                    Although your warriors fought valiantly, their efforts were not enough.\n" + RESET)
    if rando == 2:
        print(RED + "                    Despite their best efforts, your army has been thoroughly decimated. \n                    The survivors look towards home in shame.\n" + RESET)
    if rando == 3:
        print(RED + "                    The enemy's superior forces quickly overpowered your warriors. What a shame.\n" + RESET)
    if rando == 4:
        print(RED + "                    The enemy made a mockery of your strategy and destroyed your forces. \n                    Have fun explaining this to all your citizens back home.\n" + RESET)
    if rando == 5:
        print(RED + "                    Against all odds, your army was swiftly crushed. Better luck next time." + RESET)
    if rando == 6:
        print(RED + "                    In this world there are winners and losers. Today you are a loser.\n" + RESET)
    if rando == 7:
        print(RED + "                    I've never seen a battle go this poorly. Good thing you don't have many \n                    survivors left to tell the tales of your incompetence." + RESET)
    if rando == 8:
        print(RED + "                    Your warriors, in all their might, were unable to overcome the enemy forces." + RESET)
    if rando == 9:
        print(RED + "                    The story of this battle will be told for years to come. Unfortunately they \n                    won't be told by your warriors. Because they died." + RESET)
    if rando == 10:
        print(RED + "                    You seem to have misjudged your enemies defenses. \n                    Your forces were quickly subjugated." + RESET)
    
def pas_battle_won():
    rando = random.randint(1,10)
    if rando == 1:
        print(TEAL + "                    As the dust settles, you appear victorious.\n" + RESET)
    if rando == 2:
        print(TEAL + "                    There is no glory in war, although as the winner of this battle, you feel pretty \n                    glorious right now." + RESET)
    if rando == 3:
        print(TEAL + "                    As the last blade falls, you gaze upon your new fiefdom. You will treat it well." + RESET)
    if rando == 4:
        print(TEAL + "                    Your forces are able to quickly overcome the enemy. You have won this fight." + RESET)
    if rando == 5:
        print(TEAL + "                    In this world there are winners and losers. On this day, you are a winner." + RESET)
    if rando == 6:
        print(TEAL + "                    You breathe a sign of relief. You have won this day." + RESET)
    if rando == 7:
        print(TEAL + "                    Unfortunately for your enemy, your warriors know what they're doing. \n                    You have won this battle." + RESET)
    if rando == 8:
        print(TEAL + "                    You feel the wind changing. This battle is yours." + RESET)
    if rando == 9:
        print(TEAL + "                    Your foe's reign of terror has come to an end. You have sent your enemy \n                    to the shadow realm." + RESET)
    if rando == 10:
        print(TEAL + "                    War is hell, but you will live to see another day. This battle is yours." + RESET)

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#                      Stronghold Passages (Forest)
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def pas_stronghold_forest():
    rando = random.randint(1,8)
    if rando == 1:
        print(GREEN + "Deep in the heart of the forest, your stronghold thrives." + RESET)
    if rando == 2:
        print(GREEN + "These trees are all you have ever known. You would give anything to protect them." + RESET)
    if rando == 3:
        print(GREEN + "It is peaceful here in the shade of the canopy that has protected your family for generations." + RESET)
    if rando == 4:
        print(GREEN + "The leaves are still. The forest listens." + RESET)
    if rando == 5:
        print(GREEN + "Few have dared to venture this far into the old forest. It is the only home you have known." + RESET)
    if rando == 6:
        print(GREEN + "A cool wind causes the treetops to sway as your people go about their lives." + RESET)
    if rando == 7:
        print(GREEN + "This forest has been here as long as time. You must protect it with all that you have." + RESET)
    if rando == 8:
        print(GREEN + "Green always was your favorite color, you say to yourself. The forest agrees." + RESET)

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#                      Stronghold Passages (Plains)
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def pas_stronghold_plains():
    rando = random.randint(1,8)
    if rando == 1:
        print(textColor.WARNING + "Your stronghold sits tall and proud over an endless sea of prarie grass." + RESET)
    if rando == 2:
        print(textColor.WARNING + "These walls have weathered many a storm. You must not let them fall." + RESET)
    if rando == 3:
        print(textColor.WARNING + "The sky really is bigger out here." + RESET)
    if rando == 4:
        print(textColor.WARNING + "People come from all around to see your great walls. They're all you have ever known." + RESET)
    if rando == 5:
        print(textColor.WARNING + "Your family has protected this prarie for hundreds of years." + RESET)
    if rando == 6:
        print(textColor.WARNING + "A cool wind causes the prarie grass to ripple as your people bustle about their chores." + RESET)
    if rando == 7:
        print(textColor.WARNING + "This prarie has seen more blood than you care to think about. Still, these walls stand tall." + RESET)
    if rando == 8:
        print(textColor.WARNING + "Life is tough on these plains. That never stopped you before." + RESET)

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#                      Stronghold Passages (Mountains)
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def pas_stronghold_mountains():
    rando = random.randint(1,8)
    if rando == 1:
        print(textColor.LIGHT_GRAY + "Nestled deep inside a mountain valley, your people thrive" + RESET)
    if rando == 2:
        print(textColor.LIGHT_GRAY + "The weather may be cold, but your hearts are warm." + RESET)
    if rando == 3:
        print(textColor.LIGHT_GRAY + "These icy peaks cast a long shadow over the only home you have ever known." + RESET)
    if rando == 4:
        print(textColor.LIGHT_GRAY + "Your stronghold appears to be carved out of the rock itself. You feel safe here." + RESET)
    if rando == 5:
        print(textColor.LIGHT_GRAY + "Your family has guarded these mountains for generations." + RESET)
    if rando == 6:
        print(textColor.LIGHT_GRAY + "Snow is the least of your worries out here. These mountains hide a dark secret." + RESET)
    if rando == 7:
        print(textColor.LIGHT_GRAY + "The mountain people are proud. This stronghold has never fallen." + RESET)
    if rando == 8:
        print(textColor.LIGHT_GRAY + "Few people venture this deep into the mountains. Those who do are greeted warmly." + RESET)

