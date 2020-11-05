#!/bin/python3

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):










if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        print(result)

        # fptr.write(result + '\n')

    # fptr.close()
