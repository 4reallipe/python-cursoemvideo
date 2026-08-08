print('-=-'*15)
num = int(input('Digite um número inteiro qualquer: '))
print('-=-'*15)
print('Escolha uma base de conversão')
print('1 - Binária\n2 - Octal\n3 - Hexadecimal')
print('-=-'*15)
esc = int(input('Escolha: '))
print('-=-'*15
if esc==1:
    print(f'O número {num} em hexadecimal é {bin(num)[2:]}')
elif esc==2:
    print(f'O número {num} em hexadecimal é {(oct(num))}')
elif esc==3:
    print(f'O número {num} em hexadecimal é {hex(num)}')
else:
    print('Opção inválida.')
print('-=-'*15)