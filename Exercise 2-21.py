value = int(input('how much do you want to withdraw? '))
units = value % 10
tens = ((value - units) % 100)
hundreds = (value - units - tens) % 1000
fives = 0
ones = 0
tensd = 0
fifties = 0
hundreddb = 0
if units < 5:
    ones = units - tens
if 5 <= units < 10:
    fives = fives + 1
    ones = units -5
if 10 <= tens < 50:
    tensdb = tens / 10
if 50 <= tens <100:
    fifties = fifties + 1
    tensdb = (tens -50)/10
if hundreds>100:
    hundreddb = hundreddb + (hundreds / 100)

print('ones: ', ones)
print('fives: ', fives)
print('tens: ', int(tensdb))
print('fifties: ', fifties)
print('hudreds: ', int(hundreddb))