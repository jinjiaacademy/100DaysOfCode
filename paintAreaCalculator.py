# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 14:38:41 2023

@author: Jinjia
"""
import math

def paint_calc(height, width, cover):
    num_cans = (height * width) / cover
    return math.ceil(num_cans)


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

print(paint_calc(height=test_h, width=test_w, cover=coverage))