#!/bin/python3

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    
    date = '12.09.' if (year <= 1917 and year % 4 == 0) or (year >= 1919 and (year % 4 == 0 and year % 100 != 0) or year % 400 == 0) else '26.09.' if year == 1918 else '13.09.' 

    return date + str(year)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
