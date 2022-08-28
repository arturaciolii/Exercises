sal = int(input('Type your salary: '))
if sal <= 280:
    rais = sal*0.20
    nsal = sal + rais
    print('The old salary is: ', sal,
          '\nThe percentage of raise is: 20%',
          '\nThe value of the raise is: ', rais,
          '\nThe raised salary is: ', nsal)
if 280 <= sal <= 700:
    rais = sal*0.15
    nsal = sal + rais
    print('The old salary is: ', sal,
          '\nThe percentage of raise is: 15%',
          '\nThe value of the raise is: ', rais,
          '\nThe raised salary is: ', nsal)
if 700 <= sal <= 1500:
    rais = sal*0.10
    nsal = sal + rais
    print('The old salary is: ', sal,
          '\nThe percentage of raise is: 10%',
          '\nThe value of the raise is: ', rais,
          '\nThe raised salary is: ', nsal)
if sal > 1500:
    rais = sal*0.05
    nsal = sal + rais
    print('The old salary is: ', sal,
                  '\nThe percentage of raise is: 5%',
                  '\nThe value of the raise is: ', rais,
                  '\nThe raised salary is: ', nsal)
