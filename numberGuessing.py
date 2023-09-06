# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 13:03:08 2023

@author: Jinjia
"""
import random

def numberGuess():
    
    target = random.randint(1, 100)
    
    print("Welcome to the Number Guessing Game!\n")
    print("I am thinking of a number between 1 and 100.\n")
    
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    
    turns = 0
    
    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5
        
    while turns < attempts:
        
        print(f"You have {attempts-turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        
        if guess == target:
            print(f"You got it.The answer is {guess}.")
            break
        else:
            if guess > target:
                print("Too high.")
            else:
                print("Too low.")
        print("Guess again!")
        
        turns += 1
        
    print("You run out of your attempts.")
    
numberGuess()

if input("Do you want to try the game again? y or n") == 'y':
    numberGuess()