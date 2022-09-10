# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Eight Task

# Extracting function from func.py file
from funcs import *
Arr1 = []
Arr2 = []

# Extracting array from text file
text_file1 = open("prob8_Arr1.txt","r")
text_file2 = open("prob8_Arr2.txt","r")

line1 = text_file1.read().splitlines()
line2 = text_file2.read().splitlines()
for i in line1:
    Arr1.extend(i.split())
for j in line2:
    Arr2.extend(j.split())

# Input Array 1 
print("Input Array1: ",Arr1)    
# Input Array 2
print("Input Array2: ",Arr2)    

print("Output: ",SortedMerge(Arr1,Arr2))