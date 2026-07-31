nome = input('Digite seu nome: ')

print(f"Seu nome têm silva? {'Silva' in nome.title()}")

if(nome.title().find('Silva') != -1):
    print(f'Tem Silva no nome no caracter: {nome.title().find('Silva')}')
else:
    print('Não têm "Silva no nome."')