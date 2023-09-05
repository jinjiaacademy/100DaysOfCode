# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 11:06:57 2023

@author: Jinjia Liu
"""

programRunning = True

print("Welcome to the secret auction program.")

bidding = {}

while programRunning:
    name = input("What is your name? ")
    bid = float(input("What is your bid? $"))
    bidding[name] = bid
    
    otherBidder = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    
    if otherBidder == 'no':
        programRunning = False

highestBidder = ""
highestBid = 0

for name in bidding:
    if bidding[name] > highestBid:
        highestBidder = name
        highestBid = bidding[name]

print(f"The highest bidder is {highestBidder} and the bid is {highestBid}")    
    
            
        
    
    