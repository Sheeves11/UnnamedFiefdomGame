from globals import *

class Market:
    merchandise = []

    def AddGood(self, seller, shelfLife, goodType, goodAmount, costType, costAmount):
        newGood = Good(seller, shelfLife, goodType, goodAmount, costType, costAmount)
        self.merchandise.append(newGood)
    
    def ListGoods(self):
        for i in range(len(self.merchandise)):
            self.merchandise[i].ListDetails()

    def write(self):
        marketFile = 'market/' + self.name + '.txt'
        
        #this part creates a file if it isn't made yet.
        try:
            with open(marketFile, 'x') as f:
                f.write(str("["))
                for i in range(len(self.merchandise)):
                    f.write(str("["))
                    for j in range(len(self.merchandise[i])):
                        if j < len(self.merchandise[i]) - 1:
                            f.write("'" + str(self.merchandise[i][j]) + "',")
                        else:
                            f.write("'" + str(self.merchandise[i][j]) + "'")
                    if i < len(self.merchandise) - 1:
                        f.write(str("],"))
                    else:
                        f.write(str("]"))
                f.write(str("]"))
        except:
            pass

        #write the class variables down line by line in the text file
        try:
            with open(marketFile, 'w') as f:
                f.write(str("["))
                for i in range(len(self.merchandise)):
                    f.write(str("["))
                    for j in range(len(self.merchandise[i])):
                        if j < len(self.merchandise[i]) - 1:
                            f.write("'" + str(self.merchandise[i][j]) + "',")
                        else:
                            f.write("'" + str(self.merchandise[i][j]) + "'")
                    if i < len(self.merchandise) - 1:
                        f.write(str("],"))
                    else:
                        f.write(str("]"))
                f.write(str("]"))
        except:
            pass

    #--------------------------------------------------------------------------------------------------------------
    #   Opens the market file and reads each good from the list into a new good class, then appends that class
    #   to the merchandise list.
    #--------------------------------------------------------------------------------------------------------------
    def read(self):
        marketFile = 'market/' + self.name + '.txt'
        try:
            readMarketFile = open(marketFile, 'r')
            readList = eval(readMarketFile.read())
            readMarketFile.close()
            self.merchandise = []
            for count in range(len(readList)):
                self.AddGood(readList[count][0], readList[count][1], readList[count][2], readList[count][3], readList[count][4], readList[count][5])

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
    def ListDetails(self):
        if self.seller == "Wandering Merchant": #This is the default merchant name. It's a Drakkhen reference, but no one knows that game.
            print("Seller: " + WARNING + str(self.seller) + RESET + " Trading: " + WARNING + str(self.goodAmount) + " " + self.GetGoodColor() + str(self.goodType) + RESET + " for " + WARNING + str(self.costAmount) + " " + self.GetCostColor() + str(self.costType))

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



