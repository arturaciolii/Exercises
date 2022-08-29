a = int(input('type a number: '))
b = int(input('type a number: '))
option = input('choose an option (+,-,*,/) ')
result = 0
if option == '+':
    result = a+b
elif option == '-':
    result = a-b
elif option == '*':
    result = a*b
elif option == '/':
    result = a/b
print('Result= ', result)
if (result%2) == 0:
    print('1- the number is even')
else:
    print('1- The number is odd')
if result>0:
    print('2- The number is positive')
else:
    print('2- The number is negative')
if result == round(result):
    print('3- the number is integer')
else:
    print('3- The number is decimal')
