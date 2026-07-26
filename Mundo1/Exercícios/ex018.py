from math import sin, cos, tan, radians
print('|==== Sistema de cálculo de Sen Cos Tg ====|')
num = float(input('Digite um ângulo: '))

print(f'\nÂngulo escolhido: {num}º\nSeno de {num}º: {sin(num):.2f}\nCosseno de {num}º: {cos(num):.2f}\nTangente de {num}º: {tan(radians(num)):.2f}')