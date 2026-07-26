from random import sample
print('==== Sistema de sorteio de alunos ====')
alunos = 'Ana', 'Claudio', 'Gustavo', 'Felipe'

print('A ordem para apresentação é: {}', sample(alunos, 4))