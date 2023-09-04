# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 14:50:50 2023

@author: Jinjia
"""

def primeNumberCheker(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

# n = int(input("Check this number: "))

# if primeNumberCheker(n):
#     print(f"{n} is a prime number.")
# else:
#     print(f"{n} is not a prime number.")

for number in range(1, 101):
    if primeNumberCheker(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")