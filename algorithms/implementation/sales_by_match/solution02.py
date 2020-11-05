#!/bin/python3

# Complete the sockMerchant function below.
def sockMerchant(n, ar):

    count = 0 # initialize variables
    d = {}

    for i in ar:
        d[i] = d.get(i, 0) + 1 # if i exists in d, it will return its value, otherwise return 0 to avoid an error
                               # overwrites 'value' for corresponding 'key' by No of times the 'key' appears in arr

    for i in d.keys():          # iterate through 'keys' for i to be the 'key' to retrieve corresponding 'value' further
        count += d[i] // 2      # if corresponding 'value' divides by 2 with no remaining, the result is No of pairs of that keys in arr 
                                # if 'value' divides by 2 with remaining == 1 > only 1 pair of 'key' elements exist
    
    return count
    
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
