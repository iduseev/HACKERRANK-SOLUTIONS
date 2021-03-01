#!/bin/python3

#
# Complete the 'taumBday' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER b - number of black gifts to present
#  2. INTEGER w - number of white gifts to present
#  3. INTEGER bc - price for one black gift
#  4. INTEGER wc - price for one white gift
#  5. INTEGER z - price to convert black gift to white and vice versa 
#

def taumBday(b, w, bc, wc, z):
    
    b_total = b * bc
    w_total = w * wc 
    b_to_w = w * (bc + z) # price of converting required number of black gifts to white
    w_to_b = b * (wc + z) # price of converting required number of white gifts to black

    return min(b_total + w_total, b_total + b_to_w, w_total + w_to_b)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        b = int(first_multiple_input[0])

        w = int(first_multiple_input[1])

        second_multiple_input = input().rstrip().split()

        bc = int(second_multiple_input[0])

        wc = int(second_multiple_input[1])

        z = int(second_multiple_input[2])

        result = taumBday(b, w, bc, wc, z)

        print(result)

        # fptr.write(str(result) + '\n')

    # fptr.close()
