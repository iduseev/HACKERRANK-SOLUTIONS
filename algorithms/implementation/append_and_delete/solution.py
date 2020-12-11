#!/bin/python3

# Complete the appendAndDelete function below.
def appendAndDelete(initial, desired, k):

    counter = 0 # initialize counter for counting the length of common substring

    for i, j in zip(initial, desired): # iterate through both strings to find the length of common substring 
        if i == j:
            counter += 1
        else:
            break

# define a variable 'unique_len' which is a total length of two unique parts of each string (not considering common substring)
    unique_len = (len(initial) - counter) + (len(desired) - counter) 

# if total length of both strings is less than or equal to k, we delete initial str and append desired str, or delete from empty str
    if len(initial) + len(desired) <= k: 
        return 'Yes'

# if unique_len equals to k, we simply delete unique part of initial str and append new part of desired str.
# However, if unique_len is less than or equal to k, but (k - unique_len) is even,
# we can compensate the difference by appending and deleting one element
    elif (k >= unique_len) and (k - unique_len) % 2 == 0: 
        return 'Yes'

    else:   return 'No'

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    initial = input()

    desired = input()

    k = int(input())

    result = appendAndDelete(initial, desired, k)

    print(result)
    
    # fptr.write(result + '\n')

    # fptr.close()
