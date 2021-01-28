#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
 
    d = {} # initialize empty array of length n
 
    for i in arr:   # code to count frequency of each element in the array
        d[i] = arr.count(i)
    
    # difference between n and most frequent element in the array results to minimum num of deletion required
    return n - max(d.values()) 

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
