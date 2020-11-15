#!/bin/python3

import string 

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):

    alphabet_list = list(string.ascii_lowercase) # create a list with alphabetical characters with corresponding indexes

    # use list comprehension to create list of indexes of each letter in word
    # iterate through each index of a letter in word to create list of each word letter's height
    # return max value of list of heights multiplied by length of a word

    return max([h[alphabet_list.index(letter)] for letter in word]) * len(word)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
