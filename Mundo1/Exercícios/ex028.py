import random

b = random.randrange(0, 6)
a = int(input('Digite um número entre 0 e 5: '))

print(f'\nMáquina escolhendo número...\n\nNúmero escolhido: {a}\nNúmero escolhido pela máquina: {b}')
if a == b:
    print('Acertou')
else:
    print('errou')