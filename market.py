from colors import *
from classes import *
import random

#This file contains the Market and Good classes. 
#The Market class contains a list of Good classes. 
#The Market class can print all the goods it contains with the function "ListGoods"

#Some Common shelf lifes to use:

ONE_HOUR = 3600
TWO_HOURS = 7200
THREE_HOURS = 10800
SIX_HOURS = 21600
TWELVE_HOURS = 43200
ONE_DAY = 86400
TWO_DAYS = 172800
THREE_DAYS = 259200
INTERVAL = 3600

GOODS_AT_LAUNCH = 10
RESTOCK_THRESHOLD = 10
MERCHANT_TAX = 0.25

#Resource base prices in Gold:
FOOD_COST = 5
WOOD_COST = 10
STONE_COST = 10
ORE_COST = 25
#Resource weights
#Raise SELL weights to see the item for sale more often.
#Raise BUY weights to see the item as a price more often
SELL_GOLD_WEIGHT = 5
SELL_FOOD_WEIGHT = 3
SELL_WOOD_WEIGHT = 3
SELL_STONE_WEIGHT = 3
SELL_ORE_WEIGHT = 2

BUY_GOLD_WEIGHT = 6
BUY_FOOD_WEIGHT = 2
BUY_WOOD_WEIGHT = 2
BUY_STONE_WEIGHT = 2
BUY_ORE_WEIGHT = 1

#Multipliers for below:
GOLD_RESOURCE_MULT = 30
COMMON_RESOURCE_MULT = 10
RARE_RESOURCE_MULT = 5
MERCHANT_NEEDS_MOD = 5
#Minimum and maximum sale amounts for each resource.
#NOTE: Ore is multiplied by 5, others are multiplied by 10.
MIN_GOLD = 10
MAX_GOLD = 100
MIN_FOOD = 1
MAX_FOOD = 5
MIN_WOOD = 1
MAX_WOOD = 5
MIN_STONE = 1
MAX_STONE = 5
MIN_ORE = 1
MAX_ORE = 5

