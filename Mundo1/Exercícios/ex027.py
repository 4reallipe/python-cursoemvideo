nome = input('Digite seu nome completo: ')

print(f'''
    Seu nome completo: {nome}
    Primeiro nome: {nome.split()[0]}
    Último nome: {nome.title().rsplit()[-1]}
''')