#!/bin/python3

# Complete the breakingRecords function below.
def breakingRecords(scores):
    best_count = 0
    worst_count = 0

    best = scores[0]
    worst = scores[0]

    for score in scores:
        if score > best:
            best = score
            best_count += 1
        elif score < worst:
            worst = score
            worst_count += 1
    return best_count, worst_count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(result)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
