print('=-='*20)
print('Cálculo de Reajuste Salárial')
print('=-='*20)

salario = float(input('Digite seu atual salário: '))

if salario<=1250:
    print(f'Seu novo salário é de {salario+(salario*0.15):.2F}')
else:
    print(f'Seu novo salário é de {salario + (salario * 0.10):.2F}')
print('=-='*20)