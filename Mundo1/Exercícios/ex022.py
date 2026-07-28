nome = input('Digite seu nome inteiro: ')
print(f'''
    Nome em maiúsculo: {nome.upper()}
    Nome em minúsculo: {nome.lower()}
    Total de letras: {len(nome.replace(' ', ''))}
    Quantidade de letras do primeiro nome: {len(nome.split()[0])}
''')