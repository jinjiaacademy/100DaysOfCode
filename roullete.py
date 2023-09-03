# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 11:23:51 2023

@author: Jinjia
"""

import random

namesStr = input("Give me everybody's names, seperated by a comma.")
names = namesStr.split(",")

choice = random.choice(names)
print(f"{choice} is going to buy the meal today.") 