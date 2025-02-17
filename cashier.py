class Cashier:
    def __init__(self, lDollar = 0, hDollar = 0, quater = 0, nickels = 0):
        self.lDollar = lDollar
        self.hDollar = hDollar
        self.quater = quater
        self.nickels = nickels

    def process_coins(self):
        self.lDollar = int(input("how many large dollars?:") or 0)
        self.hDollar = int(input("how many half dollars?:") or 0)
        self.quater = int(input("how many quarters?:") or 0)
        self.nickels = int(input("how many nickels?:") or 0)

        return self.lDollar + (self.hDollar*.5) + (self.quater*.25)  + (self.nickels*.05)

    def transaction_result(self, coins, cost):
        if (coins < cost):            
            return False        
        return True
