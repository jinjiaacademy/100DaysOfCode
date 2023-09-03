# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 11:03:50 2023

@author: Jinjia Liu
"""

import random

# coin = ["Heads", "Tails"]

# # choice = random.choice(coin)

# count = 0
# for i in range(1000):
#     choice = random.choice(coin)
#     if choice == "Heads":
#         count += 1
# print(count)

randomSide = random.randint(0, 1)
if randomSide == 0:
    print("Tails")
else:
    print("Heads")