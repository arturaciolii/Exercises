m = int(input('type the month: '))
d = int(input('type the day: '))
y = int(input('type the year: '))
if d > 31 or d < 1:
    print('invalid date')
elif m > 12 or m < 1:
    print('invalid date')
else:
    print('{}/{}/{}'.format(m, d, y))
