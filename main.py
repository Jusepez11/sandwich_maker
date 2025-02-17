import data
from sandwich_maker import SandwichMachine
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMachine(resources)
cashier_instance = Cashier()




def main():
    looping = True
    menu = ""

    while looping:        
        menu = str(input("What would you like? (small/ medium/ large/ off/ report):"))

        while menu not in ("small", "medium", "large", "off", "report"):        
            print("Please select valid option")
            menu = str(input("What would you like? (small/ medium/ large/ off/ report):"))

        if menu not in ("off", "report"):
            money = cashier_instance.process_coins()
            if cashier_instance.transaction_result(money, recipes.get(menu).get("cost")):            
                change = money - recipes.get(menu).get("cost")
                print("Here is $%2.2f in change" % change)

                sandwich_maker_instance.make_sandwich(menu, recipes)
            else:
                print("Sorry that's not enough money. Money refunded.")

        elif menu == "report":
            print(sandwich_maker_instance)

        else:
            looping = False

if __name__=="__main__":
    main()
