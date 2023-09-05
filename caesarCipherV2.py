# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 23:47:35 2023

@author: Jinjia
"""

def caesor(cipherDirection, cipherMessage, shiftAmount):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    finalText = ""
    for letter in cipherMessage:
        if letter in alphabet:
            position = alphabet.index(letter)
            if cipherDirection == "encode":
                newPosition = position + shiftAmount
                if newPosition >= len(alphabet):
                    finalText += alphabet[newPosition-len(alphabet)]
                else:
                    finalText += alphabet[newPosition]
            else:
                newPosition = position - shiftAmount
                if newPosition < 0:
                    finalText += alphabet[len(alphabet)+newPosition]
                else:
                    finalText += alphabet[newPosition]        
        else:
            finalText += letter
    return finalText


programRunning = True

while programRunning:
    print("Welcome to the Caesor Cipher Application")
    print("If you want to run the application, enter 'yes' or 'no'")
    decision = input().lower()
    if decision == "yes":
        print("Do you want to encode or decode: ")
        direction = input().lower()
        print("Please enter your message: ")
        message = input().lower()
        print("Please enter the amount of shift: ")
        shift = int(input())
        text = caesor(direction, message, shift)
        print(f"Your {direction} message is '{text}'.")
    else:
        programRunning = False
print("Thank you for using the Caesor Cipher Application.")
print("Good bye!")