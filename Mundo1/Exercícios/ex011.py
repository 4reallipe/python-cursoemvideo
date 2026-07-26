print('===== Sistema de cálculo de uso de tinta =====')

base = float(input('Digite a base em Metros: '))
altura = float(input('Digite a altura em Metros: '))

area = base * altura
qtd = float(area/2)

print(f'\nSerão necessários {qtd:.2f}L de tinta para pintar sua parede de área {area:.2f}M²')