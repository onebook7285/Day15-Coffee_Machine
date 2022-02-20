MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

SECRET = ["off", "report"]

def GetAvailableOptions():
    options = []
    for item in MENU:
        ingredients = MENU[item]["ingredients"]
        sufficient = True
        for ingredient in ingredients:
            if resources[ingredient] < ingredients[ingredient]:
                sufficient = False
        if sufficient:
            options.append(item)
    return options

def TakeCoins():
    quaters = int(input("How many quaters would you like to use? "))
    dimes = int(input("How many dimes would you like to use? "))
    nickles = int(input("How many nickles would you like to use? "))
    pennies = int(input("How many pennies would you like to use? "))
    total = quaters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return total

def ProcessTransaction(orderItem, coins):
    costOfOrder = orderItem["cost"]
    if coins < costOfOrder:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif coins > costOfOrder:
        change = coins - costOfOrder
        print(f"Here is ${round(change,2)} dollars in change.")
    return True

def UpdateReport(orderItem):
    for ingredient in orderItem["ingredients"]:
        resources[ingredient] -=  orderItem["ingredients"][ingredient]

def PrintReport():
    for key in resources:
        unit = "ml"
        if key == "coffee":
            unit = "g"
        print(f"{key}: {resources[key]}{unit}")
    print(f"Money: ${profit}")

def RunSecret(secret):
    if userOrder == "report":
        PrintReport()
    elif userOrder == "off":
        return True
    return False

turnOff = False
profit = 0.00
while not turnOff:
    options = GetAvailableOptions()
    optionsString = "/".join(options)
    if len(options) > 0:
        userOrder = input(f"What would you like? ({optionsString}]):").lower()
        if userOrder in SECRET:
            turnOff = RunSecret(userOrder)
        elif userOrder in options:
            orderItem = MENU[userOrder]
            coins = TakeCoins()
            if ProcessTransaction(orderItem, coins):
                profit += orderItem["cost"]
                UpdateReport(orderItem)
                print(f"Here is your {userOrder}. Enjoy!")
        else:
            print("The item you order is not available, please try again.")
    else:
        turnOff = True