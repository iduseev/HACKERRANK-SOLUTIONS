#!/bin/python3

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):

    p = 0 # initial position

    e = 100 #initial energy 
    
    while e != 0:           # energy will decrease until conditions are not met
        
        e -= (c[p] * 2 + 1) # energy decreases depending whether the value of c[p] is 0 or 1 
        p += k              # position increments by step k

        if p >= n:          # if position of character is greater than of equal to the number of elements in array c 
            p = p % n       # return remaining of the division
        
        if p == 0:          # if position turns into 0 after returning remaining of the division which means that p == n:
            break           # break the loop as per task

    return e                

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
