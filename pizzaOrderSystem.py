# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 14:34:24 2023

@author: Jinjia
"""

# Build an automatic pizza order program.
# Based on a user's order, work out their final bill.
#  Small Pizza: $15
#  Medium Pizza: $20
#  Large Pizza: $25
 
#  Pepperoni for small pizza: +$2
#  Pepperoni for Medium or Large pizza: +$3
 
#  Extra cheese for any size pizza: +$1

# prices for different sizes pizza 
small = 15
medium = 20
large = 25

# extra pepperoni charge for different sizes
pepSmall = 2
pepML = 3

# extra cheese charge
extraCheeseCharge = 1

print("Welcome to Python Pizza Deliveries!")
print("What size pizza do you want? S, M or L ")
size = input()
print("Do you want pepperoni? Y or N ")
addPepperoni = input()
print("Do you want extra cheese? Y or N ")
extraCheese = input()

# check what size and add pepperoni or not
if size == "S":
    finalBill = small
    if addPepperoni == "Y":
        finalBill = finalBill + pepSmall
else:
    if size == "M":
        finalBill = medium
    else:
        finalBill = large
    if addPepperoni == "Y":
        finalBill = finalBill + pepML

# check if add extra cheese
if extraCheese == "Y":
    finalBill = finalBill + extraCheeseCharge

print(f"Your final bill is ${finalBill}.")      

