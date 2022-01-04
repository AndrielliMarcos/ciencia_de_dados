# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

valor = float(input('Quantos reais você tem na carteira? R$ '))
dolar = valor / 3.27
print('Com esse valor você poderá comprar {:.2f} dolares.'.format(dolar))
