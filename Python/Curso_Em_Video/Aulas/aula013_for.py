# range(inicio, fim, iteração)
'''
for c in range(1, 6): # VAI FAZER DE 1 ATÉ 5, E NO 6 O PROGRAMA IRÁ PARAR. pOR ISSO O 6 NÃO ENTRA NA CONTAGEM
    print('Oi')
print('FIM')

for c in range(0, 6): # CONTAGEM DE 0 ATÉ 5
    print(c)
print('FIM')


for c in range(6, 0, -1): # CONTAGEM DE 6 ATÉ 1
    print(c)
print('FIM')


for c in range(0, 7, 2): # CONTAGEM DE 0 ATÉ 6, CONTANDO DE 2 EM 2
    print(c)
print('FIM')


n = int(input('Digite um número: '))
for c in range(0, n): # CONTAGEM DE 0 ATÉ O NÚMERO DIGITADO-1
    print(c)
print('FIM')


# Faça um programa que faça uma contagem.
# Ele deve pedir o usuário o início da contagem, o fim e de quanto em quanto.
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
for c in range(inicio, fim+1, passo):
    print(c)
print('FIM')


for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('FIM')
'''

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n # s = s + n
print('O somatório de todos os valores foi {}.'.format(s))
