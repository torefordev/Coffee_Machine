MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "price": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "price": 2.25,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "price": 3.00,
    }
}

resources = {
    "water": 500,
    "milk": 300,
    "coffee": 100,
    "sugar": 50,
}


def coinCalculator():
    """returns total money"""
    print("Only coins are accepted.")
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickles = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))
    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return total

def compare(money, price):
    """para az ise 0, para çok ise 1, para tam ise 2 döndürür"""
    change = money - price
    if price > money:
        return 0,change #sipariş iptal
    elif price < money:
        return 1,change.__round__(2) #fazlalık para iade
    else:
        return 2,change #para üstü yok

def resourceCheck(drink):
    """enough resoruces -> returns True, not enough -> returns False"""
    for resource in resources:
        if resource in drink["ingredients"]:
            if resources[resource] == 0:
                print(f"{resource.title()} is depleted. Please fill or shut down.")
            elif resources[resource] < drink["ingredients"][resource]:
                print(f"{resource.title()} is not enough. Please order another drink.")
                return False
    return True

def resourceDecrease(drink):
    for resource in resources:
        if resource in drink["ingredients"]:
            resources[resource] -= drink["ingredients"][resource]


def resourceFill():
    resource = input("Which resource do you want to fill? (water,milk,coffee): ")
    amount = int(input("How much do you want to fill? : "))
    resources[resource] += amount

def list():
    drinks = ["espresso","latte","cappuccino"]
    available_drinks = []
    available = True
    for resource in resources:
        for i in range(3):
            for resource in MENU[drinks[i]]["ingredients"]:
                if resources[resource] < MENU[drinks[i]]["ingredients"][resource]:
                    available = False
            if available == True and drinks[i] not in available_drinks:
                available_drinks.append(drinks[i])

    if available_drinks == []:
        print("Resources are not enough for any drink. Please fill or shut down.")

    for item in available_drinks:
        print(item.title())


def coffeeMachine(money):
    money_in_machine = money
    choice = input("What do you wanna drink? (espresso/latte/cappuccino): ")
    if choice == "list":
        list()
        coffeeMachine(money_in_machine)
    if choice == "fill":
        resourceFill()
        coffeeMachine(money_in_machine)
    if choice == "off":
        exit(("Coffee machine shut off manually."))
    if choice == "report":
        for resource in resources:
            if resource == "water" or resource == "milk":
                print(f"{resource}: {resources[resource]}ml")
            else:
                print(f"{resource}: {resources[resource]}gr")
        print(f"Money: ${money_in_machine}")
        coffeeMachine((money_in_machine))

    enough = resourceCheck(MENU[choice])
    if enough == False:
        coffeeMachine(money_in_machine)

    total_money = coinCalculator()
    drink_price = MENU[choice]["price"]
    output,change = compare(total_money, drink_price)
    if output == 0:
        print("Not enough money to buy this drink.")
    else:
        resourceDecrease(MENU[choice])
        if output == 1:
            print(f"Change: ${change}. {choice.title()} ready. Enjoy!")
        else:
            print(f"{choice.title()} ready. Enjoy!")
        money_in_machine += drink_price

    coffeeMachine(money_in_machine)

coffeeMachine(0)