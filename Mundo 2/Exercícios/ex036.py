print('-=-'*25)
valor = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do quanto recebe de salário: '))
anos = float(input('Digite a quantidade de anos que pretende parcelar: '))
prestacao = valor/anos
print('-=-'*25)
if prestacao>(salario*0.30)
    print('Empréstimo negado. Prestações excedem 30% do salário.')
else:
    print('Empréstimo aprovado! Tenha um Bom Dia!!')
print(f''' 
    valor da casa: {valor:.2f}\n
    Prestação: {prestacao:.2f}\n
    Anos pagando: {anos:.1f}
''')