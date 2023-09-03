# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 13:02:21 2023

@author: Jinjia Liu
"""

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")
    
# # Write a program that works out whether if a given number is an odd
# # or even number.

# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print(f"{num} is an even number.")
# else:
#     print(f"{num} is an odd number.")
    
# Write a program that interprets the BMI based on a user's wieght
# and height.
# It should tell them the interpretation of their BMI based on the 
# BMI value.
#  - Under 18.5 they are underweight
#  - Over 18.5 but below 25 they have a normal weight
#  - Over 25 but below 30 they are overweight
#  - Over 30 but below 35 they are obese
#  - Above 35 they are clinically obese
 
print("Enter your weight in kilograms: ")
weight = float(input())
print("Enter your height in meters: ")
height = float(input())

BMI = round(weight / height**2, 2)

if BMI < 18.5:
    condition = "underweight"
else:
    if BMI < 25:
        condition = "normal weight"
    else:
        if BMI < 30:
            condition = "overweight"
        else:
            if BMI < 35:
                condition = "obese"
            else:
                condition = "clinically obese"

print(f"Your BMI is {BMI} and you are {condition}.")
