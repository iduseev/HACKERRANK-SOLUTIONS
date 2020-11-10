#!/bin/python3

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):

    s = sum(s, []) # convert 2d matrix to 1d
    
    magic = []

    for a in range(1, 10):      # generate all 8 possible magic square matrix combinations 
        for b in range(1, 10):
            if set([a, 15-a-b, b, 5+b-a, 5, 5+a-b, 10-b, a+b-5, 10-a]) == set(range(1, 10)):
                magic.append([a, 15-a-b, b, 5+b-a, 5, 5+a-b, 10-b, a+b-5, 10-a])

    min_cost = 100              # IDK why but need to establish this variable to some big number 

    for m in magic:             # need to iterate through each magic square and compare difference between each its element
                                # with each element in matrix s to find magic square with minimal absolute sum of differences 
        diff = 0
        for i, j in zip(s, m):  # zip method allows parallel iteration
            diff += abs(i - j)  # add up absolute difference values to a variable 'diff'
        min_cost = min(min_cost, diff) # choose between minimal values
    
    return min_cost     # return a value with minimal difference between elements of s and elements of most close magic square matrix

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
