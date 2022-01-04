'''
Crie um programa que leia o nome e o preço  de vários produtos. O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
Qual é o total gasto na compra.
Quantos produtos custam mais de R$1000.00
Qual é o nome do produto mais barato.
'''
print('-'*30)
print('SUPER BARATÃO')
print('-'*30)
soma = contMil = cont = menor = 0
menorProd = ''
while True:
    prod = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$ '))
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    cont += 1
    soma += preco
    if preco > 1000.00:
        contMil += 1
    if cont == 1:
        menor = preco
        menorProd = prod
    else:
        if preco < menor:
            menor = preco
            menorProd = prod
    while continua not in 'SsNn':
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break
print('----- FIM DO PROGRAMA -----')
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {contMil} produto(s) custando mais de R$1000,00')
print(f'O produto mais barato foi {menorProd} que custa R${menor:.2f}')
