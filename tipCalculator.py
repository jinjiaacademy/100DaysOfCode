# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 23:13:24 2023

@author: Jinjia Liu
"""

# Ask the user to enter the total bill and calculate the money everyone 
# should pay with tips. The tip rates options are 10, 12 or 15 percentage.

print("Welcome to the tip calculator.")

totalBill = float(input("What was the total bill? "))
tipPercentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
numPeople = int(input("How many people to split the bill? "))

pay = totalBill * (1 + tipPercentage/100) / numPeople

print(f"Each person should pay: ${pay:.2f}")

