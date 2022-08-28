a = int(input('type a number: '))
b = int(input('type a number: '))
c = int(input('type a number: '))
if a > b and a > c:
    print('the biggest number is ', a)
    if b < c:
        print('the lowest number is ', b)
    else:
        print('the lowest number is ', c)
elif b > a and b > c:
    print('the biggest number is ', b)
    if a < c:
        print('the lowest number is ', a)
    else:
        print('the lowest number is ', c)
else:
    print('the biggest number is ', c)
if a < b:
    print('the lowest number is', a)
else:
    print('the lowest number is ', b)
