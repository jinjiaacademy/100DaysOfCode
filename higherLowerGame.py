# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 23:03:22 2023

@author: Jinjia Liu
"""
from game_data import data
from art import logo, vs
import random

def celebrity():
    return random.choice(data)

def highLowGame():
    gameRunning = True
    
    score = 0
    
    print(logo)
    
    A = celebrity()
    B = celebrity()
    
    if A == B:
        B = celebrity()
    
    while gameRunning:
        
        print()
        print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
        print(vs)
        print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")
        print()
        
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        if choice == "A":
            if A['follower_count'] > B['follower_count']:
                score += 1
                print(f"You're right! Current score: {score}")
                A = B
                B = celebrity()
            else:
                gameRunning = False
                print(f"Sorry, that's wrong. Final score: {score}")
        else:
            if B['follower_count'] > A['follower_count']:
                score += 1
                print(f"You're right! Current score: {score}")
                A = B
                B = celebrity()
            else:
                gameRunning = False
                print(f"Sorry, that's wrong. Final score: {score}")
            
highLowGame()

if input("Do you want to play the game again? yes or no ? ") == "yes":
    highLowGame()        



    