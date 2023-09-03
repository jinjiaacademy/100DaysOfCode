# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 22:18:42 2023

@author: Jinjia Liu
"""

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("You're at a cross road. Where do you want to go? Type 'left' or 'right'")
direction = input()

if direction.lower() == "left":
    print("Swim or wait? ")
    action = input()
    if action.lower() == "wait":
        print("Which door would you like to choose? Red, Yellow, or Blue.")
        door = input()
        if door.lower() == "yellow":
            print("You win!")
        else:
            if door.lower() == "red":
                print("Burned by fire. Game over.")
            else:
                print("Eaten by beasts. Game over.")
    else:
        print("Attacked by trout. Game over.")
else:
    print("Fall into a hole. Game over.")