#!/bin/python3

# Complete the repeatedString function below.
def repeatedString(s, n):

    count_a = 0

    s_len = len(s)
    
    x = n // s_len # s is no of times s entirely appears in repeated string 

    r = n % s_len # r is a remainder to reveal how many first letters of s to be considered for search of 'a'

    for i in s: # count num of 'a' appearance in s
        if i == 'a':
            count_a += 1

    count_a *= x # if x > 1 then appearances of 'a' in repeated string are x times greater than those in s 

    for i in range(int(r)):
        if s[i] == 'a':
            count_a += 1

    return count_a

if __name__ == '__main__':

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
