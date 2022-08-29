a = int(input('type the side of the triangle'))
b = int(input('type the side of the triangle'))
c = int(input('type the side of the triangle'))
if (a+b) <= c or (a+c) <= b or (b+c) <= a:
    print('its not a triangle')
else:
    if a == b == c:
        print('the triangle is equilateral')
    elif a == b or a == c or b == c:
        print('the triangle is isosceles')
    elif a != b != c:
        print('the triangle is scalene')
