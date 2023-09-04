# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 10:30:47 2023

@author: Jinjia
"""
import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f"The chosen word is {chosen_word}")

word_length = len(chosen_word)

display = []
display += "_" * word_length
print("".join(display))

gameRunning = True
life = 9

while gameRunning:
    guess = input("Guess a letter: ").lower()
    
    if guess in chosen_word:
        if guess not in "".join(display):
            for i in range(word_length):
                letter = chosen_word[i]
                if guess == letter:
                    display[i] = guess
            print("".join(display))
            
            if "".join(display) == chosen_word:
                gameRunning = False
                print("You win!!!")
        else:
            print("You have guess the letter. You lost one life.")
            life = life - 1
    else:
        print("Your guess is not in the word. You lose one life.")
        life = life - 1
        if life == 0:
            gameRunning = False
            print("You lose.")

print("Game over!!!")
        

