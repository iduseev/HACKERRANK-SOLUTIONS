#!/bin/python3

# Complete the acmTeam function below.
def acmTeam(topics):

    max_subjects = 0 # initialize variables
    team_counter = 0

    for i in range(n):                          # given 'i', iterate through the range (i+1, n) to get access to the next list of topics
        for j in range(i + 1, n):
            subjects = 0                            # after each loop empty 'subjects' variable for each team of 2 persons

            for x, y in zip(topics[i], topics[j]):  # iterate through every element for first person and every next person at the same
                                                    # time; each person's known topics are stored as a string in 'topics' list 
                if x == '1' or y == '1':            # either one of elements equals to 1, team's known subjects number is incremented
                    subjects += 1
                
            if subjects > max_subjects:             # once we find a team which knows more subjects than the best from previous teams,
                max_subjects = subjects             # max_subjects is updated by greater new value of known subjects
                team_counter = 1                    # and there is only one new best team then 

            elif subjects == max_subjects:          # if any team knows equal subjects as the current leading team does
                team_counter += 1                   # number of the best teams is incremented

    return (max_subjects, team_counter)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topics = []

    for _ in range(n):
        topic = input()
        topics.append(topic)

    result = acmTeam(topics)

    print(result)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()