print('''
Faça um programa que leia um número qualquer e mostre o seu fatorial
ex.: 5! = 5*4*3*2*1
''')
num = int(input('Digite um valor: '))
x = num
f = 1
print('Calculando {}! = '.format(num), end='')
while x >= 1:
    print('{}'.format(x), end='')
    print(' x ' if x > 1 else ' = ', end='')
    # f = f * x
    f *= x
    x -= 1
print('{}'.format(f))
'''from math import factorial
n = int(input('Digite um valor para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))'''


