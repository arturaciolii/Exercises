import math
a = int(input('type the coefficient a: '))
if a==0:
    print('This is not a 2 degree equation')
else:
    b = int(input('type the coefficient b: '))
    c = int(input('type the coefficient c: '))
    d = b**2 + (-4*a*c)

    if d==0:
        x1 = -b/2*a
        print(x1)
    elif d<0:
        print('the equation does not have real roots')
    else:
        x1 = (-b+math.sqrt(d)) / (2*a)
        x2 = (-b-math.sqrt(d)) / (2*a)
        print('x1= ', x1, '\nx2= ', x2)

