# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 10:38:25 2023

@author: Jinjia
"""

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


def printReport(choice):
    """Print the report of the coffee ingredients and price."""
    coffee = MENU[choice]
    ingredients = coffee["ingredients"]
    price = coffee["cost"]
    for ing in ingredients:
        print(f"{ing.title()}: {ingredients[ing]}")
    print(f"Money: {price}")
    

def checkResources(choice):
    