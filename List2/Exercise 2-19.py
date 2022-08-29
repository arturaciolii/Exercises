num = int(input('type a number lower than 1000: '))
if num > 1000:
    print('invalid number')
else:
    units = num%10
    tens = ((num - units)%100)
    hundreds = (num - units - tens)%1000
    print('units: ',units)
    print('tens: ',int((tens/10)))
    print('hundreds: ',int((hundreds/100)))