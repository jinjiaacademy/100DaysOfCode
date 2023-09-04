# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 21:22:28 2023

@author: Jinjia Liu
"""

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
           'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


letterChosen = ""
symbolChosen = ""
numberChosen = ""

print('Welcome to the PyPassword Generator!')

numLetters = int(input("How many letters would you like in your password?\n"))
numSymbols = int(input("How many symbols would you like?\n"))
numNumbers = int(input("How many numbers would you like?\n"))

for i in range(numLetters):
    letterChosen += random.choice(letters)

for i in range(numSymbols):
    symbolChosen += random.choice(symbols)

for i in range(numNumbers):
    numberChosen += random.choice(numbers)
    
password = list(letterChosen + symbolChosen + numberChosen)
random.shuffle(password)
# password = random.sample(password, len(password))
password = "".join(password)
print(f"Here is the password: {password}")