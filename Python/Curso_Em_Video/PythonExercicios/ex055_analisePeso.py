print('''
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
''')
maior = 0
menor = 0
for x in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(x)))
    if x == 1: # se for o primeiro laço
        maior = peso
        menor = peso
    else:
        if peso >= maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi {:.1f}Kg'.format(maior))
print('O menor peso foi {:.1f}Kg'.format(menor))
