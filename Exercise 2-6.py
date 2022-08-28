a = int(input('type a number: '))
b = int(input('type a number: '))
c = int(input('type a number: '))
if a>b and a>c:
    print('the biggest number is ',a)
elif b>a and b>c:
    print('the biggest number is ', b)
else:
    print('the biggest number is ', c)