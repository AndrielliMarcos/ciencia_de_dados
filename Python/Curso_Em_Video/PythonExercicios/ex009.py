# Faça um programa que leia um número inteiro qualquer e mostre sua tabuada

num = int(input('Digite um número: '))
print('-' * 12)
for x in range(11):
    resul = num * x
    print('{} * {:2} = {}'.format(num, x, resul))
print('-' * 12)
