print('Digite números diferentes.\n')
x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))
z = int(input('Digite o terceiro número: '))
print('='*25)

# maior
if y < x and x > z:
    print('O maior é o primeiro.')
if x < y and y > z:
    print('O maior é o segundo.')
if x < z and z > y:
    print('O maior é o terceiro.')
# menor
if y > x and x < z:
    print('O menor é o primeiro.')
if x > y and y < z:
    print('O menor é o segundo.')
if x > z and z < y:
    print('O menor é o terceiro.')