a = float(input('how many in square meter will you paint? '))
l = a/6
c=numc=g=numg=0
while c<l:
    c = c +18
    numc = numc+1
price = numc*80
while g<l:
    g = g +3.6
    numg = numg+1
priceg = numg*25
print('if you only buy cans: ')
print('The number of cans you will have to buy is', numc)
print('The total price of cans is R$',price)
print('if you only buy gallons: ')
print('The number of gallons you will have to buy is', numg)
print('The total price of gallons is R$',priceg)