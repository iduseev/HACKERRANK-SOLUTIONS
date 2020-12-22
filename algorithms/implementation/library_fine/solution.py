#!/bin/python3

# Complete the libraryFine function below.
def libraryFine(d1, m1, y1, d2, m2, y2):

# First consider the case when book brought back next year(s) after it was due to, return fine 10000 
    if y1 > y2: return 10000 
        
    elif y1 < y2: return 0 # if book was brought back year(s) earlier than it was due to > return fine = 0, nothing to do here 

    else: # if book was brought back the same year: see further
        
        if m1 > m2: return 500 * (m1 - m2) # if book was brought back next mpnth(s) > return fine as per rules 
            
        elif m1 < m2: return 0 # if book was brought back month(s) earlier, no fine applied

        else: # if book was brought back the same month, check days
        
            if d1 <= d2: return 0 # if book was brought back day(s) earlier or the day it was due to > return fine = 0

            else: return 15 * (d1 - d2) # if book was brought back day(s) later, return fine as per rules

        

        







if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    d1M1Y1 = input().split()

    d1 = int(d1M1Y1[0])

    m1 = int(d1M1Y1[1])

    y1 = int(d1M1Y1[2])

    d2M2Y2 = input().split()

    d2 = int(d2M2Y2[0])

    m2 = int(d2M2Y2[1])

    y2 = int(d2M2Y2[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
