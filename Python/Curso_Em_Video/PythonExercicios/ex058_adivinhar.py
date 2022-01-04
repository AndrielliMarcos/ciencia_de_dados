print('''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi 
o número escolhido pelo computador.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer
''')
from random import randint
'''computador = randint(0, 10)
usuario = int(input('Tente adivinhar o número escolhido pelo computador entre 0 e 10: '))
cont = 1
while usuario != computador:
    usuario = int(input('Você errou! Tente adivinhar o número escolhido pelo computador: '))
    cont += 1
print('Parabéns! Você acertou o número que o computador escolheu. Para isso você precisou de {} palpites!'.format(cont))'''

computador = randint(0, 10)
print('Sou seu computador. Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
cont = 0
acertou  = False
while not acertou:
    usuario = int(input('Qual o seu palpite? '))
    cont += 1
    if usuario == computador:
        acertou = True
    else:
        if usuario < computador:
            print('Tente um número maior!')
        elif usuario > computador:
            print('Tente um número menor!')
print('Acertou com {} tentativas. Parabéns!'.format(cont))
