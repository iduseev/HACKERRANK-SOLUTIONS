#!/bin/python3

def migratoryBirds(arr):
    
    l = [0] * len(arr)

    for i in range(len(arr)):
        
        l[arr[i]] += 1 # each fact of number appearance is written in the corresponding cell of initialized l list
                        # therefore every time the number appears in the array, its counter is incremented
                        # index(max(l)) = arr[i] =>  most frequent bird ID is index of the most 'filled out' cell in list l

    return (l.index(max(l)))

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
