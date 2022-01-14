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
    print("")
def pas_forest_p3():
    print("")

# Secondary Passages:
def pas_forest_s1():
    print("Bushels of red berries decorate the skirts of the trees, beckoning the foolish and repelling the wise.")
def pas_forest_s2():
    print("")
def pas_forest_s3():
    print("")

# Tertiary Passages:
def pas_forest_t1():
    print("")
def pas_forest_t2():
    print("")
def pas_forest_t3():
    print("")

#------------------------------------------------------------------------------
# Mountains
#------------------------------------------------------------------------------
# Primary Passages:
def pas_mountain_p1():
    print("")
def pas_mountain_p2():
    print("")
def pas_mountain_p3():
    print("")

# Secondary Passages:
def pas_mountain_s1():
    print("")
def pas_mountain_s2():
    print("")
def pas_mountain_s3():
    print("")

# Tertiary Passages:
def pas_mountain_t1():
    print("")
def pas_mountain_t2():
    print("")
def pas_mountain_t3():
    print("")

#------------------------------------------------------------------------------
# Plains
#------------------------------------------------------------------------------
# Primary Passages:
def pas_plains_p1():
    print("")
def pas_plains_p2():
    print("")
def pas_plains_p3():
    print("")

# Secondary Passages:
def pas_plains_s1():
    print("")
def pas_plains_s2():
    print("")
def pas_plains_s3():
    print("")

# Tertiary Passages:
def pas_plains_t1():
    print("")
def pas_plains_t2():
    print("")
def pas_plains_t3():
    print("")


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
    print("")

def pas_c1_2():
    print("")

#   Encounter 2 - "Name it here"
def pas_c2_1():
    print("")
