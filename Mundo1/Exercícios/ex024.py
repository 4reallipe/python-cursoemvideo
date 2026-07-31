cidade = input('Digite o nome da sua cidade: ')

print(f'{'Santo' in cidade.split()[0]}')
if(cidade.find('Santo') == 0):
    print('Sua cidade começa com "Santo".')
else:
    print('Não começa com "Santo".')
