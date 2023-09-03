# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 13:57:38 2023

@author: Jinjia Liu
"""

# Write a program that works out whether if a given year is a leap
# year. 
# This is how you work out whether if a particular year is a leap 
# year:
#     on every year that is evenly divisible by 4
#         except every year that is evenly divisible by 100:
#             unless the year is also evenly divisible by 400

year = int(input("Which year do you want to check if it is a leap year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")