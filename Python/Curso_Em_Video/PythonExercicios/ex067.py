'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo
'''
while True:
    print('-' * 10)
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 10)
    if num < 0:
        break
    x = 1
    while x <= 10:
        print(f'{num} x {x} = {num * x}')
        x += 1
print('PROGRAMA TABUADA ENCERRADO!')
