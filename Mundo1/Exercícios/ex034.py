salario = float(input('Digite seu salário: '))

if salario<=1250:
    print(f'Seu novo salário é de {salario+(salario*0.15):.2F}')
else:
    print(f'Seu novo salário é de {salario + (salario * 0.10):.2F}')