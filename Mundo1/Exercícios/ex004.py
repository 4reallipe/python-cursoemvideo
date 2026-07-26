print('==== Sistema de verificação de informações sobre texto inserido ====')

n = input('Digite algo: ')

print(f'É numérico? {n.isnumeric()}.')
print(f'É alfanumérico? {n.isalnum()}.')
print(f'É printable? {n.isprintable()}')