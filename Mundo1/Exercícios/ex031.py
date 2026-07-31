distancia = float(input('Digite a distância viajada(em km): '))

print(f'Distância viajada: {distancia}Km')
if distancia>=200:
    print(f'valor a ser pago: {distancia*(45/100):.2f}R$')
else:
    print(f'valor a ser pago: {distancia*(50/100):.2f}R$')