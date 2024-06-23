import resources

money = 0


def check_ingredients(coffee_type):
    flags = [False, False, False]
    if resources.MENU[coffee_type]["ingredients"]["water"] <= resources.resources["water"]:
        flags[0] = True
    if resources.MENU[coffee_type]["ingredients"]["milk"] <= resources.resources["milk"]:
        flags[1] = True
    if resources.MENU[coffee_type]["ingredients"]["coffee"] <= resources.resources["water"]:
        flags[2] = True
    if flags[0] and flags[1] and flags[2] :
        return True
    else:
        return False


def take_transaction(coffee_type):
    global money
    print("Please insert coins.")
    coin1 = int(input("Enter quarters :"))
    coin2 = int(input("Enter dimes :"))
    coin3 = int(input("Enter nickels :"))
    coin4 = int(input("Enter pennies :"))
    total = (coin1 * 0.25) + (coin2 * 0.10) + (coin3 * 0.05) + (coin4 * 0.01)
    cost = resources.MENU[coffee_type]["cost"]
    if total >= cost:
        print("Here is you change", round(total - cost,2))
        money += cost
        return True
    else:
        print("Entered money is less!!!")
        return False


def manage_resource(coffee_type):
    resources.resources["water"] -= resources.MENU[coffee_type]["ingredients"]["water"]
    resources.resources["milk"] -= resources.MENU[coffee_type]["ingredients"]["milk"]
    resources.resources["coffee"] -= resources.MENU[coffee_type]["ingredients"]["coffee"]


while True:
    choice = input("Would you like (latte/cappuccino/espresso): ").lower()
    if choice == "report":
        print(f"Water : {resources.resources["water"]}.")
        print(f"Milk : {resources.resources["milk"]}.")
        print(f"Coffee : {resources.resources["coffee"]}.")
        print(f"Money : {money}.")
    elif choice == "latte" or choice == "cappuccino" or choice == "espresso":
        sufficient = check_ingredients(choice)
        if sufficient:
            check = take_transaction(choice)
            if check:
                manage_resource(choice)
                print("Here is your coffee☕")
        else:
            print("Not enough resources!!!")
    elif choice == "exit":
        break