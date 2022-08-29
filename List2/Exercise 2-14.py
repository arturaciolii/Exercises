score1 = int(input('Type your first score'))
score2 = int(input('Type your second score'))
average = (score1 + score2)/2
if 9 < average <= 10:
    concept = 'A'
elif 7.5 < average <= 9:
    concept = 'B'
elif 6 < average <= 7.5:
    concept = 'C'
elif 4 < average <= 6:
    concept = 'D'
elif 0 < average <= 4:
    concept = 'E'
if concept == 'A' or concept == 'B' or concept =='C':
    print(score1, score2)
    print(average)
    print(concept)
    print('Approved')
else:
    print(score1, score2)
    print(average)
    print(concept)
    print('Disapproved')

