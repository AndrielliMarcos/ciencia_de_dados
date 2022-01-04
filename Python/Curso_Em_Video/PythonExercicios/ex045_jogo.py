print('''Crie um programa que faça o computador jogar Jokenpô com você.
''')
from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')
jogador = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('\033[1;32mEMPATE')
    elif jogador == 1:
        print('\033[1;33mJOGADOR VENCE')
    elif jogador == 2:
        print('\033[1;35mCOMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('\033[1;33mJOGADOR VENCE')
    elif jogador == 1:
        print('\033[1;32mEMPATE')
    elif jogador == 2:
        print('\033[1;35mCOMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2: # computador jogou tesoura
    if jogador == 0:
        print('\033[1;33mJOGADOR VENCE')
    elif jogador == 1:
        print('\033[1;35mCOMPUTADOR VENCE')
    elif jogador == 2:
        print('\033[1;32mEMPATE')
    else:
        print('JOGADA INVÁLIDA')





