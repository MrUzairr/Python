# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Nineth Task

# Extracting function from func.py file
from funcs import *


# Taking Input
string = input("Enter Something: ")
 
# Checking Condition
if string == PalindromRecursive(string):
    print("Palindrome")
else:
    print("Is not Palindrome")