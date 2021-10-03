#!/bin/python3

#
# Complete the 'howManyGames' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER d
#  3. INTEGER m
#  4. INTEGER s

def howManyGames(p: int, d: int, m: int, s: int) -> int:
    """
    Return the number of games you can buy

    :param p int: initial price of movie 
    :param d int: amount of discount
    :param m int: minimal possible price
    :param s int: units of currency in wallet
    :return int: amount of items to be bought
    """
    price = 0  # init variables
    counter = 0

    s -= p # first film bought for initial price
    # counter += 1 
    # price = p - d  # calculate price for 2nd movie
    price = p
    print(f'currency in wallet after 1st purshase: {s}, price for 1st movie: {price}')

    while s >= 0:  # while there is money available in wallet
        if price >= m and price - d >= m:  # check if price has not already become less than minimal price for movie
            price = price - d  # movie price decrements after each purshase by d
            print(f'actual price: {price}, n of movies: {counter}, currency left: {s}')
        else:  # else if price < minimal price - use m as price for movie
            price = m
            # counter += 1  # movie was bought for minimal price
            print(f'actual price: {price}, n of movies: {counter}, currency left: {s}')
        s -= price
        counter += 1
    # movies = s // price
    return counter


# driver code
if __name__ == '__main__':

    # p, d, m, s = (20, 3, 6, 80)

    first_multiple_input = input().rstrip().split()

    p = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    m = int(first_multiple_input[2])

    s = int(first_multiple_input[3])

    answer = howManyGames(p, d, m, s)

    print(answer)
