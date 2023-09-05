# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 10:09:13 2023

@author: Jinjia Liu
"""

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62}

student_grades = {}

for name in student_scores:
    score = student_scores[name]
    if score >= 91:
        grade = "Outstanding"
    else:
        if score >= 81:
            grade = "Exceeds Expectations"
        else:
            if score >= 71:
                grade = "Acceptable"
            else:
                grade = "Fail"
    student_grades[name] = grade

print(student_grades)