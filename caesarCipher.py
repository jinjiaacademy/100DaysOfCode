# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 21:36:13 2023

@author: Jinjia Liu
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 
            'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
            'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrpyt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(direction, message, shift):
    text = ""
    for char in message:
        if char in alphabet:
            position = alphabet.index(char)
            if direction == "encode":
                new_position = position + shift
            else:
                new_position = position - shift
            text += alphabet[new_position]
        else:
            text += char     
    return text

message = caesar(direction, text, shift)
print(message)