

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):

    i = 0 # initial index
    jump = 0 # count number of jumps

    while i < n - 1: # use n-1 because we ought to red last value in the array 
    # and it shouldn't not exceed n until we increment i

        if i + 2 < n and c[i + 2] == 0: # first check if i + 2 doesn't exceed the range and then the value of c[i+2]
            jump += 1 # increment jump
            i += 2 # increment i to check next i every time we made a jump
            
        elif c[i + 1] == 0: # no need to check if i + 1 < n because it already considered in while loop
            jump += 1
            i += 1

    return jump


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    print("Executing main function")

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print (result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
