#!/bin/python3

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):

# according to condition that "the absolute diff is less or equal to 1", we choose either:
# 1. Integers with identical values (abs diff == 0)
# 2. Consecutive integers (abs diff == 1)
# Create frequency array and write num of occurences of each integer in that array into corresponding index of that integer 
# Then we iterate through frequency array to find the max sum of numbers of occurences between adjacent elements
# Each time we sum up only two frequencies of adjacent elements because the difference between integers should be <= 1 
# so no need to compare the third element appearance frequancy

    freq = [0]*100 # initialize array with maximum of 100 zero elements because n<= 100 according to condition

    for num in a:
        freq[num] += 1

    maxsum = 0

    for i in range(1,100):
        maxsum = max(maxsum, freq[i-1]+ freq[i]) # sum up every two adjacent elements starting with index 0 
                                                 # write maximum sum of occurences in variable 'maxsum'
    return maxsum

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()

#   The idea and a part of code is contributed by @alessandrobardini at GitHub