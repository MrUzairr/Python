# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Seventh Task

# Extracting function from func.py file
from funcs import *
A = []

# Extracting array from text file
with open("prob7.txt") as text_file:
    for line  in text_file:
        a = [item.strip() for item in line.split(' ')]
        A.append(a)

# Making array in integer
for j in range(len(A)):
    for k in range(len(A)):
        A[j][k] = int(A[j][k])

# Input Array
print("Input Array: ",A)

# Given Output
print("Column-Wise: ",ColumnWiseSum(A))
print("Row-Wise: ",RowWiseSum(A))
