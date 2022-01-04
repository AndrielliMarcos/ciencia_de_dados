print('''
Crie um programa que mostre na tela todos os números pares entre 1 e 50
''')
for c in range(2, 51, 2):
    print(c)
print('FIM')
# a solução abaixo consome mais das máquinas, já que faz mais repetições
'''for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=' ')
print('FIM')'''
