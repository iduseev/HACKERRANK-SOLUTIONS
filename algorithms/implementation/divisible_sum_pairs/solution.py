#!/bin/python3

def divisibleSumPairs(n, k, ar):

    # first = 0
    # result = 0

    # for i in range(n):
    #     if (ar[first] + ar[i]) % k == 0:
    #         result += 1

    res = 0            

    for i in range(n-1):                    # use range (n-1) to avoid index out of range while i = len(ar) and j = i + 1
        j = i + 1                    

        while j < n:                        # iterate through each next array element j with given i
            if (ar[i] + ar[j]) % k == 0:    # if sum of fixed ar[i] and any of ar[j] for sliding j is divisible to k:
                res += 1                    # increment res variable
            j += 1                          # if divisibility condition is not met, increment j

    return res

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    print(result)
