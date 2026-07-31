from random import randint
from time import sleep


computador = randint(0, 6)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5, tente acertar...')
print('-=-'*20)
usuario = int(input('Em que número eu pensei? '))

print('Processando...')

sleep(2)

if usuario == computador:
    print('PARABÉNS! Você ganhou...')
    print(f'\nNúmero escolhido por você: {usuario}\nNúmero escolhido pela máquina: {computador}')
else:
    print('GANHEI! Você perdeu...')
    print(f'Número escolhido por você: {usuario}')
    print(f'Número escolhido pela máquina: {computador}')