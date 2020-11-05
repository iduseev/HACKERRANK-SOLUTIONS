#!/bin/python3

def pageCount(n, p):

    front = p//2

    back = (n-p) // 2 if n % 2 == 1 else (n-p+1) // 2

    return min(front, back)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
