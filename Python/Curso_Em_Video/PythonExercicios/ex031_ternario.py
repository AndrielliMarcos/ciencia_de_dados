print('''Desenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km
e R$0,45 para viagens mais longas
''')

km = float(input('Digite a distância da sua viagem em km: '))
'''if km <= 200:
    valor = km * 0.5
else:
    valor = km * 0.45'''
valor = km * 0.50 if km <= 200 else km * 0.45
print('O valor da sua passagem é de R$ {:.2f}'.format(valor))

