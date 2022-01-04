print('''Crie um programa que leia o nome completo de uma pessoa.
O nome com todas as letras minúsculas.
O nome com todas as letras maiúsculas.
Quantas letras ao todo sem considerar os espaços.
Quantas letras tem o primeiro nome
''')
nome = str(input('Digite seu nome completo: ')).strip()
print('Maiúsculas: {}'.format(nome.upper()))
print('Minusculas: {}'.format(nome.lower()))

nomeDividido = nome.split()
'''qtdNomes = len(nomeDividido)
qtdLetras = 0
for x in range(qtdNomes):
    qtdLetras += len(nomeDividido[x])
print('Total de letras no nome {}: {}'.format(nome, qtdLetras))'''
print('Total de letras no nome {}: {}'.format(nome, len(nome) - nome.count(' ')))
print('Total de letras do primeiro nome: {}'.format(len(nomeDividido[0])))
