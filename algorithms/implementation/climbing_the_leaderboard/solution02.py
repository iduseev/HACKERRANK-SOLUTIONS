#!/bin/python3

# this solution fails runtime in Hackerrank and returns unintended '1' in scores[1] index

def climbingLeaderboard(ranked, player):
    
    d = {}

    d[1] = ranked[0]  # assign the best result the 1st place

    r = list(sorted(set(ranked), reverse = True))   # set() eliminates duplicates, sorted() sorts in descending order,
                                                    # list() concatenates it back to list (iterable object) 
    for i in range(len(r)): # assign places according to 
        # if r[i] < ranked[0]:
        d[i+1] = r[i]
               
    l = list(d.values())    # list from dictionary values
    scores = []

    for i in range(m):
        j = 0
        if player[i] < r[-1]: # check if player's score is less than last(smallest) score in 'ranked'
            d[(len(r)+1)] = player[i]   # append least player score to dictionary d as value with last place as key
                                        # len(r) is last because it is greater than last index of r by 1
            scores.append((len(r)+1))   # append the last place in empty list 'scores'                       
        else:                             
            while player[i] < l[j]: # as player's score is greater than least score in ranked, we compare it with greatest (first) score
                j += 1              # and so on until the score becomes greater or equal than score in ranked
                
        d[j+1] = player[i]          # j+1 because the place in ranking is greater by 1 than correspodning index of the result
        scores.append(j+1)          # we can override the previous score of that place in ranked because it is not important now
                                    # as 'player's' scores come in ascending order >> they will occupy higher and higher places in ranked
    
    return scores

if __name__ == '__main__':

    n = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    print(result)