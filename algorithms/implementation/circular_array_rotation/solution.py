#!/bin/python3

# there are 2 cases to consider 
# if i > 0 then a[i] becomes a[i-1]
# if i = 0, then a[i] becomes a[i-1+n] for all i

# This operation is similar to a[i] changing to a[i-1+n] for all i
# 
# After K operations, a[i] changes to a[i-k+n] % n.
# If k > n, then (i-k+n) may go to negative& To circumvent this, we keep adding n until n > 0 and then just take modulo n.


# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    
# When the value of K is equal to N, the value of the array will remain the same after N rotations
# n%k is the number of times the rotation has actually to take place

    for _ in range(queries):
        print(a[m-1] if)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()

    n = int(nkq[0]) # n - number of elements in the integer array

    k = int(nkq[1]) # k - rotation count

    q = int(nkq[2]) # q - number of queries

    a = list(map(int, input().rstrip().split())) # initial integer array

    queries = []

    for _ in range(q):
        queries_item = int(input()) # the index of the element to return from array a
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
