print('''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
A média de idade do grupo.
Qual é o nome do homem mais velho.
Quantas mulheres têm menos de 20 anos.
''')
soma = 0
idadeMaior = 0
nomeMaisVelho = ''
cont = 0
for x in range(1, 5):
    print('----- {}ª PESSOA -----'.format(x))
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [ F ][ M ]: ')).strip().upper()
    soma += idade
    if x == 1 and sexo == 'M': #se for o primeiro laço
        idadeMaior = idade
        nomeMaisVelho = nome
    if sexo == 'M' and idade > idadeMaior:
        idadeMaior = idade
        nomeMaisVelho = nome
    if sexo == 'F' and idade < 20:
        cont += 1
media = soma / 4
print('A média de idade do grupo é {:.2f} anos'.format(media))
print('{} é o homem mais velho com {} anos'.format(nomeMaisVelho, idadeMaior))
print('{} mulher(es) têm menos de 20 anos'.format(cont))

