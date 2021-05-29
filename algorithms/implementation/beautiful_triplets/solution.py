#!/bin/python3
#
# Complete the 'beautifulTriplets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def beautifulTriplets(d, arr):
    # Write your code here
    counter = 0
    for i in range(len(arr)):
        arr_i = arr[i]
        arr_j = arr[i] + d  #   due to definition, arr[j] - arr[i] = d => arr[j] = arr[i] + d
        arr_k = arr[i] + (2 * d)    #   arr[k] - arr[j] = d => arr[k] = arr[i] + 2 * d

        if arr_j in arr and arr_k in arr:   #   no need to check presence of num_1 (arr[i]) in arr, obviously
            counter += 1
        
    return counter

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
