#!/bin/python3

# Complete the permutationEquation function below.
def permutationEquation(p):

    y = [] # initialize variables
# for in loop ranging from 1 and end with n+1 because task uses shifted indexes
# e.x. as per problem, 5 in list p = [4,3,5,1,2] is at 'index' 3 and 4 is at 'index' 1
    for i in range(1, n + 1): # therefore iterate from 1 to n + 1
        y.append(p.index(p.index(i) + 1) + 1) # add up 1 twice in formula because of that shifted 'indexing' system

    return y

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    print(result)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
