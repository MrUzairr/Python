# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# All Problem Files function

# Prob1
def SearchA(Arr,x):
    array = []
    # checking the no. that is entered how much time is repeated
    for i in range(len(Arr)):
        if int(x)==Arr[i]:
            array.append(i)       
    return array 

# Prob2  
def SearchB(Arr,x):
    # Sorting Array
    for i in range(len(Arr)):
        Arr.sort()
        
    array = []
    # checking the no. that is entered how much time is repeated
    for j in range(len(Arr)):
        if int(x)==Arr[j]:
            array.append(j)       
    return array 

# Prob3
def Minimum(Arr,starting,ending):
    x = Arr[0]
    for i in range(int(starting),int(ending)+1):
        if x>Arr[i]:
            x = Arr[i]
    for j in range(0,len(Arr)):
        if x==Arr[j]:
            return j
     
# Prob4
def Sort4(Arr):
    for i in range(len(Arr)):
        Arr.sort()
    return Arr

# Prob5
def StringReverse(Str,start,end):
    start = int(start)
    end = int(end)
    if Str == "":
        return Str
    else:
        string = Str[::1][start:end+1]
        string = string[::-1]
        return string

    
# Prob6
def SumIterative(x):
    sum = 0
    for digit in str(x):
        sum += int(digit)
    return sum
def SumRecursive(x):
    if x == 0:
       return x
    else:
        return x%10 + Recursive(int(x/10))

# Prob7
def ColumnWiseSum(Mat):
    array = []
    sum0 = 0
    sum1 = 0
    sum2 = 0
    for i in range(3):
        for j in range(3):
            if j == 0:
                sum0 += Mat[i][0]
            if j == 1:
                sum1 += Mat[i][1]
            if j == 2:
                sum2 += Mat[i][2]
    array = [sum0,sum1,sum2]                    
    return array

def RowWiseSum(Mat):
    array = []
    sum0 = 0
    sum1 = 0
    sum2 = 0
    for i in range(3):
        for j in range(3):
            if i == 0:
                sum0 += Mat[0][j]
            if i == 1:
                sum1 += Mat[1][j]
            if i == 2:
                sum2 += Mat[2][j]
    array = [sum0,sum1,sum2]                    
    return array

# Prob8
def SortedMerge(A1,A2):
    # merge unsorted arrays
    sortedArray = A1+A2
    # making them in integer
    for i in range(len(sortedArray)):
        sortedArray[i] = int(sortedArray[i])
    # making them sorted
    for j in range(len(sortedArray)):
        key = sortedArray[j]
        j = j-1
        while key<sortedArray[j] and j>0:
            sortedArray[j+1] = sortedArray[j]
            j = j-1
        sortedArray[j+1] = key
    return sortedArray

# Prob9
def PalindromRecursive(Str):
    # check palindrome
    if len(Str) != 1:
        s1 = PalindromeRecursive(Str[1:]) + Str[0]
        print(s1)
        return s1
    else:
        return Str
    
# Prob10
def Sort10(Arr):
    array = []
    array1 = []
    array2 = []
    
    #Sorted Array
    for j in range(len(Arr)):
        key = Arr[j]
        j = j-1
        while key<Arr[j] and j>=0:
            Arr[j+1] = Arr[j]
            j = j-1
        Arr[j+1] = key
    for k in range(len(Arr)):
        
        
        if Arr[k]<0:  #Negative Array
            array1.append(Arr[k])
        else:         #Positive Array
            array2.append(Arr[k])
    
    #Given Output
    for l in range(len(Arr)):
        if l < len(array1):
            array.append(array1[l])
        if l < len(array2):
            array.append(array2[l])
           
    print("Sorted Array: ",Arr)         
    print("Negative Array: ",array1)   
    print("Positive Array: ",array2)   
     
            
    return array