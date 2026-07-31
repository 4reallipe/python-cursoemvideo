n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma vale {}, a multiplicação vale {} e a divisão é {:.3f}'.format(s, m, d), end=', ')
print('A divisão inteira é {} e a Potência é {}'. format(di, e))

# nome = input('qual é seu nome? ')
# print('Prazer em te conhecer {:=^20}!'.format(nome))