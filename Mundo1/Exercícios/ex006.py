import gtts

print('==== Sistema de cálculo de dobro, triplo e raíz quadrada ====')

num = int(input('Digite seu número: '))

dob = num * 2
tri = num * 3
raiz = num ** (1/2)

print('Seu dobro é {}, Seu triplo é {}, Sua raiz quadrada é {:.0f}'.format(dob,tri,raiz))