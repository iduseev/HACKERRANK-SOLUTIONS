#!/bin/python3


# Complete the utopianTree function below.

def utopianTree(n):

    h = 0 

    # for i in range(n):
        
    if n == 0: 
        h = 1

    elif n%2 == 0: 
        h = 2 ** ((n//2)+1) - 1
        

    else:
        h = 2 ** (((n+1)//2)+1) - 2
        

    return int(h)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        print(result)

        # fptr.write(str(result) + '\n')

    # fptr.close()

# idea by @abhinav354