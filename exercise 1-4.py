a = int(input('type your first test score: '))
b = int(input('type your second test score: '))
c = int(input('type your third test score: '))
d = int(input('type your fourth test score: '))
if 0<a<=10 and 0<b<=10 and 0<c<=10 and 0<d<=10:
    average = (a+b+c+d)/4
    print('Your average was: {}'.format(average))
else:print('You typed a wrong score')