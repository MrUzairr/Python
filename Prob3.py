# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Third Task

# Extracting function from func.py file
from funcs import *

Array=[]
# Extracting array from text file
text_file = open("prob3.txt","r")

line = text_file.read().splitlines()
for i in line:
    Array.extend(i.split())

# Making array in integer
for j in range(len(Array)):
    Array[j] = int(Array[j])

# Unsorted Array
print("Unsorted Array: ",Array)

# Taking Input
a = input("StartingIndex: ")
b = input("EndingIndex: ")

# Given Output
print("Output: ",Minimum(Array,a,b))