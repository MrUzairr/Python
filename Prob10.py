# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Tenth Task

# Extracting function from func.py file
from funcs import *

X = []

# Extracting array from text file
text_file = open("prob10.txt","r")

line = text_file.read().splitlines()

# Unsorted Array
for i in line:
    X.extend(i.split())

# Making array in integer
for j in range(len(X)):
    X[j] = int(X[j])
    
# Unsorted Array
print("Unsorted Array: ",X)   

# Given Output
print("Given Output: ",Sort10(X))