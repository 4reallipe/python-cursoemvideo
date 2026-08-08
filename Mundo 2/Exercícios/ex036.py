print('-=-'*25)
valor = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o valor do quanto recebe de salário: '))
anos = int(input('Digite a quantidade de anos que pretende parcelar: '))
prestacao = valor/(anos*12)
print('-=-'*25)
if prestacao>(salario*0.30):
    print('Empréstimo negado. Prestações excedem 30% do salário.')
else:
    print('Empréstimo aprovado! Tenha um Bom Dia!!')
print(f'Valor da casa: {valor:.2f}')
print(f'Prestação: {prestacao:.2f}')
print(f'Anos pagando: {anos:.1f}')
print('-=-'*25)