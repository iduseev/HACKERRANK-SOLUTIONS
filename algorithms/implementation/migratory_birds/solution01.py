#!/bin/python3

def migratoryBirds(arr):
    
    d = {i : arr.count(i) for i in arr}    # append {element : counter} tuples in a dict for each element in an array

    least_ele = [num for num, count in d.items() if count == max(d.values())]  # append elements to a list if they appear in d as frequent
                                                                               # as maximum counter value in the dict
                                                                               # needeed in case of several elements appear
                                                                               # with the same maximum frequency
    return min(least_ele)                                                       # return minimum number in the array

if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(result)

