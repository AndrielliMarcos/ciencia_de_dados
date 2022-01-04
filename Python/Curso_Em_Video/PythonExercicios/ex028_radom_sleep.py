print('''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi 
o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu
''')
import random
from time import sleep
num = random.randint(0, 5)
# print('Numero do computador: {}'.format(num))
numUsuario = int(input('Digite um número de 0 a 5: '))
print('Processando...')
sleep(3)
if numUsuario == num:
    print('Parabéns! Você acertou o número indicado pelo computador')
else:
    print('Que pena! Você não acertou o número. Você digitou {}, mas o computador pensou o número {}'.format(numUsuario, num))





