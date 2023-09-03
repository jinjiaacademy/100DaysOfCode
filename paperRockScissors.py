# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 11:56:10 2023

@author: Jinjia Liu
"""

import random

choices = ["paper", "rock", "scissors"]
human = input("What do you choose? Paper, rock or scissor? ").lower()
computer = random.choice(['paper', 'rock', 'scissor'])

if human not in choices:
    print("You entered the invalid words, Game over!!")
else:
    print(f"You: {human} vs. Computer: {computer}")
    if computer == "paper":
        if human == "paper":
            print("Tie")
        else:
            if human == "rock":
                print("Computer wins")
            else:
                print("Human wins")
    else:
        if computer == "rock":
            if human == "paper":
                print("Human wins")
            else:
                if human == "rock":
                    print("Tie")
                else:
                    print("Computer wins")
        else:
            if human == "paper":
                print("Computer wins")
            else:
                if human == "rock":
                    print("Human wins")
                else:
                    print("Tie")
