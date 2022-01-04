# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa

from math import hypot
cateto1 = float(input('Digite o valor do cateto oposto: '))
cateto2 = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = hypot(cateto1, cateto2)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
