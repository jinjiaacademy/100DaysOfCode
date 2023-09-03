# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 14:08:48 2023

@author: Jinjia Liu
"""

# You are going to write a program that calculates the average student
# height from a list of heights.

total = 0
students = int(input("How many students: "))

for i in range(1, students+1):
    height = int(input(f"Enter the No.{i} student's height in cm: "))
    total += height    
averageHeight = total/students

print(f"There are {students} students in the group.")
print(f"The average height in the group is {averageHeight:.2f}cm.")
