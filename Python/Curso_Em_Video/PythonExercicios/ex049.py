print('''Refaça o desafio 009. mostrando a tabuada de um número que o usuário escolher
''')
num = int(input('Digite um valor: '))
print('TABUADA DE {}'.format(num))
for c in range(0, 11):
    print('{} x {:2} = {}'.format(num, c, c*num))

