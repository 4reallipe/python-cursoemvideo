
print('=-='*20)
print('Digite três retas e verá se elas formam ou não um triângulo.')
print('=-='*20)

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
print('=-='*20)


if r1+r2 > r3:
    print('Pode formar um triângulo.')
else:
    print('Não pode formar um triângulo.')
print('=-='*20)