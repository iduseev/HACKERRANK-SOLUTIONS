#!/bin/python3

import math
import time

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):

    f = math.factorial(n)

    return f

if __name__ == '__main__':
    n = int(input())

    result = extraLongFactorials(n)

    print(result)
