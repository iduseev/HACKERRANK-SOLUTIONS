#!/bin/python3

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    
    n = (x1 - x2) / (v2 - v1) # n is a number of jumps which has to be the same for both kanagroos

    if v2 < v1 and n == int(n):
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
