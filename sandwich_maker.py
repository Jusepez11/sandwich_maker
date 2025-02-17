class SandwichMachine:      

    def __init__(self, machine_resources):
        self.machine_resources = machine_resources

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

    def make_sandwich(self, sandwich_size, order_ingredients):        
        condition, missingItem = self.check_resources_improved(order_ingredients.get(sandwich_size).get("ingredients"))
        if (condition):
            for item, amount in zip(self.machine_resources.keys(), order_ingredients.get(sandwich_size).get("ingredients").values()):
                self.machine_resources[item] -=  amount
            print("%s sandwich is ready. Bon appetit!" % sandwich_size)
        else:
            print("Sorry there is not enough " + missingItem)
        
    def __str__(self):
        portion = {
            "bread": "slice(s)",
            "ham": "slice(s)",
            "cheese":"pound(s)"
        }

        text = ""
        for item, amount in self.machine_resources.items():
            text += "%s: %s %s\n" % (item, amount, portion[item])        
        return text   