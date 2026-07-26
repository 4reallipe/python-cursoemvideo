print('==== Sistema de cálculo de reajuste salarial ====')

salario = float(input('Digite seu salário: R$'))

print(f'Seu salário sem ajuste: {salario:.2f}R$\nSeu salário com ajuste: {salario+(salario*0.15):.2f}R$')