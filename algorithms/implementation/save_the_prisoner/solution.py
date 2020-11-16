#!/bin/python3


# Complete the saveThePrisoner function below.
def saveThePrisoner(prisoners, candy, start):

    result = (candy + start - 1) % prisoners # the number of prisoner getting last candy is the same as the remainder from division 
                                # of candy to number of prisomers as it means that every prisoner will get one candy (full cycle)
                                # and then the remainder will be distributed between rest of prisoners from 1 to  
        # Delta = start - 1 because we sum up result with difference between given starting point and default starting point (1)                                                         

    
    return result if result != 0 else prisoners # in case if remainder equals to 0 >> each prisoner gets one candy 
                                                              # so last one is given to last prisoner
    # if remainder is not equal to 0 then we return result of modulo with starting prisoner's number considered

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        pcs = input().split()

        prisoners = int(pcs[0])

        candy = int(pcs[1])

        start = int(pcs[2])

        result = saveThePrisoner(prisoners, candy, start)

        print(result)

        # fptr.write(str(result) + '\n')

    # fptr.close()
