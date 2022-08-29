s1 = int(input('type your first score'))
s2 = int(input('type your second score'))
s3 = int(input('type your third score'))
average = (s1 + s2 +s3)/3
if average==10:
    print('approved with distinction')
elif average>=7:
    print('approved')
elif average<7:
    print('disapproved')