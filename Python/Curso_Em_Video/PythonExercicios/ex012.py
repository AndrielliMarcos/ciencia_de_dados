# Faça um algoritmo que leia o preço de um produto e mostre seu nome preço com 5% de desconto

valor = float(input('Qual o valor do produto? '))
desconto = valor - (valor * 0.05)
print('O valor deste produto sai a {:.2f} com 5% de desconto.'.format(desconto))
