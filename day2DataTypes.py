# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 18:37:08 2023

@author: Jinjia Liu
"""

num_char = len(input("What is your name? "))
print("Your name has " + str(num_char) + " characters.")


a = 123
print(type(a))

print(70 + float("100.15"))
print(str(70) + str("100.15"))

# Write a program that adds the digits in a 2 digit number.
# e.g. if the input was 35, then the output should be 3 + 5 = 8

num = input("Please enter 2-digit number e.g. 35: ")
sumDigits = int(num[0]) + int(num[1])
print("The sum of 2-digit number " + num + " is " + str(sumDigits))

# Write a program that calculate the Body Mass Index (BMI) from a user's 
# weight and height.

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))
BMI = weight / (height**2)
print("Your BMI is " + str(round(BMI)))


# Create a program using maths and f-strings that tells us how many days,
# weeks, months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time 
# left in this format:
#     You have x days, y weeks, and z months left.
    
age = int(input("Enter your current age: "))
yearsLeft = 90 - age
daysLeft = yearsLeft * 365
weeksLeft = yearsLeft * 52
monthsLeft = yearsLeft * 12
print(f"You have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} months.")

  