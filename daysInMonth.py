# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 13:53:04 2023

@author: Jinjia
"""

def isLeapYear(year):
    """
    Return the year is leap year or not 
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def daysInMonth(year, month):
    """
    Input the year and the month 
    Return the days of the month in the year
    """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isLeapYear(year) and month == 2:
        return 29
    return month_days[month-1]
    
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = daysInMonth(year, month)
print(days)