print('==== Sistema de aluguel de carros ====')
dia = int(input('Quantos dias o carro esteve alugado?\n'))
km = float(input('Quantos Km o carro percorreu?\n'))
preco = (dia*60)+(km*0.15)

print(f'\nKm rodados: {km}Km\nDia(s) alugado: {dia} dias\nValor à ser pago: {preco:.2f}R$')
