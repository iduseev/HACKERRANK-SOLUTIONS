#!/bin/python3

# Using Recursive algorithm

def utopianTree(n):

    if n < 3:
        return n + 1

    if n % 2 == 0:
        return (utopianTree(n - 2) * 2) + 1
        
    else:
        return (utopianTree(n - 2) + 1) * 2
				

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        print(result)

        # fptr.write(str(result) + '\n')

    # fptr.close()