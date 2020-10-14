#!/bin/python3

# import os
# import sys

#
# Complete the plusMinus function below.
#
def plusMinus(arr):

    positive = [num for num in arr if num > 0] # apply list comprehension to count positive integers
    pos_count = len(positive)

    negative = [num for num in arr if num < 0] # apply list comprehension to count negative integers
    neg_count = len(negative)

    zero_count = len(arr) - pos_count - neg_count # number of zeroes equals to number of elements in a row
                                                  # minus all positive and negative

    pos_prop = pos_count / len(arr) # calculate ratios of negative, positive and zero elements in the row 
    neg_prop = neg_count / len(arr)
    zero_prop = zero_count / len(arr)

    print('{:.6f}'.format(pos_prop)) # print out ratios up to 6 decimal places
    print('{:.6f}'.format(neg_prop))
    print('{:.6f}'.format(zero_prop))

if __name__ == '__main__':
    n = int(input().strip())

    arr = [int(x) for x in input().strip().split()] # apply list comprehension for input elements to convert into integers

    plusMinus(arr)

