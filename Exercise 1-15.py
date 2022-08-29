g = float(input('How much do you gain an hour? '))
h = float(input('How much do you work per month? '))
s = g*h
it = s*0.11
inss = s*0.08
synd = s*0.05
ls = s - it - inss - synd
print('Income : R$ ',s,'\nIncome tax : R$',it, '\nInss : R$ ',inss,'\nSyndicate: R$ ',synd,'\nSalary: R$',ls)
