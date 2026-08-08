from datetime import date

ano = int(input('Digite o ano que nasceu: '))
hoje = date.today().year

if (hoje-ano)==18:
    print('Tempo de se alistar')
elif (hoje-ano)>18:
    print(f'Passou do tempo de se alistar. Passaram-se {abs((hoje-ano)-18)} anos do seu alistamento')
else:
    print(f'Ainda vai se alistar, o que vai demorar {abs((hoje-ano)-18)} anos')