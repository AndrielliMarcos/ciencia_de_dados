print('''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma memsagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
''')

km = float(input('Digite a velocidade do seu veículo em km/h: '))
if km > 80:
    multa = (km - 80) * 7
    # print(multa)
    print('Você excedeu o limite de velociade e terá que pagar uma multa no valor de R$ {:.2f}'.format(multa))
print('------FIM-------')
