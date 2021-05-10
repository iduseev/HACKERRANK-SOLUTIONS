#!/bin/python3

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    # Write your code here
    w_len = len(w)
    w = list(w)

    #   search for index i of the head of suffix
    i = w_len - 1
    while i > 0 and w[i - 1] >= w[i]:
        i -= 1

    if i <= 0: 
        return 'no answer'

    #   search for pivot at index j
    j = w_len - 1

    # while j <= i and w[j] <= w[i - 1]:
    while w[j] <= w[i - 1]: # why we should not write j <= i? Index j should be always less than i, nuh?
        j -= 1

    #   swap the pivot and the rightmost element in suffix that is greater than the pivot
    w[j], w[i - 1] =  w[i - 1], w[j] 

    #   reverse suffix to be in incrementing order
    w[i : ] = w[w_len - 1: i - 1 : -1]

    return ''.join(w)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        print(result)

    #     fptr.write(result + '\n')

    # fptr.close()
