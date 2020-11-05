#!/bin/python3

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):

    level = valley = 0 # initialize variables
    
    for step in path:   # iterate through path
        if step == 'U': # for each 'U' in path increment 'level' value
            level += 1
        
        else:           # else if step == 'D'

            if level != 0: # if level != 0 then we are either on mountain or valley, not on sea level
                level -= 1

            else:          # if level == 0, we are at the sea level then, and as step == 'D', two conditions are met
                           # valley start detected 
                level -= 1
                valley += 1
    
    return valley

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
