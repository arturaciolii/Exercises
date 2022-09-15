a = input('Did you call the victim? (y/n)')
b = 0
if a == 'y':
    b += 1
a = input('Where you on the crime scene? (y/n)')
if a == 'y':
    b += 1
a = input('Do you live close to the victim? (y/n)')
if a == 'y':
    b += 1
a = input('Did you own the victim? (y/n)')
if a == 'y':
    b += 1
a = input('Did you ever work with the victim? (y/n)')
if a == 'y':
    b += 1
if b == 2:
    print('suspect')
elif b == 3 or b == 4:
    print('accomplice')
elif b == 5:
    print('murderer')
else:
    print('innocent')



