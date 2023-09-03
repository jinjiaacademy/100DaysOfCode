# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 21:44:42 2023

@author: Jinjia Liu
"""
print("Welcome to the Love Calculator!")
print("What is your name?")
name1 = input().lower()
print("What is their name?")
name2 = input().lower()

trueCount = 0
loveCount = 0

for char in "true":
    trueCount += name1.count(char) + name2.count(char)

for char in "love":
    loveCount += name1.count(char) + name2.count(char)
    
score = str(trueCount) + str(loveCount)
score = int(score)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together liek coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
