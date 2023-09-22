# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 10:38:25 2023

@author: Jinjia
"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def chooseCoffee(choice):
    """Input the selected coffee
        Return the contents of the coffee."""
    coffeeChosed = {}
    coffee = MENU[choice]
    waterAmount = coffee["ingredients"]["water"]
    milkAmount = coffee["ingredients"]["milk"]
    coffeeAmount = coffee["ingredients"]["coffee"]
    price = coffee["cost"]
    coffeeChosed["water"] = waterAmount
    coffeeChosed["milk"] = milkAmount
    coffeeChosed["coffee"] = coffeeAmount
    coffeeChosed["price"] = price
    return coffeeChosed
    
def printReport(coffee=None):
    if coffee:
        coffeeChosen = chooseCoffee(coffee)
        waterLeft = resources["water"] - coffeeChosen["water"]
        milkLeft = resources["milk"] - coffeeChosen["milk"]
        coffeeLeft = resources["coffee"] - coffeeChosen["coffee"]
        money = profit + coffeeChosen["price"]
    else:
        waterLeft = resources["water"]
        milkLeft = resources["milk"]
        coffeeLeft = resources["coffee"]
        money = 0
    print(f"Water: {waterLeft}ml\nMilk: {milkLeft}ml\nCoffee: {coffeeLeft}g\nMoney: ${money}")

    
def ingredientsLeft(coffee):
    coffeeChosen = chooseCoffee(coffee)
    waterLeft = resources["water"] - coffeeChosen["water"]
    milkLeft = resources["milk"] - coffeeChosen["milk"]
    coffeeLeft = resources["coffee"] - coffeeChosen["coffee"]
    return {"waterLeft": waterLeft,
            "milkLeft": milkLeft,
            "coffeeLeft": coffeeLeft
            }

def checkResourcesSufficient(coffee):
    coffeeChosed = chooseCoffee(coffee)
    if resources["water"] >= coffeeChosed["water"] and\
        resources["milk"] >= coffeeChosed["milk"] and\
            resources["coffee"] >= coffeeChosed["coffee"]:
        return True

def processCoins():
    quaters = int(input("Please insert quater coins: "))
    dimes = int(input("Please insert dimes coins: "))
    nickles = int(input("Please insert nickle coins: "))
    pennies = int(input("Please insert penny coins: "))
    total = quaters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total


def coffeeMachine():
    coffeeMachineRunning = True
    
    while coffeeMachineRunning:
        
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        
        if choice == "off":
            coffeeMachineRunning = False
        else:
            if choice == "report":
                report = printReport()
            else:
                if checkResourcesSufficient(choice):
                    totalCoinsInsert = processCoins()
                    coffeePrice = chooseCoffee(choice)["price"]
                    
                    if totalCoinsInsert >= coffeePrice:
                        report = printReport(choice)
                        change = totalCoinsInsert - coffeePrice
                        print(f"Here's ${change:.2f} dollars in change.")
                        print(f"Here is your {choice}. Enjoy!")
                    else:
                        coffeeMachineRunning = False
                        print("Sorry that's not enough money. Money refunded.")
                else:
                    print("Sorry there is not enough ingredients.")

coffeeMachine()

if input("Would you order a coffee: ") == "yes":
    coffeeMachine()

