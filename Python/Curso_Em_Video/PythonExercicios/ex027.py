print('''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente''')

nome = str(input('Digite seu nome completo: ')).strip()
nomeDividido = nome.split()
qtdNomes = len(nomeDividido)
print('Primeiro: {}'.format(nomeDividido[0]))
print('Último: {}'.format(nomeDividido[qtdNomes - 1]))
