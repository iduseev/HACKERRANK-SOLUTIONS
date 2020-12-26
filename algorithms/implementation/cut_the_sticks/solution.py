#!/bin/python3

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    
    ''' I faced a problem that I literally don't need to return any value here in this problem. Not even 'None' return value
allowed because it is not accepted by Hackerrank. 
Meanwhile, I dodn't want to use 'raise-except' here in code to avoid any errors. 
Therefore I decided just to use the code w/o defining a function (hence, w/o return value) and paste it on Hackerrank.'''

    while arr: # arr is always overridden so while it exists, loop continues
        print(len(arr)) # we print current length of arr for solution
        smallest_stick = min(arr) # define the smallest stick length in current array 
    
    # use list comprehension to create and override an array 'arr' with elements composed of difference between 
    # each element and the smallest element of the array, but only if the resulting element is not equal to 0
        arr = [stick - smallest_stick for stick in arr if (stick - smallest_stick) != 0]
    
    return None
    
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    print(result)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
