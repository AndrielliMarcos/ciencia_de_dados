# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

num = int(input('Digite um valor: '))
# a = num - 1
# b = num + 1
# print('O antecessor de {} é {}. E seu sucessor é {}'.format(num, a, b))
print('O antecessor de {} é {}. E seu sucessor é {}'.format(num, (num - 1), (num + 1)))
