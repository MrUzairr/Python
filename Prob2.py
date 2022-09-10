# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Second Task

# Extracting function from func.py file
from funcs import *

X = []
# Extracting array from text file
text_file = open("prob1.txt","r")

line = text_file.read().splitlines()
for i in line:
    X.extend(i.split())

# Making array in integer
for j in range(len(X)):
    X[j] = int(X[j])

# Unsorted Array
print("Unsrted Array: ",X)

# Taking Input
a = input("Enter the number: ")

# Given Output
print("Index: ",SearchB(X,a))
