print('''
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maior idade e quantas já são maiores
''')
from datetime import date
anoAtual = date.today().year
contMaior = 0
contMenor = 0
for c in range(1, 8):
    nascimento = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = anoAtual - nascimento
    if idade >= 18:
        contMaior += 1
    else:
        contMenor += 1
print('{} pessoas ainda não aingiram a maior idade.'.format(contMenor))
print('{} pessoas já atingiram a maior idade'.format(contMaior))

