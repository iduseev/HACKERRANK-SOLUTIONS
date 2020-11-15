#!/bin/python3

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):

    beauty = 0 # initialize variables

    for day in range(i, j+1): # iterate through range of days from i to j as per requirements
        if abs(day - int(str(day)[::-1])) % k == 0: # turn int day to string to access it reversed and again back to integer
                                                    # if absolute difference is divisible by k >> 
            beauty += 1                             # increment 'beauty' value

    return beauty

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
