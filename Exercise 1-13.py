h = float(input('Type your height in meters'))
g = input('are you a man or woman?')
if g == "man":
    w = (72.7*h) - 58
    print('your ideal weight is ',w)
else:
    w = (62.1 * h) - 44.7
    print('your ideal weight is ', w)