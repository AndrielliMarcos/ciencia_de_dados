# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado

dias = int(input('Quantidade de dias alugado: '))
km = float(input('Quantidade de km percorrido: '))
valorDia = dias * 60
valorKm = km * 0.15
print('O valor total do aluguel para um carro que ficou alugado durante {} dia(s) e percorreu {}km é de R$ {:.2f}'.format(dias, km, (valorDia + valorKm)))

