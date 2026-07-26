print('======= Conversor Metros -> Centímetros e Milímetros =======')

num = float(input('Digite o valor em Metros (Max 2 casas dps da virgula): '))
cen = num * 100
mil = num * 1000

print('O valor de {} em Cm é: {}Cm'.format(num,cen))
print('O valor de {} em Mm é: {}Mm'.format(num,mil))