a = float(input('how many in square meter will you paint? '))
l = a/3
c = 0
numc = 0
while c<l:
    c = c +18
    numc = numc+1
price = numc*80

print('The number of cans you will have to buy is', numc)
print('The total price of cans is R$',price)