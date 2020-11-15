#!/bin/python3

# Complete the hurdleRace function below.
def hurdleRace(k, height):

    return (max(height) - k) if k < max(height) else 0

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
