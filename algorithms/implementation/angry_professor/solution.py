#!/bin/python3

# Complete the angryProfessor function below.
def angryProfessor(k, a):

    for i in range(t):
        on_time = [i for i in a if i <= 0] # iterate through array a and add non-positive integers to list 'on_time'

        return 'YES' if len(on_time) < k else 'NO' # return YES if No of students came on time (<=0) less than desired No of students k

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        print(result)

        # fptr.write(result + '\n')

    # fptr.close()
