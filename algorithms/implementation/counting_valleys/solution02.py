#!/bin/python3

def countingValleys(steps, path):

    valley = level = 0

    d = {'U':1, 'D':-1} # dictionary with corresponding step value based on step direction

    for step in path:
        level += d[step]     # alters 'level' value based on 'step' value (either 'U' or 'D')
        if level == 0 and step == 'U': # checks two conditions to be met for valley detection
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
