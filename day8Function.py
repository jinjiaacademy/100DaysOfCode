# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 14:20:01 2023

@author: Jinjia Liu
"""

def greet(name):
    print("Hello, everyone.")
    print(f"My name is {name}.")
    print("Nice to see you.")

# name = input("Enter a name to greeting: ")
# greet(name)

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

# name = input("Enter a name: ")
# location = input("Enter a location: ")
greet_with(name = "Jinjia", location = "London")