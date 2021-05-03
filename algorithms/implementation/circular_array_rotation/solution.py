#!/bin/python3

# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    
    while k > 0: 
        # first_el = a[0]
        last_el = a[-1]
        a.insert(0, last_el)    #   insert last element to the index 1
        a.pop()
        k -= 1
    
    elements = []
    for q in queries:
        elements.append(a[q])
    return elements

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

    for r in result:
        print(r)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
