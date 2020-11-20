#!/bin/python3

# Complete the findDigits function below.
def findDigits(n):

    div = 0 # initialize variable div to count divisors

    nlist = [int(num) for num in str(n)] # concatenate list of integers made of n 
    
    for i in nlist: # iterate through each element
        if i != 0 and n % i == 0: # check if element != 0 not to divide by zero and check if n evenly divides by i
            div += 1               # increment div
        
    return div

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        print(result)

        # fptr.write(str(result) + '\n')

    # fptr.close()
