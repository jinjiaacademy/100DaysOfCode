# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 14:26:12 2023

@author: Jinjia Liu
"""

highestScore = 0
studentNumber = 0
numStudents = int(input("How many students' score to enter? "))

for i in range(1, numStudents+1):
    score = int(input(f"Enter the No.{i} student's score: "))
    if score > highestScore:
        highestScore = score
        studentNumber = i

print(f"The highest score is {highestScore}.")
print(f"No.{studentNumber} student got it!!! Congratulations!!!")
        