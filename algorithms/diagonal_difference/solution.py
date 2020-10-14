#!/bin/python3

def diagonalDifference(matrix):
    major_diag = 0
    minor_diag = 0
    for i in range(n):
        # main_diag.append(matrix[i][i]) # append elements of main diagonal to a list
        major_diag += matrix[i][i]
        minor_diag += matrix[i][n-i-1]

    return abs(major_diag - minor_diag)    
    #     swapDiag = matrix.copy()  # copying  matrix to swap diagonals without affecting initial matrix 
    #     swapDiag[i][i], swapDiag[i][n-i-1] = swapDiag[i][n-i-1], swapDiag[i][i] # swap elements in temporary matrix to 
    #                                                                             # access to the minor diagonal elements
    #     minor_diag.append(swapDiag[i][i]) # append elements of minor diagonal to a list
                                                                        
    # print(d)
    # print(matrix)
    # print(major_diag)
    # print(minor_diag)

    # main_sum = sum(main_diag) # get sum of elements of main and minor diagonals
    # minor_sum = sum(minor_diag)
    
    # return (abs(main_sum - minor_sum))  # returning absolute value of sums of matrix diagonals
        


import math
import os
import random
import re
import sys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')


    n = int(input().strip())
    matrix = []

    for i in range(n):
        # row = [int(x) for x in input().strip().split(' ')] # apply list comprehension
        row = [int(x) for x in input().strip().split()] #  use dictionary and apply list comprehension
        matrix.append(row) # append the corresponding value (input as a list) to the list to create a matrix



    result = diagonalDifference(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()
