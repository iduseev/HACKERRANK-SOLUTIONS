#!/bin/python3


# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    
    bill.pop(k)

    res = sum(bill)/2

    if res == b:
        print ('Bon Appetit')
    else:
        print (int(b - res))

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
