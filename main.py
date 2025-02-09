### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}

portion = {
    "bread": "slice(s)",
    "ham": "slice(s)",
    "cheese":"pound(s)"
}

money = [
    1,       ##large dollars
    .5,      ##half dollars
    .25,     ##quarters
    .05      ##nickels
]

### Complete functions ###

class SandwichMachine:

    

    def __init__(self, machine_resources, lDollar = 0, hDollar = 0, quater = 0, nickels = 0):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources
        self.lDollar = lDollar
        self.hDollar = hDollar
        self.quater = quater
        self.nickels = nickels


    #Returns True when order can be made, False if ingredients are insufficient.
    def check_resources(self, ingredients):
        for remaining, ingredient in zip(self.machine_resources.values(), ingredients.values()):
            if (ingredient>remaining):
                return False
        return True
    
    def check_resources_improved(self, ingredients):
        for remainingItem, remainingAmount in self.machine_resources.items():
            ingredient = ingredients.get(remainingItem)
            if (ingredient>remainingAmount):
                return [False, remainingItem]
        return [True, None]

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

    def make_sandwich(self, sandwich_size, order_ingredients = None):        
        condition, missingItem = self.check_resources_improved(recipes.get(sandwich_size).get("ingredients"))
        if (condition):
            for item, amount in zip(self.machine_resources.keys(), recipes.get(sandwich_size).get("ingredients").values()):
                self.machine_resources[item] -=  amount
            print("%s sandwich is ready. Bon appetit!" % sandwich_size)
        else:
            print("Sorry there is not enough " + missingItem)
        
    def __str__(self):
        text = ""
        for item, amount in self.machine_resources.items():
            text += "%s: %s %s\n" % (item, amount, portion[item])        
        return text   

### Make an instance of SandwichMachine class and write the rest of the codes ###


r = SandwichMachine(resources)


looping = True
menu = ""

while looping:        
    menu = str(input("What would you like? (small/ medium/ large/ off/ report):"))

    while menu not in ("small", "medium", "large", "off", "report"):        
        print("Please select valid option")
        menu = str(input("What would you like? (small/ medium/ large/ off/ report):"))

    if menu not in ("off", "report"):
        money = r.process_coins()
        if r.transaction_result(money, recipes.get(menu).get("cost")):            
            change = money - recipes.get(menu).get("cost")
            print("Here is $%2.2f in change" % change)

            r.make_sandwich(menu)
        else:
            print("Sorry that's not enough money. Money refunded.")

    elif menu == "report":
        print(r)

    else:
        looping = False