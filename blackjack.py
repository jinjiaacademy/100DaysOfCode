# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 10:04:48 2023

@author: Jinjia Liu
"""
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

gameRunning = True
cardPicking = True

gameOption = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

while gameRunning:
    computer = []
    player = []   
    if gameOption == "y":
        
        for i in range(2):
            playerCard = random.choice(cards)
            player.append(playerCard)
        
        playerTotal = sum(player)
        
        computerCard = random.choice(cards)
        computer.append(computerCard)
        
        print(f"Your card: {player}, current score: {playerTotal}")
        print(f"Computer's first card: {computerCard}")
        
        while cardPicking:
            anotherCard = input("Type 'y' to get another card, type 'n' to pass: ")
            
            if anotherCard == "y":
                playerCard = random.choice(cards)
                player.append(playerCard)
                
                playerTotal = sum(player)
                
                print(f"Your card: {player}, current score: {playerTotal}")
                print(f"Computer's first card: {computerCard}")
            
            else:
                print(f"Your final card: {player}, current score: {playerTotal}")
                
                while sum(computer) < 17:
                    computerCard = random.choice(cards)
                    computer.append(computerCard)
                print(f"Computer's final hand : {computer}, final score: {sum(computer)}")
                
                cardPicking = False
                
        if playerTotal > 21:
            print("You bust and lost!!!")
        else:
            if playerTotal == 21:
                print("You win!!!")
            else:
                if playerTotal == sum(computer):
                    print("Draw!!!")
                else:
                    if playerTotal < sum(computer):
                        if sum(computer) < 21:
                            print("You lose!!!")
                        else:
                            print("You win!!!")
                    else:
                        print("You win!!!")
        
        gameOption = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if gameOption == "n":
            gameRunning = False
    else:
        gameRunning = False
                
                
        
        
        