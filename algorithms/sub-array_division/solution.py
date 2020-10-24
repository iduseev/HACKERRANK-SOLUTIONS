#!/bin/python3

# Complete the birthday function below.
def birthday(squares, d, m):
    ways = 0 # initialize number of ways to divide chocolate bar

    for i in range(0, n - m + 1):   # num of  sliding windows to slide through  squares is related with num of 
                                    # chocolate bar pieces ('month') as n - m + 1
                                    
        if sum(s[i : m + i]) == d:  # we slice the list to sliding windows using for/in loop
            ways += 1               # if sum of elements in particular sliding window equals to 'days', we increment 'ways' variable

    return ways 

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    print(result)
    
    # fptr.write(str(result) + '\n')

    # fptr.close()
