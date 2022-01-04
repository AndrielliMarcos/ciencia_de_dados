n = s = 0
while True: # looping infinito
    n = int(input('Digite um número: '))
    if n == 999:
        break # vai parar o looping infinito
    s += n
# print('A soma vale {}'.format(s))
print(f'A soma vale {s}')

# OUTRO EXEMPLO DE FSTRING
nome = 'José'
idade = '33'
print(f'{nome} tem {idade} anos.')

