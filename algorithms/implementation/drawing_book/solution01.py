#!/bin/python3

def pageCount(n, p):

    return min (p//2, (n//2 - p//2)) # choose min from either turning page from book beginning or  

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