class Market:
    merchandise = []
    #==================================================================================
    #   [InitializeGoods]
    #   parameters: self
    #       Initializes the market with a set number of goods.
    #==================================================================================
    def InitializeGoods(self):
        for i in range(GOODS_AT_LAUNCH):
            self.GenerateGood()
        self.write()
        self.read()

    #==================================================================================
    #   [AddGood]
    #   parameters: self, seller, shelfLife, goodType, goodAmount, costType, costAmount
    #       Adds a new good to the Market's merchandise list
    #==================================================================================
    def AddGood(self, seller, shelfLife, goodType, goodAmount, costType, costAmount):
        newGood = Good(seller, shelfLife, goodType, goodAmount, costType, costAmount)
        self.merchandise.append(newGood)
    
    #==================================================================================
    #   [GetGoods]
    #   parameters: self
    #       Gets a neat list by using the Good classes "ListDetails" function for
    #       each good the Market contains.
    #==================================================================================
    def GetGoods(self):
        merch = []
        for i in range(len(self.merchandise)):
            merch.append(self.merchandise[i].ListDetails())
        return merch

    #==================================================================================
    #   [GetGood]
    #   parameters: self, number
    #       Returns a Good object at passed index
    #==================================================================================
    def GetGood(self, index):
        return self.merchandise[index]

    #==================================================================================
    #   [ListGoods]
    #   parameters: self
    #       Prints a neat list by using the Good classes "ListDetails" function for
    #       each good the Market contains.
    #==================================================================================
    def ListGoods(self):
        self.read()
        for i in range(len(self.merchandise)):
            print(str(self.merchandise[i].ListDetails()))

    #==================================================================================
    #   [RemoveGood]
    #   parameters: self, index
    #       Removes item at index from the merchandise list.
    #==================================================================================
    def RemoveGood(self, index):
        self.merchandise.pop(index)
        self.write()

    #==================================================================================
    #   [PurgeGoods]
    #   parameters: self
    #       Removes any goods with a shelfLife of 0
    #       If the goods were posted by a user, they are returned to that user.
    #==================================================================================
    def PurgeGoods(self):
        try:
            if len(self.merchandise) == 0:
                return
            for i in range(len(self.merchandise)):
                if int(self.merchandise[i].shelfLife) == 0:
                    if self.merchandise[i].seller == "The Wandering Merchant":
                        self.merchandise.pop(i)
                    else:
                        tempStronghold = Stronghold()
                        tempStronghold.name = str(self.merchandise[i].seller)
                        tempStronghold.read()
                        if self.merchandise[i].goodType == "Gold":
                            tempStronghold.gold = int(tempStronghold.gold) + int(self.merchandise[i].goodAmount)
                        elif self.merchandise[i].goodType == "Food":
                            tempStronghold.food = int(tempStronghold.food) + int(self.merchandise[i].goodAmount)
                        elif self.merchandise[i].goodType == "Wood":
                            tempStronghold.wood = int(tempStronghold.wood) + int(self.merchandise[i].goodAmount)
                        elif self.merchandise[i].goodType == "Stone":
                            tempStronghold.stone = int(tempStronghold.stone) + int(self.merchandise[i].goodAmount)
                        elif self.merchandise[i].goodType == "Ore":
                            tempStronghold.ore = int(tempStronghold.ore) + int(self.merchandise[i].goodAmount)
                        self.merchandise.pop(i)
                        tempStronghold.write()
                        tempStronghold.read()

            self.write()
            self.read()
        except:
            self.write()
            self.read()
            self.PurgeGoods()
            

    #==================================================================================
    #   [CheckRestock]
    #   parameters: self
    #       Generates goods equal to the restock_threshold if the number of goods
    #       is equal to or less than the restock_threshold
    #==================================================================================
    def CheckRestock(self):
        count = 0
        for i in range(len(self.merchandise)):
            if self.merchandise[i].seller == "The Wandering Merchant":
                count = int(count) + 1

        if int(count) <= RESTOCK_THRESHOLD:
            for i in range(RESTOCK_THRESHOLD):
                self.GenerateGood()
            self.write()
            self.read()

    #==================================================================================
    #   [NumListings]
    #   parameters: self, username
    #       Returns number of listings under the passed username
    #==================================================================================
    def NumListings(self, username):
        count = 0
        for i in range(len(self.merchandise)):
            if str(self.merchandise[i].seller) == str(username):
                count = int(count) + 1
        return count
            

    #==================================================================================
    #   [DecrementMerchandiseShelfLife]
    #   parameters: self, amount
    #       Decrements all goods shelfLife in merchandise list by passed amount
    #==================================================================================
    def DecrementMerchandiseShelfLife(self, amount):
        for i in range(len(self.merchandise)):
            self.merchandise[i].DecrementShelfLife(amount)
        self.PurgeGoods()
        self.write()

    #==================================================================================
    #   [CheckAbV]
    #   parameters: num
    #   returns: a number based on the passed number. Basically, this is an abs() 
    #   function that returns 1 if the result is ever 0.
    #==================================================================================
    def CheckAbV(self, num):
        result = abs(num)
        if result == 0:
            return 1
        else:
            return result

    #==================================================================================
    #   [GenerateGood]
    #   parameters: self
    #       Creates a random new good to go on the market
    #==================================================================================
    def GenerateGood(self):
        seller = "The Wandering Merchant"
        shelfLife = THREE_HOURS
        
        #Create a list of SELL GOOD/WEIGHT tuples:
        goodTypes = [("Gold", SELL_GOLD_WEIGHT), ("Food", SELL_FOOD_WEIGHT), ("Wood", SELL_WOOD_WEIGHT), ("Stone", SELL_STONE_WEIGHT), ("Ore", SELL_ORE_WEIGHT)]

        #Create a new table and expand it:
        goodTable = []
        for item, weight in goodTypes:
            goodTable.extend([item]*weight)
        
        #Pick a random good out of the expanded table:
        pickedGoodType = random.choice(goodTable)

        #Create a list of BUY GOOD/WEIGHT tuples, making sure goodType and costType are not the same:
        if pickedGoodType == "Gold":
            costTypes = [("Food", BUY_FOOD_WEIGHT), ("Wood", BUY_WOOD_WEIGHT), ("Stone", BUY_STONE_WEIGHT), ("Ore", BUY_ORE_WEIGHT)]
        elif pickedGoodType == "Food":
            costTypes = [("Gold", BUY_GOLD_WEIGHT), ("Wood", BUY_WOOD_WEIGHT), ("Stone", BUY_STONE_WEIGHT), ("Ore", BUY_ORE_WEIGHT)]
        elif pickedGoodType == "Wood":
            costTypes = [("Gold", BUY_GOLD_WEIGHT), ("Food", BUY_FOOD_WEIGHT), ("Stone", BUY_STONE_WEIGHT), ("Ore", BUY_ORE_WEIGHT)]
        elif pickedGoodType == "Stone":
            costTypes = [("Gold", BUY_GOLD_WEIGHT), ("Food", BUY_FOOD_WEIGHT), ("Wood", BUY_WOOD_WEIGHT), ("Ore", BUY_ORE_WEIGHT)]
        elif pickedGoodType == "Ore":
            costTypes = [("Gold", BUY_GOLD_WEIGHT), ("Food", BUY_FOOD_WEIGHT), ("Wood", BUY_WOOD_WEIGHT), ("Stone", BUY_STONE_WEIGHT)]

        if pickedGoodType == "Gold":
            pickedGoodAmount = random.randint(MIN_GOLD, MAX_GOLD) * COMMON_RESOURCE_MULT
        elif pickedGoodType == "Food":
            pickedGoodAmount = random.randint(MIN_FOOD, MAX_FOOD) * COMMON_RESOURCE_MULT
        elif pickedGoodType == "Wood":
            pickedGoodAmount = random.randint(MIN_WOOD, MAX_WOOD) * COMMON_RESOURCE_MULT
        elif pickedGoodType == "Stone":
            pickedGoodAmount = random.randint(MIN_STONE, MAX_STONE) * COMMON_RESOURCE_MULT
        elif pickedGoodType == "Ore":
            pickedGoodAmount = random.randint(MIN_ORE, MAX_ORE) * RARE_RESOURCE_MULT

        #Create a new table and expand it:
        costTable = []
        for item, weight in costTypes:
            costTable.extend([item]*weight)
        
        #Pick a random good out of the expanded table:
        pickedCostType = random.choice(costTable)

        #Each item should be converted into its COST global value in gold so it can be taxed properly.
        #Run it through the works for each specific scenario. 
        if pickedCostType == "Gold":
            if pickedGoodType == "Food":
                pickedCostAmount = int(pickedGoodAmount * FOOD_COST) + int(int(pickedGoodAmount * FOOD_COST) * MERCHANT_TAX)
            elif pickedGoodType == "Wood":
                pickedCostAmount = int(pickedGoodAmount * WOOD_COST) + int(int(pickedGoodAmount * WOOD_COST) * MERCHANT_TAX)
            elif pickedGoodType == "Stone":
                pickedCostAmount = int(pickedGoodAmount * STONE_COST) + int(int(pickedGoodAmount * STONE_COST) * MERCHANT_TAX)
            elif pickedGoodType == "Ore":
                pickedCostAmount = int(pickedGoodAmount * ORE_COST * 10) + int(int(pickedGoodAmount * ORE_COST * 10) * MERCHANT_TAX)
        elif pickedCostType == "Food":
            if pickedGoodType == "Gold":
                pickedCostAmount = int(pickedGoodAmount / FOOD_COST) + int(int(pickedGoodAmount / FOOD_COST) * MERCHANT_TAX)
            elif pickedGoodType == "Wood":
                pickedCostAmount = int(pickedGoodAmount / self.CheckAbV(int(FOOD_COST - WOOD_COST))) + int(int(pickedGoodAmount * self.CheckAbV(int(FOOD_COST - WOOD_COST))) * MERCHANT_TAX)
            elif pickedGoodType == "Stone":
                pickedCostAmount = int(pickedGoodAmount / self.CheckAbV(int(FOOD_COST - STONE_COST))) + int(int(pickedGoodAmount * self.CheckAbV(int(FOOD_COST - STONE_COST))) * MERCHANT_TAX)
            elif pickedGoodType == "Ore":
                pickedCostAmount = int(pickedGoodAmount / self.CheckAbV(int(FOOD_COST - ORE_COST))) + int(int(pickedGoodAmount * self.CheckAbV(int(FOOD_COST - ORE_COST))) * MERCHANT_TAX)
        elif pickedCostType == "Wood":
            if pickedGoodType == "Gold":
                pickedCostAmount = int(pickedGoodAmount / WOOD_COST) + int(int(pickedGoodAmount / WOOD_COST) * MERCHANT_TAX)
            elif pickedGoodType == "Food":
                pickedCostAmount = int(pickedGoodAmount / self.CheckAbV(int(WOOD_COST - FOOD_COST))) + int(int(pickedGoodAmount * self.CheckAbV(int(WOOD_COST - FOOD_COST))) * MERCHANT_TAX)
            elif pickedGoodType == "Stone":
                pickedCostAmount = int(pickedGoodAmount / self.CheckAbV(int(WOOD_COST - STONE_COST))) + int(int(pickedGoodAmount * self.CheckAbV(int(WOOD_COST - STONE_COST))) * MERCHANT_TAX)
            elif pickedGoodType == "Ore":
                pickedCostAmount = int(pickedGoodAmount / self.CheckAbV(int(WOOD_COST - ORE_COST))) + int(int(pickedGoodAmount * self.CheckAbV(int(WOOD_COST - ORE_COST))) * MERCHANT_TAX)
        elif pickedCostType == "Stone":
            if pickedGoodType == "Gold":
                pickedCostAmount = int(pickedGoodAmount / STONE_COST) + int(int(pickedGoodAmount / STONE_COST) * MERCHANT_TAX)
            elif pickedGoodType == "Food":
                pickedCostAmount = int(pickedGoodAmount / self.CheckAbV(int(STONE_COST - FOOD_COST))) + int(int(pickedGoodAmount * self.CheckAbV(int(STONE_COST - FOOD_COST))) * MERCHANT_TAX)
            elif pickedGoodType == "Wood":
                pickedCostAmount = int(pickedGoodAmount / self.CheckAbV(int(STONE_COST - WOOD_COST))) + int(int(pickedGoodAmount * self.CheckAbV(int(STONE_COST - WOOD_COST))) * MERCHANT_TAX)
            elif pickedGoodType == "Ore":
                pickedCostAmount = int(pickedGoodAmount / self.CheckAbV(int(STONE_COST - ORE_COST))) + int(int(pickedGoodAmount * self.CheckAbV(int(STONE_COST - ORE_COST))) * MERCHANT_TAX)
        elif pickedCostType == "Ore":
            if pickedGoodType == "Gold":
                pickedCostAmount = int(pickedGoodAmount / ORE_COST) + int(int(pickedGoodAmount / ORE_COST) * MERCHANT_TAX)
            elif pickedGoodType == "Food":
                pickedCostAmount = int(pickedGoodAmount / self.CheckAbV(int(ORE_COST - FOOD_COST))) + int(int(pickedGoodAmount / self.CheckAbV(int(ORE_COST - FOOD_COST))) * MERCHANT_TAX)
            elif pickedGoodType == "Wood":
                pickedCostAmount = int(pickedGoodAmount / self.CheckAbV(int(ORE_COST - WOOD_COST))) + int(int(pickedGoodAmount / self.CheckAbV(int(ORE_COST - WOOD_COST))) * MERCHANT_TAX)
            elif pickedGoodType == "Stone":
                pickedCostAmount = int(pickedGoodAmount / self.CheckAbV(int(ORE_COST - STONE_COST))) + int(int(pickedGoodAmount / self.CheckAbV(int(ORE_COST - STONE_COST))) * MERCHANT_TAX)
        
        #This is a bandaid to make selling goods more approachable:
        if pickedGoodType == "Gold":
            pickedGoodAmount = int(pickedGoodAmount * MERCHANT_NEEDS_MOD)
        
        if pickedCostType == "Gold":
            pickedCostAmount = int(pickedCostAmount * MERCHANT_NEEDS_MOD)

        if int(pickedCostAmount) == 0:
            pickedCostAmount = 1
        
        if int(pickedGoodAmount) == 0:
            pickedCostAmount = 1

        self.AddGood(seller, shelfLife, pickedGoodType, pickedGoodAmount, pickedCostType, pickedCostAmount)
        

    #==================================================================================
    #   [write]
    #==================================================================================
    def write(self):
        marketFile = 'market/serverMarket.txt'
        #If no file has been made yet:
        try:
            with open(marketFile, 'x') as f:
                f.write(str("["))
                for i in range(len(self.merchandise)):
                    f.write(str("["))
                    f.write("('" + str(self.merchandise[i].seller) + "'), ")
                    f.write("('" + str(self.merchandise[i].shelfLife) + "'), ")
                    f.write("('" + str(self.merchandise[i].goodType) + "'), ")
                    f.write("('" + str(self.merchandise[i].goodAmount) + "'), ")
                    f.write("('" + str(self.merchandise[i].costType) + "'), ")
                    f.write("('" + str(self.merchandise[i].costAmount) + "')")
                    if i < len(self.merchandise) - 1:
                        f.write(str("], "))
                    else:
                        f.write(str("]"))
                f.write(str("]"))
        except:
            pass
        #If file has already been made:
        try:
            with open(marketFile, 'w') as f:
                f.write(str("["))
                for i in range(len(self.merchandise)):
                    f.write(str("["))
                    f.write("('" + str(self.merchandise[i].seller) + "'), ")
                    f.write("('" + str(self.merchandise[i].shelfLife) + "'), ")
                    f.write("('" + str(self.merchandise[i].goodType) + "'), ")
                    f.write("('" + str(self.merchandise[i].goodAmount) + "'), ")
                    f.write("('" + str(self.merchandise[i].costType) + "'), ")
                    f.write("('" + str(self.merchandise[i].costAmount) + "')")
                    if i < len(self.merchandise) - 1:
                        f.write(str("], "))
                    else:
                        f.write(str("]"))
                f.write(str("]"))
        except:
            pass

    #==================================================================================
    #   [read]
    #==================================================================================
    def read(self):
        marketFile = 'market/serverMarket.txt'
        self.merchandise = []
        try:
            readMarketFile = open(marketFile, 'r')
            rL = eval(readMarketFile.read())
            readMarketFile.close()

            for i in range(len(rL)):
                self.AddGood(str(rL[i][0]), str(rL[i][1]), str(rL[i][2]), str(rL[i][3]), str(rL[i][4]), str(rL[i][5]))

        except:
            print('Could not read market file!')
            pass


