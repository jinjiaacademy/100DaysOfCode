# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 14:49:31 2023

@author: Jinjia Liu
"""

for number in range(1, 101):
    if number % 3 == 0:
        if number % 5 == 0:
            print('FizzBuzz')
        else:
            print('Fizz')
    else:
        if number % 5 == 0:
            print('Buzz')
        else:
            print(number)
