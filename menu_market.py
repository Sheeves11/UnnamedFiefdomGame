from globals import *
from market import *

def MarketMenu(screen, userStronghold):
    global currentPage
    if screen == "market":
        os.system("clear")
        header(userStronghold.name)

        marketCount = 0
        marketMargin = 0
        goodCount = 0

        goods = serverMarket.GetGoods()

        totalMarketCount = len(goods)
        
        for i in range(totalMarketCount):
            marketCount = marketCount + 1
            marketMargin = marketCount - ((currentPage - 1) * LINES_PER_PAGE)
            if (marketMargin <= LINES_PER_PAGE) and (marketMargin > 0):
                goodCount = goodCount + 1
                leftNumber = str(CYAN + "    {" + str(goodCount) + "}" + RESET).rjust(17, " ")
                print(str(leftNumber) + " " + str(goods[i]))

        if marketMargin > LINES_PER_PAGE or currentPage > 1:
            print('\n    /// ' + WARNING + 'Page ' + str(currentPage) + RESET + ' ///')
        print("\n    Avalible Commands:")
        print('    ------------------------------------------------------')
        print('    {R}: Return to Stronghold')
        print('    {S}: Sell Resources')
        print('    {B}: Buy Resources')
        print('    {T}: Trade Resources')
        if marketMargin > LINES_PER_PAGE:
                print('    {E}: Next Page')
        if currentPage > 1:
                print('    {Q}: Previous Page')
        print('    {Enter a number above to accept the offer}: ')
        print('    ------------------------------------------------------')
        print('')
        command = input("    Enter your command: ")

        command = str(command.lower())

        if marketMargin > LINES_PER_PAGE and str(command) == 'e':
            screen = "market"
            currentPage = currentPage + 1
        elif currentPage > 1 and str(command) == 'q':
            screen = "market"
            currentPage = currentPage - 1
        elif str(command) == 'r':
            screen = "stronghold"
        elif str(command) == 's':
            screen = "market"
        elif str(command) == 'b':
            screen = "market"
        elif str(command) == 't':
            screen = "market"
        elif IsPositiveIntEqualOrLessThan(command, LINES_PER_PAGE):
            if IsPositiveIntEqualOrLessThan((int(command) + int(int(LINES_PER_PAGE) * int(int(currentPage) - 1))), totalMarketCount):
                numToPop = int(command) + int(int(LINES_PER_PAGE) * int(int(currentPage) - 1)) - 1 #Subtracts an additional 1 since lists start at 0
                if int(numToPop) <= int(totalMarketCount):
                    if PurchasedGood(userStronghold,numToPop):
                        serverMarket.RemoveGood(numToPop)
                else:
                    print("Out of range!")
            else:
                screen = "market"
        else:
            screen = "market"

        
    return screen