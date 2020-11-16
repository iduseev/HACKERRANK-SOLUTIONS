#!/bin/python3

import math

# Complete the viralAdvertising function below.
def viralAdvertising(n):

    recipients = 5 # No of recipients of the day one
    cumulative = 0
    
    for _ in range(1, n + 1): # iterate through 1 till n inclusive
        liked = math.floor(recipients/2) # as per requirements, no of likers is floor(recipients / 2)
        recipients = liked * 3 # each liker shares with exactly 3 persons
        cumulative += liked # cumulative number of lokers expands by No of fresh new likers

    return cumulative

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
