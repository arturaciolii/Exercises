s1 = float(input('type your first score: '))
s2 = float(input('type your second score: '))
av = (s1+s2)/2
if av==10:
    print('approved with distinction')

elif av>=7:
    print('approved')
else:
    print('failed')

