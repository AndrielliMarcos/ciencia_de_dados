print('''Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
o primeiro valor é maior
o segundo valor é maior
não existe valor maior, os dois são iguais
''')
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
if n1 > n2:
    print('{} é maior {}!'.format(n1, n2))
elif n2 > n1:
    print('{} é maior que {}'.format(n2, n1))
else:
    print('Não existe valor maior, os dois são iguais.')
