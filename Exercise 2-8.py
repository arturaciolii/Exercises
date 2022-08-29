prod1 = int(input('type the price of the first product: '))
prod2 = int(input('type the price of the second product: '))
prod3 = int(input('type the price of the third product: '))
if prod1<prod2 and prod1<prod3:
    print('You should buy the first product')
elif prod2<prod1 and prod2<prod3:
    print('you should buy the second product')
else:
    print('you should buy the third product')