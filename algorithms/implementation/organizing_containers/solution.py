#!/bin/python3

""" Key for solution is, while swap operation, both elements are to be swapped simultaneously, not one. The 
number of balls left in the container should always remain constant. Therefore, if sum of them balls of one type
is equal to the number of the rest types of balls, swap operation is possible, otherwise impossible. """ 

# Complete the organizingContainers function below.
def organizingContainers(container):
            
    sum_columns = [sum(row[i] for row in container) for i in range(len(container[0]))] # sum up No of balls in a column 
    sum_rows = [sum(row) for row in container] # sum up No of balls in a row

    if set(sum_columns) == set(sum_rows): # if sum of balls of one type in columns is equal to number of those in rows 
        return ('Possible')
    else: 
        return ('Impossible')
        

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):

        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        print(result)

        # fptr.write(result + '\n')

    # fptr.close()
