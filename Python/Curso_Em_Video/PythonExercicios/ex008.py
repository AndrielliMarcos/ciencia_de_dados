# Escreva um programa que leia um valor em metros e o exiba convertendo em centimetros e em milimetros

metros = float(input('Digite um valor em metros: '))
cent = metros * 100
mm = metros * 1000
print('Valor digitado: {}\n Valor correspondente em centímetros: {:.0f}cm\n Valor correspondente em milímetros: {:.0f}mm'.format(metros, cent, mm))
