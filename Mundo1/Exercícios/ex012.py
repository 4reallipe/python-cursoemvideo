print('==== Sistema de cálculo de desconto ====')

preco = float(input('Digite o preço: '))

print(f'Valor sem desconto: {preco:.2f}R$\nValor com desconto: {preco-(preco*0.05):.2f}R$')