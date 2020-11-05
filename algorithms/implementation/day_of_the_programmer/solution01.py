#!/bin/python3

import calendar


def number_of_days(year, month):    # define function to return number of days in month according to Gregorian calendar
    return calendar.monthrange(year, month)[1]

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):

    month_num = {month: index for index, month in enumerate(calendar.month_abbr) if month} # temp dict with month numbers and month names

    d = {month:number_of_days(year,index) for month, index in month_num.items()} # temp dict to store month abbreviation and No of days in month 

# consider shift to Gregorian calendar in 1918 year (changed number of days in Feb) and leap years before 1918 (Julian calendar usage)
# replace number of days in Feb correspondingly

    if year < 1918 and year % 4 == 0: 
        d['Feb'] = 29
    elif year == 1918:
        d['Feb'] = 15
    elif year < 1918 and year % 4 != 0:
        d['Feb'] = 28

# substract No of days in each month from 256 (Day of P) till result will be less than No of days in the shortest month (28 in Feb) 
    PDay = 256
    month_count = 1
     
    for days in d.values():
        if PDay > 28:
            PDay -= days
            month_count += 1

    return (str(PDay) + "." + '{:02}'.format(month_count) + "." + str(year))

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
