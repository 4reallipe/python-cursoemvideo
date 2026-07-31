vel = float(input('Informe a velocidade em km: '))

if(vel > 80):
    print('Você foi multado!')
    print(f'velocidade: {vel}Km/h\nVelocidade Máx. Permitida: 80Km/h')
    print(f'Multa a ser paga: {(vel-80)*7:.2f}R$')
else:
    print('Tenha um bom dia!')