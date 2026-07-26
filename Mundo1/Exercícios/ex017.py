from math import hypot
print('==== Sistema de cálculo da hipotenusa ====')

a = float(input('Digite o valor do cateto adjascente: '))
b = float(input('Digite o valor do cateto oposto: '))

print(f'\nCateto adjascente: {a}\nCateto Oposto: {b}\nHipotenusa: {hypot(a,b):.2f}')