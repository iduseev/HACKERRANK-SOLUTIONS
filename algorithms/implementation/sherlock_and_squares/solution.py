#!/bin/python3
import math

# Complete the squares function below.
def squares(a, b):

# as naive brutal force approach to iterate through entire range and check if square root from every number is an integer leads to TLE

# we can take left and right edges (a and b, respectively) 

# for right edge (b) take the square root and floor it down so we got the integer 'right_edge' which is in range ((sqrt(a), sqrt(b))
# which means that square of this number is in range (a, b)

# for left edge we ceil up sqrt(a) and get the integer 'left_edge' the same way

# difference of these two integers results to a number of integers which lie in a range ((sqrt(a), sqrt(b))
# therefore their squares definately lie in a range (a, b)

    left_edge = math.ceil(math.sqrt(a))
    right_edge = math.floor(math.sqrt(b))

    return (right_edge - left_edge + 1)
    
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        print(result)

        # fptr.write(str(result) + '\n')

    # fptr.close()
