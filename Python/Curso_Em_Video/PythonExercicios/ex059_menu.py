'''
Crie um programa que leia dois valores e mostre um menu na tela:
[1]somar
[2]multiplicar
[3]maior
[4]novos números
[5]sair
Seu programa deverá realizar a operação solicitada em cada caso
'''
from time import sleep
num1 = float(input('Digite um valor: '))
num2 = float(input('Digite outro valor: '))
print('''Operações:
[ 1 ]Somar
[ 2 ]Multiplicar
[ 3 ]Maior
[ 4 ]Novos números
[ 5 ]Sair
''')
operacao = int(input('Escolha uma das opções acima: '))
while operacao != 5:
    if operacao == 1:
        print('SOMA: {} + {} = {}'.format(num1, num2, num1 + num2))
        operacao = int(input('Agora escolha uma das opções acima: '))
    elif operacao == 2:
        print('MULTIPLICAÇÃO: {} x {} = {}'.format(num1, num2, num1 * num2))
        operacao = int(input('Agora escolha uma das opções acima: '))
    elif operacao == 3:
        if num1 > num2:
            print('{} é maior que {}'.format(num1, num2))
        elif num2 > num1:
            print('{} é maior que {}'.format(num2, num1))
        else:
            print('{} é igual a {}'.format(num1, num2))
        operacao = int(input('Agora escolha uma das opções acima: '))
    elif operacao == 4:
        print('Escolha novos numeros: ')
        num1 = float(input('Novo valor: '))
        num2 = float(input('Mais um novo valor: '))
        operacao = int(input('Agora escolha uma das opções acima: '))
    elif operacao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Tente novamente.')
    print('=-='*10)
    sleep(2)
print('----- FIM DO PROGRAMA -----')
