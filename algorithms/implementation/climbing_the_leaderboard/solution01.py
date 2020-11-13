#!/bin/python3

# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    
    r = list(sorted(set(ranked), reverse = False))   # set() eliminates duplicates, sorted() sorts in descending order,
                                                    # list() concatenates it back to list (iterable object) 
    i = 0                                           # initialize variables and an empty list
    result = []
    k = len(r)

    for playscore in player:
        while i < k and r[i] <= playscore:      # we increment i until we find playscore which is greater or equal than ranked score 
            i += 1
        result.append(k - i + 1)                # we add up 1 because of using zero-index array 
        # we do not initializing i to 0 after each iteration because playscore is sorted in ascending order
        # in 'player' array and either is 'r'  

    return result

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    print(result)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