class Good:
    def __init__(self, seller, shelfLife, goodType, goodAmount, costType, costAmount):
        self.seller = seller
        self.shelfLife = shelfLife
        self.goodType = goodType
        self.goodAmount = goodAmount
        self.costType = costType
        self.costAmount = costAmount

    #==================================================================================
    #   [DecrementShelfLife]
    #       Reduces shelfLife of the good by passed amount
    #==================================================================================
    def DecrementShelfLife(self, amount):
        self.shelfLife = int(self.shelfLife) - int(amount)
        if int(self.shelfLife) < 0:
            self.shelfLife = 0
    
    #==================================================================================
    #   [ListDetails]
    #       Neatly prints the Good classes contents. (make this return instead?)
    #==================================================================================
    def ListDetails(self):
        if self.seller == "The Wandering Merchant": #This is the default merchant name. It's a Drakkhen reference, but no one knows that game.
            sellerColor = TEAL
            seller = str(sellerColor + str(self.seller) + RESET).ljust(30, "-")
        else:
            sellerColor = MAGENTA
            seller = str(sellerColor + str(self.seller) + RESET).ljust(31, "-")

        if self.costType == "Gold":
            transaction = "sell"
            lead = str(CYAN + "[Selling]" + RESET).ljust(17, "-")
        elif self.goodType == "Gold":
            transaction = "buy"
            lead = str(GREEN + "[Buying] " + RESET).ljust(17, "-")
        else:
            transaction = "trade"
            lead = str(WARNING + "[Trading]" + RESET).ljust(17, "-")

        if int(self.shelfLife) <= ONE_HOUR:
            timeLeft = str(RED + " [1 Hour] " + RESET).ljust(17, "-")
        elif int(self.shelfLife) <= TWO_HOURS:
            timeLeft = str(ORANGE + " [2 Hours] " + RESET).ljust(17, "-")
        elif int(self.shelfLife) <= THREE_HOURS:
            timeLeft = str(WARNING + " [3 Hours] " + RESET).ljust(17, "-")
        elif int(self.shelfLife) <= SIX_HOURS:
            timeLeft = str(WARNING + " [6 Hours] " + RESET).ljust(17, "-")
        elif int(self.shelfLife) <= TWELVE_HOURS:
            timeLeft = str(GREEN + " [12 Hours] " + RESET).ljust(17, "-")
        elif int(self.shelfLife) <= ONE_DAY:
            timeLeft = str(GREEN + " [1 Day] " + RESET).ljust(17, "-")
        elif int(self.shelfLife) <= TWO_DAYS:
            timeLeft = str(CYAN + " [2 Days] " + RESET).ljust(17, "-")
        elif int(self.shelfLife) <= THREE_DAYS:
            timeLeft = str(CYAN + " [3 Days] " + RESET).ljust(17, "-")

        if transaction == "sell" or transaction == "trade":
            good = str(WARNING + " " + str(self.goodAmount) + " " + self.GetGoodColor() + str(self.goodType) + RESET).rjust(30, "-")
            cost = str(WARNING + " " + str(self.costAmount) + " " + self.GetCostColor() + str(self.costType) + RESET).ljust(30, "-")
            line = str(" " + seller + " " + lead + " " + good + " -[For]-" + cost + timeLeft)
        else:
            good = str(WARNING + " " + str(self.goodAmount) + " " + self.GetGoodColor() + str(self.goodType) + RESET).ljust(30, "-")
            cost = str(WARNING + " " + str(self.costAmount) + " " + self.GetCostColor() + str(self.costType) + RESET).rjust(30, "-")
            line = str(" " + seller + " " + lead + " " + cost + " -[For]-" + good + timeLeft)

        return line
        # print(line)

    #==================================================================================
    #   [GetGoodColor]
    #       Returns a color based on the goodType
    #==================================================================================
    def GetGoodColor(self):
        if self.goodType == "Gold":
            return C_GOLD
        if self.goodType == "Food":
            return C_FOOD
        if self.goodType == "Wood":
            return C_WOOD
        if self.goodType == "Stone":
            return C_STONE
        if self.goodType == "Ore":
            return C_ORE
        else:
            return RESET
    
    #==================================================================================
    #   [GetCostColor]
    #       Returns a color based on the costType
    #==================================================================================
    def GetCostColor(self):
        if self.costType == "Gold":
            return C_GOLD
        if self.costType == "Food":
            return C_FOOD
        if self.costType == "Wood":
            return C_WOOD
        if self.costType == "Stone":
            return C_STONE
        if self.costType == "Ore":
            return C_ORE
        else:
            return RESET

    


