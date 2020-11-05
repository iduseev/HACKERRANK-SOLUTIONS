#!/bin/python3

# Complete the sockMerchant function below.
def sockMerchant(n, ar):

    count = 0 # initialize variables
    i = 0

    ar.sort() # sort elements in the array in ascending order

    ar.append('*') # append element with index [n] to avoid IndexError when calling ar[i+1] in last case

    while i < n: 
        if ar[i] == ar[i+1]: # compare adjacent elements and if they are equal, 
            count += 1       # increment count var
            i += 2           # jump to the i+2 element to compare it with its adjacent element 
        else:
            i += 1           # appeal to next element if adjacent elements are not equal
        
    return count
    
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
