num = input('Digite um número entre 0 e 9999: ')

if(num.isnumeric() == False):
    print('Não é número.')
else:
    print(f'''
        Unidade: {num[3]}
        Dezena: {num[2]}
        Centena: {num[1]}
        Milhar: {num[0]}
    ''')