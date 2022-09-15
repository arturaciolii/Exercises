a = input('type g for gasoline or e for ethanol ')
l = float(input('How many liters? '))
p = 0
if a == 'g':
    if l <= 20:
        p = 2.5 * l - 2.5 * l * 0.03
    if l > 20:
        p = 2.5 * l - 2.5 * l * 0.05

if a == 'e':
    if l <= 20:
        p = 1.9 * l - 2.5 * l * 0.04
    if l > 20:
        p = 1.9 * l - 2.5 * l * 0.06
print(p)
