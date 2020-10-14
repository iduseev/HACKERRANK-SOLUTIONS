#!/bin/python3

def countApplesAndOranges(s, t, a, b, apples, oranges):

    house = [i for i in range(s,t+1)] # initialize house list containing integers from s to t inclusively

    apple_count = 0                   # initialize counters for oranges and apples
    orange_count = 0

    for index in range((len(apples))):
        if ((apples[index]) + a) in house:
            apple_count += 1
    print(apple_count)
    
    for index in range((len(oranges))):
        if ((oranges[index]) + b) in house:
            orange_count += 1
    print(orange_count)

    # for index, orange in enumerate(oranges):
    #     print(index, orange)
    #     if (orange + b) in house:
    #         orange_count += 1
    #         print(orange_count)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
