'''
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER.
Mostrando o total de vitórias consecutivas que ele conquistou no final do jogo
'''
from random import randint
print('-=-'*10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=-'*10)
cont = 0
while True:
    computador = randint(0, 10)
    usuario = int(input('Diga um valor: '))
    tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    soma = computador + usuario
    tipoSoma = ''
    if soma % 2 == 0:
        tipoSoma = 'PAR'
    else:
        tipoSoma = 'ÍMPAR'
    print('-'*20)
    print(f'Você jogou {usuario} e o computador {computador}. Total de {soma} DEU {tipoSoma}')
    print('-'*20)
    if tipo == 'P' and tipoSoma == 'PAR' or tipo == 'I' and tipoSoma == 'ÍMPAR':
        print('Você VENCEU! \n Vamos jogar novamente...')
        print('-=-' * 10)
        cont += 1
    else:
        print('Você PERDEU!')
        break
print('-=-'*10)
print(f'GAME OVER! Você venceu {cont} vez(es)')
