# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 14:12:17 2023

@author: Jinjia
"""

def add(n1, n2):
    return n1 + n2

def minus(n1, n2):
    return n1 - n2

def multiple(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculation(firstNumber, secondNumber, operator):
    if operator == "+":
        result = add(firstNumber, secondNumber)
    elif operator == "-":
        result = minus(firstNumber, secondNumber)
    elif operator == "*":
        result = multiple(firstNumber, secondNumber)
    else:
        result = divide(firstNumber, secondNumber)  
    return result



def calculator():
    num1 = float(input("What is the first number: "))
    
    should_continue = True
    
    while should_continue:
        operator = input("Pick an operator + - * / : ")
        num2 = float(input("What is the next number: "))
        answer = calculation(num1, num2, operator)
        
        print(f"{num1} {operator} {num2} = {answer}")
        
        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ")== "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()
        
        
    