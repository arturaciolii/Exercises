hour = float(input('Type how many do you gain per hour: '))
time = float(input('Type how many hours do you work per month: '))
sal = hour * time
ir = 0
if sal <= 900:
    ir = 0
elif 900 < sal <= 1500:
    ir = 0.05
elif 1500 < sal <= 2500:
    ir = 0.1
elif sal > 2500:
    ir = 0.2
print(ir)
print('Brute salary: R$', sal,
      '\nIr: R$',sal*ir,
                  '\nInss: R$ ',(sal*0.1),
                  '\nFGTS: R$', (sal*0.11),
                  '\nTotal discount: R$', (sal*float(ir)+(sal*0.1)),
                  '\nLiquid Salary: R$ ', (sal-(sal*float(ir)+(sal*0.1))))

