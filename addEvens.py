# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 14:43:21 2023

@author: Jinjia
"""

total = 0

for number in range(2, 101, 2):
    print(f"{total} + {number} = {total + number}")
    total += number
    
print(f"The total of even numbers from 1 to 100 is {total}.")